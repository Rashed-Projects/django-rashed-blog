# Generated by Django 3.1 on 2020-08-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles_model',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
