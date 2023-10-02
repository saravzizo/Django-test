from django import forms
from django.db import models
from django.forms import ValidationError
from django.core import validators

def validate_username_model(value):
    if len(value) <10:
        raise ValidationError("Please enter more than 10 digit")

def validate_password_model(value):
    if len(value)<6:
        raise ValidationError("Please enter more than 6 digit")
    
def validate_mail(value):
    if "@gmail.com" in value:
        return value
    if "@yahoo.com" in value:
        return value 
    if "@outlook.com" in value:
        return value
    else:
        raise ValidationError("Email should contain valid domain")
    
# Create your models here

class Register_table(models.Model):
    id = models.AutoField( primary_key=True,verbose_name ='ID')
    firstname = models.CharField(max_length=200, validators=[validate_password_model])
    lastname = models.CharField(max_length=200,validators=[validate_password_model])
    email = models.CharField(max_length=254,unique=True,validators=[validators.EmailValidator(),validate_mail] )
    password = models.CharField(max_length=250,validators=[validate_password_model])
    
    
class Login_table(models.Model):
    id = models.AutoField(primary_key=True, verbose_name ='ID')
    username = models.CharField(max_length=200, unique=True, validators=[validate_username_model])
    password = models.CharField(max_length=250 , validators=[validate_password_model])
 