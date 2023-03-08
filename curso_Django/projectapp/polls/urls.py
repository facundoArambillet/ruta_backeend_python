from django.urls import path

from . import views  # El . se refiere al paquete(carpeta) que estas parado

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:question_id>", views.detail, name="detail"),
    path("results/<int:question_id>", views.results, name="results"),
    path("vote/<int:question_id>", views.vote, name="vote"),
]
