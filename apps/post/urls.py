from django.urls import path, include

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, CommentUpdateDeleteAPIView, CommentListAPIView, ArticleUpvoteAPIView, ArticleDownvoteAPIView
urlpatterns = [
    path('channels/<int:channel_pk>/posts/', ArticleListCreateAPIView.as_view()),
    path('posts/<int:article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('posts/<int:article_pk>/comments/', CommentListAPIView.as_view()),
    path('comments/<int:comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
    path('posts/<int:article_pk>/upvote/', ArticleUpvoteAPIView.as_view()),
    path('posts/<int:article_pk>/downvote/', ArticleDownvoteAPIView.as_view()),
]
