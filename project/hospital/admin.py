from django.contrib import admin
from .models import Departments,Doctors,Booking,ContactMessage

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