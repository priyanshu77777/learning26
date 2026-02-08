from django.contrib import admin
from .models import Student,Product,Car,StudentProfile,Category,Service,Instructor,Batch
# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Instructor)
admin.site.register(Batch)