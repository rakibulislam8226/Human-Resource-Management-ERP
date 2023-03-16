from employee.models import Employee
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template import Context, loader
from django.template.loader import get_template



def print_task():
    print("Django q working and check done.")

def employee_permanent_mail(employee: Employee):
    print('permanent mail')

    html_template = get_template('mail/employee_permanent_mail.html')
    html_content = html_template.render({
        'employee': employee
    })
    email = EmailMultiAlternatives(subject=f'Permanent email.')
    email.attach_alternative(html_content, 'text/html')
    email.to = [employee.email]
    email.from_email = 'Rakibul Islam. <career@rakibul.com>'
    email.send()