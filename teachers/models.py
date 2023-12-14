from django.db import models

from diary.models import Subject


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='photos/teachers', verbose_name='Аватар', null=True, blank=True)
    login = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.TextField(verbose_name='Полное имя')
    position = models.TextField(verbose_name='Должность')
    email = models.EmailField(unique=True)
    subjects = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.teacher_id)

    class Meta:
        # managed = False
        # db_table = 'teacher'
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ['teacher_id']
