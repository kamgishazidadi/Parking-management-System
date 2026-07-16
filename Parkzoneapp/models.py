from django.db import models
from django.utils.timezone import now

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    phone = models.CharField(max_length=10)
    residence = models.CharField(null = True,max_length=50 )
    password = models.CharField(max_length=32,)

    def __str__(self):
        return f"{self.name}"


class ParkingLot(models.Model):
    CATEGORY_CHOICES = {
        "PARMANENT":"PARMANENT",
        "TEMPORARY":"TEMPORARY"
    }
    AVAILABILITY_CHOICES ={
        "AVAILABLE":"AVAILABLE",
        "OCCUPIED":"OCCUPIED",
        "RESERVED":"RESERVED"
    }

    slotNumber = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, default="TEMPORARY",max_length=100)
    availability = models.CharField(choices=AVAILABILITY_CHOICES, default="AVAILABLE",max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"Slot: {self.slotNumber} is {"Temporary" if self.category== "TEMPORARY" else "Parmanent"}"


class Reservation(models.Model):
    STATUS_CHOICES = {
    "PENDING":"PENDING",
    "COMFIRMED":"COMFIRMED",
    "CENCELLED":"CENCELLED"
}

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    parkingLot = models.ForeignKey(ParkingLot, on_delete = models.CASCADE)
    reservationDate = models.DateField(auto_now=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status =models.CharField(choices=STATUS_CHOICES, default="PENDING",max_length=100)

    def __str__(self):
        return f"Reservation {self.id} done by {self.customer.name}"


class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default= now)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, default='Pending')  # Successful or Failed

    def __str__(self):
        return f"Payment for Reservation {self.reservation.id}- ({self.payment_status})"
