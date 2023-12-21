from django.contrib.auth.models import User
from django.db import models
from groups.models import ClassField, Specialization


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    student_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='photos/students/', verbose_name='Аватар', null=True, blank=True)
    full_name = models.TextField(verbose_name='Полное имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    class_field = models.ForeignKey(ClassField, models.DO_NOTHING, verbose_name='Курс')
    specialization = models.ForeignKey(Specialization, models.DO_NOTHING, verbose_name='Специализация', null=True,
                                       blank=True)

    def __str__(self):
        return str(self.student_id)

    class Meta:
        # managed = False
        # db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['student_id']
