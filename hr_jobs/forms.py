from django import forms
from django.forms import widgets
from .models import JobModel

STATUS_CHOICES =(
    ('draft', 'draft'),
    ('Confirm', 'confirm'),
    ('Cancel', 'cancel')
)

class JobForm(forms.ModelForm):
    
    class Meta:
        model = JobModel
        fields = "__all__"
        labels  = {
            'name':'Enter Name', 
            'sequence':'Enter Sequence',  
            'open_date':'Enter Open Date',
            'expected_salary':'Enter Expected Salary', 
            'note':'Internal Note', 
            'status':'Status', 
            'is_active':'Is Active', 
            'create_date':'Enter Create Date', 
            'attachment':'Upload Attachment',
            'department': 'Department',
            'tags': 'Tags'
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Job Name','class': 'form-control'}),
            'sequence': widgets.NumberInput(attrs={'placeholder':'Job Sequence','class': 'form-control'}),
            'open_date': widgets.DateInput(attrs={'placeholder':'Job Open Date', 'type': 'date','class': 'form-control'}),
            'expected_salary': widgets.TextInput(attrs={'placeholder':'Expected Salary','class': 'form-control'}),
            'note': widgets.TextInput(attrs={'placeholder':'Internal Note','class': 'form-control'}),
            'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'is_active': widgets.CheckboxInput(),
            'create_date': widgets.DateTimeInput(attrs={'type':'datetime-local','class': 'form-control'}),
            'attachment': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            'department': widgets.Select(attrs={'class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple()
        }