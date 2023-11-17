from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
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
