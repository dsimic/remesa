from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class UserByEmail(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
