from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email'))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(email, password=password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True)
    phone = models.IntegerField(verbose_name=_('Phone Number'), unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    is_staff = models.BooleanField(default=False, verbose_name=_("is_staff"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("is_superuser"))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
