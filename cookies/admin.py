from django.contrib import admin

from .models import Cookie
# Register your models here.
@admin.register(Cookie)
class CookieAdmin(admin.ModelAdmin):
    list_display = ['name','calories','type','size','description','imagepath']

