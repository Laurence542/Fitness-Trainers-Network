from django.shortcuts import render


def main_index(request):
    return render(request, 'index.html')



def WhyUs(request):
    return render(request, 'why_us.html')