# Generated by Django 2.0.5 on 2018-06-25 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entrada_de_blog_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada_de_blog',
            name='page_slug',
        ),
    ]
