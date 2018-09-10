from django.urls import path, include

from .views import ArticleCreateAPIView, ArticleRetrieveUpdateAPIView

urlpatterns = [
    path('post/', ArticleCreateAPIView.as_view()),
    path('post/<pk>/', ArticleRetrieveUpdateAPIView.as_view()),
]
