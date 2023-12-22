# forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import TrainerRegistration

class TrainerRegistrationForm(UserCreationForm):
    class Meta:
        model = TrainerRegistration
        fields = '__all__'
