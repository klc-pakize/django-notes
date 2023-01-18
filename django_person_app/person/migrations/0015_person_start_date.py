# Generated by Django 4.1.4 on 2023-01-10 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0014_remove_person_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
