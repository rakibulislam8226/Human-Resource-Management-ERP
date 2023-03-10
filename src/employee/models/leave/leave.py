import datetime
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import truncatewords
from config.models.TimeStampMixin import TimeStampMixin
from config.models.AuthorMixin import AuthorMixin
from django.core.exceptions import ValidationError
from django_userforeignkey.request import get_current_user
from employee.models import Employee
from settings.models import PublicHolidayDate
from employee.models.leave.leaveMixin import LeaveMixin


# TODO : leave calculation by permanent date
# TODO : leave in cash in every january
class Leave(TimeStampMixin, AuthorMixin, LeaveMixin):
    message = models.TextField(validators=[MinLengthValidator(150)])
    status_changed_by = models.ForeignKey(User, limit_choices_to={'is_superuser': True}, null=True,
                                          on_delete=models.RESTRICT)
    status_changed_at = models.DateField(null=True)

    @property
    def short_message(self):
        return truncatewords(self.message, 10)

    class Meta:
        permissions = (
            ("can_approve_leave_applications", "Can able to approve leave applications"),
        )


class LeaveAttachment(TimeStampMixin, AuthorMixin):
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE)
    attachment = models.FileField(help_text='Image , PDF or Docx file ')



