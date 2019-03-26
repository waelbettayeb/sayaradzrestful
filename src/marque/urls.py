from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListeMarques.as_view()),
    path('new', views.NewMarque.as_view()),
]