from django.urls import path
from . import views

urlpatterns = [
    path('ComposerVehcule/',views.Compose_Vehicule.as_view()),
    path('', views.List_All_Vehicule_Composed.as_view()),
]

