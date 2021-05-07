from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Salom")

def second(request):
    return HttpResponse("Salom men second")