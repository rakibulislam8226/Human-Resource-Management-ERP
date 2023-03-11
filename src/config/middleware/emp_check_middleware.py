from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect
from employee.models import Employee
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models import Subquery, OuterRef
from django.contrib import messages


users_without_employee_id = User.objects.filter(
  ~Q(id__in=Subquery(
    Employee.objects.values_list('user')
  ))
)

        
class CheckUserHasEmployee:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    return response

  def process_view(self, request, view_func, view_args, view_kwargs):
    if request.path_info == "/admin/":
      if request.user.is_authenticated:
        if request.user in users_without_employee_id:
          messages.error(request, "You have no employee account.")
          return redirect("admin:logout")


