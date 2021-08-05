from django.shortcuts import render

from blog.models import Article


def index(request):
    qs = Article.objects.all()
    return render(request, "blog/article_list.html", {
        "article_list": qs,
    })


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, "blog/article_detail.html", {
        "article": article,
    })
