from django.db import models

# Create your models here.
from django.utils import timezone
from hr_employees.models import EmployeeModel
from hr_tags.models import PayrollTagModel

class PayrollModel(models.Model):

    class Meta:
        permissions = (
            ("view_payrollmodel", "Can view payroll model"),
        )

    name = models.CharField(max_length=20, verbose_name='Name')
    salary = models.IntegerField(max_length=20, verbose_name='Salary',default=None)
    ot_rate = models.IntegerField(verbose_name='OT Rate')
    allowance = models.IntegerField(verbose_name='Allowance')
    leave = models.DateField(verbose_name='Leave', default=timezone.now)
    fine = models.IntegerField(max_length=20, verbose_name='Fine',default=None)
    #expected_salary = models.CharField(max_length=20, verbose_name='Expected Salary', default=None)
    note = models.TextField(max_length=100, verbose_name='Note')  
    status = models.CharField(max_length=10, verbose_name='Status', default='draft')
    #is_active = models.BooleanField(verbose_name='Is Active', default=False)  
    create_date = models.DateTimeField(verbose_name='Create Date', default=timezone.now)
    attachment = models.ImageField(verbose_name='Image', default=None, blank=True)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField(PayrollTagModel)

    def __str__(self):
        return self.name

# Create your models here.
