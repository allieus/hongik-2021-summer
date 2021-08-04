from django.shortcuts import render

from travel.models import Post


def index(request):
    qs = Post.objects.all()
    return render(request, "travel/post_list.html", {
        "post_list": qs,
    })
