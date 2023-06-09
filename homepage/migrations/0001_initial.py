# Generated by Django 4.1 on 2023-05-15 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(blank=True)),
                ('position', models.CharField(max_length=30)),
                ('date_pub', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
