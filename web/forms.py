from django import forms
from .models import Expense,Income
from django.utils.timezone import localtime
from django.contrib.auth.models import User



class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        
class LoginForm(forms.ModelForm):
    username=forms.CharField(max_length=150,required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
        
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


class IncomeForm(forms.ModelForm):
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