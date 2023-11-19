from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.admin_id)

    class Meta:
        # managed = False
        # db_table = 'admin'
        verbose_name = 'admin'
        verbose_name_plural = 'admins'
        ordering = ['admin_id']
