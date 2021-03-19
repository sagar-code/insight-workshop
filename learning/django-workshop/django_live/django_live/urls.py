from django.contrib import admin
from django.urls import path

from z.views import home, display_country

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('display_country/<str:place>/', display_country)
]
