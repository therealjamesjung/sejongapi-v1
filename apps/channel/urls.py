from django.urls import path

from .views import ChannelCreateAPIView, ChannelRetrieveUpdateAPIView

app_name = 'channel'
urlpatterns = [
    path('channels/', ChannelCreateAPIView.as_view()),
    path('channels/<int:channel_pk>/', ChannelRetrieveUpdateAPIView.as_view()),
]
