import os

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify

from employee.models import Employee
from config.models.AuthorMixin import AuthorMixin
from config.models.TimeStampMixin import TimeStampMixin


def user_directory_path(instance, filename):
    username = instance.employee.user.username
    filename = get_file_name(instance.file_name, filename)
    return f'hr/employee/{username}/{filename}'


class Attachment(TimeStampMixin, AuthorMixin):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file_name = models.CharField(null=True, blank=True, max_length=155)
    file = models.FileField(
        help_text='*.pdf, *.doc, *.png, *.jpeg',
        upload_to=user_directory_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'png', 'jpeg', 'jpg'])
        ])


def get_file_name(given_name, filename):
    file_extension = os.path.basename(filename).split('.')[-1]
    if given_name:
        return slugify(given_name) + "." + file_extension
    return filename
