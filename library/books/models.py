from django.db import models

from authors.models import Author
from users.models import User


class Book(models.Model):
    name = models.CharField(max_length=128, unique=True)
    date = models.DateField(null=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
