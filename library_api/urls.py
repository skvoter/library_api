from django.urls import path
from library_api.views import GetReader, GetReadersCSV, GetBooksCSV
from library_api.models import Book

urlpatterns = [
    path('reader', GetReader.as_view()),
    path('export_readers_csv', GetReadersCSV.as_view()),
    path('export_books_csv', GetBooksCSV.as_view()),
]
