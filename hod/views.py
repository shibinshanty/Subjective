from django.shortcuts import render,redirect
from . models import *
from teacher . models import *
from student . models import *
from django.contrib import messages

# Create your views here.
def hod(request):
    return render(request,'index.html')

def hreg(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        phoneno=request.POST['Number']
        Qualification=request.POST['Qualification']
        Department=request.POST['Department']
        Password=request.POST['Password']
        conPassword=request.POST.get("conPassword")
        if Password==conPassword:
            if HOD.objects.filter(Name=name).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=HOD(Name=name,Email=email,Number=phoneno,
            Qualification=Qualification,Department=Department,Password=Password)
              userdata.save()
              return redirect("hlog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'hod/hregister.html')
    



def hlog(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email') 
            Password=request.POST.get('password')
            log=HOD.objects.get(Email=email,Password=Password)
            request.session['email']=log.Email
            request.session['id']=log.id
            return redirect('hpage')
        except HOD.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'hod/hlogin.html')


def hpage(request):
    return render(request,'hod/hpage.html')

def hprofile(request):
    hid=request.session['id']
    prof=HOD.objects.get(id=hid)
    return render(request,'hod/hprofile.html', {'pro':prof})

def heditprofile(request,id):
    edit=HOD.objects.get(id=id)
    if request.method=="POST":
        
        # if len(request.FILES)!=0:
   
        #     edit.Image=request.FILES.get('img')

        edit.Name=request.POST.get("Name")
        edit.Number=request.POST.get("Number")
        edit.Qualification=request.POST.get("Qualification")
        edit.Email=request.POST.get("Email")
        edit.Department=request.POST.get("Department")        
        edit.Password=request.POST.get("Password")
        edit.save()
        
        return redirect("hprofile")
    return render(request,'hod/heditprofile.html',{'pro':edit})

def hteacher(request):
    prof=teacher_reg.objects.all()
    return render(request,'hod/hteacher.html', {'pro':prof})

def tapprove(request,pk):
    teacher_reg.objects.filter(id=pk).update(status=True)
    return redirect("hteacher")
def tdlt(request,pid):
    cart = teacher_reg.objects.get(id=pid)
    if request.method == "POST":
        cart.delete()
        return redirect("hpage")
    return render(request,'hod/tdlt.html',{'carters':cart})

def hstudent(request):
    prof=student_reg.objects.all()
    return render(request,'hod/hstudent.html', {'pro':prof})

def sapprove(request,pk):
    student_reg.objects.filter(id=pk).update(status=True)
    return redirect("hstudent")
def sdlt(request,pid):
    cart = student_reg.objects.get(id=pid)
    if request.method == "POST":
        cart.delete()
        return redirect("hpage")
    return render(request,'hod/sdlt.html',{'carters':cart})
def studentdet(request):
    
    data=Questions.objects.all()
    return render(request,'hod/hprofile.html', {'data':data})