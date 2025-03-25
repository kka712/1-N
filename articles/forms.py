from django.forms import ModelForm
from .models import Article, Comment
from django import forms
class ArticleForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    class Meta():
        model = Article
        fields = '__all__'
        widgets = {
            'A': forms.TextInput(attrs={'class': 'form-control'}),
            'B': forms.TextInput(attrs={'class': 'form-control'})
        }
class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields는 추가할 필드 목록
        # fields = ['answer']
        # fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
        # exclude는 제외할 필드 목록
        exclude = ('article', )
        