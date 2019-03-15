from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .form import PostForm, CommentForm
# Create your views here.

# views это отображение на странице

# Функция отображения всех статей на странице

def post_list(request):
    posts = Post.objects.filter(publisher_date__lte=timezone.now()).order_by('publisher_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Функци отображения конкретной статьи

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    сomment = Comment.objects.filter(post_pk=pk)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment': сomment,
        })
# Функция создания новой статьи из страницы сайта

def post_new(request):
    if request.method == 'POST':
        # form = данные которые пользователь отправил
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

# функция создания нововых комментарий
def comment_new(request, pk):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            # указываем, что пост_пк равен ИД поста, чтобы в конкретном посте отображались только его комментарии
            com.post_pk = Post.objects.get(id=pk)
            com.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'form': form})

# Функция редактирования статьи

def post_edit(request, pk):
    # Получаем статью или при ее отсутсвии выдаем 404
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # instance = исходное состояние поста
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

