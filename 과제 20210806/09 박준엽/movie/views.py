from movie.models import Actor, Movie, Video, Review
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from movie.forms import MovieForm, ReviewForm

# index = ListView.as_view(model=Movie)


def index(request: HttpRequest):
    qs = Movie.objects.all()
    return render(request, "movie\movie_list.html", {"movie_list": qs,},)


# def post_detail(request, pk):
#    post = Post.objects.get(pk=pk)


def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    review_list = movie.review_set.all()
    video_list = movie.video_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {"movie": movie, "review_list": review_list, "video_list": video_list,},
    )


def movie_new(request: HttpRequest):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False를 지정하면, post.save() 가 호출되지 않은
            # post 인스턴스 반환
            movie = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            # post  # 아직 post.save()가 호출되지 않은 상태.
            # post.ip = request.META["REMOTE_ADDR"]
            movie.save()
            # return redirect("/journal/" + str(1) + "/")
            return redirect(f"/movie/{movie.pk}/")
    else:
        form = MovieForm()

    return render(request, "movie/movie_form.html", {"form": form,},)


def movie_edit(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            # post = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            # post.ip = request.META["REMOTE_ADDR"]
            # post.save()
            return redirect(f"/movie/{movie.pk}/")
    else:
        form = MovieForm(instance=movie)

    return render(request, "movie/movie_form.html", {"form": form,},)


def review_new(request: HttpRequest, movie_pk: int):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect(f"/movie/{movie_pk}")

    else:  # GET 방식으로 받은 경우
        form = ReviewForm()

    return render(request, "movie/review_form.html", {"form": form,},)


def review_edit(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/movie/{movie_pk}/")
    else:
        form = ReviewForm(instance=review)

    return render(request, "movie/review_form.html", {"form": form,},)


# GET 요청 : <form>을 통해서 정말 삭제할 것인지를 물어봅니다.
# POST 요청 : 삭제하고, 다른 주소로 이동시킵니다.


def review_delete(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/movie/{movie_pk}/")

    return render(request, "movie/review_confirm_delete.html", {"review": review,},)


def actor_list(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    actor_list = Actor.objects.all()
    return render(request, "movie/actor_list.html", {"actor_list": actor_list,},)
