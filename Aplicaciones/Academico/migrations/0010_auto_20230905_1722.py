# Generated by Django 3.2 on 2023-09-05 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0009_auto_20230905_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='productos',
        ),
        migrations.DeleteModel(
            name='DetalleFactura',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
    ]