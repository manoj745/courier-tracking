
from django.contrib import admin

# Register your models here.
from .models import Booking, Profile


admin.site.register(Booking)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','photo']