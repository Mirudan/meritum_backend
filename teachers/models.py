from django.db import models


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    full_name = models.TextField()
    position = models.TextField()
    email = models.CharField(max_length=128, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    subjects = models.ForeignKey('Subject', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'
