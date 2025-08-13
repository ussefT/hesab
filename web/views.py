# -*- coding: utf-8 -*-


from django.shortcuts import render,redirect
from web.models import User,Token,Expense,Income,PassworresetCodes
from datetime import datetime
from .forms import ExpenseForm,RegisterForm,LoginForm
import requests
from django.conf import settings
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.


def main_(req):
    return render(req,'main.html')

@login_required
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
    context={'message':success_message}
    return render(req,"expend.html",
                  {
                    "form":form,
                   },context)

    # return render(req,"result.html")


def submit_income(req):
    """user submit an income"""
    
    success_message = None
    
    if req.method == 'POST':
        form=Income(req.POST)
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
    
@login_required
def result(req):
    expends=Expense.objects.select_related("user").order_by("-date")
    incomes=Income.objects.select_related("user").order_by("-date")
    return render(req,
                  "result.html",
                  {"expends":expends,"incomes":incomes})

def send_verification_email(email,verification_code):
    api_url = "https://api.resend.com/emails"
    api_key = settings.RESEND_API_KEY
    data={
        "from":"hesab@example.com",
        "to":[email],
        "subject":"Verify Your Account",
        "html":f"<p>Your verification code is: <strong>{verification_code}</strong></p>"
    }
    
    response = requests.post(api_url, json=data, headers={"Authorization": f"Bearer {api_key}"})
    return response.status_code == 200

def random_str(length=8):
    import string
    char=string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length))

def login(req):
    if req.method=='POST':
        form=LoginForm(req.POST)
        if form.is_calid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req,user)
                return redirect('main')
            else:
                form.add_error(None, "Invalid username or password.")

    else:
        form=LoginForm()
        
    return render(req,'login.html',{"form":form})

def register(req):
    # form is filled 
    if req.method == 'POST' :
        form=RegisterForm(req.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            
            if RegisterForm.objects.filter(email=email).exists():
                context={'message':"Email already exists"}
                
                return render(req,
                            "register.html",
                            {"form":form,"erorr":"Email already exists"})
            
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                verification_code=str(random.randint(100000, 999999))
                now=datetime.now()
                email=req.POST['email']
                username=req.POST['username']
                password=req.POST['password']
                temporary_code=PassworresetCodes(
                    code=verification_code,
                    email=email,
                    time=now,
                    username=username,
                    password=password
                )
                temporary_code.save()
                if send_verification_email(email, verification_code):
                    return render(req,
                                  "verify.html",
                                  {"email":email,"code":verification_code})
                else:
                    context={"message":"Failed to send verification email. Please try again later."}
                    return render(req,
                                  "register.html",
                                  {"form":form},context)
            else:
                context={"message":"Username already exists"}
                return render(req,
                            "register.html",
                            {"form":form},context)
        else:
             return render(req, 'register.html', {'form': form})
    elif req.GET.get('code'):
        email = req.GET.get('email')
        code = req.GET.get('code')
        if PassworresetCodes.objects.filter(code=code).exists():
            new_temp_user=PassworresetCodes.objects.get(code=code)
            newUser=User.object.create(username=new_temp_user.username,password=new_temp_user.password,email=new_temp_user.email)
            this_token=random_str(48)
            token=Token.objects.create(user=newUser,token=this_token)
            token.save()
            PassworresetCodes.object.filter(code=code).delete()
            context={'message':'Registration successful! You can now log in. Your Token {}'.format(this_token)}
            return render(req, 'login.html', context)
        else:
            context={'message':'Invalid verification code. Try again.'}
            return render(req, 'login.html', context)
    else:
        form=RegisterForm()
        return render(req,'register.html',{'form':form})