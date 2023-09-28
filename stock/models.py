from enum import Enum
from django.db import models

class JenisEvent(Enum):
    MASUK = 'Masuk'
    KELUAR = 'Keluar'

# Create your models here.
class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    jumlah = models.IntegerField()
    expired = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    jenis = models.CharField(
        max_length=7,
        choices=[(choice.value, choice.name) for choice in JenisEvent],
        default=JenisEvent.MASUK.value
    )
    
    def __str__(self):
        return self.nama
    
