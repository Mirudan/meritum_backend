from django.db import models


class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.TextField()


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=64)
    specialization = models.ForeignKey('Specialization', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'semester'


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    semester = models.ForeignKey('Semester', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'class'
