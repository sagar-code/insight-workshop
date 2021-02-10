from django.shortcuts import render

# importing HttpResponse
from django.http import HttpResponse

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

