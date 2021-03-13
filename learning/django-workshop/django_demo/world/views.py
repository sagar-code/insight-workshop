from django.http import HttpResponse, HttpResponseNotFound, JsonResponse


def home(request):
    return HttpResponse("Hi, from Home.")


def profile(request, username):

    data = {
        'ram': 'Ram Bahadur',
        'shyam': 'Shyam Bahadur',
        'hari': 'Hari Bahadur',
    }

    full_name = data.get(username)

    if not full_name:
        return HttpResponseNotFound("You have enter the wrong username.")
        # or
        # return HttpResponse('Username not found.',status=404)

    string_data = "Your name is {}.".format(full_name)

    return HttpResponse(string_data)


def profile_json(request, username):

    data = {
        'ram': 'Ram Bahadur',
        'shyam': 'Shyam Bahadur',
        'hari': 'Hari Bahadur',
    }

    full_name = data.get(username)

    if not full_name:
        return HttpResponseNotFound("You have enter the wrong username.")

    json_data = {
        'full-name': full_name
    }

    return JsonResponse(json_data)


def int_convertor_view(request, int_data):
    print(type(int_data))

    try:
        _ = int(int_data)
    except ValueError:
        return HttpResponse("Something is wrong.", status=404)



    return HttpResponse("Ok Ok Ok")


def debug_request(request):

    print('Request Method: ', request.method)
    print('Body: ', request.body)
    print('Scheme: ', request.scheme)
    print('Headers: ', request.headers)
    print('Request GET: ', request.GET)

    return HttpResponse('Okay from debug')