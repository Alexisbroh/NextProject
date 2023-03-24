from django.urls import path , include
from . import views
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',  views.index , name='index'),
    path('contactForm', views.contactForm , name='contactform'),
    path('precios', views.precios, name='precios'),
    path('tratamiento', views.tratamientos, name='tratamientos'),
    path('disponibilidad', views.disponibilidad, name='disponibilidad'),
    path('signup', views.signup, name='signup'),#we assigned in the signup where the api can be functionality
    path('accounts/', include('allauth.urls')),
     
]