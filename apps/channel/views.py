from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel
from .serializers import ChannelCreateSerializer, ChannelRetrieveSerializer, ChannelUpdateSerializer, SubscribeSerializer


class ChannelListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ChannelCreateSerializer
    queryset = Channel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            moderators=request.data.get('moderators', { request.user.profile }),
            subscribers=request.data.get('subscribers', { request.user.profile })
        )
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

        if request.user.profile in channel.blacklist.all():
            raise PermissionDenied('This user does not have permission to view this channel.')

        serializer = self.retrieve_serializer_class(channel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, channel_pk=None, *args, **kwargs):
        try:
            channel = self.queryset.get(pk=channel_pk)
        except Channel.DoesNotExist:
            raise NotFound('A channel with this pk does not found.')

        if not request.user.profile in channel.moderators.all():
            raise PermissionDenied('This user does not have permission to update this channel.')

        if request.user.profile in channel.blacklist.all():
            raise PermissionDenied('This user does not have permission to view this channel.')

        serializer = self.update_serializer_class(channel, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChannelSubscribeAPIView(UpdateAPIView):
    serializer_class = SubscribeSerializer
    lookup_url_kwarg = 'channel_pk'

    def get_queryset(self):
        channel_pk = self.kwargs.get('channel_pk')
        queryset = Channel.objects.filter(id = channel_pk)
        return queryset

    def update(self, request, *args, **kwargs):
        serializer_instance = self.get_object()
        for data in serializer_instance.get_subscribers().all():
            if data == request.user.profile:
                return Response('You are already subscibing this channel.')
        serializer_instance.add_subscriber(request.user.profile)
        serializer = self.get_serializer(serializer_instance, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)




class ChannelUnsubscribeAPIView(UpdateAPIView):
    serializer_class = SubscribeSerializer
    lookup_url_kwarg = 'channel_pk'
    def get_queryset(self):
        channel_pk = self.kwargs.get('channel_pk')
        queryset = Channel.objects.filter(id = channel_pk)
        return queryset

    def update(self, request, *args, **kwargs):
        serializer_instance = self.get_object()
        for data in serializer_instance.get_subscribers().all():
            if data == request.user.profile:
                serializer_instance.remove_subscriber(request.user.profile)
                serializer = self.get_serializer(serializer_instance, data = request.data, partial = True)
                serializer.is_valid(raise_exception = True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('You are already not subscibing this channel.')
