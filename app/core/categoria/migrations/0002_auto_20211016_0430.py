# Generated by Django 3.2.5 on 2021-10-16 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'managed': False, 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='subcategoria',
            options={'managed': False, 'verbose_name': 'Sub-Categoria', 'verbose_name_plural': 'Sub-Categorias'},
        ),
    ]