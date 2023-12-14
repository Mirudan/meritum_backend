# Generated by Django 4.2.6 on 2023-11-19 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': 'specialization',
                'verbose_name_plural': 'specializations',
                'ordering': ['specialization_id'],
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=64)),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='groups.specialization')),
            ],
            options={
                'verbose_name': 'semester',
                'verbose_name_plural': 'semesters',
                'ordering': ['semester_id'],
            },
        ),
        migrations.CreateModel(
            name='ClassField',
            fields=[
                ('class_field_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='groups.semester')),
            ],
            options={
                'verbose_name': 'class_field',
                'verbose_name_plural': 'class_fields',
                'ordering': ['class_field_id'],
            },
        ),
    ]
