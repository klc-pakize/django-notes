# Generated by Django 4.1.4 on 2023-01-05 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0002_remove_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
