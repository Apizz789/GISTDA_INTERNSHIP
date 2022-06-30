# pages/urls.py
from django.urls import path
from .views import homePageView,MarkersMapView,MapView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "markers"

urlpatterns = [
    path("", homePageView, name="home"),
    path("map/", MapView, name="test")
]

urlpatterns += staticfiles_urlpatterns()   