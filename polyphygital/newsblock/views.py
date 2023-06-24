from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, FormView
import json

from newsblock.forms import *
from newsblock.models import *
from newsblock.utils import *
from gameblock.urls import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins
from .models import News
from django.shortcuts import render

from .serializers import *

logo = "../media/service/logo_black.png"

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'newsblock/index.html', context=context)

def news(request):
    posts = News.objects.filter(is_visible="True")

    context = {
        'posts': posts,
        'title': 'Новости',
    }

    return render(request, 'newsblock/news.html', context=context)


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Текущий пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Подтверждение нового пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    

@login_required
def delete_player_self(request):
    player = get_object_or_404(Player, user_id=request.user)
    player.delete()
    return HttpResponse("OK")

# TODO: Fix data doesnt save
@login_required
def profile(request):
    user = request.user
    is_player = Player.objects.filter(user_id=user).exists()
    player = None

    if is_player:
        player = Player.objects.get(user_id=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if is_player:
            player_form = PlayerForm(request.POST, request.FILES, instance=player)
        else:
            player_form = PlayerForm(request.POST, request.FILES)
        password_form = CustomPasswordChangeForm(user=user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
            
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)
        
        if player_form.is_valid():
            player = player_form.save(commit=False)
            player.user_id = user
            player.save()
        
        return redirect('profile', permanent=False)
    user_form = UserForm(instance=user)
    if is_player:
        player_form = PlayerForm(instance=player)
    else:
        player_form = PlayerForm()
    password_form = CustomPasswordChangeForm(user=user)
    return render(request, 'newsblock/profile.html', {'user_form': user_form, 'player_form': player_form, 'password_form': password_form})


class NewsViewSet(mixins.ListModelMixin, 
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class News_CategoryViewSet(mixins.ListModelMixin, 
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = News_Category.objects.all()
    serializer_class = News_CategorySerializer

class News_CommentViewSet(mixins.ListModelMixin, 
                          mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet,):
    queryset = News_Comment.objects.all()
    serializer_class = News_CommentSerializer

    # def get(self, request, format=None):
    #     posts = News.objects.filter(is_visible=True)
    #     serializer = NewsSerializer(posts, many=True)
    #     return Response(serializer.data)

# def show_post(request, post_slug):
#     post = get_object_or_404(News, slug=post_slug)
#     comments = Comments.objects.filter(news_id=post.id)
#     context = {
#         'title':post.title,
#         'post': post,
#         'comments' : comments,
#     }
#
#     return render(request, 'newsblock/post.html', context=context);

def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)
    comments = News_Comment.objects.filter(news_id=post.id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news_id = post
            comment.user_id = request.user
            comment.save()
            form = CommentForm()
        return redirect('post', post_slug=post_slug)

    form = CommentForm()
    context = {
        'title': post.title,
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'newsblock/post.html', context=context)

class CommentView(FormView):
    template_name = 'newsblock/post.html'
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(News, slug=self.kwargs['post_slug'])
        comments = form.save(commit=False)
        comments.news_id = post
        comments.user_id = self.request.user
        comments.time_created = timezone.now()
        comments.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post', kwargs={'post_slug': self.kwargs['post_slug']})

def pageNotFound(request, exception):
    return HttpResponse('Ты находишься на <b>СТРАНИЦЕ ОШИБКИ</b>')
    # return render(request, 'newsblock/404.html', {'menu': menu, 'title': 'Упс...'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'newsblock/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'newsblock/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form

def logout_user(request):
    logout(request)
    return redirect('login')
