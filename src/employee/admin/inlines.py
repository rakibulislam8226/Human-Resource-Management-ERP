from django.contrib import admin
from django.db import models
from django.forms import Textarea
from settings.models import BankAccount
from employee.models import EmployeeSkill, SalaryHistory


class BankAccountInline(admin.TabularInline):
    model = BankAccount
    extra = 0

    # def get_extra(self, request, obj=None, **kwargs):
    #     return 1 if not obj else 0


class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 0

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if not obj else 0


class SalaryHistoryInline(admin.TabularInline):
    model = SalaryHistory

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 60})}
    }

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if not obj else 0

    def get_fields(self, request, obj=None):
        fields = super(SalaryHistoryInline, self).get_fields(request, obj)
        if not request.user.is_superuser:
            fields.remove('note')
        return fields


class EmployeeInline(admin.ModelAdmin):
    inlines = (SalaryHistoryInline, BankAccountInline, EmployeeSkillInline)