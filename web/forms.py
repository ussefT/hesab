from django import forms
from .models import Expense,Income
from django.utils.timezone import localtime



class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=['title','date','amount','user']
        widgets = {
            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            )
        }
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if self.instance and self.instance.date:
            self.initial['date']=localtime(self.instance.date).strftime("%Y-%m-%dT%H:%M")

