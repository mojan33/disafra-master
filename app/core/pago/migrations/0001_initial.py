# Generated by Django 3.2.5 on 2021-09-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PagoCompra',
            fields=[
                ('num_pago', models.IntegerField(db_column='NUM_PAGO', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='DESCRIPCION', max_length=255, null=True)),
                ('fecha_pago', models.DateField(db_column='FECHA_PAGO')),
                ('cantidad_pagada', models.DecimalField(db_column='CANTIDAD_PAGADA', decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'pago_compra',
                'managed': False,
            },
        ),
    ]