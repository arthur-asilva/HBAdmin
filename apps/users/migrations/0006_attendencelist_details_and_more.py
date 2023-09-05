# Generated by Django 4.1.4 on 2023-07-13 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_teacher_is_hired_alter_administrator_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendencelist',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 22, 53, 25, 6697, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='attendencelist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 22, 53, 25, 9791, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 22, 53, 25, 6697, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 22, 53, 25, 6697, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_hired',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 22, 53, 25, 10358, tzinfo=datetime.timezone.utc)),
        ),
    ]