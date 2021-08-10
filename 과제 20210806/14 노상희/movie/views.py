from django.shortcuts import redirect, render
from django.views.generic import ListView
from movie.models import Actor, Movie, Video, Review
from django.http import HttpRequest, HttpResponse

from movie.forms import MovieForm, ReviewForm
from movie.models import Movie, Review


# index = ListView.as_view(model=Movie)


def index(request: HttpRequest):
    qs = Movie.objects.all()
    return render(
        request,
        "movie/movie_list.html",
        {
            "movie_list": qs,
        },
    )


def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    review_list = movie.review_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie": movie,
            "review_list": review_list,
        },
    )


def movie_new(request: HttpRequest):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.ip = request.META["REMOTE_ADDR"]
            movie.save()
            return redirect(f"/movie/{movie.pk}/")
    else:
        form = MovieForm()
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
            "actor_list": qs,
        },
    )


# def actor_detail(request:HttpRequest, actor_pk):
#     actor = Actor.Objects.get(pk=actor_pk)
#     movie_list = actor.movie_set.all()
#     return render(
#         request,
#         "movie/actor_detail.html", {
#             "actor":actor, "movie_list":movie_list,},
#     )


# def movie_edit(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
#     movie = Movie.Objects.get(pk=pk)
#     if request.method == "POST":
#         form = MovieForm(request.POST, request.FILES, instance=movie)
#         if form.is_valid():
#             movie = form.save(commit=False)
#             movie.ip = request.META["REMOTE_ADDR"]
#             movie.save()
#             return redirect(f"/movie/{movie.pk}/")
#     else:
#         form = MovieForm()
#     return render(
#         request,
#         "movie/movie_form.html",
#         {
#             "form": form,
#         },
#     )
