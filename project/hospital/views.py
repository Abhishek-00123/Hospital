from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm,ContactForm,DoctorRegistrationForm
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')


def doctors(request):
    dict_docs={
        'doctors': Doctors.objects.filter(approved=True)  # ✅ Show only approved doctors
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pay')
            # return render(request,'confirmation.html')
        
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def pay(request):
    if request.method=="POST":
        amount = int(request.POST.get('amount'))*100
        client=razorpay.Client(auth=('rzp_test_s9NGH58YEB5LpP','7Zv6d2Puo91rM0fIfJDT3sew'))
       

        payment_order = client.order.create ({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment_order)
        return render(request,'payment.html',{'payment':payment_order})
    return render(request,'payment.html')




def payment_success(request):
    return render(request,'confirmation.html')






def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to the same page after submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def doctor_register(request):
    if request.method=="POST":
        form= DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
                        doctor = form.save(commit=False)
                        doctor.is_approved = False  # Admin must approve
                        doctor.save()
                        return redirect('registration_success')  # Redirect to a success page
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor_register.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')


def approved_doctors(request):
    doctors = Doctors.objects.filter(is_approved=True)  # Only approved doctors
    return render(request, 'doctors.html', {'doctors': doctors})

