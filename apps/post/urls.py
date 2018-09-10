from django.urls import path, include

from .views import ArticleCreateAPIView, ArticleListAPIView

urlpatterns = [
    path('post/', ArticleCreateAPIView.as_view()),
    path('post/<article_pk>/', ArticleListAPIView.as_view()),
]
