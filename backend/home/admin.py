from django.contrib import admin
from .models import (
    Contact,
    CustomerText,
    ForwordedMessage,
    HomePage,
    Message,
    MessageAction,
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
admin.site.register(Message)
admin.site.register(HomePage)
admin.site.register(MessageAction)
admin.site.register(CustomerText)
admin.site.register(ForwordedMessage)

# Register your models here.
