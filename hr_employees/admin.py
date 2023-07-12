from django.contrib import admin

# Register your models here.
from .models import EmployeeModel
# from file_name import class_name

admin.site.register(EmployeeModel)