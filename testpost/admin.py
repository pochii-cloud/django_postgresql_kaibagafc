from django.contrib import admin

# Register your models here.
from testpost.models import Room, Joined

admin.site.register(Room)
admin.site.register(Joined)

