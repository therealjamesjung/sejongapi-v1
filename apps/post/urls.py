from django.urls import path, include

from .views import ArticleCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, CommentUpdateDeleteAPIView

urlpatterns = [
    path('post/', ArticleCreateAPIView.as_view()),
    path('post/<article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('post/<article_pk>/<comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
]
