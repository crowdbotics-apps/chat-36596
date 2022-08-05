from django.contrib import admin
from .models import (
    Contact,
    Profile,
    Thread,
    Thread_members,
    ThreadAction,
    VerificationCode,
)

admin.site.register(VerificationCode)
admin.site.register(Contact)
admin.site.register(ThreadAction)
admin.site.register(Thread)
admin.site.register(Profile)
admin.site.register(Thread_members)

# Register your models here.
