from django import forms
from django.forms import widgets
from .models import AttendanceModel

STATUS_CHOICES =(
    ('draft', 'draft'),
    ('Confirm', 'confirm'),
    ('Cancel', 'cancel')
)

class AttendanceForm(forms.ModelForm):
    
    class Meta:
        model = AttendanceModel
        fields = "__all__"
        labels  = {
            'name':'Enter Name', 
            'sequence':'Enter Sequence',  
            'signin_time':'Enter Signin Time',
            'signout_time':'Enter Signout Time',
            'time':'Enter Time', 
            'note':'Internal Note', 
            'status':'Status', 
            'is_active':'Is Active', 
            
            'attachment':'Upload Attachment',
            
            
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Attendance Name','class': 'form-control'}),
            'sequence': widgets.NumberInput(attrs={'placeholder':'Attendance Sequence','class': 'form-control'}),
            'signin_time': widgets.DateInput(attrs={'placeholder':'Attendance Signin Time', 'type': 'date','class': 'form-control'}),
            'signout_time': widgets.TextInput(attrs={'placeholder':'Signout Time','class': 'form-control'}),
            'time': widgets.TextInput(attrs={'placeholder':'Time','class': 'form-control'}),
            'note': widgets.TextInput(attrs={'placeholder':'Internal Note','class': 'form-control'}),
            'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'is_active': widgets.CheckboxInput(),
            
            'attachment': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }