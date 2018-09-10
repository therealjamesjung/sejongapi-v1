from django.urls import path, include

from .views import ArticleListCreateAPIView

urlpatterns = [
    path('post/', ArticleListCreateAPIView.as_view()),
]
