from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import RegistrationAPIView

app_name = 'auth'
urlpatterns = [
    path('auth/register/', RegistrationAPIView.as_view()),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
]
