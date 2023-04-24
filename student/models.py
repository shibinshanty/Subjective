from django.db import models

# Create your models here.
class student_reg(models.Model):
    Name=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    Password=models.CharField(max_length=200)
    Department=models.CharField(max_length=50)
    RegisterNumber=models.CharField(max_length=200)
    Number=models.CharField(max_length=200)
    status=models.BooleanField(default=False)

    def _str_(self) :
        return self.Name




 