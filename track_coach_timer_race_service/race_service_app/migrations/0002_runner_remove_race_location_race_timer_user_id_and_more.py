# Generated by Django 5.0.1 on 2024-03-29 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_service_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='race',
            name='location',
        ),
        migrations.AddField(
            model_name='race',
            name='timer_user_id',
            field=models.CharField(default='defaultuserid', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='title',
            field=models.CharField(default='Default Title', max_length=50),
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lap_number', models.IntegerField()),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='split', to='race_service_app.race')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='split', to='race_service_app.runner')),
            ],
        ),
    ]
