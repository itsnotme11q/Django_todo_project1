from django.shortcuts import render, HttpResponse , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if(password == confirm_password):
            user=User(username=username)
            user.set_password(password)
            user.save()
            return redirect('/login')
    return render(request,'registration_page.html')
    #return HttpResponse("This is home")

def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_auth=User.objects.filter(username=username).first()
        if user_auth is None:
            messages.success(request, 'User not found')
            return redirect('/login')
        user_pass= authenticate(username=username,password=password)
        print("user",user_pass)
        if( user_pass ):
            login(request,user_auth)
            return redirect('/home')
        else:
            messages.success(request, 'Wrong password')
            return redirect('/login')
    return render(request,'login_page.html')
    # return HttpResponse("This is home")

def home(request):
    contacts=Contact.objects.all()
    context={'contacts':contacts}
    return render(request,'home.html',context)
    # return HttpResponse("This is home")

def dynamic_home(request,id):
    contacts=Contact.objects.all()
    context={'title':f'home{id}','id':id,'contacts':contacts}
    return render(request,'home.html',context)
    # return HttpResponse("This is dnamic home")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is home")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        if(name!=None and address!=None and phone!=None):
            contact_obj=Contact(name=name,address=address,phone=phone)
            contact_obj.save()
    return render(request,'contact.html')
    #return HttpResponse("This is home")

@login_required(login_url='/login/')
def todo(request):
    print(request.user)
    if request.method=="POST":
        todo=request.POST.get("todo")
        if(todo!=None):
            todo_obj=Todo(todo=todo,user=request.user)
            todo_obj.save()
        return redirect('/todo')
    todos=Todo.objects.filter(user=request.user)
    context={"todos":todos}
    return render(request,'todo.html',context)
    #return HttpResponse("This is home")

def todo_delete(request , id):
    try:
        todo=Todo.objects.get(id=id)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return redirect('/todo')


def is_complete_fun(request , id):
    try:
        todo=Todo.objects.get(id=id)
        if(todo.is_complete):
            todo.is_complete=False
            todo.save()
        else:
            todo.is_complete=True
            todo.save()
    except Todo.DoesNotExist:
        pass
    return redirect('/todo')

def logout_page(request):
    return redirect('login_page.html')
    #return HttpResponse("This is home")