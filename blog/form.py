from django import forms

from .models import Post, Comment

# Форма для создания комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')


# Форма для создания и редактирования постов

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Создано два поля, для загаловка и текста
        fields = ('title', 'text')