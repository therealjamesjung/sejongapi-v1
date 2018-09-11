from rest_framework import serializers

from apps.profile.serializers import ProfileSerializer

from .models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', )
