# Generated by Django 4.1.4 on 2023-01-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_alter_person_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
