from django.db import models


# This model will then not be used to create any database table.
# Instead, when it is used as a base class for other models, its fields will be added to those of the child class
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True