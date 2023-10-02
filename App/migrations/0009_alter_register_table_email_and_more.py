# Generated by Django 4.2.5 on 2023-10-02 07:01

import App.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_register_table_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='email',
            field=models.CharField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(), App.models.validate_mail]),
        ),
        migrations.AlterField(
            model_name='register_table',
            name='firstname',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='register_table',
            name='lastname',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='register_table',
            name='password',
            field=models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
