from django.db import models


class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Специализация")

    def __str__(self):
        return str(self.specialization_id)

    class Meta:
        # managed = False
        # db_table = 'specialization'
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        ordering = ['name']


class ClassField(models.Model):
    class_field_id = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name='Номер курса')

    def __str__(self):
        return str(self.class_field_id)

    class Meta:
        # managed = False
        # db_table = 'class_field'
        verbose_name = 'Номер курса'
        verbose_name_plural = 'Номера курсов'
        ordering = ['number']
