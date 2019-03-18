from django.urls import path
from . import views

urlpatterns = [
    path('',views.AllVerions.as_view()),
    path('new', views.NewVersion.as_view()),
    path('<str:Id_Modele>', views.VersionByModele.as_view()),
    path('default/<str:Id_Version>', views.option_version.as_view())

]