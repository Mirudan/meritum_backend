from django.db import models

from diary.models import Subject


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='photo/teachers', blank=True, null=True)
    login = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.TextField()
    position = models.TextField()
    email = models.EmailField(max_length=128, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    subjects = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.teacher_id)

    class Meta:
        # managed = False
        # db_table = 'teacher'
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        ordering = ['teacher_id']
