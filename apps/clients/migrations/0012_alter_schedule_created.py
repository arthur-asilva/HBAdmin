# Generated by Django 4.1.4 on 2023-10-10 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_alter_classes_client_alter_classes_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 21, 14, 33, 903010, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]