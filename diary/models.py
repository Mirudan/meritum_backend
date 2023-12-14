from django.db import models

from groups.models import ClassField
from students.models import Student


class Subject(models.Model):
    subjects_id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return str(self.subjects_id)

    class Meta:
        # managed = False
        # db_table = 'subject'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
        ordering = ['subjects_id']


class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    date_mark = models.DateField()
    student = models.ForeignKey(Student, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    mark = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.mark_id)

    class Meta:
        # managed = False
        # db_table = 'mark'
        verbose_name = 'mark'
        verbose_name_plural = 'marks'
        ordering = ['mark_id']


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    class_field = models.ForeignKey(ClassField, models.DO_NOTHING)
    date_lesson = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.schedule_id)

    class Meta:
        # managed = False
        # db_table = 'schedule'
        verbose_name = 'schedule'
        verbose_name_plural = 'schedules'
        ordering = ['schedule_id']
