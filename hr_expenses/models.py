from django.db import models

# Create your models here.
from django.utils import timezone
# from hr_employees.models import EmployeeModel
# from hr_tags.models import ExpenseTagModel

class ExpenseModel(models.Model):

    class Meta:
        permissions = (
            ("view_expensemodel", "Can view expense model"),
        )

    name = models.CharField(max_length=20, verbose_name='Name')
    sequence = models.IntegerField(verbose_name='Sequence')
    
    note = models.TextField(max_length=100, verbose_name='Note')
    quality = models.TextField(max_length=100, verbose_name='Quality')
    product = models.TextField(max_length=100, verbose_name='Product') 
    price = models.IntegerField(max_length=100, verbose_name='Price')
    total = models.IntegerField(max_length=100, verbose_name='Total')
    reason = models.TextField(max_length=100, verbose_name='Reason') 
    status = models.CharField(max_length=10, verbose_name='Status', default='draft')
    
    attachment = models.ImageField(verbose_name='Image', default=None, blank=True)
    

    def __str__(self):
        return self.name