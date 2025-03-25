from django import forms
from .models import Booking,ContactMessage,Doctors

class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['p_name','p_phone','p_email','doc_name','booking_date']
        widgets={
            'booking_date':DateInput(),
        }
        labels={
            'p_name':"Patient Name: ",
            'p_phone':"Patient Phone: ",
            'p_email':"Patient Email: ",
            'doc_name':"Doctor Name: ",
            'booking_date':"Booking Date: ",
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        labels = {
            'name': "Your Name",
            'email': "Your Email",
            'message': "Your Message",
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4})
        }

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model= Doctors
        fields=['doc_name','doc_spec','dep_name','doc_image']
        labels = {
            'doc_name': "Doctor's Name",
            'doc_spec': "Specialization",
            'dep_name': "Department",
            'doc_image': "Upload Profile Image",
        }


