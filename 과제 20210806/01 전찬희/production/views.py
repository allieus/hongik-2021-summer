from production.forms import ReviewForm
from django.db.models.fields import CharField
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.views.generic import ListView
from production import models
from production.models import Movie, Actor, Review, Video

index = ListView.as_view(model=Actor)
movie_index = ListView.as_view(model=Movie)


def actor_list_detail(request: HttpRequest, pk):
    actor = Actor.objects.get(pk=pk)
    movie_list = actor.movie_set.all()
    return render(
        request,
        "production/actor_list_detail.html",
        {
            "actor": actor,
            "movie_list": movie_list,
        },
    )


def movie_list_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    review_list = movie.review_set.all()
    video_list = movie.video_set.all()
    return render(
        request,
        "production/movie_list_detail.html",
        {
            "movie": movie,
            "review_list": review_list,
            "video_list": video_list,
        },
    )


def review_new(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect(f"/actor/movie/{movie.pk}/")
    else:
        form = ReviewForm()

    return render(
        request,
        "production/review_form.html",
        {
            "form": form,
        },
    )


def review_edit(request: HttpRequest, review_pk, pk):
    movie = Movie.objects.get(pk=pk)
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect(f"/actor/movie/{movie.pk}/")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "production/review_form.html",
        {
            "form": form,
        },
    )


# GET ?????? : <form>??? ????????? ?????? ????????? ???????????? ???????????????.
# POST ?????? : ????????????, ?????? ????????? ??????????????????.


def review_delete(request: HttpRequest, review_pk: int, pk: int) -> HttpResponse:
    movie = Movie.objects.get(pk=pk)
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review.delete()  # DB??? ?????? DELTE ????????? ??????
        return redirect(f"/actor/movie/{movie.pk}/")

    return render(
        request,
        "production/review_confirm_delete.html",
        {
            "review": review,
        },
    )
