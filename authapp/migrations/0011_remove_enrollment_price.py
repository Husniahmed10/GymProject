# Generated by Django 5.1.2 on 2024-12-13 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_enrollment_duedate_enrollment_paymentstatus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='Price',
        ),
    ]
