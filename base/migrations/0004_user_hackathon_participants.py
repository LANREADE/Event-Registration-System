# Generated by Django 4.2 on 2023-05-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_events_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hackathon_participants',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
