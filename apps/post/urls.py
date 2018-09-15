from django.urls import path, include

from .views import ArticleCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, CommentUpdateDeleteAPIView, CommentListAPIView

urlpatterns = [
    path('post/', ArticleCreateAPIView.as_view()),
    path('post/<article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('post/<article_pk>/comments/', CommentListAPIView.as_view()),
    path('post/<article_pk>/comments/<comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
]
