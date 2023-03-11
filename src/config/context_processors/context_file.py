from employee.models import Bookmarks


def bookmarks_menu_list(request):
  if request.user.is_authenticated and request.user.employee is not None:
    f_menu = Bookmarks.objects.filter(employee_id=request.user.employee.id)
    data = {}
    data['object_list'] = f_menu
    return data
  return []