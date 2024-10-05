from django.urls import path
from myApp.views import form

urlpatterns = [
    path('', form),
]
