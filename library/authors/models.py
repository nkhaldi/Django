from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)
    birth = models.DateField(null=None)
    image = models.ImageField(upload_to='authors_images')
