from django.urls import path

from .views import ChannelCreateAPIView, ChannelListUpdateAPIView

app_name = 'channel'
urlpatterns = [
    path('channels/', ChannelCreateAPIView.as_view()),
    path('channels/<int:channel_pk>/', ChannelListUpdateAPIView.as_view()),
]
