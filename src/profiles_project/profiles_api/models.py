from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager


class UserProfileManager():
    """Ayuda a Django a trabajar con nuestro modelo de usuario"""

    def create_user(self, email, name, password=None):
        """Crea un nuevo objeto user profile"""

        if not email:
            raise ValueError('Usuario debe tener una dirección email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Crea un nuevo super usuario con los datos entregados"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class UserProfiles(AbstractBaseUser, PermissionsMixin):
    """Representa un 'perfil de usuario dentro del sistema'"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Usado para obtener un nombre de usuario"""

        return self.name

    def get_short_name(self):
        """Usado para obtener un nombre corto de usuario"""

        return self.name

    def __str__(self):
        """Usado Por Django para convertir objeto en string"""

        return self.email
