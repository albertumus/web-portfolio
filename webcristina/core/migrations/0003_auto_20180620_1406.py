# Generated by Django 2.0.5 on 2018-06-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180619_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizacion',
            name='menu1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título Menú 1 '),
        ),
        migrations.AddField(
            model_name='personalizacion',
            name='menu2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título Menú 2 '),
        ),
        migrations.AddField(
            model_name='personalizacion',
            name='menu3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título Menú 3 '),
        ),
        migrations.AddField(
            model_name='personalizacion',
            name='menu5',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título Menú 4 '),
        ),
    ]
