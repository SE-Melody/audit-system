from django.urls import path

from . import views

app_name = 'stud'

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('reg_syl', views.reg_syl, name='reg_syl'),
    path('check', views.check, name='check'),
]