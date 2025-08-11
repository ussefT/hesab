from django.contrib import admin
from .models import Expense,Income,Token

# Register your models here.

class Expense_admin(admin.ModelAdmin):
    list_display=("title","amount")
    list_filter=("date","amount")
admin.site.register(Expense,Expense_admin)

class Income_admin(admin.ModelAdmin):
    list_display=("title","amount")
    list_filter=("date","amount")
    
admin.site.register(Income,Expense_admin)

admin.site.register(Token)