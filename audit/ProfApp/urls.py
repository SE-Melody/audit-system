from django.urls import path

from . import views

app_name = 'prof'

urlpatterns = [
    path('', views.index, name='index'),
    path('before/', views.before, name='before'),
    path('ing/', views.ing, name='ing'),
    path('after/', views.after, name='after'),
]