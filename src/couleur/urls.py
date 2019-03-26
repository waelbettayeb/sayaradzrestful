from django.urls import path
from . import views

urlpatterns = [
    path('', views.All_Couleur.as_view()),
    path('new', views.New_Couleur.as_view()),
    path('<str:Id_Modele>', views.Couleur_By_Modele.as_view()),
]