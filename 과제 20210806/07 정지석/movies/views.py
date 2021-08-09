from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from movies.models import Actor, Movie, Video, Review
from movies.forms import ReviewForm

def index(request):
    qs = Actor.objects.all()
    return render(
        request,
        "movies/actor_list.html",
        {
            "actor_list": qs,
        },
    )

def actor_detail(request, pk):
    actor = Actor.objects.get(pk=pk)
    movie = Movie.objects.filter(actor=pk)
    movie_list = Movie.objects.filter(actor = pk)
    # related name
    #review_list = actor.review_set.all()
    return render(
        request,
        "movies/actor_detail.html",
        {
            "actor": actor,
            "movie": movie,
            "movie_list": movie_list,
        },
    )

def movie_list(request):
    qs = Movie.objects.all()
    return render(
        request,
        "movies/movie_list.html",
        {
            "movie_list": qs,
        },
    )

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    video = Video.objects.filter(movie=pk)

    review_list = movie.review_set.all()
    return render(
        request,
        "movies/movie_detail.html",
        {
            "movie": movie,
            "video_list": video,
            "review_list": review_list,
        },
    )

def review_new(request: HttpRequest, movie_pk: int) -> HttpResponse:
    movie = Movie.objects.get(pk=movie_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect(f"/movies/movie/{movie_pk}/")
    else:
        form = ReviewForm()

    return render(
        request,
        "movies/review_form.html",
        {
            "form": form,
        },
    )

def review_edit(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/movies/movie/{movie_pk}/")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "movies/review_form.html",
        {
            "form": form,
        },
    )

def review_delete(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/movies/movie/{movie_pk}/")

    return render(
        request,
        "movies/review_confirm_delete.html",
        {
            "review": review,
        },
    )
