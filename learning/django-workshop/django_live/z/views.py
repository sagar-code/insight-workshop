from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    country = request.GET.get('country', 'Nepal')
    return HttpResponse(f"Your country is {country}")
