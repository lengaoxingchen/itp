from django.contrib import admin
from .models import WebCase, WebCaseStep


# Register your models here.

class WebCaseStepAdmin(admin.TabularInline):
    list_display = ['id', 'web_test_step', 'web_test_objname', 'web_find_method', 'web_ve_element',
                    'web_opt_method', 'web_test_date', 'web_assert_data', 'web_test_result', 'create_time', 'web_case']
    model = WebCaseStep
    extra = 1


class WebCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'web_case_name', 'web_test_result', 'create_time']
    inlines = [WebCaseStepAdmin]


admin.site.register(WebCase, WebCaseAdmin)
