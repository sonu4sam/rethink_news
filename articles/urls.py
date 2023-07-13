from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView, # new
    )

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:pk>/edit", ArticleUpdateView.as_view(), name="article_edit"),
    path('', ArticleListView.as_view(), name='article_list'),
]
