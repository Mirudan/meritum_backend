# Generated by Django 4.2.6 on 2023-12-20 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_teacher_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subjects',
        ),
    ]
