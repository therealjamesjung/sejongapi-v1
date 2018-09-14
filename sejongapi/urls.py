from django.urls import path, include

api_root = 'api/v1/'
urlpatterns = [
    path(api_root, include('apps.authentication.urls')),
    path(api_root, include('apps.profile.urls')),
]
