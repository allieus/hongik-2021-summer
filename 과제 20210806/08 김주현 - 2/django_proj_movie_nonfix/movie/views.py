from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from movie.models import Actor, Movie, Video, Review
from movie.forms import MovieForm, ReviewForm

def index(request: HttpRequest):
    qs = Movie.objects.all()
    return render(
        request, 
        "movie/movie_list.html",
        {
            "movie_list":qs,
            },
    )

def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    comment_list = movie.review_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie":movie, 
            "comment_list":comment_list,
            },
    )

def movie_new(request: HttpRequest):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(f"/movie/{movie.pk}/")
    else:
        form = MovieForm()
    return render(
        request, 
        "movie/movie_form.html", 
        {
            "form":form
            },
    )

def movie_edit(request: HttpRequest, pk):
    post = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"/movie/{post.pk}/")
    else:
        form = MovieForm(instance=post)
    return render(
        request,
        "movie/movie_form.html",
        {
            "form": form,
        },
    )

def actor_index(request: HttpRequest):
    qs = Actor.objects.all()
    return render(
        request,
        "movie/actor_list.html",
        {
            "actor_list":qs
            },
    )

def actor_detail(request: HttpRequest, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    movie_list = actor.movie_set.all()
    return render(
        request,
        "movie/actor_detail.html",
        {
            "actor":actor, 
            "movie_list":movie_list
            },
    )

def Review_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = Movie.objects.get(pk=post_pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f"/movie/{post_pk}/")
    else:
        form = ReviewForm()

    return render(
        request,
        "movie/review_form.html",
        {
            "form": form,
        },
    )

def Review_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/movie/{post_pk}/")
    else:
        form = ReviewForm(instance=comment)

    return render(
        request,
        "movie/review_form.html",
        {
            "form": form,
        },
    )

def Review_delete(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Review.objects.get(pk=pk)
    if request.method == "POST":
        comment.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/movie/{post_pk}/")

    return render(
        request,
        "movie/review_confirm_delete.html",
        {
            "comment": comment,
        },
    )