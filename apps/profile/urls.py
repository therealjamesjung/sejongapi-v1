from django.urls import path

from .views import ProfileRetrieveUpdateAPIView, ProfileRetrieveAPIView, FollowUpdateAPIView, UnfollowUpdateAPIView

app_name = 'profile'
urlpatterns = [
    path('profiles/', ProfileRetrieveUpdateAPIView.as_view()),
    path('profiles/<int:user_pk>/', ProfileRetrieveAPIView.as_view()),
    path('profiles/<int:user_pk>/follow/', FollowUpdateAPIView.as_view()),
    path('profiles/<int:user_pk>/unfollow/', UnfollowUpdateAPIView.as_view()),
]
