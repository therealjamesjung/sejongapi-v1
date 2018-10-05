from rest_framework import serializers

from apps.profile.serializers import ProfileSerializer

from .models import Channel


class ChannelCreateSerializer(serializers.ModelSerializer):
    moderators = ProfileSerializer(many=True, read_only=True)
    subscribers = ProfileSerializer(many=True, read_only=True)
    blacklist = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', 'subscribers', 'blacklist', 'created_at', 'updated_at',)


class ChannelRetrieveSerializer(serializers.ModelSerializer):
    moderators = ProfileSerializer(many=True)
    subscribers = ProfileSerializer(many=True)
    blacklist = ProfileSerializer(many=True)

    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', 'subscribers', 'blacklist', 'created_at', 'updated_at',)


class ChannelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', 'subscribers', 'blacklist', 'created_at', 'updated_at',)


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('subscribers',)
