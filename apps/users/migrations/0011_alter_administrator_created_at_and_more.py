# Generated by Django 4.1.4 on 2023-09-12 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_attendencelist_likes_attendencelist_total_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 4, 26, 143928, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='attendencelist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 17, 4, 26, 147220, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 4, 26, 143928, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 4, 26, 143928, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 4, 26, 147945, tzinfo=datetime.timezone.utc)),
        ),
    ]
