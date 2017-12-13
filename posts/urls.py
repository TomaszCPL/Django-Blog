from django.contrib import admin
from django.urls import include, url
from posts import views

from .views import (
posts_list,
posts_create,
post_detail,
)

urlpatterns = [
    url(r'^$', "posts.views.post_list"),
    url(r'^create$', "posts.views.post_create"),
    url(r'^detail', "posts.views.post_detail"),
    url(r'^create$', "posts.views.post_update"),
    url(r'^create$', "posts.views.post_delete"),
]