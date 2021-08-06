from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("journal/", include("journal.urls")),
    # path("", lambda request: redirect("/journal/")),
    path("", RedirectView.as_view(url="/journal/")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
