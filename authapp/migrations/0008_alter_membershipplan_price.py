# Generated by Django 5.1.2 on 2024-12-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_alter_enrollment_duedate_alter_enrollment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
