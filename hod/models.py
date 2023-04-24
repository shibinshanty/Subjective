from django.db import models

# Create your models here.
class HOD(models.Model):
    Name=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=200)
    Number=models.BigIntegerField()
    Email=models.EmailField(max_length=50)
    Department=models.CharField(max_length=50)
    Password=models.CharField(max_length=20,default="null")
    
    def __str__(self) :
        return self.Name