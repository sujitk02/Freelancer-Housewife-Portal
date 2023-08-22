
from django.shortcuts import render, redirect
from django.http import HttpResponse
from application.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    
    return render(request, 'about.html')

def problem_statement(request):
    return render(request, 'problem-statement.html')

def project_scope(request):
    return render(request, 'project-scope.html')

def driver_form(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')

        enquiry = driver_table(name = a, email = b, phone = c, message = d)
        enquiry.save()

        messages.success(request, 'Driver Reg. Form Submitted Successfully...')

    return render(request, 'driver-form.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            # is not None is keyword None 'N' is capital which check above user (username and password) is available in database or not

            login(request, user)
            
            request.session['username_id'] = username    

            # Redirect to a success page.
            return redirect('dashboard')
            # from django.shortcuts import redirect, render - this module we need to import in same file, to access redirect() where only path name should be call
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')

@login_required(login_url='login_user')
def dashboard(request):
    
    info = driver_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}

    print('You are logged in, Hi', request.session.get('username_id'))

    return render(request, 'dashboard/dashboard.html', data)

def driver_info(request):

    info = driver_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}

    
    return render(request, 'dashboard/tables.html', data)



