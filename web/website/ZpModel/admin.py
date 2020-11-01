from django.contrib import admin
from .models import Zp,Com,CV
# Register your models here.
admin.site.site_title="衡水学院招聘网站后台"
admin.site.site_header="后台管理"
admin.site.index_title="欢迎登陆"

class ZpAdmin(admin.ModelAdmin):
    list_display = ('number','jobName','jobType','jobTitle','pre','academic','welfare','jobprofile','need_number','com')

class ComAdmin(admin.ModelAdmin):
    list_display = ('number','name','Cinfo','logo','Companyprofile')

class CVAdmin(admin.ModelAdmin):
    list_display = ('name','sex','location','photo','resume')

admin.site.register(Zp,ZpAdmin)
admin.site.register(Com,ComAdmin)

admin.site.register(CV,CVAdmin)