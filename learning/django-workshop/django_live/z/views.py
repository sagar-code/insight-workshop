from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def home(request):
    country = request.GET.get('country', 'Nepal Country')
    return HttpResponse(f"Your country is {country}")


def display_country(request, place):
    print(HttpRequest.get_full_path(request))
    return HttpResponse(f"Displaying country: {place}")

