from django.urls import path
from .views import TrainersLogin, TrainerSignUp, PersonalInformation,ProfessionalDetails,ProfileEnhancement,PricingAndPayment,user_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', TrainersLogin, name='login'),
    path('sign-up/', TrainerSignUp, name='sign_up'),
    path('profiles/<str:username>/', PersonalInformation, name='personal-information'),
    path('profiles/<str:username>/professional/', ProfessionalDetails, name='professional-details'),
    path('profile-enhancement/<str:username>/', ProfileEnhancement, name='profile-enhancement'),
    path('pricing-and-payment/', PricingAndPayment, name='pricing-and-payment'),
    path('user-profile/<str:username>/', user_profile, name='user-profile'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)