from django.db import models
from student . models import *
# Create your models here.
class teacher_reg(models.Model):
    Name=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    Password=models.CharField(max_length=200)
    Department=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=200)
    Number=models.CharField(max_length=200)
    status=models.BooleanField(default=False)

    def _str_(self) :
        return self.Name



class Questions(models.Model):
    question=models.CharField(max_length=600)
    answer=models.CharField(max_length=10000,default=0)
    ans=models.CharField(max_length=600)
    mark=models.CharField(max_length=600,null=True)
    grade=models.CharField(max_length=20,default="No grade")
    teacherid=models.ForeignKey(teacher_reg,on_delete=models.CASCADE,null=True)
    studentid=models.ForeignKey(student_reg,on_delete=models.CASCADE,null=True)

    def _str_(self) :
        return self.question

 