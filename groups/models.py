from django.db import models


class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return str(self.specialization_id)

    class Meta:
        # managed = False
        # db_table = 'specialization'
        verbose_name = 'specialization'
        verbose_name_plural = 'specializations'
        ordering = ['specialization_id']


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    specialization = models.ForeignKey(Specialization, models.DO_NOTHING)

    def __str__(self):
        return str(self.semester_id)

    class Meta:
        # managed = False
        # db_table = 'semester'
        verbose_name = 'semester'
        verbose_name_plural = 'semesters'
        ordering = ['semester_id']


class ClassField(models.Model):
    class_field_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    semester = models.ForeignKey(Semester, models.DO_NOTHING)

    def __str__(self):
        return str(self.class_field_id)

    class Meta:
        # managed = False
        # db_table = 'class_field'
        verbose_name = 'class_field'
        verbose_name_plural = 'class_fields'
        ordering = ['class_field_id']
