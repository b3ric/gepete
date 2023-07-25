from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/img", views.img, name="img"),
    path("/aud", views.aud, name="aud"),
    path("/file", views.file, name="file"),
    path("/chat", views.chat, name="chat"),
]