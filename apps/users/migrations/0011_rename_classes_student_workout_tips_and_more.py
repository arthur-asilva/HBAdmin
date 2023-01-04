# Generated by Django 4.1.4 on 2023-01-02 23:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_classes_is_active'),
        ('users', '0010_merge_20230102_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='classes',
            new_name='workout_tips',
        ),
        migrations.RemoveField(
            model_name='student',
            name='exercise',
        ),
        migrations.AddField(
            model_name='student',
            name='born_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_access',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 23, 29, 15, 962121, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 23, 29, 15, 959618, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 23, 29, 15, 959618, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 23, 29, 15, 959618, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('enrollment_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enrollment_class', to='clients.classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student', to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='AttendenceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2023, 1, 2, 23, 29, 15, 963757, tzinfo=datetime.timezone.utc))),
                ('status', models.IntegerField(choices=[(0, 'Present'), (1, 'Absent'), (2, 'Justificado'), (3, 'Reagendado')])),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enrollment', to='users.enrollment')),
            ],
        ),
    ]
