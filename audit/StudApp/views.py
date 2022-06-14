from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from StudApp.forms import BettingForm
from StudApp.models import Stud

def index(request):
    return render(request, 'StudApp/index.html')

def reg(request):
    return render(request, 'StudApp/desired_class_registration.html')

def reg_syl(request):
    if request.method == "POST":
        form = BettingForm(request.POST)
        if form.is_valid():
            mileage = form.cleaned_data['admin_mileage']
            # print(mileage)
            Apply = form.save(commit=False)
            Apply.apply_time = timezone.now()
            Apply.save()
            context = {'mileage': mileage}
            return render(request, 'StudApp/desired_class_registration_syllabus.html', context)
        else :
            return redirect('stud:reg_syl')

    else :
        form = BettingForm()
    context = {'form': form}
    return render(request, 'StudApp/desired_class_registration_syllabus.html', context)
    # return render(request, 'StudApp/desired_class_registration_syllabus.html')

def check(request):
    return render(request, 'StudApp/audit_class_check_.html')
