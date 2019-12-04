import datetime
from django.db import models

# Create your models here.

class Reader(models.Model):

    name = models.CharField(max_length=150)

class Book(models.Model):

    name = models.CharField(max_length=140)
    date_of_publishing = models.DateField(default=datetime.date(1970, 1, 1))
    available = models.BooleanField(default=True)
    reader = models.ForeignKey(
        Reader,
        on_delete=models.PROTECT,
        related_name="books",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.reader:
            self.available = False
        super().save(*args, **kwargs)
