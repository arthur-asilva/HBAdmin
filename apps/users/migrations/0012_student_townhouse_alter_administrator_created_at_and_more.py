# Generated by Django 4.1.4 on 2023-09-12 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_classes_weekday'),
        ('users', '0011_alter_administrator_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='townhouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='townhouse', to='clients.client'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 9, 54, 778699, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='attendencelist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 17, 9, 54, 781530, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 9, 54, 778699, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 9, 54, 778699, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 17, 9, 54, 782288, tzinfo=datetime.timezone.utc)),
        ),
    ]