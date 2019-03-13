from django import forms

from .models import Post

# Форма для создания и редактирования постов

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Создано два поля, для загаловка и текста
        fields = ('title', 'text')