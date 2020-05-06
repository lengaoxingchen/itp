from django.contrib import admin
from .models import Bug


# Register your models here.

class BugAdmin(admin.ModelAdmin):
    list_display = ['id', 'bug_name', 'bug_detail', 'bug_status', 'bug_level', 'bug_creater', 'bug_assign',
                    'create_time', ]


admin.site.register(Bug, BugAdmin)
