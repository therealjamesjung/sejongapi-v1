from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import RegistrationAPIView, StudentAuthAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/signup/', RegistrationAPIView.as_view()),
    path('users/login/', obtain_jwt_token),
    path('users/refresh/', refresh_jwt_token),
    path('users/auth/', StudentAuthAPIView.as_view())
]
