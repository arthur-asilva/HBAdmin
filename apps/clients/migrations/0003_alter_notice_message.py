# Generated by Django 4.1.4 on 2023-10-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_notice_media_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
