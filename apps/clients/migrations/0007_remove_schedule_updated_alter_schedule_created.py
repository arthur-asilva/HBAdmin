# Generated by Django 4.1.4 on 2023-10-01 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_alter_schedule_professional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='updated',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 21, 34, 29, 975467, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
