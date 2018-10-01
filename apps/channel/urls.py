from django.urls import path

from .views import ChannelListCreateAPIView, ChannelRetrieveUpdateAPIView, ChannelSubscribeAPIView, ChannelUnsubscribeAPIView

app_name = 'channel'
urlpatterns = [
    path('channels/', ChannelListCreateAPIView.as_view()),
    path('channels/<int:channel_pk>/', ChannelRetrieveUpdateAPIView.as_view()),
    path('channels/<int:channel_pk>/subscribe/', ChannelSubscribeAPIView.as_view()),
    path('channels/<int:channel_pk>/unsubscribe/', ChannelUnsubscribeAPIView.as_view()),
]
