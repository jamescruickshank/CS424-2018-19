from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True,blank=True)# we allow this field to be null

    def initials(self):
        first_names = self.first_name.split(" ")
        last_names = self.last_name.split("'")

        return self.first_name[:1]+self.last_name[:1]


class CommitteeRole(models.Model):
    name = models.CharField(max_length=100)
    member = models.ForeignKey(Member,null=True,on_delete=models.CASCADE)
