from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, reverse
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def article(request):

    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(auth=request.user)
    context = {"articles": articles}
    return render(request, "dashboard.html", context)

