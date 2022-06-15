from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from StudApp.forms import BettingForm
from StudApp.models import Stud

def index(request):
    return render(request, 'StudApp/index.html')

def reg(request):
    hong = Stud.objects.get(id=1234567890)
    context = {'mileage': hong.mileage}
    return render(request, 'StudApp/desired_class_registration.html', context)

def reg_syl(request):
    hong = Stud.objects.get(id=1234567890)
    apply_num = 2
    if request.method == "POST":
        form = BettingForm(request.POST)
        apply_num += 1 
        if form.is_valid():
            mileage = form.cleaned_data['admin_mileage']
            deducted = hong.mileage - mileage
            hong.mileage = deducted
            hong.save()
            
            # print(mileage)
            Apply = form.save(commit=False)
            Apply.apply_time = timezone.now()
            Apply.student_id = hong.id
            Apply.save()
            context = {'original': hong.mileage, 'apply_num': apply_num}
            return render(request, 'StudApp/desired_class_registration_syllabus.html', context)
        else :
            return redirect('stud:reg_syl')

    else :
        form = BettingForm()
    context = {'form': form, 'original': hong.mileage, 'apply_num': apply_num}
    return render(request, 'StudApp/desired_class_registration_syllabus.html', context)
    # return render(request, 'StudApp/desired_class_registration_syllabus.html')

def check(request):
    hong = Stud.objects.get(id=1234567890)
    context = {'mileage': hong.mileage}
    return render(request, 'StudApp/audit_class_check_.html', context)
