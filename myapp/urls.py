from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',  views.index , name='index'),
    path('contactForm', views.contactForm , name='contactform'),
    path('precios', views.precios, name='precios'),
    path('tratamiento', views.tratamientos, name='tratamientos'),
    path('disponibilidad', views.disponibilidad, name='disponibilidad'),
    path('signup', views.signup, name='signup')
    
    

]