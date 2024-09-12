# Generated by Django 5.0 on 2024-09-12 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('interval', models.DurationField(default=datetime.timedelta(days=1))),
            ],
        ),
    ]
