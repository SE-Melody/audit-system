from django.shortcuts import render

def index(request):
    return render(request, 'StudApp/index.html')

def reg(request):
    return render(request, 'StudApp/desired_class_registration.html')

def reg_syl(request):
    return render(request, 'StudApp/desired_class_registration_syllabus.html')

def check(request):
    return render(request, 'StudApp/audit_class_check_.html')
