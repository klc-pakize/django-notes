# Generated by Django 4.1.4 on 2023-01-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
