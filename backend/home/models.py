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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="threadaction_thread",
    )
    profile = models.OneToOneField(
        "home.ThreadAction",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="threadaction_profile",
    )
    timestamp_action = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
