from . import views
from django.urls import path

urlpatterns = [
    path('',views.Shop),
    path('contact',views.formpage),
    path('savesession',views.saveSession),
    path('getsession',views.getSession),
    path('removesession',views.deleteSession),
    path('loginpage',views.loginpage),
    path('dashboard',views.dashboard),
    path('loginprocess',views.loginprocess),
    path('logout',views.logout),
    path('maildemo',views.mailsenddemo),
    path('process',views.contactpageprocess),
    path('addstudent',views.addstudent),
    path('student-process',views.studentprocess),
    path('display-student',views.displaystudent,name='display_student'),
    path('delete-student/<int:id>',views.deletestudent,name='delete_student'),

]
