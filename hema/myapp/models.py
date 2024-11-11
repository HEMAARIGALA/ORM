from django.db import models
from django.contrib import admin
class Costumer(models.Model):
   cid=models.CharField(max_length=20,primary_key="cid")
   accountnumber=models.IntegerField()
   name=models.CharField(max_length=20)
   age=models.IntegerField()
   address=models.CharField(max_length=50)
   phonenumber=models.IntegerField()



class CostumerAdmin(admin.ModelAdmin):
   list_display=('cid','accountnumber','name','age','address','phonenumber')