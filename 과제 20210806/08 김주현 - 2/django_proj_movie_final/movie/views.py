from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from movie.models import Actor, Movie, Video, Review
from movie.forms import MovieForm, ReviewForm, ActorForm

def actor_list(request: HttpRequest):
    actor = Actor.objects.all()
    return render(
        request, 
        "movie/actor_list.html",
        {
            "actor_list":actor,
            },
    )

def actor_new(request: HttpRequest):
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return redirect(f"/movie")
    else:
        form = ActorForm()
    return render(
        request, 
        "movie/actor_form.html", 
        {
            "form":form
            },
    )

def actor_edit(request: HttpRequest, pk: int) -> HttpResponse:
    comment = Actor.objects.get(pk=pk)
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/movie")
    else:
        form = ActorForm(instance=comment)

    return render(
        request,
        "movie/actor_form.html",
        {
            "form": form,
        },
    )

def actor_delete(request: HttpRequest, pk: int) -> HttpResponse:
    comment = Actor.objects.get(pk=pk)
    if request.method == "POST":
        comment.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/movie")

    return render(
        request,
        "movie/actor_confirm_delete.html",
        {
            "comment": comment,
        },
    )

def actor_detail(request: HttpRequest, pk: int):
    actor = Actor.objects.get(pk=pk)
    movie_list = actor.movie_set.all()
    return render(
        request,
        "movie/actor_detail.html",
        {
            "actor":actor, 
            "movie_list":movie_list,
            },
    )

def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    comment_list = movie.review_set.all()
    vid = Video.objects.all()
    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie":movie,
            "comment_list":comment_list,
            "vid":vid,
            },
    )

def Review_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = Movie.objects.get(pk=post_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = post
            comment.save()
            return redirect(f"/movie/movie/{post_pk}/")
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
            return redirect(f"/movie/movie/{post_pk}/")
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
        return redirect(f"/movie/movie/{post_pk}/")

    return render(
        request,
        "movie/review_confirm_delete.html",
        {
            "comment": comment,
        },
    )

def movie_new(request: HttpRequest, pk: int):
    actor = Actor.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(f"/movie/{actor.pk}")
    else:
        form = MovieForm()
    return render(
        request, 
        "movie/movie_form.html", 
        {
            "form":form,
            },
    )

def movie_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/movie/{post_pk}")
    else:
        form = MovieForm(instance=comment)

    return render(
        request,
        "movie/movie_form.html",
        {
            "form": form,
        },
    )

def movie_delete(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Review.objects.get(pk=pk)
    if request.method == "POST":
        comment.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/movie/{post_pk}")

    return render(
        request,
        "movie/movie_confirm_delete.html",
        {
            "comment": comment,
        },
    )