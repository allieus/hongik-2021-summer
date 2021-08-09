from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from movie.models import Actor, Movie, Video, Review, Trailer


from movie.forms import MovieForm, ReviewForm


def index(request: HttpRequest):
    qs = Actor.objects.all()
    # 전체 값을 가져옴
    # qs = QuerySet: 데이터베이스로의 쿼리를 생성, 실행
    return render(request, "movie/actor_list.html", {"actor_list": qs,})


def actor_detail(request: HttpRequest, pk):
    actor = Actor.objects.get(pk=pk)  # actor에 pk를 저장
    return render(request, "movie/actor_detail.html", {"actor": actor,})


def movie_list(request: HttpRequest):
    qs = Movie.objects.all()
    return render(request, "movie/movie_list.html", {"movie_list": qs,})


def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    trailer_list = movie.trailer_set.all()
    review_list = movie.review_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {"movie": movie, "review_list": review_list, "trailer_list": trailer_list},
    )


def movie_new(request: HttpRequest):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(f"/movie/movie/")  # 슬래시('/') 꼭 넣기!!!!
    else:
        form = MovieForm()

    return render(request, "movie/movie_form.html", {"form": form,})


def movie_edit(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(f"/movie/movie/")
    else:
        form = MovieForm(instance=movie)

    return render(request, "movie/movie_form.html", {"form": form})


def review_new(request: HttpRequest, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect(f"/movie/movie/{ movie_pk }/")
    else:
        form = ReviewForm()

    return render(request, "movie/review_form.html", {"form": form,})


def review_edit(request, movie_pk, review_pk):
    movie = Movie.objects.get(pk=movie_pk)
    review = Review.objects.get(pk=review_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/movie/movie/{ movie_pk }/")
    else:
        form = ReviewForm(instance=review)

    return render(request, "movie/review_form.html", {"form": form,})
