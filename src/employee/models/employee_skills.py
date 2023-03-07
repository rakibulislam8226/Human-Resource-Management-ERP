from django.db import models
from config.models.TimeStampMixin import TimeStampMixin
from config.models.AuthorMixin import AuthorMixin
from employee.models import Employee


class Skill(AuthorMixin, TimeStampMixin):
    title = models.CharField(unique=True, max_length=255)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class EmployeeSkill(AuthorMixin, TimeStampMixin):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    percentage = models.FloatField(max_length=100)

