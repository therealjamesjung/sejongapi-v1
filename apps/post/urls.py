from django.urls import path, include

from .views import ArticleCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, CommentUpdateDeleteAPIView, CommentListAPIView

urlpatterns = [
    path('channels/<channel_pk>/posts/', ArticleCreateAPIView.as_view()),
    path('channels/<channel_pk>/posts/<article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('channels/<channel_pk>/posts/<article_pk>/comments/', CommentListAPIView.as_view()),
    path('channels/<channel_pk>/posts/<article_pk>/comments/<comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
]
