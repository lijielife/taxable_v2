from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class System(models.Model):
    """
    评估体系：1.存量住房分区域计税价格
              2.特殊住宅小区计税价格
              3.存量商业用房分区域住宅价格
    """
    name = models.CharField(max_length=32,verbose_name="评估价体系")
    country = models.ManyToManyField('Country')

    class Meta:
        db_table = "System"
        verbose_name_plural = "评估价体系"

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    所在区县：1，东城  2.西城  3.朝阳 ......
    """
    name = models.CharField(max_length=32,verbose_name="所在区县")
    class Meta:
        db_table = "Country"
        verbose_name_plural = '所在区县'

    def __str__(self):
        return self.name


class Area(models.Model):
    """
    所在的区域: 1.安定门外   2.东直门外
    """
    name = models.CharField(max_length=32,verbose_name="所在区域")
    country = models.ForeignKey("Country",on_delete=models.CASCADE)

    class Meta:
        db_table = "Area"
        verbose_name_plural = "所在区域"

    def __str__(self):
        return  self.name


class House(models.Model):
    """
    房型：1.楼房  2.平房  3，地下室
    """
    name = models.CharField(max_length=32,verbose_name='房型')
    #house = models.ForeignKey("System",on_delete=models.CASCADE)
    class Meta:
        db_table = 'House'
        verbose_name_plural = "房型"

    def __str__(self):
        return self.name


class Time(models.Model):
    time = models.CharField(max_length=64,verbose_name='建成年代')

    class Meta:
        db_table = 'Time'
        verbose_name_plural = '建成年代'
    def __str__(self):
        return self.time


class Plot(models.Model):
    """
    小区：朝向、户型....
    """
    title = models.CharField(max_length=64,verbose_name="小区名称")
    system = models.ForeignKey("System",null=True,blank=True,on_delete=models.CASCADE)
    country = models.ForeignKey("Country", null=True, blank=True, on_delete=models.CASCADE)
    area  = models.ForeignKey('Area',null=True,blank=True,on_delete=models.CASCADE)
    house = models.ForeignKey('House',null=True,blank=True,on_delete=models.CASCADE)
    time = models.ForeignKey('Time', on_delete=models.CASCADE)
    orientation = models.CharField(max_length=64,verbose_name='朝向')
    design = models.CharField(max_length=32,verbose_name='户型')
    acreage= models.IntegerField(verbose_name='面积')
    price = models.IntegerField(verbose_name='成交价格')
    total_floor = models.IntegerField(verbose_name='总楼层')
    floor = models.IntegerField(verbose_name='所在楼层')
    element = models.IntegerField(verbose_name='楼栋号')
    vouch_price = models.IntegerField(verbose_name='核定评估价')

    class Meta:
        db_table = 'Plot'
        verbose_name_plural = '小区'

    def __str__(self):
        return self.title