from django.conf import settings
from django.db import models


class VerificationCode(models.Model):
    "Generated Model"
    code = models.CharField(
        max_length=256,
    )
    sent_to = models.OneToOneField(
        "home.Contact",
        on_delete=models.CASCADE,
        related_name="verificationcode_sent_to",
    )
    is_verified = models.CharField(
        max_length=256,
    )
    timestamp_created = models.CharField(
        max_length=256,
    )
    timestamp_verified = models.CharField(
        max_length=256,
    )


class Contact(models.Model):
    "Generated Model"
    added_by = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contact_added_by",
    )
    added_profile = models.CharField(
        max_length=256,
    )
    is_blocked = models.CharField(
        max_length=256,
    )
    is_favourite = models.CharField(
        max_length=256,
    )
    timestamp_created = models.CharField(
        max_length=256,
    )


class ThreadAction(models.Model):
    "Generated Model"
    action = models.CharField(
        max_length=256,
    )
    thread = models.OneToOneField(
        "home.ThreadAction",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="threadaction_thread",
    )
    profile = models.OneToOneField(
        "home.ThreadAction",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="threadaction_profile",
    )
    timestamp_action = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )


class Thread(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    thread_photo = models.CharField(
        max_length=256,
    )
    timestamp_created = models.DateTimeField()


class Profile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="profile_user",
    )
    mobile_number = models.IntegerField()
    pin = models.CharField(
        max_length=256,
    )
    photo = models.CharField(
        max_length=256,
    )
    status = models.CharField(
        max_length=256,
    )
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=256,
    )
    timestamp_created = models.CharField(
        max_length=256,
    )
