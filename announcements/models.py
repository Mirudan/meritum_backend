from django.db import models

from teachers.models import Teacher


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    publication_date = models.DateField()

    def __str__(self):
        return str(self.news_id)

    class Meta:
        # managed = False
        # db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['news_id']


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    publication_date = models.DateField()
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING)

    def __str__(self):
        return str(self.course_id)

    class Meta:
        # managed = False
        # db_table = 'course'
        verbose_name = 'course'
        verbose_name_plural = 'course'
        ordering = ['course_id']
