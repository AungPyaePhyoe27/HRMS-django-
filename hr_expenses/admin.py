from django.contrib import admin

# Register your models here.
from hr_expenses.models import ExpenseModel

admin.site.register(ExpenseModel)