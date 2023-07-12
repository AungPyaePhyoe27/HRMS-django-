from django.db import models

# Create your models here.
from django.utils import timezone
#from hr_employees.models import EmployeeModel
#from hr_tags.models import AttendanceTagModel

class AttendanceModel(models.Model):

    class Meta:
        permissions = (
            ("view_attendancemodel", "Can view attendance model"),
        )

    name = models.CharField(max_length=20, verbose_name='Name')
    sequence = models.IntegerField(verbose_name='Sequence')
    signin_time = models.DateTimeField(verbose_name='Signin Time', default=timezone.now)
    signout_time = models.DateTimeField(verbose_name='Signout Time', default=timezone.now)
    time = models.DateTimeField(verbose_name='Time', default=timezone.now)

    note = models.TextField(max_length=100, verbose_name='Note')  
    status = models.CharField(max_length=10, verbose_name='Status', default='draft')
    is_active = models.BooleanField(verbose_name='Is Active', default=False)  
    attachment = models.ImageField(verbose_name='Image', default=None, blank=True)
    # employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
    # #tags = models.ManyToManyField(AttendanceTagModel)

    def __str__(self):
        return self.name