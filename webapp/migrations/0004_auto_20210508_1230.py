# Generated by Django 3.1.6 on 2021-05-08 07:00

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='date',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='receiver',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='sender',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='transaction_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]