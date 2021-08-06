from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import ListView

from journal.forms import PostForm
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
    return render(
        request,
        "journal/post_detail.html",
        {
            "post": post,
            "comment_list": comment_list,
        },
    )


def post_new(request: HttpRequest):
    if request.method == "GET":
        form = PostForm()
    else:  # POST
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  # 방금 저장한 모델 객체를 반환
            # return redirect("/journal/" + str(1) + "/")
            return redirect(f"/journal/{post.pk}/")

    return render(
        request,
        "journal/post_form.html",
        {
            "form": form,
        },
    )


# def post_edit(request, pk):
#     pass


# def post_delete(request, pk):
#     pass
