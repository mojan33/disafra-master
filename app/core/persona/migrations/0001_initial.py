# Generated by Django 3.2.5 on 2021-09-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.IntegerField(db_column='ID_PERSONA', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=50)),
                ('apellido', models.CharField(db_column='APELLIDO', max_length=50)),
                ('fecha_nacimiento', models.DateField(db_column='FECHA_NACIMIENTO')),
                ('edad', models.IntegerField(db_column='EDAD')),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
    ]
