from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your models here.

# 创建数据库内容







# 公交车线路
class Line(models.Model):

    country = models.CharField(max_length=20, verbose_name='城市')
    name = models.CharField(max_length=20,verbose_name='公交车线路名称')
    start = models.IntegerField(verbose_name='开始运行时间')
    end = models.IntegerField(verbose_name='结束运行时间')
    count = models.IntegerField(verbose_name='每趟间隔时间')
    need = models.IntegerField(verbose_name='站点间隔时间')
    money = models.IntegerField(verbose_name='票价')

    def __str__(self):
        return self.name


class Bus(models.Model):
    Bus_ID = models.CharField(max_length=50,verbose_name='电子身份证')
    car_type = models.CharField(max_length=20,verbose_name='车辆型号')
    car_name = models.CharField(max_length=20,verbose_name='驾驶员名字')
    car_com = models.CharField(max_length=20,verbose_name='运行公司')
    car_phone = models.CharField(max_length=20,verbose_name='司机电话')
    line = models.ForeignKey(Line,on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name


# 公交站点
class Station(models.Model):
    name = models.CharField(max_length=20,verbose_name='公交车站点名称')
    number = models.IntegerField(verbose_name='第几站')
    bus = models.ForeignKey(Line, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 评论内容
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    add_date = models.DateTimeField(verbose_name='评论时间',default = timezone.now)


    def __str__(self):
        return self.content