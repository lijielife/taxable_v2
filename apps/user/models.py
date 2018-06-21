from django.db import models

# Create your models here.
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser

class User(AbstractUser,BaseModel):
    """用户模型类"""

    class Meta:
        db_table = 'taxable_user'
        verbose_name_plural = '用户表'