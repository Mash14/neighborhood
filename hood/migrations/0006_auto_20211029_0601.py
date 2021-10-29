# Generated by Django 3.2.8 on 2021-10-29 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0005_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='post/'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('image', models.ImageField(blank=True, upload_to='post/')),
                ('description', tinymce.models.HTMLField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
