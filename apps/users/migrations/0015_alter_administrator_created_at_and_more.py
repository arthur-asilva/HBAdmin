# Generated by Django 4.1.4 on 2023-01-03 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_administrator_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 22, 13, 53, 698831, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='attendencelist',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 22, 13, 53, 701627, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 22, 13, 53, 698831, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_access',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 22, 13, 53, 700901, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 22, 13, 53, 698831, tzinfo=datetime.timezone.utc)),
        ),
    ]
