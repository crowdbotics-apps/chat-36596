from django.contrib import admin
from .models import Contact, ThreadAction, VerificationCode

admin.site.register(VerificationCode)
admin.site.register(Contact)
admin.site.register(ThreadAction)

# Register your models here.
