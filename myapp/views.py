from django.shortcuts import render,redirect
from django.http import HttpResponse
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



def process(request):
    a = int(request.POST['C'])
    b = int(request.POST['C++'])
    c = int(request.POST['OOPS'])
    total = a + b + c   
    per = total / 3
    d = ""
    if per > 90 :
        d = "O grade"
    elif per > 80 and per <= 90:
        d = "A Grade"
    elif per > 70 and per <= 80:
        d = "B Grade"
    elif per > 60 and per <= 70:
        d = "C Grade"
    else:
        d ="Failed"
    
    #return HttpResponse(msg)
    return render(request,'ans.html',{'mark1':a,'mark2':b,'mark3':c,'mytotal':total,'percentage':per,'Grade':d})


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


