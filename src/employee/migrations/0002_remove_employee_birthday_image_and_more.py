# Generated by Django 4.1.7 on 2023-03-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='birthday_image',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='birthday_image_shown',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='list_order',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='pf_eligibility',
        ),
    ]