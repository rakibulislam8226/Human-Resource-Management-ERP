from django.contrib.auth.models import User
from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class AuthorMixin(models.Model):
    created_by = UserForeignKey(auto_user_add=True, verbose_name="Created By",
                                related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True
