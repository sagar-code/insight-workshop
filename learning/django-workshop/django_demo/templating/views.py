from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def hello_templates(request):
    template = loader.get_template('hello.html')
    context = {
        'name': 'Sagar Budhathoki'
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)


def hello_render(request):
    context = {
        'name': 'Rabina Karki'
    }

    return render(request, 'hello-render.html', context)