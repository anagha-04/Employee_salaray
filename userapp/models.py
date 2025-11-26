from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    mobile_number = models.CharField(max_length=11, unique=True)


class EmployeeModel(models.Model):

    name = models.CharField(max_length=100)

    base_salary = models.IntegerField()

    bonus = models.IntegerField()

    tax = models.IntegerField()

    net_salary = models.IntegerField()




    

