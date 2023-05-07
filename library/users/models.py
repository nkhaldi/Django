from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=False, max_length=256, verbose_name='email address')
    is_verified_email = models.BooleanField(default=False)
