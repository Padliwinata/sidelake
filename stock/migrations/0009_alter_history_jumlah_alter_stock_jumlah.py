# Generated by Django 4.1 on 2023-12-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_history_satuan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='jumlah',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='jumlah',
            field=models.FloatField(),
        ),
    ]
