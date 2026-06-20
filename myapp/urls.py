from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.Shop),
    path('contact',views.formpage),
    path('savesession',views.saveSession),
    path('getsession',views.getSession),
    path('removesession',views.deleteSession),
    path('maildemo',views.mailsenddemo),
    path('process',views.contactpageprocess),
    path('addstudent',views.addstudent),
    path('student-process',views.studentprocess),
    path('display-student',views.displaystudent,name='display_student'),
    path('delete-student/<int:id>',views.deletestudent,name='delete_student'),

    path('loginpage', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),

     path('add-category',views.add_category,name='add_category'),
    path('display-category',views.display_category, name='display_category'),
  

]
