from django.contrib import admin
from employee.models import Employee, LeaveManagement, PayScale, Designation, Skill, EmployeeSkill
from django.db import models
from .inlines import EmployeeInline



@admin.register(Employee)
class EmployeeAdmin(EmployeeInline, admin.ModelAdmin):
    autocomplete_fields = ['user', ]

    def get_actions(self, request):
        if not request.user.is_superuser:
            return []
        return super(EmployeeAdmin, self).get_actions(request)

    def get_list_display(self, request):
        list_display = ['full_name', ]
        # if not request.user.is_superuser:
        #     list_display.remove('salary_history')
        return list_display
    
    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title',]

    def has_module_permission(self, request):
        return False


@admin.register(LeaveManagement)
class LeaveManagementAdmin(admin.ModelAdmin):
    list_display = ['title', 'casual_leave', 'medical_leave']


@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ['skill',]

    def has_module_permission(self, request):
        return False


@admin.register(PayScale)
class PayScaleAdmin(admin.ModelAdmin):
    list_display = ['title',]

    def has_module_permission(self, request):
        return False


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['title',]