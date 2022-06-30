# pages/urls.py
from django.urls import path
from .views import homePageView,MarkersMapView,MapView,CesiumView,MapPluemView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "markers"

urlpatterns = [
    path("", homePageView, name="home"),
    path("map/", MapView, name="test"),
    path("cesium/", CesiumView, name="cesium"),
    path("mapPluem/", MapPluemView, name="mapall"),
]

urlpatterns += staticfiles_urlpatterns()   