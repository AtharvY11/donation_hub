# Register your models here.
from django.contrib import admin
from .models import Donation, UserProfile

admin.site.register(Donation)
admin.site.register(UserProfile)
