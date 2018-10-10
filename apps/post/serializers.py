from rest_framework import serializers

from apps.profile.serializers import ProfileSerializer

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    writer = ProfileSerializer(read_only=True)
    channel_name = serializers.CharField(source='channel.name', read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('channel_name', 'writer', 'title', 'content', 'upvoted', 'downvoted', 'is_pinned', 'comments_count', 'created_at', 'updated_at', 'id', )
        read_only_fields = ('writer', 'channel_name', 'comments_count', )

    def get_comments_count(self, article):
        return article.get_number_of_comments()


class CommentSerializer(serializers.ModelSerializer):
    writer = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('writer', 'post', )

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('upvoted', 'downvoted')
