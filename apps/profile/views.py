from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Profile
from .serializers import ProfileSerializer


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
