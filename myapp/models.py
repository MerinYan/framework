from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)


class MyTest(BaseUserManager):
    """BK user manager."""

    def _create_user(self, username, is_staff, is_superuser, **extra_fields):
        """Create and saves a User with the given username and password."""
        if not username:
            raise ValueError(u"'The given username must be set")

        now = timezone.now()
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, username, **extra_fields):
        return self._create_user(username, False, False,
                                 **extra_fields)

    def create_superuser(self, username, **extra_fields):
        return self._create_user(username, True, True,
                                 **extra_fields)