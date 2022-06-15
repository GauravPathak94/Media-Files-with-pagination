from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','name','address', 'media']
admin.site.register(Employee, EmployeeAdmin)
