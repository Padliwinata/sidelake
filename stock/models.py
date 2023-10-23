from enum import Enum
from django.db import models
from django.utils import timezone

class JenisEvent(Enum):
    MASUK = 'Masuk'
    KELUAR = 'Keluar'

# Create your models here.
class Stock(models.Model):
    stock_id = models.CharField(primary_key=True, max_length=11)
    nama = models.CharField(max_length=50)
    jumlah = models.IntegerField()
    satuan = models.CharField(max_length=10, blank=True, null=True)
    expired = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    # jenis = models.CharField(
    #     max_length=7,
    #     choices=[(choice.value, choice.name) for choice in JenisEvent],
    #     default=JenisEvent.MASUK.value
    # )
    
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

    def __str__(self):
        return self.stock.nama
    
