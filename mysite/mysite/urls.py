from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pybird/", include("pybird.urls")),
    path("admin/", admin.site.urls),
]