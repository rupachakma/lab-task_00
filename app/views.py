from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from app.models import Students

# Create your views here.
def home(request):
    students = Students.objects.all()
    return render(request,"home.html",{'students':students})

def signuppage(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password2")
        if pass1 == pass2:
            myuser = User.objects.create_user(name,email,pass1)
            myuser.save()
            return redirect("loginpage")
        else:
            return redirect("signuppage")
    return render(request,"signup.html")

def loginpage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            return redirect("loginpage")
    return render(request,"login.html")

def addstudentpage(request):
    if request.method == "POST":
        username = request.POST.get("name")
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile_num = request.POST.get("m_number")
        profilepic = request.FILES.get("profilepic")
        students = Students(
            username = username,
            fullname = fullname,
            email = email,
            phone_number =mobile_num,
            profilepic = profilepic
        )
        students.save()
        return redirect("homepage")
    return render(request,"addstudent.html")


def editPage(request,id):
   
    student=Students.objects.filter(id=id)
    context={
        "student":student,
    }
    return render(request,"edit.html",context)

def updatestudentpage(request):

    if request.method == "POST":
        username = request.POST.get("name")
        user_id = request.POST.get("userid")
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile_num = request.POST.get("m_number")
        profilepic = request.FILES.get("profilepic")

        students = Students(
            id=user_id,
            username = username,
            fullname = fullname,
            email = email,
            phone_number =mobile_num,
            profilepic = profilepic
        )
        students.save()
        return redirect("homepage")
    return render(request,"edit.html")

def deletestudent(request,id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("homepage")

