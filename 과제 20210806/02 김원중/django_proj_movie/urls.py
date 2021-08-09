from django.contrib import admin
from django.urls import path, include

# media 관련
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("movie/", include("movie.urls")),
]

# media 관련
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
