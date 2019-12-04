from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    date_of_publishing = serializers.DateField()
    available = serializers.BooleanField()

class ReaderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    books = BookSerializer(many=True)