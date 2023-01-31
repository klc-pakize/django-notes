from django.db import models

# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Personnel(models.Model):

    TITLE=(
        ("Team Lead", "LEAD"),
        ("Mid Lead", "MID"),
        ("Junior", "JUN"),
    )

    GENDER = (
        ("Female","F"),
        ("Male","M"),
        ("Other","O"),
        ("Prefer Not Say","N"),
    )

    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True, related_name = 'personnels')
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 5, choices = TITLE)
    gender = models.CharField(max_length= 1, choices = GENDER)
    salary = models.IntegerField(default = 1250)
    start_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f" {self.department.name} - {self.title} - {self.first_name} "
    