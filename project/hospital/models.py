from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    approved = models.BooleanField(default=False)  # Admin approval field



    def __str__(self):
        return 'Dr '+self.doc_name +'-('+self.doc_spec+')'
    
class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date = models.DateField()  # Fixed typo (was 'bookig_date')
    booked_on = models.DateField(auto_now=True)  # Fixed typo (was 'book_on')
    # payment_id=models.CharField(max_length=30)
    # paid = models.BooleanField(default=False)  # New field to track payment

    # def __str__(self):
#     #     return f"{self.p_name} - {self.doc_name} ({'Paid' if self.paid else 'Pending'})"
        

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
    
    
    

class SuccessfulBooking(models.Model):
    booking=models.OneToOneField(Booking,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=50,unique=True)
    payment_status=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.booking.p_name}-{self.booking.doc_name} ({'Paid' if self.payment_status else 'Pending'})"


 