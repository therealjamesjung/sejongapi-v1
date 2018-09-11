from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel
from .serializers import ChannelSerializer


class ChannelCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ChannelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChannelListUpdateAPIView(ListAPIView, UpdateAPIView):
    queryset = Channel.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ChannelSerializer

    def list(self, request, channel_pk=None, *args, **kwargs):
        try:
            channel = Channel.objects.filter(pk=channel_pk)
        except Channel.DoesNotExist:
            raise NotFound('A channel with this pk does not found.')

        serializer = self.get_serializer(channel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, channel_pk=None, *args, **kwargs):
        try:
            channel = self.queryset.get(pk=channel_pk)
        except Channel.DoesNotExist:
            raise NotFound('A channel with this pk does not found.')

        serializer = self.get_serializer(channel, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
