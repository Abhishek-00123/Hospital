from django.contrib import admin
from .models import Departments,Doctors,Booking,ContactMessage,SuccessfulBooking

# Register your models here.

admin.site.register(Departments)
# admin.site.register(Doctors)
admin.site.register(ContactMessage)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_spec', 'dep_name', 'approved')
    list_filter = ('approved',)
    actions = ['approve_doctors']

    def approve_doctors(self, request, queryset):
        queryset.update(approved=True)
    approve_doctors.short_description = "Approve selected doctors"

admin.site.register(Doctors, DoctorsAdmin)

admin.site.register(SuccessfulBooking)
class SuccessfulBookingAdmin(admin.ModelAdmin):
    list_display=('get_patient_name','get_docter_name',"get_booking_date",'payment_id',"payment_status")
    search_fields = ('booking__p_name', 'booking__doc_name__doc_name', 'payment_id')
    list_filter = ('payment_status', 'booking__booking_date')

    def get_patient_name(self, obj):
        return obj.booking.p_name
    get_patient_name.short_description = 'Patient Name'

    def get_doctor_name(self, obj):
        return obj.booking.doc_name.doc_name  # Get doctor's name from the ForeignKey
    get_doctor_name.short_description = 'Doctor Name'

    def get_booking_date(self, obj):
        return obj.booking.booking_date
    get_booking_date.short_description = 'Booking Date'