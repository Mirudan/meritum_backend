from django.db import models

from groups.models import ClassField, Specialization
from students.models import Student


class PlanLesson(models.Model):
    plan_lesson_id = models.AutoField(primary_key=True)
    numbers_lesson = models.IntegerField(verbose_name="Номер урока")
    start_time = models.TimeField(verbose_name="Начало урока")
    end_time = models.TimeField(verbose_name="Окончание урока")

    class Meta:
        verbose_name_plural = "Расписание звонков"
        ordering = ["plan_lesson_id"]


class Subject(models.Model):
    subjects_id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название предмета")

    def __str__(self):
        return str(self.subjects_id)

    class Meta:
        # managed = False
        # db_table = 'subject'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
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
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'
        ordering = ['mark_id']


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    specialization = models.ForeignKey(Specialization, models.DO_NOTHING, verbose_name='специализация')
    subject = models.ForeignKey(Subject, models.DO_NOTHING, verbose_name='предмет')
    classroom = models.IntegerField(blank=True, null=True, verbose_name='кабинет')
    class_field = models.ForeignKey(ClassField, models.DO_NOTHING, verbose_name='курс')
    semester = models.IntegerField(verbose_name='семестр', blank=True, null=True)
    date_lesson = models.DateField(verbose_name='дата урока')
    plan_lesson = models.ForeignKey(PlanLesson, models.DO_NOTHING, verbose_name='номер урока')
    teacher = models.CharField(max_length=250, blank=True, null=True, verbose_name='преподаватель')
    type_lesson = models.CharField(max_length=250, blank=True, null=True, verbose_name='тип занятия')

    def __str__(self):
        return str(self.schedule_id)

    class Meta:
        # managed = False
        # db_table = 'schedule'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['schedule_id']
