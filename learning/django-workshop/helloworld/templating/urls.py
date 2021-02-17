from django.urls import path

from templating.views import index_templating, index_render

urlpatterns = [
    # /template/hello
    path('index/', index_templating),
    path('index-render/', index_render),
]