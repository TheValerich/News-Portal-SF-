from django.urls import path
from .views import (
    NewsList, NewsDetail, PostCreateView, PostUpdateView, PostDeleteView, NewsSearch
)


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),

    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('articles/create/', PostCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', PostUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDeleteView.as_view(), name='article_delete'),

    path('search/', NewsSearch.as_view(), name='news_search')
]
