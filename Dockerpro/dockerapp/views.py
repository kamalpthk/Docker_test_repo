from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("This is a Websites made in Django")
