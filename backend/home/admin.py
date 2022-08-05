from django.contrib import admin
from .models import Contact, Profile, Thread, ThreadAction, VerificationCode

admin.site.register(VerificationCode)
admin.site.register(Contact)
admin.site.register(ThreadAction)
admin.site.register(Thread)
admin.site.register(Profile)

# Register your models here.
