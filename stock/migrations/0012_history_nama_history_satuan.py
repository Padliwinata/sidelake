# Generated by Django 4.1 on 2023-12-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0011_stock_merchant"),
    ]

    operations = [
        migrations.AddField(
            model_name="history",
            name="nama",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="history",
            name="satuan",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
