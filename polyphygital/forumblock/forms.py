from django import forms
from django.forms import HiddenInput
from .models import *

class TopicCommentForm(forms.ModelForm):
    class Meta:
        model = Topic_Comment
        fields = ['content']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'slug', 'topic_category_id', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput
        self.fields['slug'].widget = forms.TextInput
        self.fields['topic_category_id'].queryset = Topic_Category.objects.all()