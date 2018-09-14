from django.urls import path

from .views import ProfileRetrieveUpdateAPIView, ProfileRetrieveAPIView

app_name = 'profile'
urlpatterns = [
    path('profiles/', ProfileRetrieveUpdateAPIView.as_view()),
    path('profiles/<int:user_pk>/', ProfileRetrieveAPIView.as_view()),
]
