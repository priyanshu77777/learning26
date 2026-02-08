from django.contrib import admin
from .models import Society,Flat,Member,Maintenance,Complaint,Notice
# Register your models here.

admin.site.register(Society)
admin.site.register(Flat)
admin.site.register(Member)
admin.site.register(Maintenance)
admin.site.register(Complaint)
admin.site.register(Notice)