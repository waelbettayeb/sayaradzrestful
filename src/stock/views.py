from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from stock import serializers
from stock.DataHandling.DataHandler import DataHandler


class UploadStock(APIView):

    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = serializers.StockFileSerializer(data = request.FILES)
        print(request.data)
        if serializer.is_valid():
            data_handler = DataHandler()
            response = {}
            errors = data_handler.handle_data(request.FILES['file'])
            if not errors:
                response['success'] = True
                response['message'] = 'All the vehiculs have been successfully inserted'
                response_status = status.HTTP_200_OK
            else:
                response['success'] = False
                response.update(errors)
                response_status = status.HTTP_207_MULTI_STATUS

            return Response(data= response, status = response_status)
        else:
            print('Not valid')
            print(serializer.data)
            return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)

