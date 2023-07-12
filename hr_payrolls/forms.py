from django import forms
from django.forms import widgets
from .models import PayrollModel

STATUS_CHOICES =(
    ('draft', 'draft'),
    ('Confirm', 'confirm'),
    ('Cancel', 'cancel')
)

class PayrollForm(forms.ModelForm):
    
    class Meta:
        model = PayrollModel
        fields = "__all__"
        labels  = {
            'name':'Enter Name', 
            'salary':'Enter Salary',  
            'ot_rate':'Enter OT Rate',
            'allowance':'Enter Allowance', 
            'leave':'Enter Leave',
            'fine':'Enter Fine',
            'note':'Internal Note', 
            'status':'Status', 
            # 'is_active':'Is Active', 
            'create_date':'Enter Create Date', 
            'attachment':'Upload Attachment',
            'employee': 'Employee',
            'tags': 'Tags'
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Payroll Name','class': 'form-control'}),
            'salary': widgets.NumberInput(attrs={'placeholder':'Payroll Salary','class': 'form-control'}),
            'leave': widgets.DateInput(attrs={'placeholder':'Payroll Leave', 'type': 'date','class': 'form-control'}),
            'ot_rate': widgets.NumberInput(attrs={'placeholder':'Payroll OT Rate','class': 'form-control'}),
            'allowance': widgets.NumberInput(attrs={'placeholder':'Payroll Allowance','class': 'form-control'}),
            'fine': widgets.NumberInput(attrs={'placeholder':'Payroll Fine','class': 'form-control'}),
            'note': widgets.TextInput(attrs={'placeholder':'Internal Note','class': 'form-control'}),
            'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'create_date': widgets.DateTimeInput(attrs={'type':'datetime-local','class': 'form-control'}),
            'attachment': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            'employee': widgets.Select(attrs={'class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple()
        }