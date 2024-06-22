# Generated by Django 5.0.2 on 2024-06-20 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion_clases', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('tel', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('matricula', models.BooleanField(default=False)),
                ('inasistencias', models.IntegerField(default=0)),
                ('pago_al_dia', models.BooleanField(default=False)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.curso')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.estado')),
            ],
        ),
    ]