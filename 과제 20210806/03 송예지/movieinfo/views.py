from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from movieinfo.forms import ActorForm, MovieForm, LinkForm, ReviewForm
from movieinfo.models import Actor, Movie, Video, Review


def index(request: HttpRequest):
    qs = Actor.objects.all()
    return render(request, "movieinfo/actor_list.html",
                  {
                      "actor_list": qs,
                  })


def movie_list(request: HttpRequest):
    movie_list = Movie.objects.all()
    return render(
        request,
        "movieinfo/movie_list.html",
        {
            "movie_list": movie_list,
        },
    )


def actor_detail(request: HttpRequest, pk: int):
    actor = Actor.objects.get(pk=pk)
    poster_list = actor.movie_set.all()
    return render(
        request,
        "movieinfo/actor_detail.html",
        {
            "actor": actor,
            "poster_list": poster_list,
        },
    )


def movie_detail(request: HttpRequest, pk: int, movie_pk: int):
    actor = Actor.objects.get(pk=pk)
    movie = Movie.objects.get(pk=movie_pk)
    video_list = movie.video_set.all()
    review_list = movie.review_set.all()
    return render(
        request,
        "movieinfo/movie_detail.html",
        {
            "actor": actor,
            "movie": movie,
            "video_list": video_list,
            "review_list": review_list,
        },
    )


def actor_new(request: HttpRequest) -> HttpRequest:
    actor = Actor.objects.all()
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False를 지정하면, post.save() 가 호출x
            # post 인스턴스를 반환
            actor = form.save()  # 방금 저장한 모델 객체를 반환
            return redirect(f'/movieinfo')

    else:
        form = ActorForm()

    return render(
        request,
        "movieinfo/actor_form.html",
        {
            "form": form,
        },
    )


def movie_new(request: HttpRequest, pk: int) -> HttpRequest:
    actor = Actor.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()  # 방금 저장한 모델 객체를 반환
            return redirect(f'/movieinfo/{actor.pk}')

    else:
        form = MovieForm()

    return render(
        request,
        "movieinfo/movie_form.html",
        {
            "form": form,
            "actor": actor,
        },
    )


def video_new(request: HttpRequest, pk: int, movie_pk: int) -> HttpRequest:
    actor = Actor.objects.get(pk=pk)
    movie = Movie.objects.get(pk=movie_pk)
    video = Video.objects.all()
    if request.method == "POST":
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()  # 방금 저장한 모델 객체를 반환
            return redirect(f'/movieinfo/{actor.pk}/movies/{movie_pk}')

    else:
        form = LinkForm()

    return render(
        request,
        "movieinfo/video_form.html",
        {
            "form": form,
            "movie": movie,
        },
    )


def review_new(request: HttpRequest, pk: int, movie_pk: int) -> HttpRequest:
    actor = Actor.objects.get(pk=pk)
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False를 지정하면, post.save() 가 호출x
            # post 인스턴스를 반환
            review = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            # return redirect("/journal/"+str(1)+"/")
            # post post.save() 아직 호출되지 않은 상태
            review.movie = movie
            review.save()
            return redirect(f'/movieinfo/{actor.pk}/movies/{movie_pk}')

    else:
        form = ReviewForm()

    return render(
        request,
        "movieinfo/review_form.html",
        {
            "form": form,
        },
    )


def review_edit(request: HttpRequest, pk: int, movie_pk: int, review_pk: int) -> HttpResponse:
    actor = Actor.objects.get(pk=pk)
    movie = Movie.objects.get(pk=movie_pk)
    review = Review.objects.get(pk=review_pk)

    # 댓글쓰기에 성공하면, post detail 로 이동
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/movieinfo/{actor.pk}/movies/{movie_pk}")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "movieinfo/review_form.html",
        {
            "form": form,
        },
    )

# GET 요청 : <form>을 통해서 정말 삭제할 것인지를 물어봅니다.
# POST 요청 : 삭제하고, 다른 주소로 이동시킵니다.


def review_delete(request: HttpRequest, pk: int, movie_pk: int, review_pk: int) -> HttpResponse:
    actor = Actor.objects.get(pk=pk)
    movie = Movie.objects.get(pk=movie_pk)
    review = Review.objects.get(pk=review_pk)

    if request.method == "POST":
        review.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/movieinfo/{actor.pk}/movies/{movie_pk}")

    return render(
        request,
        "movieinfo/review_confirm_delete.html",
        {
            "review": review,
        },
    )

# def index(request):
#     qs = Movie.objects.all()
#     return render(
#         request,
#         "movieinfo/movie_list.html",
#         {
#             "movie_list": qs,
#         },
#     )
