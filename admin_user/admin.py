from django.contrib import admin
from .models import AdUser

# Register your models here.
class AdUserAdmin(admin.ModelAdmin):
    list_display = ('user_id',)

admin.site.register(AdUser, AdUserAdmin)