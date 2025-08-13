from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PassworresetCodes(models.Model):
    code=models.CharField(max_length=32)
    email=models.CharField(max_length=120)
    time=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class Token(models.Model):
    user=models.OneToOneField(
        User,on_delete=models.CASCADE
    )
    token=models.CharField(max_length=48)
    
    def __unicode__(self):
        return "{}_token".format(self.user)
    
class Expense(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # return string in admin page
    def __unicode__(self):
        return "{}-{}".format(self.date,self.amount)

class Income(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # return string in admin page
    def __unicode__(self):
        return "{}-{}".format(self.date,self.amount)
