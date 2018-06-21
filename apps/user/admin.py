from django.contrib import admin

# Register your models here.
from apps.user import models
admin.register(models.User)