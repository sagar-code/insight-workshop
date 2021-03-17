from django.contrib import admin
from django.urls import path, include

from world.views import home, profile, profile_json, int_convertor_view, debug_request

urlpatterns = [
    path('home/', home),
    path('profile/<str:username>/', profile),
    path('profile-json/<str:username>/', profile_json),
    path('path/<str:int_data>/', int_convertor_view),
    path('test/', debug_request),
    path('template/', include('templating.urls'))
]
