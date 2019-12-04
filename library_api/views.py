from rest_framework.views import APIView
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
