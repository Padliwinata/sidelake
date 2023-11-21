from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password='Password', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    class Merchant(models.TextChoices):
        LAKESIDE = 'Lakeside', 'Lakeside Cafe FIK'
        AGROPEDIA = 'Agropedia', 'Agropedia Workspace RAA'
        LITERASI = 'Literasi', 'Literasi Cafe Open Library'
    
    merchant = models.CharField(
        max_length=10,
        choices=Merchant.choices,
        default=Merchant.LAKESIDE
    )

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
