from django.contrib import admin
from .models import Hotel
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'location_slug':('location',)}


admin.site.register(Hotel,HotelAdmin)