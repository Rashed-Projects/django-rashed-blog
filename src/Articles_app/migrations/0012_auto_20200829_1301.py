# Generated by Django 3.1 on 2020-08-29 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles_app', '0011_merge_20200829_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles_model',
            name='main',
        ),
        migrations.RemoveField(
            model_name='articles_model',
            name='status',
        ),
    ]
