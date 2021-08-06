from django.views.generic import ListView
from django.shortcuts import render
from journal.models import Post

# FBV (Function Based View)
# def index(request):
#     qs = Post.objects.all()
#     return render(
#         request,
#         "journal/post_list.html",
#         {
#             "post_list": qs,
#         },
#     )

index = ListView.as_view(model=Post)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # comment_list = Comment.objects.filter(post__id=post.id)
    # comment_list = Comment.objects.filter(post=post)
    # related name
    comment_list = post.comment_set.all()
    return render(request, "journal/post_detail.html", {
        "post": post,
        "comment_list": comment_list,
    })
