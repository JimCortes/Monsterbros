# Generated by Django 4.2.7 on 2024-01-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
