from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Token(models.Model):
    user=models.OneToOneField(
        User,on_delete=models.CASCADE
    )
    token=models.CharField(max_length=48)

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
