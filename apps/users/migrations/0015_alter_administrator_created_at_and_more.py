# Generated by Django 4.1.4 on 2023-10-01 21:34

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
            field=models.DateField(default=datetime.datetime(2023, 10, 1, 21, 34, 29, 967955, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='attendencelist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 21, 34, 29, 970792, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 1, 21, 34, 29, 967955, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 1, 21, 34, 29, 967955, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 1, 21, 34, 29, 971418, tzinfo=datetime.timezone.utc)),
        ),
    ]