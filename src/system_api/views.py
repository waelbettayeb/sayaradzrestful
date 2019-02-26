from django.http import HttpResponse
from .models import Version
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from  rest_framework.response import Response
from rest_framework import status



