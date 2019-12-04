import pytest

from library_api.models import Reader, Book

@pytest.mark.django_db
def test_availability_change():
    book = Book.objects.create(name="Test Book")
    assert book.reader is None
    assert book.available is True

    reader = Reader.objects.create(name="Test Reader")
    book.reader = reader
    book.save()
    assert book.available is False
