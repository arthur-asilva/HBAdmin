# Generated by Django 4.1.4 on 2022-12-29 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_administrator_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('photo', models.CharField(default='...', max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('access_group', models.CharField(choices=[('ADM', 'Administrador'), ('PRO', 'Professor'), ('ALU', 'Aluno')], max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime(2022, 12, 29, 14, 41, 15, 420475, tzinfo=datetime.timezone.utc))),
                ('classes', models.JSONField(default={})),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('mass', models.DecimalField(decimal_places=2, max_digits=5)),
                ('exercise', models.JSONField(default={})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='administrator',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 14, 41, 15, 420475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 14, 41, 15, 420475, tzinfo=datetime.timezone.utc)),
        ),
    ]