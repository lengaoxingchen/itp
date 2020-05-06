from django.contrib import admin
from .models import Set


# Register your models here.
class SetAdmin(admin.ModelAdmin):
    list_display = ['id', 'set_name', 'set_value', ]


admin.site.register(Set,SetAdmin)
