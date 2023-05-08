from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, phone, password=None, **extra_fields):
        if not username:
            raise ValueError(_('Users must have an username'))
        if not phone:
            raise ValueError(_('Users must have an Phone Number'))

        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, password=None, **extra_fields):
        extra_fields.setdefault(_('is_staff'), True)
        extra_fields.setdefault(_('is_superuser'), True)
        extra_fields.setdefault(_('is_active'), True)

        user = self.create_user(
            username,
            phone,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name=_("Username"))
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True)
    phone = models.IntegerField(verbose_name=_('Phone Number'), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
