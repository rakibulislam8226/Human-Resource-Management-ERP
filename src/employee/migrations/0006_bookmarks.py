# Generated by Django 3.2.18 on 2023-03-11 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0005_leave_leaveattachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu_link', models.CharField(max_length=255)),
                ('menu_name', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_bookmarks_related', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('employee', models.ForeignKey(limit_choices_to={'active': True}, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'verbose_name': 'Bookmark',
                'verbose_name_plural': 'Bookmarks',
            },
        ),
    ]
