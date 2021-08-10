from django.shortcuts import redirect, render

from movist.forms import ReviewForm
from movist.models import Actor, Movie, Review


# actor list
def actor_list(request):
    qs = Actor.objects.all()
    return render(request, "movist/actor_list.html", {
        "actor_list": qs,
    })


# actor detail
def actor_detail(request, pk):
    actor = Actor.objects.get(pk=pk)
    # movie_list = actor.movie_set.all()
    return render(request, "movist/actor_detail.html", {
        "actor": actor,
    })


# movie list
def movie_list(request):
    qs = Movie.objects.all()
    return render(request, "movist/movie_list.html", {
        "movie_list": qs,
    })


# movie detail + review 쓰기
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, "movist/movie_detail.html", {
        "movie": movie,
    })


def review_new(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review: Review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect(f"/movist/movies/{movie_pk}/")
    else:  # GET
        form = ReviewForm()

    return render(request, "movist/review_form.html", {
        "form": form,
    })


def review_edit(request, movie_pk, pk):
    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review: Review = form.save()
            return redirect(f"/movist/movies/{movie_pk}/")
    else:  # GET
        form = ReviewForm(instance=review)

    return render(request, "movist/review_form.html", {
        "form": form,
    })


# GET 방식으로 요청을 받았을 때에는, 절대 삭제하지마세요.

def review_delete(request, movie_pk, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect(f"/movist/movies/{movie_pk}/")
    return render(request, "movist/review_confirm_delete.html")
