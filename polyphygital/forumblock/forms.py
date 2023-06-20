from django import forms
from django.forms import HiddenInput
from .models import *

class TopicCommentForm(forms.ModelForm):
    class Meta:
        model = Topic_Comment
        fields = ['content']

class TopicForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок обсуждения', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст обсуждения', widget=forms.Textarea(attrs={'class': 'form-control'}))
    topic_category_id = forms.ModelChoiceField(label='Категория обсуждения', queryset=Topic_Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    is_closed = forms.BooleanField(label='Отображение', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Topic
        fields = ['title', 'content', 'topic_category_id', 'is_closed']
        