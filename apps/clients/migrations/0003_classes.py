# Generated by Django 4.1.4 on 2022-12-26 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_administrator_created_at_and_more'),
        ('clients', '0002_client_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=5)),
                ('weekday', models.IntegerField(choices=[(0, 'Segunda'), (1, 'Terça'), (2, 'Quarta'), (3, 'Quinta'), (4, 'Sexta'), (5, 'Sábado'), (6, 'Domingo')])),
                ('service', models.CharField(max_length=250)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client', to='clients.client')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to='users.teacher')),
            ],
        ),
    ]
