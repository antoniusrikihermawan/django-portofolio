from django.shortcuts import render

def home_view(request):
    return render(request, 'base.html') 

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html') 

def contact_view(request):
    return render(request, 'contact.html')   

def portofolio(request):
    return render(request, 'index.html')