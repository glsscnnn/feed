from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post_something/', views.post_something, name="post_something"),
]
