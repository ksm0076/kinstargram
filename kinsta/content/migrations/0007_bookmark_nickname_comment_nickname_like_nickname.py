# Generated by Django 5.1 on 2024-09-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_bookmark_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='nickname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='like',
            name='nickname',
            field=models.TextField(default=''),
        ),
    ]
