from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name_plural = '注册用户管理'
