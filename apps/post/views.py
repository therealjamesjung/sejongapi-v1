from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(writer = request.user, upvoted = None, downvoted = None)
        return Response(serializer.data, status = status.HTTP_201_CREATED)



class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        article_pk = self.kwargs.get('article_pk')
        queryset = Article.objects.filter(id = article_pk)
        return queryset
