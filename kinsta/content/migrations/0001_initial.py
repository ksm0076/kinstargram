# Generated by Django 5.1 on 2024-08-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.TextField()),
                ('user_id', models.TextField()),
                ('image', models.TextField()),
                ('content', models.TextField()),
                ('like_count', models.IntegerField()),
            ],
        ),
    ]
