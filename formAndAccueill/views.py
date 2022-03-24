from django.shortcuts import render

# Create your views here.
def formAr_view(request):
    return render(request,'formAr.html')

def formFr_view(request):
    return render(request,'formFr.html')

def formEn_view(request):
    return render(request,'formEn.html')

def home_view(request):
    return render(request,'Ac.html')

def login_view(request):
    return render(request,'login.html')
