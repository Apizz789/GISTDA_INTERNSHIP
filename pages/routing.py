from django.urls import path
from .user import TLE_user

ws_urlpatterns =[
    path('ws/pages/', TLE_user.as_asgi())
]