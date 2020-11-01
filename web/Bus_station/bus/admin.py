from django.contrib import admin

# Register your models here.

from .models import Bus, Station, Message,Line
# from django.contrib.auth.models import User


class LineAdmin(admin.ModelAdmin):
    list_display = ('name','id')


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'bus')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'add_date')



class BusAdmin(admin.ModelAdmin):
    list_display = ('Bus_ID','id')

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('password','is_superuser','username')

admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Bus,BusAdmin)