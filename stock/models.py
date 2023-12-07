from enum import Enum
from django.db import models
from django.utils import timezone
from custom_auth.models import CustomUser

class JenisEvent(Enum):
    MASUK = 'In'
    KELUAR = 'Out'
    EDIT = 'Edit'

# Create your models here.
class Stock(models.Model):
    stock_id = models.CharField(primary_key=True, max_length=11)
    nama = models.CharField(max_length=10, blank=True, null=True)
    jumlah = models.IntegerField()
    satuan = models.CharField(max_length=10, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    # added_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    merchant = models.CharField(blank=True, null=True, max_length=20)
    
    def __str__(self):
        return self.nama


class History(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    jenis = models.CharField(
        max_length=7,
        choices=[(choice.value, choice.name) for choice in JenisEvent],
        default=JenisEvent.MASUK.value
    )
    jumlah = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.stock.nama
    
