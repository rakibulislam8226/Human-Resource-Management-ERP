from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

from config.models.AuthorMixin import AuthorMixin
from config.models.TimeStampMixin import TimeStampMixin


class CredentialCategory(AuthorMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Credential(AuthorMixin, TimeStampMixin):
    STATUS_CHOICES = (
        ('ACTIVE', '✔ Active'),
        ('INACTIVE', '✖ InActive'),
    )
    title = models.CharField(max_length=255)
    category = models.ForeignKey(CredentialCategory, on_delete=models.RESTRICT)
    description = HTMLField()
    privileges = models.ManyToManyField(User, blank=True)
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default='Active',)

    class Meta:
        permissions = [
            ("access_all_credentials", "Can able to see all credentials")
        ]
