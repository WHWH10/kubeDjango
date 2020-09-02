from django.contrib import admin
from .models import PushInfo

# Register your models here.
class PushInfoAdmin(admin.ModelAdmin):
    list_display = ('message_title',)

admin.site.register(PushInfo, PushInfoAdmin)
