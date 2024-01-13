from django.contrib import admin
from django.urls import path,include
from .views import main_index,WhyUs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_index, name='main_index'), 
    path('why_us/', WhyUs, name='why_us'),
    path('', include('trainers.urls')),
] 
