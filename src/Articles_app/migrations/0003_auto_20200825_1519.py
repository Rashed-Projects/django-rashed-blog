# Generated by Django 3.1 on 2020-08-25 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articles_app', '0002_articles_model_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles_model',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
