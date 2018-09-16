from rest_framework import serializers

from apps.profile.serializers import ProfileSerializer

from .models import Channel


class ChannelCreateSerializer(serializers.ModelSerializer):
    moderators = ProfileSerializer(many=True, read_only=True)
    subscribers = ProfileSerializer(many=True, read_only=True)
    blacklist = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', 'subscribers', 'blacklist', )


class ChannelRetrieveSerializer(serializers.ModelSerializer):
    moderators = ProfileSerializer(many=True)
    subscribers = ProfileSerializer(many=True)
    blacklist = ProfileSerializer(many=True)

    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', 'subscribers', 'blacklist', )

        
class ChannelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', 'subscribers', 'blacklist', )
