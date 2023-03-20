from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.html import format_html
from config.widgets.select_multiple import UserFilteredSelectMultiple

from asset_management.models import CredentialCategory, Credential


@admin.register(CredentialCategory)
class CredentialCategoryAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class CredentialAdminForm(forms.ModelForm):
    queryset = User.objects.filter(employee__active=True, is_superuser=False)
    privileges = forms.ModelMultipleChoiceField(
        required=False,
        queryset=queryset,
        widget=UserFilteredSelectMultiple(verbose_name='privileges', is_stacked=False))

    class Meta:
        model = Credential
        fields = "__all__"


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'access_count','status_col',)
    form = CredentialAdminForm
    list_filter = ('category','status')
    search_fields = ('title', 'description')
    actions = ['mark_as_active', 'mark_as_inactive',]
    change_form_template = 'admin/credentials/change_form.html'

    def get_queryset(self, request):
        query_set = super(CredentialAdmin, self).get_queryset(request)
        if not request.user.is_superuser and not request.user.has_perm('asset_management.access_all_credentials'):
            return query_set.filter(privileges__in=[request.user])
        return query_set

    @admin.display(description='Total Privileges')
    def access_count(self, obj: Credential):
        return obj.privileges.count()
    
    @admin.action(description='Mark as Active')
    def mark_as_active(self, request, queryset):
        if request.user.is_superuser :
            queryset.update(status='ACTIVE')
            
    @admin.action(description='Mark as InActive')
    def mark_as_inactive(self, request, queryset):
        if request.user.is_superuser :
            queryset.update(status='INACTIVE')

    @admin.display(description='Status')
    def status_col(self, obj):
        color = 'green'
        if obj.status == 'INACTIVE':
            color = 'red'
        return format_html(
            f'<b style="color: {color}">{obj.get_status_display()}</b>'
        )
