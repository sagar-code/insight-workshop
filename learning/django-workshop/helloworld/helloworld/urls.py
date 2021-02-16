"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

# importing our views.py from world app
from world.views import home, profile, profile_json, int_converter_view, debug_request


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('profile/ram-bahadur', profile),
    path('profile/<str:username>', profile),
    path('profile_json/<str:username>', profile_json),
    path('path/<str:int_data>', int_converter_view),
    path('test-path/', debug_request),

]
