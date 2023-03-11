from django.contrib import admin
from employee.models import Bookmarks



@admin.register(Bookmarks)
class BookmarksAdmin(admin.ModelAdmin):
  list_display = ('employee', 'menu_name')
  date_hierarchy = 'created_at'
  list_per_page = 20
  # exclude = ('employee',)

  def get_queryset(self, request):
    qs = super().get_queryset(request)
    return qs.filter(employee_id=request.user.employee)
  
  def save_model(self, request, obj, form, change):
    if not change:
      obj.employee = request.user.employee
    super().save_model(request, obj, form, change)
  

  def get_fields(self, request, obj=None):
    fields = super().get_fields(request)
    fields.remove('employee')
    return fields