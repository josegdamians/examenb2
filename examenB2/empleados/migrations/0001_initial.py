# Generated by Django 3.2.4 on 2021-06-11 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apat', models.CharField(max_length=50)),
                ('amat', models.CharField(max_length=50)),
                ('fechanacimiento', models.DateField()),
                ('correo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=1)),
                ('telefono', models.CharField(max_length=12)),
                ('celular', models.CharField(max_length=10)),
                ('fechaingreso', models.DateField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.departamento')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empresa')),
            ],
        ),
    ]
