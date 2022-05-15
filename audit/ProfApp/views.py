from django.shortcuts import render

def index(request):
    return render(request, 'ProfApp/index.html')

def after(request):
    return render(request, 'ProfApp/class_management_after.html')