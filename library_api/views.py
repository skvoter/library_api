from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from rest_framework.response import Response

from library_api.models import Reader, Book
from library_api.serializers import ReaderSerializer


# Create your views here.

def error_message(msg):
    return {'error': msg}


class GetReader(APIView):

    def get(self, request):
        pk = request.query_params.get('id')
        if not pk:
            return Response(error_message('Please specify id'))
        try:
            instance = Reader.objects.prefetch_related('books').get(id=pk)
        except Reader.DoesNotExist:
            return Response(error_message('Not Found'), status=404)
        else:
            ser = ReaderSerializer(instance)
            return Response(ser.data)

# Common view for CSV export
class GetCSV(APIView):

    renderer_classes = (r.CSVRenderer, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    queryset = None
    def get(self, request):
        return Response(list(self.queryset.all()))

# Readers CSV export
class GetReadersCSV(GetCSV):

    queryset = Reader.objects.annotate(Count("books")).values()


# Books CSV export
class GetBooksCSV(GetCSV):

    queryset = Book.objects.values()
