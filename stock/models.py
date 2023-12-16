from enum import Enum
from django.db import models
from django.utils import timezone


class JenisEvent(Enum):
    MASUK = "In"
    KELUAR = "Out"
    EDIT = "Edit"


# Create your models here.
class Stock(models.Model):
    stock_id = models.CharField(primary_key=True, max_length=11)
    nama = models.CharField(max_length=10, blank=True, null=True)
    jumlah = models.FloatField()
    satuan = models.CharField(max_length=10, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    merchant = models.CharField(max_length=10, blank=True, null=True)
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
        default=JenisEvent.MASUK.value,
    )
    jumlah = models.FloatField()
    nama = models.CharField(max_length=10, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock.nama
