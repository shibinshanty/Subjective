from django.shortcuts import render,redirect
from . models import *
from teacher . models import *
from django.contrib import messages

# Create your views here.


def sreg(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        phoneno=request.POST['Number']
        RegisterNumber=request.POST['RegisterNumber']
        Department=request.POST['Department']
        Password=request.POST['Password']
        conPassword=request.POST.get("conPassword")
        if Password==conPassword:
            if student_reg.objects.filter(Name=name).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=student_reg(Name=name,email=email,Number=phoneno,
            RegisterNumber=RegisterNumber,Department=Department,Password=Password)
              userdata.save()
              return redirect("slog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'student/sregister.html')
    

def slog(request):
    if request.method =="GET":
        return render(request,"student/slogin.html")
    else:
        email=request.POST.get('email') 
        Password=request.POST.get('password')
        error_message = None
        farmer_gen = student_reg.objects.get(email=email)
        data={'farmer_gen':farmer_gen}
        print(data)
            
        if farmer_gen and farmer_gen.status==1 :
            if(Password==farmer_gen.Password):
                flag=1

            if flag :
                request.session['id']=farmer_gen.id
                request.session['email']=farmer_gen.email
                return render(request,"student/spage.html",data)
            else:
                error_message = 'Email or Password invalid !!'
                return render(request,"student/slogin.html",{'error':error_message})
        else:
            if farmer_gen.status==0:
                    error_message="Admin permission required"
            else:
                error_message = 'Email or Password invalid !!'
    return render(request,'student/slogin.html',{'error':error_message})


def smssg(request):
    return render(request,'student/smssg.html')
# def slog(request):
#     if request.method=="POST":
#         try:
#             email=request.POST.get('email') 
#             Password=request.POST.get('password')
#             log=student_reg.objects.get(email=email,Password=Password)
#             request.session['email']=log.email
#             request.session['id']=log.id
#             return redirect('spage')
#         except student_reg.DoesNotExist as e :
#             messages.info(request,'Invalid User')
#     return render(request,'student/slogin.html')


def spage(request):
    return render(request,'student/spage.html')

def sprofile(request):
    hid=request.session['id']
    prof=student_reg.objects.get(id=hid)
    return render(request,'student/sprofile.html', {'pro':prof})

def seditprofile(request,id):
    edit=student_reg.objects.get(id=id)
    if request.method=="POST":
        
        # if len(request.FILES)!=0:
   
        #     edit.Image=request.FILES.get('img')

        edit.Name=request.POST.get("Name")
        edit.Number=request.POST.get("Number")
        edit.RegisterNumber=request.POST.get("RegisterNumber")
        edit.email=request.POST.get("Email")
        edit.Department=request.POST.get("Department")        
        edit.Password=request.POST.get("Password")
        edit.save()
        
        return redirect("sprofile")
    return render(request,'student/seditprofile.html',{'pro':edit})



def viewquestion(request):
    prof=Questions.objects.all()
    return render(request,'student/viewquestion.html', {'pro':prof})


def answer(request,id):
    prof=Questions.objects.get(id=id)

    if request.method=="POST":
            prof.ans=request.POST.get("ans")
            prof.studentid_id=request.session['id']
            # userdata=Questions(question=question,teacherid_id=tid)


            prof.save()

            return redirect('spage')
        # prof=Questions.objects.filter(id=id).update(ans=ans)
    return render(request,'student/answer.html', {'pro':prof})
def markdet(request):
    id=request.session['id']
    data=Questions.objects.filter(studentid=id)
    return render(request,'student/marks.html', {'data':data})
    
    
