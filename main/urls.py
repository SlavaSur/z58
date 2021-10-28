from django.urls import path
from main.views import hello
from django.http import HttpResponse

urlpatterns = [
    path ('', hello),
]