from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django_app import forms


def djangoproject(request):
    # It somewhat looks like 'SELECT * from Musician ORDER BY first_name '
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'text': 'This view is coming from "first_app" view',
        'musician_list': musician_list
    }
    return render(request, 'django_app/django_app.html', context=diction)


def form(request):
    # data of the fields of the form copied
    new_form = forms.user_form()
    diction = {
        "text": "This form is created using Django",
        'test_form': new_form
    }
    return render(request, 'django_app/form.html', context=diction)
