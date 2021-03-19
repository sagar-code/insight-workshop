from django.shortcuts import render
from django.http import HttpResponse

from .forms import MyForm, FormsModelForm


# Create your views here.
def forms_home(request):
    if request.method == "GET":
        return render(request, 'formpractice/form.html', {})
    else:  # post method
        print(request.POST.get('name'))
        return HttpResponse("OKOKOK")


def django_form(request):
    if request.method == 'GET':
        form = MyForm()
        print(form)
        return render(request, 'formpractice/django_form.html', {'form': form})
    else:
        form_data = MyForm(request.POST)
        if form_data.is_valid():
            clean_data = form_data.cleaned_data
            return HttpResponse(f"Your form is valid: {clean_data}")
        else:
            return render(request, 'formpractice/django_form.html', {'form': form_data})


def django_model_form(request):
    if request.method == 'GET':
        form = FormsModelForm()
        print(form)
        return render(request, 'formpractice/form_model_form.html', {'form': form})
    else:
        form_data = FormsModelForm(request.POST)
        if form_data.is_valid():
            clean_data = form_data.cleaned_data
            print('djangomodel form', clean_data)
            return HttpResponse(f"Your form is valid: {clean_data}")
        else:
            return render(request, 'formpractice/form_model_form.html', {'form': form_data})
