from django.urls import path
from .views import index, TrainerSignUpView
from Trainers .views import trainer_loginpage,dashboard

urlpatterns = [
    path('', index, name='index'),
    path('trainer_login_page', trainer_loginpage, name='trainer_login_page'),
    path('trainer_sign_up_page/', TrainerSignUpView, name='trainer_sign_up_page'),
    path('Dashboard', dashboard, name='dashboard'),

]
