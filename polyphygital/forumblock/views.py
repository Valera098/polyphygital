from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, FormView
import json

from forumblock.models import *


def forum(request):
    treads = Topic.objects.all()

    context = {
        'treads': treads,
        'title': 'Форум',
    }

    return render(request, 'forumblock/forum.html', context=context);