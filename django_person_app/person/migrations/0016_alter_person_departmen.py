# Generated by Django 4.1.4 on 2023-01-10 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0015_person_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='departmen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department', to='person.department'),
        ),
    ]