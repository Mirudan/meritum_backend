# Generated by Django 4.2.6 on 2023-12-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_schedule_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='classroom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
