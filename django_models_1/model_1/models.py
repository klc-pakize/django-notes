from django.db import models

# Create your models here.
# Create a table:
class Student(models.Model):

  
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField()  # 0 to 32767
    about = models.TextField(blank = True, null = True)  # With blank and null being True we made it possible to leave it blank
    register = models.DateTimeField(auto_now_add = True)  # auto_now_add= When we add True. When the product is created, it can be added to the creation archives automatically.
    last_update_date = models.DateTimeField(auto_now = True)  # The auto_now=True argument replaces the field with the current date when the save method is called.
    is_activate = models.BooleanField(default = True)


    def __str__(self):
        return f"{self.first_name} {self.number}"  # It allows the records of students registered in the admin panel to be displayed with their names and numbers.

    class Meta:
        ordering = ["number"]  # sort students by number in the admin panel


    
