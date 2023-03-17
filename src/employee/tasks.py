from employee.models import Employee
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template import Context, loader
from django.template.loader import get_template
from django.core import management



def increment_notification(employees):
    html_body = loader.render_to_string('mail/increment_notification.html',
                                        context={'employees': employees, 'total_emp': len(employees)})
    email = EmailMultiAlternatives()
    email.subject = f"Increment Notification there are {len(employees)} employee(s) in the lis of increment"
    email.attach_alternative(html_body, 'text/html')
    email.to = ['rakibulislam8226@gmail.com']
    email.bcc = ['rakibkhan9065@gmail.com']
    email.from_email = 'Rakibul Islam. <career@rakibul.com>'
    email.send()

def execute_increment_notification():
    management.call_command('increment_notifi')


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