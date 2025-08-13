from django.urls import path
from . import views


urlpatterns=[
    path('', views.main_, name='main'),

    path('submit/expense/',
        views.submit_expense,name='submit_expense')
,
    path('submit/income/',
         views.submit_income,name='income_expense')
    ,
    path('register/',views.register,name="register")
]