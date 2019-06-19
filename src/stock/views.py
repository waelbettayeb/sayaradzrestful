from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from stock import serializers
from stock.DataHandling.CSVFileReader import CsvFileReader
from stock.DataHandling.DataHandler import DataHandler


class UploadStock(APIView):

    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = serializers.StockFileSerializer(data = request.FILES)
        file_reader = CsvFileReader()
        print(request.data)
        if serializer.is_valid():
            data_handler = DataHandler()
            errors = data_handler.handle_data(request.FILES['file'])
            #print(errors)
            return Response(data= serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('Not valid')
            print(serializer.data)
            return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)

