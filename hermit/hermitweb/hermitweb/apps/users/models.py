from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11,
                             unique=True,
                             verbose_name='手机号码')

    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
