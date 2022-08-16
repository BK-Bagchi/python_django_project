# this custom created page and the content of this page is used for url mapping
from django.urls import path
from django_app import views

urlpatterns = [
    path('django_app/', views.djangoproject, name='djangoproject')
]
