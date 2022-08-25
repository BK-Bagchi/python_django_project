from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    # It somewhat looks like 'SELECT * from Musician ORDER BY first_name ASC'
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'text': 'This view is coming from "first_app" view',
        'musician_list': musician_list
    }
    return render(request, 'first_app/index.html', context=diction)
