from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import  Patient, Student, contact_form
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta
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
    return render(request, 'account/login.html')

def create_event(request):
    credentials = get_credentials()
    service = build('calendar', 'v3', credentials=credentials)
    start_time = datetime(2023, 4, 1, 10, 0, 0)  # Hora de inicio del evento
    end_time = start_time + timedelta(hours=1)  # Hora de finalización del evento
    event = {
        'summary': 'ToothBank Calendar',
        'location': 'México',
        'description': 'Aqui yu podras usar el calenadario ',
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/Mexico_City',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/Mexico_City',
        },
        'reminders': {
            'useDefault': True,
        },
    }
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        return HttpResponse(f'Evento creado: {event.get("htmlLink")}')
    except HttpError as error:
        return HttpResponse(f'Error: {error}')

