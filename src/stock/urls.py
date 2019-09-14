from django.urls import path

from stock import views

urlpatterns = [
    path('upload',views.UploadStock.as_view()),

]