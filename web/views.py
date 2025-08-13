from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from json import JSONEncoder
from web.models import User,Token,Expense,Income
from datetime import datetime
from django.template import loader
# Create your views here.


def main_(req):
    return render(req,'main.html')

def submit_expense(req):
    """user submit an expense"""
    if req.method == 'POST':
        title=req.POST.get('title')
        amount=req.POST.get('amount')
        date=req.POST.get('date')
        
        Income.objects.create(
            title=title,
            amount=amount,
            date=datetime.strptime(date, '%Y-%m-%d'),
            user=req.user
        )
        return render(req,"result.html")
    return render(req,"expend.html")

    # return render(req,"result.html")


def submit_income(req):
    """user submit an income"""
    pass
    

def register(request):
    # form is filled 
    pass
    # if request.POST.has_key('requescode'):
        
    #     if not grecaptcha_verify(request):
    #         context={'message':''}
    #         return render(request,'register.html')