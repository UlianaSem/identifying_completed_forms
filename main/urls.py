from django.urls import path

from main.apps import MainConfig
from main.views import get_form

app_name = MainConfig.name

urlpatterns = [
    path("get_form/", get_form, name='get-form')
]
