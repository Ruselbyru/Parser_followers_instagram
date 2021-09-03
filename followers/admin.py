from django.contrib import admin
from .models import Profile,Followers,Files

# Register your models here.
admin.site.register(Profile)
admin.site.register(Followers)
admin.site.register(Files)