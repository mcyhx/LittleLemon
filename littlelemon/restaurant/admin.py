from django.contrib import admin

# Register your models here.
from .models import MenuItem, Booking

admin.site.register(MenuItem)
admin.site.register(Booking)
 



