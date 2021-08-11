from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


# 로그인하지 않은 유저는 접근해서는 안 될 뷰
@login_required
def profile(request: HttpRequest):
    # if not request.user.is_authenticated:  # User 모델 인스턴스 이거나 AnonymousUser 클래스 인스턴스
    #     return redirect("/accounts/login/")
    return render(request, "accounts/profile.html")
