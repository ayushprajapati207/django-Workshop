from . import views
from django.urls import path

urlpatterns = [
    path('',views.Shop),
    path('contact',views.formpage),
    path('process',views.process),
]
