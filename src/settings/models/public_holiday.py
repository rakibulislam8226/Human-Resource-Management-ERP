from django.db import models
from config.models.TimeStampMixin import TimeStampMixin
from config.models.AuthorMixin import AuthorMixin



class PublicHoliday(TimeStampMixin, AuthorMixin):
    title = models.CharField(max_length=255)
    note = models.TextField(null=True)

    def __str__(self):
        return self.title

class PublicHolidayDate(TimeStampMixin):
    public_holiday = models.ForeignKey(PublicHoliday, on_delete=models.CASCADE, related_name='public_holiday')
    date = models.DateField()