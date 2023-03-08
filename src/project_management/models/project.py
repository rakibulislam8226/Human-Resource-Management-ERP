from django.db import models
from config.models.AuthorMixin import AuthorMixin
from config.models.TimeStampMixin import TimeStampMixin
from employee.models import Employee
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta, FR



# Create your models here.
class Tag(TimeStampMixin, AuthorMixin):
    icon = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Client(TimeStampMixin, AuthorMixin):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=80)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Project(TimeStampMixin, AuthorMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True, unique=True)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    in_active_at = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    show_in_website = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    on_boarded_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                      limit_choices_to={'active': True})

    def __str__(self):
        return self.title

    @property
    def created_at_timestamp(self):
        return int(self.created_at.strftime("%s")) * 1000
    
    def last_x_weeks_feedback(self, x):
        today = datetime.datetime.today()
        last_xth_friday = datetime.datetime.today() + relativedelta(weekday=FR(-x))
        
        return self.clientfeedback_set.filter(
            created_at__date__lte=today,
            created_at__date__gt=last_xth_friday,
        ).order_by("-created_at").exclude(project__active=False)
