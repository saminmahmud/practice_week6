# Generated by Django 4.2.7 on 2023-12-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_bankrupt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='bankrupt',
        ),
    ]
