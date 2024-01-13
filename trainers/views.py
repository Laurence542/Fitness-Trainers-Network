from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrainerRegistration, PersonalDetailForm,ProfessionalDetailForm,ProfileEnhancementForm, PricingAndPaymentForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required
from .models import TrainerSignup
from django.contrib import messages

# Create your views here.

def TrainersLogin(request):
    return render(request, 'authentication/trainer-login.html')



def TrainerSignUp(request):
    if request.method == 'POST':
         form = TrainerRegistration(request.POST)
         if form.is_valid():
             user = form.save()
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=password)
             login(request, user)
             return redirect('personal-information', username=user.username)
    else:
         form = TrainerRegistration()

    context = {
            'form': form
        }    

    return render(request, 'authentication/trainer-signup.html', context)




@login_required
def PersonalInformation(request, username):
    user = get_object_or_404(TrainerSignup, username=username)

    if request.method == 'POST':
        form = PersonalDetailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your personal information has been updated successfully.')
            return redirect('professional-details', username=user.username)
        else:
            messages.error(request, 'There was an error. Please check the form and try again.')
    else:
        form = PersonalDetailForm(instance=user)

    return render(request, 'trainers-personal-infromation.html', {'user': user, 'form': form})




@login_required
def ProfessionalDetails(request, username):
    user = get_object_or_404(TrainerSignup, username=username)

    if request.method == 'POST':
        form = ProfessionalDetailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Professional details has been updated successfully.')
            return redirect('profile-enhancement',username=user.username)
        else:
            messages.error(request, 'There was an error. Please check the form and try again.')
    else:
        form = ProfessionalDetailForm(instance=user)
   

    return render(request, 'trainers-professional-details.html', {'user': user, 'form': form})




@login_required
def ProfileEnhancement(request, username):
    user = get_object_or_404(TrainerSignup, username=username)

    if request.method == 'POST':
        form = ProfileEnhancementForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Save the form data to the user's profile
            form.save()
            messages.success(request, 'Your profile enhancement has been updated successfully.')
            return redirect('pricing-and-payment')  # Redirect to a success page
        
        else:
            messages.error(request, 'There was an error. Please check the form and try again.')
    else:
        # If it's a GET request, create a new form and populate it with user's data
        form = ProfileEnhancementForm(instance=user)

    return render(request, 'trainer-profile-enhancement.html', {'form': form})



@login_required
def PricingAndPayment(request):
    user = request.user

    if request.method == 'POST':
        form = PricingAndPaymentForm(request.POST)
        if form.is_valid():
            # Save the form data to the user's profile
            user.preferred_payment_method = form.cleaned_data['preferred_payment_method']
            user.pricing_rate = form.cleaned_data['pricing_rate']
            user.save()
            messages.success(request, 'Your pricing and payment  has been updated successfully.')
            return redirect('user-profile', username=user.username)  # Redirect to a success page
        else:
            messages.error(request, 'There was an error. Please check the form and try again.')
    else:
        # If it's a GET request, create a new form and populate it with user's data
        form_data = {
            'preferred_payment_method': user.preferred_payment_method,
            'pricing_rate': user.pricing_rate,
        }
        form = PricingAndPaymentForm(initial=form_data)

    return render(request, 'trainer-pricing-and-payment.html', {'form': form})


def user_profile(request, username):
    user = get_object_or_404(TrainerSignup, username=username)
    return render(request, 'trainer-profile.html', {'user': user})

