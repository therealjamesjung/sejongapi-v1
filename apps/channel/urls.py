from django.urls import path

from .views import (
    ChannelListCreateAPIView,
    ChannelRetrieveUpdateAPIView,
    ChannelSubscribeAPIView, ChannelUnsubscribeAPIView
)

app_name = 'channel'
urlpatterns = [
    path('channels/', ChannelListCreateAPIView.as_view()),
    path('<str:channel_slug>/', ChannelRetrieveUpdateAPIView.as_view()),
    path('<str:channel_slug>/subscribe/', ChannelSubscribeAPIView.as_view()),
    path('<str:channel_slug>/unsubscribe/', ChannelUnsubscribeAPIView.as_view()),
]
