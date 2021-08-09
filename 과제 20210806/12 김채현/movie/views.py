from django.shortcuts import render, redirect
from movie.models import Actor, Movie, Video, Review
from movie.forms import ReviewForm, LinkForm
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    qs = Actor.objects.all()
    return render(request, "movie/actor_list.html", {"actor_list": qs})


def actor_detail(request: HttpRequest, pk: int):
    actor = Actor.objects.get(pk=pk)
    post_list = actor.movie_set.all()
    return render(
        request, "movie/actor_detail.html", {
            "actor": actor, "post_list": post_list, },
    )


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    video = Video.objects.filter(movie=pk)

    message = movie.review_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie": movie,
            "video_list": video,
            "message": message,
        },
    )


def review_new(request: HttpRequest, movie_pk: int) -> HttpResponse:
    post = Movie.objects.get(pk=movie_pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = post
            comment.save()
            return redirect(f"/movie/{ movie_pk }/mov/")
    else:
        form = ReviewForm()

    return render(request, "movie/review_form.html", {"form": form, },)


def review_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/movie/{post_pk}/movie/review/edit")
    else:
        form = ReviewForm(instance=review)

    return render(request, "movie/comment_review.html", {"form": form, },)


def video_new(request: HttpRequest, pk: int, movie_pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            return redirect(f"mov/{movie_pk}/")
    else:
        form = LinkForm()

    return render(request, "mov/video_form.html", {"form": form, "movie": Movie, },)
