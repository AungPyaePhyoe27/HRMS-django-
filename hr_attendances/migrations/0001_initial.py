# Generated by Django 2.0 on 2023-06-28 15:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr_employees', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('sequence', models.IntegerField(verbose_name='Sequence')),
                ('signin_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Signin Time')),
                ('signout_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Signout Time')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time')),
                ('note', models.TextField(max_length=100, verbose_name='Note')),
                ('status', models.CharField(default='draft', max_length=10, verbose_name='Status')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('attachment', models.ImageField(blank=True, default=None, upload_to='', verbose_name='Image')),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hr_employees.EmployeeModel')),
            ],
            options={
                'permissions': (('view_attendancemodel', 'Can view attendance model'),),
            },
        ),
    ]