from django.urls import path
from . import views

urlpatterns = [
    path('CreerAnnonce/',views.Annonce_Liste.as_view()),
    path('', views.List_All_Annonce.as_view()),
    path('<int:Id_Automobiliste>', views.Annonce_By_Automobiliste.as_view())
]

