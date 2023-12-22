from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Signup(models.Model):
    username = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    confirm_password = models.TextField(max_length=50)

    def __str__(self):
        return str(self.username)

class resistration(models.Model):
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    area_code = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

   
     # Contact Preferences
    may_contact = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')])
    contact_method = models.CharField(max_length=10, choices=[('tel', 'Telephone'), ('email', 'Email')])

    # Availability
    sunday_from = models.TimeField(null=True, blank=True)
    sunday_to = models.TimeField(null=True, blank=True)
    monday_from = models.TimeField(null=True, blank=True)
    monday_to = models.TimeField(null=True, blank=True)
    tuesday_from = models.TimeField(null=True, blank=True)
    tuesday_to = models.TimeField(null=True, blank=True)
    wenesday_from = models.TimeField(null=True, blank=True)
    wenesday_to = models.TimeField(null=True, blank=True)
    thursday_from = models.TimeField(null=True, blank=True)
    thursday_to = models.TimeField(null=True, blank=True)
    friday_from = models.TimeField(null=True, blank=True)
    friday_to = models.TimeField(null=True, blank=True)
    satarday_from = models.TimeField(null=True, blank=True)
    satarday_to = models.TimeField(null=True, blank=True)
    
     # Professional Information
    fitness_instruction = models.CharField(max_length=10, choices=[('yes','Yes'), ('no', 'No')])
    personal_training = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no','No')])
    nutrition = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    pysical_therapy = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    pilates_therapy = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    sports_conditioning = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    wellness_lifestyle = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    yoga = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    massage_therapy = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    martial_arts = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    athletic_training = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    
    experience_years = models.CharField(max_length=10)

    # Ratings and Payment Methods
    charging_rate_currency = models.CharField(max_length=3, choices=[('USD', 'USD($)'), ('CAD', 'CAD')])
    charging_rate = models.CharField(max_length=100)
    
    payment_methods_cash = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    payment_methods_cashier_check = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    payment_methods_card = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    payment_methods_personal_check = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])

    
    

    def __str__(self):
        return self.full_name

class TrainerRegistration(AbstractUser):
    # Personal Details

    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    area_code = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

   
     # Contact Preferences
    may_contact = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')])
    contact_method = models.CharField(max_length=10, choices=[('tel', 'Telephone'), ('email', 'Email')])

    # Availability
    sunday_from = models.TimeField(null=True, blank=True)
    sunday_to = models.TimeField(null=True, blank=True)
    monday_from = models.TimeField(null=True, blank=True)
    monday_to = models.TimeField(null=True, blank=True)
    tuesday_from = models.TimeField(null=True, blank=True)
    tuesday_to = models.TimeField(null=True, blank=True)
    wenesday_from = models.TimeField(null=True, blank=True)
    wenesday_to = models.TimeField(null=True, blank=True)
    thursday_from = models.TimeField(null=True, blank=True)
    thursday_to = models.TimeField(null=True, blank=True)
    friday_from = models.TimeField(null=True, blank=True)
    friday_to = models.TimeField(null=True, blank=True)
    satarday_from = models.TimeField(null=True, blank=True)
    satarday_to = models.TimeField(null=True, blank=True)
    
     # Professional Information
    fitness_instruction = models.CharField(max_length=10, choices=[('yes','Yes'), ('no', 'No')])
    personal_training = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no','No')])
    nutrition = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    pysical_therapy = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    pilates_therapy = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    sports_conditioning = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    wellness_lifestyle = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    yoga = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    massage_therapy = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    martial_arts = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    athletic_training = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    
    experience_years = models.CharField(max_length=10)

    # Ratings and Payment Methods
    charging_rate_currency = models.CharField(max_length=3, choices=[('USD', 'USD($)'), ('CAD', 'CAD')])
    charging_rate = models.CharField(max_length=100)
    
    payment_methods_cash = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    payment_methods_cashier_check = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    payment_methods_card = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])
    payment_methods_personal_check = models.CharField(max_length=10, choices=[('yes', 'Yes'),('no', 'No')])

    
    

    def __str__(self):
        return self.full_name
