from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    comments = article.comment_set.all()
    
    form = CommentForm()

    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }

    return render(request, 'detail.html', context)


def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
        
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'update.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            article = Article.objects.get(id=article_id)
            comment.article = article
            comment.save()

            return redirect('articles:detail', id=article_id)

    else:
        return redirect('articles:index')
