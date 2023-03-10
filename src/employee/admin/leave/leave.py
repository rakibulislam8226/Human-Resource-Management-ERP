from django.contrib import admin
from employee.models import Leave

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['short_message',]

    # def has_module_permission(self, request):
    #     return False