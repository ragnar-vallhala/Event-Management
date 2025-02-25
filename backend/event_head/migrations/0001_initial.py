# Generated by Django 5.1.1 on 2025-02-01 02:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('event', '0002_event_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventHead',
            fields=[
                ('EventHead_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('EventHead_Name', models.CharField(blank=True, max_length=50)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]
