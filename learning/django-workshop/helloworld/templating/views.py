from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def index_templating(request):
    template = loader.get_template('index.html')
    context = {'name': 'Sagar Budhathoki'}
    template_data = template.render(context, request)
    return  HttpResponse(template_data)


def index_render(request):
    context = {
        'info': 'This is shortcut form for rendering the context in template.'
    }
    return render(request, 'index-render.html', context)