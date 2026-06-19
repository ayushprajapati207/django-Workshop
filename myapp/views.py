from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . models import student
# Create your views here.

def Shop(request):
    return render(request,"shop.html")

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


def loginpage(request):
    return render(request,'login.html')

def loginprocess(request):
    txt = request.POST['txt1']
    request.session['myname'] = txt
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myname'):
        return render(request,'dashboard.html')
    else:
        return redirect(loginpage)
    
def logout(request):
    del request.session['myname']
    return redirect(loginpage)

def addstudent(request):
    return render(request,'add-student.html')

def studentprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    return HttpResponse("Thank You")


