from io import TextIOWrapper

from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts import permissions as users_permissions

from stock import serializers
from stock.DataHandling.DataHandler import DataHandler


class UploadStock(APIView):

    parser_classes = (MultiPartParser,)
    #permission_classes = (IsAuthenticated, users_permissions.IsAdminFabriquant)
    authentication_classes = (OAuth2Authentication, )
    def post(self, request):
        serializer = serializers.StockFileSerializer(data = request.FILES)
        if serializer.is_valid():
            data_handler = DataHandler()
            response = {}
            file = TextIOWrapper(request.FILES['file'], encoding = request.encoding)
            errors, status_code = data_handler.handle_data(file)
            if not errors:
                response['success'] = True
                response['message'] = 'All the vehiculs have been successfully inserted'
                response_status = status.HTTP_200_OK
            else:
                response['success'] = False
                response.update(errors)
                if status_code == 206 :
                    response_status = status.HTTP_206_PARTIAL_CONTENT
                else:
                    response_status = status.HTTP_406_NOT_ACCEPTABLE

            return Response(data= response, status = response_status)
        else:
            return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)

