from django.db import models
from employee.models import Employee
from config.models.AuthorMixin import AuthorMixin
from config.models.TimeStampMixin import TimeStampMixin


class Bank(TimeStampMixin, AuthorMixin):
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.RESTRICT)
    account_number = models.CharField(max_length=100)
    default = models.BooleanField(default=True)

    def __str__(self):
        return self.bank.name