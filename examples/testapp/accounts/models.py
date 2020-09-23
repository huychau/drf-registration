from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _('username'), unique=True, max_length=50,
        validators=[MinLengthValidator(2),])
    password = models.CharField(_('password'), max_length=128)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
