from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . models import student,Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def Shop(request):
    all_products = Product.objects.all()
    return render(request, 'shop.html', {'products': all_products}) 

def formpage(request):
    return render(request,"contact.html")

def saveSession(request):
    request.session['username'] = "Krishna"
    return HttpResponse("Session Created")

def getSession(request):
    if request.session.has_key('username') :
        msg = request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("Session does not exixt")

def deleteSession(request):
    del request.session['usrename']
    return HttpResponse("Session deleted")

def contactpageprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']

    mymsg = "Hello ",txt1," has Contact you Mobile No is ",txt2," Message is ",txt3

    subject = 'Contact us From Website'
    email_from = settings.EMAIL_HOST_USER

    message = mymsg
    recipient_list = ['nobuddy2007@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Thank you for Contacting us.")



def mailsenddemo(request):
    subject = 'Mail Demo'
    message = ' Hello Myself'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nobuddy2007@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")   


def addstudent(request):
    return render(request,'add-student.html')

def studentprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    email = request.POST['txt3']
    txt4 = request.POST['txt4']
    student.objects.create(name=txt1,mobile=txt2,email=email,address=txt4)
    return HttpResponse("Thank You for signing in")

def displaystudent(request):
    mystudentlist = student.objects.all()
    return render(request,'display-student.html',{'mydata': mystudentlist})

def deletestudent(request,id):
    stud = student.objects.get(id=id)
    stud.delete()
    return redirect('display_student')





def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def add_category(request):
    if request.method == "POST":
        txt1 = request.POST['txt1']
        Category.objects.create(title=txt1)
        return redirect('add_category')
    return render(request, 'add-category.html')


def display_category(request):
    categorylist = Category.objects.all()
    return render (request,'display-category.html',{'category': categorylist})





