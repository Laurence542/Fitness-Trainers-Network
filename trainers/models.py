from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TrainerSignup(AbstractUser):
#    personal information
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=10, blank=True)  # Changed from IntegerField to CharField
    birth_date = models.CharField(max_length=255, blank=True)

    # Gender field
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)

    # Home Address
    street_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)  # Change this to a CharField
    zip_code = models.CharField(max_length=255, blank=True)  # Changed from IntegerField to CharField

     # Additional Personal Information
    specialization_fitness_training = models.CharField(max_length=255, blank=True)
    education_background = models.CharField(max_length=255, blank=True)
    calendar_type = models.CharField(max_length=255, blank=True)
    accredited_certification = models.CharField(max_length=255, blank=True)
    additional_certifications = models.CharField(max_length=255, blank=True)
    training_type = models.CharField(max_length=255, blank=True)
    preferred_training_environment = models.CharField(max_length=255, blank=True)
    languages_spoken = models.CharField(max_length=255, blank=True)
    speciality_populations = models.CharField(max_length=255, blank=True)
    event_preparation_specialties = models.CharField(max_length=255, blank=True)
    training_equipment_utilized = models.CharField(max_length=255, blank=True)


     # Profile Enhancement Fields
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    instagram_handle = models.CharField(max_length=255, blank=True)
    facebook_handle = models.CharField(max_length=255, blank=True)
    twitter_handle = models.CharField(max_length=255, blank=True)
    personal_website = models.URLField(blank=True)


    # Pricing and Payment Fields
    preferred_payment_method = models.CharField(max_length=10, choices=[('USD', 'USD'), ('CAD', 'CAD')], blank=True)
    pricing_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)



    def __str__(self):
        return self.username

