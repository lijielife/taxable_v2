from django.contrib import admin

# Register your models here.
from  apps.goods import models
admin.register(models.System)
admin.register(models.Country)
admin.register(models.Area)
admin.register(models.House)
admin.register(models.Time)
admin.register(models.Plot)