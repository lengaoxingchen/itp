from django.contrib import admin
from .models import AppCase, AppCaseStep


# Register your models here.

class AppCaseStepAdmin(admin.TabularInline):
    list_display = ['id', 'app_test_step', 'app_test_objname', 'app_find_method', 'app_ve_element', 'app_opt_method',
                    'app_test_date', 'app_assert_data', 'app_test_result', 'create_time', 'app_case']
    model = AppCaseStep
    extra = 1


class AppCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'app_case_name', 'app_test_result', 'create_time']
    inlines = [AppCaseStepAdmin]


admin.site.register(AppCase, AppCaseAdmin)
