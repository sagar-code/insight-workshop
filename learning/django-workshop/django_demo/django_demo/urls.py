from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from world.views import home, profile, profile_json, int_convertor_view, debug_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('profile/<str:username>/', profile),
    path('profile-json/<str:username>/', profile_json),
    path('path/<str:int_data>/', int_convertor_view),
    path('test/', debug_request),
    path('template/', include('templating.urls')),
    path('forms/', include('formspractice.urls')),
    path('static-demo/', include('staticmedia.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
