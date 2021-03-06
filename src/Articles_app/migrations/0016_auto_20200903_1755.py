# Generated by Django 3.1 on 2020-09-03 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles_app', '0015_delete_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Articles_app.articles_model'),
        ),
    ]
