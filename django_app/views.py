from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def djangoproject(request):  # created my custom view
    return HttpResponse('Starting a project as part of learning Django. Hope this project will be a fun.')
