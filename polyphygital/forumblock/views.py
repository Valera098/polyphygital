from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, FormView
import json

from forumblock.forms import TopicCommentForm
from forumblock.models import *
from newsblock.models import *


def forum(request):
    threads = Topic.objects.all()

    context = {
        'threads': threads,
        'title': 'Форум',
    }

    return render(request, 'forumblock/forum.html', context=context);

def show_thread(request, thread_slug):
    thread = get_object_or_404(Topic, slug=thread_slug)
    comments = Topic_Comment.objects.filter(topic_id=thread.id)
    if request.method == 'POST':
        form = TopicCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic_id = thread
            comment.user_id = request.user
            comment.save()
            form = TopicCommentForm()
    else:
        form = TopicCommentForm()
    context = {
        'title': thread.title,
        'thread': thread,
        'comments': comments,
        'form': form,
    }
    return render(request, 'forumblock/thread.html', context=context)

class CommentView(FormView):
    template_name = 'forumblock/thread.html'
    form_class = TopicCommentForm

    def form_valid(self, form):
        thread = get_object_or_404(Topic, slug=self.kwargs['thread_slug'])
        comments = form.save(commit=False)
        comments.topic_id = thread
        comments.user_id = self.request.user
        comments.time_created = timezone.now()
        comments.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('thread', kwargs={'thread_slug': self.kwargs['thread_slug']})