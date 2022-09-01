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
    new_form = forms.user_form()
    diction = {
        "text": "This form is created using Django",
        'test_form': new_form,
    }
    #
    if request.method == 'POST':
        new_form = forms.user_form(request.POST)
        #
        if new_form.is_valid():
            user_name = new_form.cleaned_data["user_name"]
            user_email = new_form.cleaned_data["user_email"]
            user_birthday = new_form.cleaned_data["user_birthday"]
            #
            diction.update({'user_name': user_name})
            diction.update({'user_email': user_email})
            diction.update({'user_birthday': user_birthday})
            diction.update({'form_submitted': 'True'})
        #
    return render(request, 'django_app/form.html', context=diction)
