from django import forms
from django.forms import widgets
from .models import ExpenseModel

STATUS_CHOICES =(
    ('draft', 'draft'),
    ('Confirm', 'confirm'),
    ('Cancel', 'cancel')
)

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = ExpenseModel
        fields = "__all__"
        labels  = {
            'name':'Enter Name', 
            'sequence':'Enter Sequence',  
            'product':'Enter Product',
            'price':'Enter Price', 
            'note':'Internal Note',
            'reason':'Reason', 
            'status':'Status', 
            'quality':'Quality',
            'total':'Enter Total', 
            'attachment':'Upload Attachment',
            
            
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Expense Name','class': 'form-control'}),
            'sequence': widgets.NumberInput(attrs={'placeholder':'Expense Sequence','class': 'form-control'}),
            'product': widgets.TextInput(attrs={'placeholder':'Expense Product','class': 'form-control'}),
            'price': widgets.TextInput(attrs={'placeholder':'Price','class': 'form-control'}),
            'note': widgets.TextInput(attrs={'placeholder':'Internal Note','class': 'form-control'}),
            'reason': widgets.TextInput(attrs={'placeholder':'Internal Reason','class': 'form-control'}),
            'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'quality': widgets.TextInput(attrs={'placeholder':'Expense Quality','class': 'form-control'}),
            'total': widgets.NumberInput(attrs={'placeholder':'Expense Total','class': 'form-control'}),
            'attachment': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }