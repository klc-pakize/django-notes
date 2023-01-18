from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name
    

class Person(models.Model):
    TITLE = [
        ("1", "Team Lead"),
        ("2", "Mid Lead"),
        ("3", "Junior")
    ]
    GENDER = [
        ("1", "Female"), 
        ("2", "Male"), 
        ("3", "Other"), 
        ("4", "Prefer Not Say")
    ]
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    is_staffed  = models.BooleanField(default = False)
    title = models.CharField(max_length=15, choices = TITLE, default = 3)
    gender = models.CharField(max_length=20, choices = GENDER, default = 2)
    salary = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add = True)  
    user = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True)
    departmen = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name="department", blank = True, null=True)  # departmen_id

    def __str__(self):
        return self.first_name
    

