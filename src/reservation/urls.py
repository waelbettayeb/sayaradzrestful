from django.urls import path
from . import views

urlpatterns = [
    path('valider', views.valider.as_view()),
    path('commande/new', views.Commander.as_view()),
    path('vehicule/disponible', views.Disponible.as_view()),
    path('commande/<str:Id_Marque>', views.Reservations.as_view()),
    path('vehicule/<str:Id_Marque>', views.Vehicules.as_view())

]