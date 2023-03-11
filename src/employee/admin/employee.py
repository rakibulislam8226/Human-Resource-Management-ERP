from django.contrib import admin
from employee.models import Employee, LeaveManagement, PayScale, Designation, Skill, EmployeeSkill
from django.db import models
from .inlines import EmployeeInline
from django.utils.html import format_html
from django.template.loader import get_template



@admin.register(Employee)
class EmployeeAdmin(EmployeeInline, admin.ModelAdmin):
    autocomplete_fields = ['user', ]

    def get_actions(self, request):
        if not request.user.is_superuser:
            return []
        return super(EmployeeAdmin, self).get_actions(request)

    def get_list_display(self, request):
        list_display = ['full_name', 'skill', 'permanent_status']
        # if not request.user.is_superuser:
        #     list_display.remove('salary_history')
        return list_display
    
    @admin.display(ordering='active', description='Status')
    def permanent_status(self, obj):
        return format_html(
            f'Active : {"<img src=/static/admin/img/icon-yes.svg />" if obj.active else "<img src=/static/admin/img/icon-no.svg />"} <br>'
            f'Permanent : {"<img src=/static/admin/img/icon-yes.svg />" if obj.permanent_date else "<img src=/static/admin/img/icon-no.svg />"}'
        )
    
    @admin.display(ordering='employeeskill__skill')
    def skill(self, obj):
        skill = ''
        for employee_skill in obj.employeeskill_set.all():
            skill += f'{employee_skill.skill.title} - {employee_skill.percentage}% </br>'
        return format_html(skill)
    
    def leave_info(self, obj: Employee):
        html_template = get_template('admin/employee/list/leave_info.html')
        html_content = html_template.render({
            'casual_passed': obj.leave_passed('casual'),
            'casual_remain': obj.leave_available('casual_leave'),
            'medical_passed': obj.leave_passed('medical'),
            'medical_remain': obj.leave_available('medical_leave'),
            'non_paid': obj.leave_passed('non_paid'),
            'employee': obj
        })
        return format_html(html_content)
    
    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title',]

    def has_module_permission(self, request):
        return False


@admin.register(LeaveManagement)
class LeaveManagementAdmin(admin.ModelAdmin):
    list_display = ['title', 'casual_leave', 'medical_leave']

    def has_module_permission(self, request):
        return False


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

    def has_module_permission(self, request):
        return False