from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True,blank=True)# we allow this field to be null



class CommitteeRole(models.Model):
    name = models.CharField(max_length=100)
    member = models.ForeignKey(Member,null=True,on_delete=models.CASCADE)
