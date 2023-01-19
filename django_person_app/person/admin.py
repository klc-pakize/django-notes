from django.contrib import admin
from .models import Department, Person


admin.site.register(Person)
admin.site.register(Department)