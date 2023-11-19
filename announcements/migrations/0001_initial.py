# Generated by Django 4.2.6 on 2023-11-19 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publication_date', models.DateField()),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
                'ordering': ['news_id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publication_date', models.DateField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.teacher')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'course',
                'ordering': ['course_id'],
            },
        ),
    ]
