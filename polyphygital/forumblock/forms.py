from django import forms

from .models import *

class TopicCommentForm(forms.ModelForm):
    class Meta:
        model = Topic_Comment
        fields = ['content']