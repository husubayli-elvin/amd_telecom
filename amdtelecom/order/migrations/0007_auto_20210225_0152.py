# Generated by Django 3.1.4 on 2021-02-24 21:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210224_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='tel_number',
            field=models.CharField(error_messages={'required': 'Mobil nomre 7 reqemli olmalidir'}, max_length=7, validators=[django.core.validators.MinLengthValidator(7)], verbose_name='telefon'),
        ),
    ]