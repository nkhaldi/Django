from django.db import models

from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(to=Author, on_delete=models.PROTECT)
