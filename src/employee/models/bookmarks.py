from django.db import models
from config.models.TimeStampMixin import TimeStampMixin
from config.models.AuthorMixin import AuthorMixin
from employee.models import Employee


class Bookmarks(TimeStampMixin, AuthorMixin):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'active': True})
  menu_link = models.CharField(max_length=255)
  menu_name = models.CharField(max_length=255)
  note = models.TextField(null=True, blank=True)

  def __str__(self) -> str:
    return f"{self.employee.full_name}" 
  
  class Meta:
    verbose_name = 'Bookmark'
    verbose_name_plural = 'Bookmarks'
    