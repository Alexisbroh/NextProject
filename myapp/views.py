from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import  Patient

# Create your views here.
 
def index(request):
    return render(request,'index.html')

def disponibilidad(request):
    return render(request,'disponibilidad.html')

def contactForm(request):
    return render(request, 'contact_form.html')

def precios(request):
    return render(request, 'precios.html')

def tratamientos(request):
    return render(request, 'tratamientos.html')

def signup(request):
    return render(request, 'signup.html')



