from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotFound

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(writer = request.user, upvoted = None, downvoted = None)
        return Response(serializer.data, status = status.HTTP_201_CREATED)



class ArticleRetrieveUpdateDeleteCommentCreateAPIView(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):

    lookup_url_kwarg = 'article_pk'

    def get_serializer_class(self):
        if self.request.method == 'PATCH' or self.request.method == 'GET':
            return ArticleSerializer
        else:
            return CommentSerializer

    def get_queryset(self):
        article_pk = self.kwargs.get('article_pk')
        queryset = Article.objects.filter(id = article_pk)
        return queryset

    def update(self, request, article_pk = None, *args, **kwargs):
        try:
            serializer_instance = self.get_queryset()
        except:
            raise NotFound('A post with this primary key does not exist.') # TODO: this exception does not works

        partial = kwargs.pop('partial', False)
        serializer_instance = self.get_object()
        if serializer_instance.writer_id == request.user.id:
            serializer = self.get_serializer(serializer_instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            raise AuthenticationFailed('You are not authorized to update this post')

    def post(self, request, *args, **kwargs):
        article_pk = self.kwargs.get('article_pk')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(writer = request.user, post_id = article_pk)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self, request, article_pk = None, *args, **kwargs):
        serializer_instance = self.get_object()
        if serializer_instance.writer_id == request.user.id:
            self.perform_destroy(serializer_instance)
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            raise AuthenticationFailed('You are not authorized to delete this post')

class CommentUpdateDeleteAPIView(mixins.DestroyModelMixin, generics.UpdateAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_pk'

    def get_queryset(self):
        comment_pk = self.kwargs.get('comment_pk')
        queryset = Comment.objects.filter(id = comment_pk)
        return queryset
    def update(self, request, comment_pk = None, *args, **kwargs):
        try:
            serializer_instance = self.get_queryset()
        except:
            raise NotFound('A comment with this primary key does not exist.') # TODO: this exception does not works

        partial = kwargs.pop('partial', False)
        serializer_instance = self.get_object()
        if serializer_instance.writer_id == request.user.id:
            serializer = self.get_serializer(serializer_instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            raise AuthenticationFailed('You are not authorized to update this comment')
    def delete(self, request, comment_pk = None, *args, **kwargs):
        serializer_instance = self.get_object()
        if serializer_instance.writer_id == request.user.id:
            self.perform_destroy(serializer_instance)
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            raise AuthenticationFailed('You are not authorized to delete this comment')
