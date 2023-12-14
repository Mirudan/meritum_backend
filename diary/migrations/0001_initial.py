# Generated by Django 4.2.6 on 2023-11-19 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjects_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': 'subject',
                'verbose_name_plural': 'subjects',
                'ordering': ['subjects_id'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_lesson', models.DateField()),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField(blank=True, null=True)),
                ('class_field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='groups.classfield')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diary.subject')),
            ],
            options={
                'verbose_name': 'schedule',
                'verbose_name_plural': 'schedules',
                'ordering': ['schedule_id'],
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('mark_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_mark', models.DateField()),
                ('mark', models.IntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diary.subject')),
            ],
            options={
                'verbose_name': 'mark',
                'verbose_name_plural': 'marks',
                'ordering': ['mark_id'],
            },
        ),
    ]
