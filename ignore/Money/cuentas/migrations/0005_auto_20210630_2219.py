# Generated by Django 3.1.7 on 2021-07-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_auto_20210628_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='categoria',
            field=models.CharField(choices=[('Trabajo', 'Trabajo'), ('Regalo', 'Regalo'), ('Comida', 'Comida'), ('Ropa', 'Ropa'), ('Gustico', 'Gustico')], max_length=20, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tipo',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], default='Ingreso', max_length=10, verbose_name='Tipo'),
        ),
    ]