from django.db import models
from authtools.models import AbstractEmailUser

# Create your models here.


class User(AbstractEmailUser):
    full_name = models.CharField('full_name', max_length=300)
    preferred_name = models.CharField('preferred_name', max_length=300)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.preferred_name
