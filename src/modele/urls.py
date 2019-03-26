from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListAllModels.as_view()),
    path('<int:Id_Marque>', views.ModelesByMarque.as_view()),
    path('new', views.NewModele.as_view())
]