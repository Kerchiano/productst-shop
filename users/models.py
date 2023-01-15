from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField(_("age"), null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
