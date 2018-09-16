from rest_framework import serializers

from apps.profile.serializers import ProfileSerializer

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    writer = ProfileSerializer(read_only = True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('writer', 'channel')

class CommentSerializer(serializers.ModelSerializer):
    writer = ProfileSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('writer', 'post')
