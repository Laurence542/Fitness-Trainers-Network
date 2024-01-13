from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TrainerSignup



class TrainerRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = TrainerSignup
        fields = ['username', 'email', 'password1', 'password2']




 # List of state choices
STATE_CHOICES = [
    ('', 'Select a state'),
   ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
    # Add more states as needed
]

class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = TrainerSignup
        fields = [
            'username',
            'first_name',
            'last_name',
            'mobile_number',
            'birth_date',
            'gender',
            'street_address',
            'city',
            'state',
            'zip_code',
            
        ]

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        # You can add additional validation for the mobile number if needed
        return mobile_number

    # State field with choices
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True)   





class ProfessionalDetailForm(forms.ModelForm):
    class Meta:
        model = TrainerSignup
        fields = [
            'specialization_fitness_training',
            'education_background',
            'calendar_type',
            'accredited_certification',
            'additional_certifications',
            'training_type',
            'preferred_training_environment',
            'languages_spoken',
            'speciality_populations',
            'event_preparation_specialties',
            'training_equipment_utilized',
        ]        


class ProfileEnhancementForm(forms.ModelForm):
    class Meta:
        model = TrainerSignup
        fields = ['profile_picture', 'bio', 'instagram_handle', 'facebook_handle', 'twitter_handle', 'personal_website']

    profile_picture = forms.ImageField(label='Profile Picture', required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}), label='Your Personal Bio', required=True)

    instagram_handle = forms.CharField(label='Instagram Handle', required=False)
    facebook_handle = forms.CharField(label='Facebook Handle', required=False)
    twitter_handle = forms.CharField(label='Twitter Handle', required=False)
    personal_website = forms.URLField(label='Personal Website', required=False)



class PricingAndPaymentForm(forms.ModelForm):
    class Meta:
        model = TrainerSignup
        fields = ['preferred_payment_method', 'pricing_rate']

    preferred_payment_method = forms.ChoiceField(choices=[('USD', 'USD'), ('CAD', 'CAD')],
                                               label='Preferred Payment Method',
                                               required=False)

    pricing_rate = forms.DecimalField(label='Pricing Rate', required=False)

    def clean_pricing_rate(self):
        pricing_rate = self.cleaned_data['pricing_rate']
        # You can add additional validation for the pricing rate if needed
        return pricing_rate


