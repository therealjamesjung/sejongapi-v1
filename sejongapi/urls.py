from django.urls import path, include
from django.contrib import admin

api_root = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_root, include('apps.authentication.urls')),
    path(api_root, include('apps.profile.urls')),
    path(api_root, include('apps.channel.urls')),
    path(api_root, include('apps.post.urls')),
]
