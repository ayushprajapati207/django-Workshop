from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Shop(request):
    return render(request,"shop.html")

def formpage(request):
    return render(request,"contact.html")

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


    