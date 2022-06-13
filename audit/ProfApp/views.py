from django.shortcuts import redirect, render
from .models import Subject, Unit

def start_week(unit):
    start_week = []
    unit = unit.replace(" ", "")
    for tar in unit.split(','):
        if '-' in tar: # 유닛인 경우
            bar_index = tar.find('-')
            tar = tar[0:bar_index]
        start_week.append(tar)
    return start_week

def index(request):
    return render(request, 'ProfApp/index.html')

def before(request):
    return render(request, 'ProfApp/class_management_before.html')

def ing(request):
    # 청강관리 눌렀을 때 아래 내용 보여주기
    # 유닛을 입력 받고 이를 저장했을 때 assign id
    if(request.method == "POST"):
        subject = Subject()
        subject.unit_list = request.POST['unit']
        unit_info = subject.unit_list
        # subject.save()
        
        unit = Unit()
        start_week_list = start_week(unit_info)
        # print(start_week_list)
        for sw in start_week_list:
            unit.id = int(sw)
            unit.apply_period = '2022-06-13'
            unit.save()

    # limit_num 추가
    
        return redirect('prof:ing')
        
    return render(request, 'ProfApp/class_management_ing.html')

def after(request):
    return render(request, 'ProfApp/class_management_after.html')