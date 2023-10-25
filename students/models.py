from django.db import models

from groups.models import Class


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    full_name = models.TextField()
    email = models.CharField(max_length=128)
    class_field = models.ForeignKey(Class, models.DO_NOTHING)

    def __str__(self):
        return str(self.student_id)

    class Meta:
        managed = False
        db_table = 'student'
