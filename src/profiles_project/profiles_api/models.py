from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        crea y salva un usuario con email y fecha de cumpleaños
        """
        if not email:
            raise ValueError('Usuario debe tener una cuenta email')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        crea y salva un usuario con email y fecha de cumpleaños y contraseña
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Tieen el usuario un permiso especifico"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "tiene el usuario permiso para ver modulo app_label"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Es el usuario miembro del staff"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class ProfileFeedItem(models.Model):
    """profile status Update"""

    user_profiles = models.ForeignKey('Myuser', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna el modelo como un string"""

        return self.status_text
