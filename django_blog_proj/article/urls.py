from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("addarticle/", views.add_article, name="addarticle"),
    path("article/<int:id>", views.detail, name="detail"),
    path("update/<int:id>", views.update_article, name="update"),
    path("delete/<int:id>", views.delete_article, name="delete"),
    path("", views.articles, name="articles"),
    path("comment/<int:id>", views.add_comment, name="comment"),
]
