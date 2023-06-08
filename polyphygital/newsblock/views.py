from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from newsblock.forms import RegisterUserForm
from newsblock.models import *
from newsblock.utils import *


def index(request):
    return render(request, 'newsblock/index.html', {'title': 'Главная'});

def news(request):
    posts = News.objects.filter(is_visible="True")

    context = {
        'posts': posts,
        'title': 'Новости',
    }

    return render(request, 'newsblock/news.html', context=context);

def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'title':post.title,
        'post': post,
    }

    return render(request, 'newsblock/post.html', context=context);

# def login(request, ):
#     return HttpResponse("Авторизация");

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