
from django.urls import path
from . import views

app_name = 'travelapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
]
