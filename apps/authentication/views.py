from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from .serializers import RegistrationSerializer

import requests


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentAuthAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        url = 'https://udream.sejong.ac.kr/main/loginPro.aspx'
        payload = \
            {
                'rUserid': request.data.get('student_id'),
                'rPW': request.data.get('password'),
                'pro': '1'
            }

        headers = \
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        response = requests.post(url=url, data=payload, headers=headers)
        if response.text.find('alert') == -1:
            return Response('This user is student-authenticated.')
        else:
            return Response('This user is not student-authenticated.', status=status.HTTP_403_FORBIDDEN)
