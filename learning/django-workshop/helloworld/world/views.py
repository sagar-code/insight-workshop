from django.shortcuts import render

# importing HttpResponse
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse


# Create your views here.
def home(request):
    response = HttpResponse()
    response.content = "Hi, from the view section of world app."
    return response
    # or
    # return HttpResponse("Hi, from the view section of world app.")


# /profile/<username>/
def profile(request, username):
    # print(f"Name is: {name}")

    # creating simple data
    data = {
        'ram': 'Ram Bahadur',
        'hari': 'Hari Bahadur',
        'shyam': 'Shyam Bahadur',
    }

    # full_name = data[username]
    full_name = data.get(username)

    if not full_name:
        # return HttpResponseNotFound("The username doesn't exist.")
        return HttpResponseNotFound("The username doen't exist.", status=404)

    string_data = f"Your full name is {full_name}."

    return HttpResponse(string_data)


def profile_json(request, username):
    print(username, type)
    data = {
        'ram': 'Ram Bahadur',
        'hari': 'Hari Bahadur',
        'shyam': 'Shyam Bahadur',
    }

    # full_name = data[username]
    full_name = data.get(username)

    if not full_name:
        # return HttpResponseNotFound("The username doesn't exist.")
        return HttpResponseNotFound("The username doesn't exist.", status=404)

    dict_data = {
        "fullname": full_name
    }

    return JsonResponse(dict_data)


def int_converter_view(request, int_data):
    print(type(int_data))
    try:
        converted_int_data = int(int_data)
        # use _ if variable is not used
        _ = converted_int_data
    except ValueError:
        return HttpResponse("Something is wrong.", status=404)
    return HttpResponse("Ok, Ok, Ok")


def debug_request(request):
    # HttpRequest Object
    print('request:', request)
    print('request scheme:', request.scheme)
    print('request.path:', request.path)
    print('request method:', request.method)
    print('request GET:', request.GET)
    print('request POST:', request.POST)
    print('request files:', request.FILES)
    print('request Header:', request.headers)
    print('request Cookies:', request.COOKIES)
    print('request content-type:', request.content_type)

    # HttpRequest Methods
    print('Request host:', request.get_host())
    print('Request port:', request.get_port())
    print('Request full path:', request.get_full_path())
    print('Request full path info:', request.get_full_path_info())
    print('Request is_secure:', request.is_secure())
    print('Request is_ajax:', request.is_ajax())

    return HttpResponse("Okay, from the debug.")
