from django.contrib import admin
from project_management.models import Tag, Client, Project

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]

    def has_module_permission(self, request):
        return False


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'country']

    def has_module_permission(self, request):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title',]