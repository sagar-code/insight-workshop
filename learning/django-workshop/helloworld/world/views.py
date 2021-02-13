from django.shortcuts import render


# importing HttpResponse
from django.http import HttpResponse


# importing python module
import datetime


# Create your views here.
# function based views


def home(request):
    response = HttpResponse()
    response.content = "<h1 style='color:red;'>Hello World</h1>"
    return response

    # or we can written as
    # return HttpResponse("Hello World")

def html(request):
    html_content = """
    <html>
    <body>
        <h1 style="font-size: 80px">This is comming from html content</h1>
        <p>This is my first web application in Django.</p>
    </body>
    <html>
    """

    return HttpResponse(html_content)


def date_time(request):
    now = datetime.datetime.now()
    date_content = f"""
    <h1> Today date: {now} </h1>
    """
    return HttpResponse(date_content)


def get_post(request):
    if request.method == 'GET':
        return HttpResponse(request.scheme)
    elif request.method == 'POST':
        return HttpResponse(request.method)


