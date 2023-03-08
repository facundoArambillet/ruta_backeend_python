from django.urls import path

from . import views  # El . se refiere al paquete(carpeta) que estas parado

app_name = "polls"

#FUNCTIONS BASED VIEWS
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("detail/<int:question_id>", views.detail, name="detail"),
#     path("results/<int:question_id>", views.results, name="results"),
#     path("vote/<int:question_id>", views.vote, name="vote"),
# ]

#GENERIC VIEWS
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail"),
    path("results/<int:pk>", views.ResultView.as_view(), name="results"),
    path("vote/<int:question_id>", views.vote, name="vote"),
]