from django.contrib import admin
from settings.models.banks_history import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['name',]

    def has_module_permission(self, request):
        return False