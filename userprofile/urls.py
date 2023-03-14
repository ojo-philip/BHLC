from django.urls import path
from .views import user_profile_update, profile


app_name = 'userprofile'
urlpatterns = [
    path('', profile, name='profile'),
    path('update/', user_profile_update, name='user_profile_update'),
]