from django.contrib import admin
from django.urls import path

# this lice needs to be included for url mapping
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # here whatever is created in the "django_app" will be shown to the user
    # writing of this format is used for url mapping
    path('django/', include('django_app.urls'))
]
