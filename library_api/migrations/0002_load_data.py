# Generated by Django 2.2.8 on 2019-12-03 16:24

import random
from datetime import date
from django.db import migrations

def random_date():
    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()
    return date.fromordinal(random.randint(start_date, end_date))

def load_data(apps, schema_editor):
    Reader = apps.get_model("library_api", "Reader")
    Book = apps.get_model("library_api", "Book")
    readers = []
    for i in range(50000):
        readers.append(Reader(name="Subscriber num {0}".format(str(i))))
    books = []
    for i in range(100000):
        books.append(Book(
            name="Book num {}".format(str(i)),
            date_of_publishing=random_date()
        ))
    Reader.objects.bulk_create(readers)
    readers = Reader.objects.all()
    for book in books:
        if random.randint(0, 1) == 1:
            book.reader = readers[random.randint(0, len(readers)-1)]
            book.available = False
    Book.objects.bulk_create(books)

class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]