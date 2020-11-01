from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 衡水学院信息表
class Com(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)#一个user有一个公司
    number = models.CharField(max_length=10, default="1")
    name = models.CharField(max_length=10)
    Cinfo = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="logo/", verbose_name='logo')
    Companyprofile = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '企业表'  # 首页列表的显示名称
        verbose_name = "企业数据"  # 列表页和详情页的显示名称


# 招聘岗位表
class Zp(models.Model):
    number = models.CharField(max_length=20)
    jobType = models.CharField(max_length=40)
    jobName = models.CharField(max_length=40)
    jobTitle = models.CharField(max_length=20)
    pre = models.CharField(max_length=20)
    academic = models.CharField(max_length=20)
    welfare = models.TextField()
    jobprofile = models.TextField()
    need_number = models.IntegerField()
    com = models.ForeignKey(Com, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobName

    class Meta:
        verbose_name_plural = '招聘表'  # 首页列表的显示名称
        verbose_name = "招聘数据"  # 列表页和详情页的显示名称


# 求职用户
class CV(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)#一个user有一个公司
    name = models.CharField(max_length=20)
    sex = models.BooleanField(default=True)
    location = models.CharField(max_length=20)
    # email = models.EmailField(max_length=30)
    photo = models.ImageField(upload_to='user', verbose_name='user')
    resume = models.FileField(upload_to='cv', verbose_name='resume')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '简历表'  # 首页列表的显示名称
        verbose_name = "简历数据"  # 列表页和详情页的显示名称


# 关系表
class Relation(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    com = models.ForeignKey(Com, on_delete=models.CASCADE)
    zp = models.ForeignKey(Zp, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=20,verbose_name='面试地点')
    tim = models.CharField(max_length=20)
    need = models.CharField(max_length=20)
    is_have = models.BooleanField(default=False)
    result = models.BooleanField(null=True)

    # class Meta:
    #     verbose_name_plural = '投递关系表'  # 首页列表的显示名称
    #     verbose_name="投递关系数据"  # 列表页和详情页的显示名称
    #     unique_together = ("user_id", "zp_id")
