from rest_framework import serializers


class StockFileSerializer(serializers.Serializer):

    file = serializers.FileField()