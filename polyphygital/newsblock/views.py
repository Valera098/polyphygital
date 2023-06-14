from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
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
def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'newsblock/index.html', context=context);

def news(request):
    posts = News.objects.filter(is_visible="True")

    context = {
        'posts': posts,
        'title': 'Новости',
    }

    return render(request, 'newsblock/news.html', context=context);

def news2(request):
    posts = News.objects.filter(is_visible="True")

    context = {
        'posts': json.dumps(posts),
        'title': 'Новости',
    }

    return render(request, 'newsblock/news2', context=context);
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
    comments = Comments.objects.filter(news_id=post.id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news_id = post
            comment.user_id = request.user
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    context = {
        'title': post.title,
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'newsblock/post.html', context=context);

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
    return HttpResponse('Ты находишься на <b>СТРАНИЦЕ ОШИБКИ</b>');
    # return render(request, 'newsblock/404.html', {'menu': menu, 'title': 'Упс...'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'newsblock/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'newsblock/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('homepage')

def logout_user(request):
    logout(request)
    return redirect('login')