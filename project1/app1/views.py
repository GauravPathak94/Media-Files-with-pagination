
from urllib.request import Request
from django.shortcuts import render,redirect
from . forms import EmployeeForm
from .models import Employee
from django.core.paginator import Paginator, EmptyPage


# Create your views here.
def EmployeeView(request):
    form = EmployeeForm()
    template_name = 'app1/empform.html'
    context = {'form':form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name, context)

def ShowEmployeeView(request,page=1):
    obj = Employee.objects.all()
    paginator = Paginator(obj, 3)
    try:
        obj = paginator.page(page)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    template_name = 'app1/showemp.html'
    context = {'obj':obj}
    return render(request, template_name, context)

def UpdateEmployeeView(request,id):
    obj = Employee.objects.get(id=id)
    form = EmployeeForm(instance=obj)
    template_name = 'app1/empform.html'
    context = {'form':form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request,template_name, context)

def DeleteEmployeeView(request,id):
    obj = Employee.objects.get(id=id)
    template_name = 'app1/confirmation.html'
    context = {'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request,template_name,context) 

