# Generated by Django 3.1.4 on 2021-04-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210427_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='product',
            name='instagram',
        ),
    ]