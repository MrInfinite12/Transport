from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _  
from .manager import CustomUserManager

STATUS_CHOICES = (
    ("available", "Available"),
    ("onroad", "On Road"),
    ("notavailable", "Not Available")
)

class Driver(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50) 
    email = models.EmailField(_('email_address'), unique=True, max_length = 200)
    mobile_number = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    aadhar_number = models.CharField(max_length=12)
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
      
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  
  
    objects = CustomUserManager()  
      
    def has_perm(self, perm, obj=None):  
        "Does the user have a specific permission?"  
        # Simplest possible answer: Yes, always  
        return True  
  
    # def is_staff(self):  
    #     "Is the user a member of staff?"  
    #     return self.is_staff  
  
    @property  
    def is_admin(self):  
        "Is the user a admin member?"  
        return self.is_admin  
  
    def __str__(self):  
        return self.email 

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    chasis_number = models.CharField(max_length=50)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    def __str__(self):  
        return self.model 

class Status(models.Model):
    availability = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'available'
        )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    def __str__(self):  
        return self.availability     
