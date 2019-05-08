from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email']

admin.site.register(Flight)
admin.site.register(Review)
admin.site.register(Hotel)
admin.site.register(HotelList)
admin.site.register(FlightList)