from django.contrib import admin
# Register your models here.
from .models import User,Coordinacion

admin.site.register(User)
admin.site.register(Coordinacion)