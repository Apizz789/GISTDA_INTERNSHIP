# django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # new
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # new
]

urlpatterns += staticfiles_urlpatterns()    