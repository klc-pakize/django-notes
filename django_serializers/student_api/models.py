from django.db import models

# Create your models here.

class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"

class Student(models.Model):

    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE) # Connection established between student and paths

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    number = models.PositiveSmallIntegerField(blank = True, null = True)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.first_name



