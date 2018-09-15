from django.urls import path, include

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, CommentUpdateDeleteAPIView, CommentListAPIView

urlpatterns = [
    path('channels/<channel_pk>/posts/', ArticleListCreateAPIView.as_view()),
    path('channels/<channel_pk>/posts/<article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('channels/<channel_pk>/posts/<article_pk>/comments/', CommentListAPIView.as_view()),
    path('channels/<channel_pk>/posts/<article_pk>/comments/<comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
]
