from django.contrib import admin

# Register your models here.
from .models import User, PersonalData

admin.site.register(User)
admin.site.register(PersonalData)
