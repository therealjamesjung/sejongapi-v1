from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel
from .serializers import ChannelCreateSerializer, ChannelRetrieveSerializer, ChannelUpdateSerializer


class ChannelCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ChannelCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(moderators=request.data.get('moderators', { request.user.profile }))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChannelRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Channel.objects.all()
    permission_classes = (IsAuthenticated, )
    retrieve_serializer_class = ChannelRetrieveSerializer
    update_serializer_class = ChannelUpdateSerializer

    def retrieve(self, request, channel_pk=None, *args, **kwargs):
        try:
            channel = self.queryset.get(pk=channel_pk)
        except Channel.DoesNotExist:
            raise NotFound('A channel with this pk does not found.')

        serializer = self.retrieve_serializer_class(channel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, channel_pk=None, *args, **kwargs):
        try:
            channel = self.queryset.get(pk=channel_pk)
        except Channel.DoesNotExist:
            raise NotFound('A channel with this pk does not found.')

        if not request.user.profile in channel.moderators.all():
            raise PermissionDenied('This user does not have permission to update this channel.')

        serializer = self.update_serializer_class(channel, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
