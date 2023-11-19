from django.urls import path

from main.apps import MainConfig
from main.views import FormAPIView

app_name = MainConfig.name

urlpatterns = [
    path("get_form/", FormAPIView.as_view(), name='get-form')
]
