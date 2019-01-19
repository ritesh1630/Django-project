from django.shortcuts import render
from ritesh import models
from ritesh import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"home.html")

@login_required
def java(request):
    return render(request,"java.html")

@login_required
def python(request):
    return render(request,"python.html")

def record(request):
    data=models.Employee.objects.all()
    return render(request,"record.html",{"data":data})

def Custforms(request):
    form = forms.CustForm()
    if request.method=="POST":
        form = forms.CustForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Custname']
            return render(request,"temp.html",{"name":name})
    return render(request,"display.html",{"form":form})


def Empforms(request):
    form=forms.EmpForm()
    if request.method=="POST":
        form=forms.EmpForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            data = models.Employee.objects.all()
            return render(request,"record.html",{"msg":"Record add sussefully","data":data})
    return render(request,"Empform.html",{"form":form})


def Sign_Up_View(request):
    form=forms.Sign_Up_Form
    if request.method =="POST":
        form = form.Sign_UP_Form(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return render(request,"home.html")
    return render(request,'temp.html',{"form":form})