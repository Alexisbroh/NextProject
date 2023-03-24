from django.db import models


# Create your models here.

class Student(models.Model):
    nameEstudiante = models.CharField(max_length=100)
    apellidoEstudiante = models.CharField(max_length=100)
    semester = models.IntegerField()

class Patient(models.Model):
    namePatient = models.CharField(max_length=100)
    lastnamePatient = models.CharField(max_length=100)
    healthCare = models.CharField(max_length=15)
    datebirth = models.CharField(max_length=15)

   
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 

class Tratamientos(models.Model):
    nombreTratamiento = models.CharField(max_length=100)    

class contact_form(models.Model):
    nombre_y_apellidos_paciente=models.CharField(max_length=100)
    numeroTelefonico=models.CharField(max_length=15)
    correoElectronico=models.CharField(max_length=25)
    seguro_medico=models.CharField(max_length=15)
    fecha_nacimiento=models.DateField()
