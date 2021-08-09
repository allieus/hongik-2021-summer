from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from django.shortcuts import redirect
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movie/", include("movie.urls")),
    path("", RedirectView.as_view(url="/movie/")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

