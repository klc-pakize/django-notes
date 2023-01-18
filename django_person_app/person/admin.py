from django.contrib import admin
from .models import Department, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Department)