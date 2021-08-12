from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render, resolve_url

from movist.forms import ReviewForm
from movist.models import Actor, Movie, Review


# actor list
def actor_list(request):
    qs = Actor.objects.all().prefetch_related("movie_set")

    return render(request, "movist/actor_list.html", {
        "actor_list": qs,
    })


# actor detail


def actor_detail(request, pk):
    # 이렇게 직접 예외처리하는 것이 번거로워요.
    # try:
    #     actor = Actor.objects.get(pk=pk)
    # except Actor.DoesNotExist:
    #     raise Http404  # django.http

    # 특정 model instance를 획득하는 제대로된 코드
    actor = get_object_or_404(Actor, pk=pk)

    # movie_list = actor.movie_set.all()
    return render(request, "movist/actor_detail.html", {
        "actor": actor,
    })


# movie list
def movie_list(request: HttpRequest):
    qs = Movie.objects.all().select_related("actor")

    # QueryDict
    # QueryString 인자 : 모든 요청에 존재할 수 있어요.
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)
    # request.POST  # POST에만 존재
    # request.FILES

    return render(request, "movist/movie_list.html", {
        "movie_list": qs,
    })


# movie detail + review 쓰기
def movie_detail(request, pk):
    # movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movist/movie_detail.html", {
        "movie": movie,
    })


# 이 응답에서 페이지 전체를 그릴 것인지? 혹은 실제 컨텐츠만 그릴 것인지를 결정.

def review_list(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    # review_list = movie.review_set.all()

    review_list = Review.objects.filter(movie__pk=movie_pk)

    # python plain objects로 변환
    # JSON으로 변환하는 파이썬 기본 라이브러리인 json.dumps를 통해서 이뤄집니다.
    #  파이썬 기본 타입에 대해서만 변환 룰을 제공해줍니다.
    #  추가 타입에 대해서는? 커스텀 Rule을 지정할 수 있습니다. => json.dumps에 cls 인자를 통해 가능
    response_data = [
        {
            "message": review.message,
            "edit_url": resolve_url("review_edit", movie_pk, review.pk),
            "delete_url": resolve_url("review_delete", movie_pk, review.pk),
            "author": {
                "username": review.author.username,
            },
        }
        for review in review_list]
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})

    # # 우리가 일반적인 응답 포맷은 HTML
    # return render(request, "movist/review_list.html", {
    #     "review_list": review_list,
    # })


@login_required
def review_new(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review: Review = form.save(commit=False)
            # 현재 로그인 유저를 author 필드에 지정
            review.author = request.user
            review.movie = movie
            review.save()
            # return redirect(f"/movist/movies/{movie_pk}/")
            # return redirect("movie_detail", movie_pk)  # URL Reverse

            # return redirect(movie.get_absolute_url())
            # redirect는 인자로 받은 객체에서 get_absolute_url 속성을 지원하면
            # get_absolute_url() 을 호출하여 그 반환값을 사용합니다.
            return redirect(movie)

            # return redirect("movie_detail", pk=movie_pk)  # URL Reverse
    else:  # GET
        form = ReviewForm()

    return render(request, "movist/review_form.html", {
        "form": form,
    })


@login_required
def review_edit(request, movie_pk, pk):
    # review = Review.objects.get(pk=pk)
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review: Review = form.save()
            # return redirect(f"/movist/movies/{movie_pk}/")
            # return redirect("movie_detail", movie_pk)  # URL Reverse
            return redirect(review.movie)
    else:  # GET
        form = ReviewForm(instance=review)

    return render(request, "movist/review_form.html", {
        "form": form,
    })


# GET 방식으로 요청을 받았을 때에는, 절대 삭제하지마세요.
@login_required
def review_delete(request, movie_pk, pk):
    # review = Review.objects.get(pk=pk)
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        review.delete()
        # return redirect(f"/movist/movies/{movie_pk}/")
        # return redirect("movie_detail", movie_pk)
        return redirect(review.movie)
    return render(request, "movist/review_confirm_delete.html")
