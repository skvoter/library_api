import pytest
import collections
from django.db.models import Count

from library_api.models import Reader, Book
from library_api.serializers import ReaderSerializer
from library_api.views import error_message


@pytest.mark.django_db
def test_get_reader(client):
    # test success

    testreader = Reader.objects.create(name="Test Reader")
    Book.objects.bulk_create([
        Book(name="Test Book 1", reader=testreader),
        Book(name="Test Book 2", reader=testreader)
    ])
    resp = client.get("/api/reader?id=%s" % testreader.id)
    ser = ReaderSerializer(testreader)
    assert resp.data == ser.data

    # test failure

    resp = client.get("/api/reader")
    assert resp.data == error_message('Please specify id')
    # test failure #2
    
    resp = client.get("/api/reader?id=100500")
    assert resp.data == error_message('Not Found')
    assert resp.status_code == 404


def get_csv(lst):
    sorted_list = [collections.OrderedDict(sorted(entry.items())) for entry in lst]
    result = ','.join(sorted_list[0].keys()) + '\r\n'
    for item in sorted_list:
        for key in item:
            item[key] = str(item[key])
        result += ','.join(item.values()) + '\r\n'
    return result.encode()

@pytest.mark.django_db
def test_csv_export(client):
    testreader = Reader.objects.create(name="Test Reader")

    Book.objects.bulk_create([
        Book(name="Test Book 1", reader=testreader),
        Book(name="Test Book 2", reader=testreader)
    ])
    resp = client.get("/api/export_readers_csv")
    # test manually set header
    assert resp['Content-Disposition'] == 'attachment; filename=library_readers.csv'
    # test data is actually what we want
    expected_data = list(Reader.objects.annotate(Count("books")).values())
    assert resp.data == expected_data
    # test data is actually csv
    assert resp.rendered_content == get_csv(expected_data)
