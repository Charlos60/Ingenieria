# Generated by Django 3.2.8 on 2023-03-17 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='deferida_categoria',
            new_name='descripcion_categoria',
        ),
    ]