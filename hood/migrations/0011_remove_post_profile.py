# Generated by Django 3.2.8 on 2021-11-01 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0010_post_neighborhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]
