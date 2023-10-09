from django.db import models


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.BinaryField(blank=True, null=True)
    publication_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'news'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.BinaryField(blank=True, null=True)
    publication_date = models.DateField()
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course'
