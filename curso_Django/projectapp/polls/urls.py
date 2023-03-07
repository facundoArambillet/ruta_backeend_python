from django.urls import path

from . import views #El . se refiere al paquete(carpeta) que estas parado

urlpatterns = [
    path("",views.index, name="index")
]
    
