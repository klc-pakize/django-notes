from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Models 1 seans..")  # Function to be displayed in the browser