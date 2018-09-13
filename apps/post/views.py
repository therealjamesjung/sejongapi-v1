from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .models import Article
from .serializers import ArticleSerializer, CommentSerializer

class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(writer = request.user, upvoted = None, downvoted = None)
        return Response(serializer.data, status = status.HTTP_201_CREATED)



class ArticleRetrieveUpdateAPIView(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'PATCH' or self.request.method == 'GET':
            return ArticleSerializer
        else:
            return CommentSerializer

    def get_queryset(self):
        article_pk = self.kwargs.get('pk')
        queryset = Article.objects.filter(id = article_pk)
        return queryset

    def update(self, request, article_pk = None, *args, **kwargs):
        try:
            serializer_instance = self.get_queryset()
        except:
            raise NotFound('A post with this primary key does not exist.')

        partial = kwargs.pop('partial', False)
        serializer_instance = self.get_object()
        serializer = self.get_serializer(serializer_instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if serializer.data.get('writer') is request.user.id:
            if getattr(serializer_instance, '_prefetched_objects_cache', None):
                serializer_instance._prefetched_objects_cache = {}
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            raise AuthenticationFailed('You are not authorized to update this post')

    def post(self, request, *args, **kwargs):
        article_pk = self.kwargs.get('pk')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(writer = request.user, post_id = article_pk)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
