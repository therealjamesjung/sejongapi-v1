from django.urls import path

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, \
    CommentUpdateDeleteAPIView, CommentListAPIView, ArticleUpvoteAPIView, ArticleDownvoteAPIView

urlpatterns = [
    path('<str:channel_slug>/posts/', ArticleListCreateAPIView.as_view()),
    path('posts/<int:article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('posts/<int:article_pk>/comments/', CommentListAPIView.as_view()),
    path('comments/<int:comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
    path('posts/<int:article_pk>/upvote/', ArticleUpvoteAPIView.as_view()),
    path('posts/<int:article_pk>/downvote/', ArticleDownvoteAPIView.as_view()),
]
