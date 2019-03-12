from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('',views.AllVerions.as_view()),
    path('<int : Id_Modele>', views.VersionByModele.as_view()),
    path('new', views.NewVersion.as_view())
]