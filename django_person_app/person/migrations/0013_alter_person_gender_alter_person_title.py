# Generated by Django 4.1.4 on 2023-01-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0012_alter_person_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other'), ('4', 'Prefer Not Say')], default=2, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('1', 'Team Lead'), ('2', 'Mid Lead'), ('3', 'Junior')], default=3, max_length=15),
        ),
    ]
