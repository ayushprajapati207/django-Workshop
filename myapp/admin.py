from django.contrib import admin
from . models import student,Category,Product
# Register your models here.

admin.site.register(student)
admin.site.register(Category)
admin.site.register(Product)