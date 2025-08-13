from django.urls import re_path
from . import views


urlpatterns=[
    re_path(r'^main/$', views.main_, name='main'),

    re_path(r'^submit/expense/$',
        views.submit_expense,name='submit_expense')
,
    re_path(r'^submit/income/$',
         views.submit_income,name='submit_income')
    ,
    re_path(r'^result/$',views.result,name='result'),
    
    re_path(r'^register/$',views.register,name="register")
    ,
    re_path(r'^login/$',views.login,name="login"),
    
]