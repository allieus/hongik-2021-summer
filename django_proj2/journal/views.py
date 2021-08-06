from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from journal.forms import CommentForm, PostForm
from journal.models import Comment, Post

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
            form.save()
            # post = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            # post.ip = request.META["REMOTE_ADDR"]
            # post.save()
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


def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = Post.objects.get(pk=post_pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f"/journal/{post_pk}/")
    else:
        form = CommentForm()

    return render(
        request,
        "journal/comment_form.html",
        {
            "form": form,
        },
    )


def comment_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Comment.objects.get(pk=pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/journal/{post_pk}/")
    else:
        form = CommentForm(instance=comment)

    return render(
        request,
        "journal/comment_form.html",
        {
            "form": form,
        },
    )


# GET 요청 : <form>을 통해서 정말 삭제할 것인지를 물어봅니다.
# POST 요청 : 삭제하고, 다른 주소로 이동시킵니다.


def comment_delete(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        comment.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/journal/{post_pk}/")

    return render(
        request,
        "journal/comment_confirm_delete.html",
        {
            "comment": comment,
        },
    )
