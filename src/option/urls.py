from django.urls import path
from . import views

urlpatterns = [
    path('',views.List_All_Options.as_view()),
    path('new', views.New_Option.as_view()),
    path('version/<str:Id_Version>', views.Option_Version.as_view())
]