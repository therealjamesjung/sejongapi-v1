from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Profile
from .serializers import ProfileSerializer, FollowerSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def retrieve(self, request, user_pk=None, *args, **kwargs):
        try:
            profile = self.queryset.get(pk=user_pk)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            profile = self.queryset.get(user=request.user)
        except Profile.DoesNotExist:
            raise NotFound('This user does not have a profile.')

        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            profile = self.queryset.get(user=request.user)
        except Profile.DoesNotExist:
            raise NotFound('This user does not have a profile.')

        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowUpdateAPIView(UpdateAPIView):
    serializer_class = FollowerSerializer
    lookup_url_kwarg = 'user_pk'

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        queryset = Profile.objects.filter(user_id=user_pk)
        return queryset

    def update(self, request, *args, **kwargs):
        serializer_instance = self.get_object()
        for data in serializer_instance.get_followers().all():
            if data == request.user.profile:
                return Response('You are already following this user.')
        serializer_instance.add_follower(request.user.profile)
        serializer = self.get_serializer(serializer_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnfollowUpdateAPIView(UpdateAPIView):
    serializer_class = FollowerSerializer
    lookup_url_kwarg = 'user_pk'

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        queryset = Profile.objects.filter(user_id=user_pk)
        return queryset

    def update(self, request, *args, **kwargs):
        serializer_instance = self.get_object()
        for data in serializer_instance.get_followers().all():
            if data == request.user.profile:
                serializer_instance.remove_follower(request.user.profile)
                serializer = self.get_serializer(serializer_instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('You are already unfollowing this user.')
