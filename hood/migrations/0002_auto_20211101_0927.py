# Generated by Django 3.2.8 on 2021-11-01 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_center', models.CharField(max_length=40)),
                ('center_number', models.CharField(max_length=15)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_station', models.CharField(max_length=30)),
                ('station_number', models.CharField(max_length=15)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood')),
            ],
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]