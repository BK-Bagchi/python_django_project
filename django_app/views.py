from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def djangoproject(request):  # created my custom view
    django_project_dictionary = {
        'text': 'I was sleeping in peace at home but have been sent forcefully by the django app dictionary'}
    return render(request, 'django_app/django_app.html', context=django_project_dictionary)
