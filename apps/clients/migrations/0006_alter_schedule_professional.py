# Generated by Django 4.1.4 on 2023-10-01 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_administrator_created_at_and_more'),
        ('clients', '0005_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='professional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='professional_schedule', to='users.teacher'),
        ),
    ]