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
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False를 지정하면, post.save() 가 호출되지 않은
            # post 인스턴스 반환
            post = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            # post  # 아직 post.save()가 호출되지 않은 상태.
            post.ip = request.META["REMOTE_ADDR"]
            post.save()
            # return redirect("/journal/" + str(1) + "/")
            return redirect(f"/journal/{post.pk}/")
    else:
        form = PostForm()

    return render(
        request,
        "journal/post_form.html",
        {
            "form": form,
        },
    )


def post_edit(request: HttpRequest, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            post.ip = request.META["REMOTE_ADDR"]
            post.save()
            return redirect(f"/journal/{post.pk}/")
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "journal/post_form.html",
        {
            "form": form,
        },
    )


# def post_delete(request, pk):
#     pass
