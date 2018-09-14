from rest_framework import serializers

from apps.profile.serializers import ProfileSerializer

from .models import Channel


class ChannelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', )

class ChannelRetrieveSerializer(serializers.ModelSerializer):
    moderators = ProfileSerializer(many=True)

    class Meta:
        model = Channel
        fields = ('name', 'description', 'rules', 'moderators', )
