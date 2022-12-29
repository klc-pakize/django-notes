from django.db import models

# Create your models here.
# Create a table:
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank = True, null = True)
    about = models.TextField(blank = True)
    email = models.EmailField()  #  automatically validates email
    is_activate = models.BooleanField(default = True)
    avatar = models.ImageField(blank = True, null = True, upload_to = "student-media")  # upload_to: Students' photos are stored separately in the student-media folder under the media folder. 


    def __str__(self):
        return f" {self.number} - {self.first_name} - {self.last_name}"
    

    class Meta:
        ordering = ("number",)  # ["number"]  = ("number",) - sort students by number in the admin panel


# How to use ImageField 
# 1- python -m pip install Pillow
# 2- main settings.py MEDIA_URL = 'media/' 
#                     MEDIA_ROOT = BASE_DIR / "media" 
# 3- main urls.py from django.conf import settings
#                 from django.conf.urls.static import static
#                      urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



# python manage.py shell   #? the area where we communicate with django from command lines
# from model_2.models import Student
# s1 = Student(first_name='aaaa',last_name='a', number=4)
# s1.save()
# s1.first_name=bbbb
# s1.save()
# s2 = Student.objects.create(first_name='cccc', last_name='c', number=5)
# student = Student.objects.all()
# print(student.query)
# for s in student: print(s)
# s1 = Student.objects.get(number=2)
# s1.number=1
# s1.save()
# s1 = Student.objects.get(number=1) errorrr
# s1 = Student.objects.filter(number=1)
# s1 = Student.objects.exclude(number=1)
# s1 = Student.objects.get(first_name__exact='Henry')
# s1 = Student.objects.get(first_name__exact='Henry')
# s1 = Student.objects.get(first_name__iexact='henry')
# s1 = Student.objects.get(last_name__contains='v')
# s1 = Student.objects.get(last_name__startswith='v')
# s1 = Student.objects.filter(number__gt=1)