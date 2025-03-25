from django.urls import path,include
from .import views
from .views import pay, payment_success,doctor_register, registration_success, approved_doctors

urlpatterns = [
    # path('',views.index),
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('pay', views.pay, name='pay'),
    path('success', views.payment_success, name='payment_success'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('approved-doctors/', views.approved_doctors, name='approved_doctors'),
    # path('success',views.success,name='success'),


]
