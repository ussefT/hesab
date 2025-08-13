from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from json import JSONEncoder
from web.models import User,Token,Expense,Income
from datetime import datetime
from django.template import loader
from .forms import ExpenseForm
# Create your views here.


def main_(req):
    return render(req,'main.html')

def submit_expense(req):
    """user submit an expense"""
    success_message = None
    
    if req.method == 'POST':
        form=ExpenseForm(req.POST)
        if form.is_valid():
            expend=form.save(commit=False)
            expend.user=req.user    
            expend.save()
            success_message = "Event saved successfully!"
            return redirect('result')
    else:
        form=ExpenseForm()
    
    return render(req,"expend.html",
                  {
                    "form":form,
                   "success_message":success_message
                   })

    # return render(req,"result.html")


def submit_income(req):
    """user submit an income"""
    pass
    
def result(req):
    expends=Expense.objects.select_related("user").order_by("-date")
    incomes=Income.objects.select_related("user").order_by("-date")
    return render(req,
                  "result.html",
                  {"expends":expends,"incomes":incomes})

def register(request):
    # form is filled 
    pass
    # if request.POST.has_key('requescode'):
        
    #     if not grecaptcha_verify(request):
    #         context={'message':''}
    #         return render(request,'register.html')