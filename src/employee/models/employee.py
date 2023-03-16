from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.utils.timesince import timesince
from django.utils.text import slugify
from django_q.tasks import async_task
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import datetime #important if using timezones

from config.models.TimeStampMixin import TimeStampMixin
from config.models.AuthorMixin import AuthorMixin




class Designation(TimeStampMixin, AuthorMixin):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class PayScale(TimeStampMixin, AuthorMixin):
    title = models.CharField(max_length=255)
    basic = models.FloatField()
    travel_allowance = models.FloatField()
    house_allowance = models.FloatField()
    medical_allowance = models.FloatField()
    net_payable = models.FloatField()
    provision_period = models.IntegerField(help_text='Month')
    increment_period = models.IntegerField(help_text='increment month count')
    increment_rate = models.FloatField(help_text='In percentage')
    leave_in_cash_medical = models.FloatField(
        help_text='Medical Leave in cash, your submitted value will count as % percentage. '
                  'It will automatically calculate to the employee salary sheet on year closing',
        verbose_name='Leave in Cash (Medical)',
        default=0.0)
    leave_in_cash_casual = models.FloatField(
        help_text='Casual leave in cash, your submitted value will count as % percentage. '
                  'It will automatically calculate to the employee salary sheet on year closing',
        verbose_name='Leave in Cash (Casual)',
        default=0.0)

    def __str__(self):
        return self.title


class LeaveManagement(TimeStampMixin, AuthorMixin):
    title = models.CharField(max_length=255)
    casual_leave = models.IntegerField()
    medical_leave = models.IntegerField()

    def __str__(self):
        return self.title


# Create your models here.
class Employee(TimeStampMixin, AuthorMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    full_name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=60, help_text='Use (,) comma for separate phone numbers')
    joining_date = models.DateField(default=timezone.now)
    national_id_no = models.CharField(max_length=20, blank=True, null=True)
    permanent_date = models.DateField(null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.RESTRICT)
    leave_management = models.ForeignKey(LeaveManagement, on_delete=models.RESTRICT)
    pay_scale = models.ForeignKey(PayScale, on_delete=models.RESTRICT)
    tax_info = models.CharField(null=True, blank=True, max_length=255,
                                help_text='i.e: 59530389237, Circle–138, Zone-11, Dhaka')
    manager = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    show_in_web = models.BooleanField(default=True)
    lunch_allowance = models.BooleanField(default=True)
    project_eligibility = models.BooleanField(default=True)
    leave_in_cash_eligibility = models.BooleanField(default=True)
    show_in_attendance_list = models.BooleanField(default=True)

    def __str__(self):
        bank = self.bankaccount_set.filter(default=True).first()
        return self.full_name

    def set_in_employee_group(self):
        group = Group.objects.get(name='Employee')
        group.user_set.add(self.user)

    @property
    def joining_date_human(self):
        return timesince(self.joining_date)

    @property
    def permanent_date_human(self):
        return timesince(self.permanent_date)

    def save(self, *args, **kwargs, ):
        self.save_user()
        if not self.slug:
            self.slug = f'{slugify(self.full_name)}-{self.email}'
        super().save(*args, **kwargs)

    def save_user(self):
        name_array = self.full_name.split()
        self.user.is_staff = True
        self.user.first_name = name_array[0]
        self.user.last_name = name_array[1] if len(name_array) > 1 else ''
        self.user.email = self.email
        self.set_in_employee_group()
        if not self.active:
            self.user.is_active = False
        self.user.save()

    @property
    def default_bank(self):
        bank = self.bankaccount_set.filter(default=True).first()
        if bank:
            return bank.bank.name
        return ''
    
    @property
    def current_salary(self):
        return self.salaryhistory_set.latest('id')

    class Meta:
        db_table = 'employees'
    

@receiver(post_save, sender=Employee)
def employee_post_save(sender, instance, created, *args, **kwargs):
    today_date = datetime.today().date()
    if instance.permanent_date == today_date:
        async_task('employee.tasks.employee_permanent_mail', instance)


class SalaryHistory(TimeStampMixin, AuthorMixin):
    payable_salary = models.FloatField()
    active_from = models.DateField(default=timezone.now)
    note = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    @property
    def active_from_human(self):
        return timesince(self.active_from)