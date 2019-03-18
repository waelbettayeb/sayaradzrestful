from django.urls import path
from . import views

urlpatterns = [
    path('version/<str:Code_Version>', views.Tarif_Version_List.as_view()),
    path('option/<str:Code_Option>', views.Tarif_Option_List.as_view()),
    path('couleur/<str:Code_Couleur>', views.Tarif_Couleur_List.as_view()),
    path('stock',views.File_Up_load.as_view()),
]