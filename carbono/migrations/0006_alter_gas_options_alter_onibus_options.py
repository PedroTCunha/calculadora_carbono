# Generated by Django 5.1.1 on 2024-10-19 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carbono', '0005_rename_modo_de_calcuo_gas_modo_de_calculo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gas',
            options={'verbose_name_plural': 'Gás'},
        ),
        migrations.AlterModelOptions(
            name='onibus',
            options={'verbose_name_plural': 'Ônibus'},
        ),
    ]