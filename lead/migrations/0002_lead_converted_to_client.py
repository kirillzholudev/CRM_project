# Generated by Django 4.1.7 on 2023-04-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_to_client',
            field=models.BooleanField(default=False),
        ),
    ]
