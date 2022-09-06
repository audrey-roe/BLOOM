from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    caregiver_name = models.CharField(max_length= 200, null=False, blank=False)
    child_age = models.PositiveIntegerField(null=False, blank=False)
    child_name = models.CharField(max_length= 200, null=False, blank=False)
    relation_to_child = models.CharField(max_length= 200, null=False, blank=False)
    caregiver_email = models.EmailField(max_length=50, null=False, blank=False)
    caregiver_phone = models.BigIntegerField( null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=True)
    score = models.IntegerField(null=True)
    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.caregiver_name


class quiz(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f"Question: {self.question} Ans: {self.ans}"