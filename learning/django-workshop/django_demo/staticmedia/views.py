from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Create your views here.
def render_static(request):
    return render(request, 'static.html', {})


def manage_media(request):
    if request.method == 'POST':
        print("Post Data: ", request.POST)
        print("FIles: ", request.FILES)

        file_obj = request.FILES['file']
        print("my file name is", file_obj.name)
        file_system = FileSystemStorage()
        filename = file_system.save(file_obj.name, file_obj)
        print('after save file name is', filename)


    return render(request, 'media.html', {})