# Generated by Django 4.0.3 on 2022-03-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstation',
            name='diesel_price',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Precio de gasolina premium'),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='premium_gasoline_price',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Precio de gasolina premium'),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='regular_gasoline_price',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Precio de gasolina regular'),
        ),
    ]
