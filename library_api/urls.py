from django.urls import path
from library_api.views import GetReader

urlpatterns = [
    path('reader', GetReader.as_view()),
]