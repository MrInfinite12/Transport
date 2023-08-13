from django.contrib import admin
from .models import Driver, Vehicle, Status

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass