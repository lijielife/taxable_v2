from django.contrib import admin

# Register your models here.
from proscenium import models

admin.site.register(models.System)
admin.site.register(models.Country)
admin.site.register(models.Area)
admin.site.register(models.House)
admin.site.register(models.Time)
admin.site.register(models.Plot)