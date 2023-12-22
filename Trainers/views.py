from django.shortcuts import render, redirect
from .forms import TrainerRegistrationForm
from .models import Signup
from django.http import HttpResponse
import re

def index(request):
    return render(request, 'index.html')


def trainer_loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            error_message = 'Please fill in all the fields.'
            return render(request, 'trainer_loginpage.html', {'error_message': error_message})

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            error_message = 'Please enter a valid email address.'
            return render(request, 'trainer_loginpage.html', {'error_message': error_message})

        if password != confirm_password:
            error_message = 'Passwords do not match.'
            return render(request, 'trainer_loginpage.html', {'error_message': error_message})

        # Check if a user with the same email already exists
        if Signup.objects.filter(email=email).exists():
            error_message = 'An account with this email already exists.'
            return render(request, 'trainer_loginpage.html', {'error_message': error_message})
        else:
            # Use Django's create_user method for better password handling
            user = Signup.objects.create(username=username, email=email, password=password)

            if user:
             # Redirect to the login page after successful signup
              error_message = 'Account created sucessfully.'
              return render(request, 'questions.html',{'error_message': error_message})

    return render(request, 'trainer_loginpage.html')


def TrainerSignUpView(request):
   if request.method == 'POST':
        form = TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect('dashboard')
   else:
        form = TrainerRegistrationForm()

   return render(request, 'trainers/trainer_signup_page.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logins(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        manager_users = Signup.objects.filter(email=email, password=password)

        if manager_users:
            return render(request, 'dashboard.html', {'error_message': 'You have successfully logged in.'})
        
        else:
             return render(request, 'register.html', {'error_message': 'Invalid username or password. Please try again'})
       
    
    return render(request, 'register.html')



def questions(request):
    return render(request, 'questions.html')





