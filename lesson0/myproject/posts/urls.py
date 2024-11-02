from django.urls import path
from . import views


urlpatterns = [
    path('posts/post_list', views.post_list, name='post_list'),
]
