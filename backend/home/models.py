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
    timestamp_action = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    profile = models.OneToOneField(
        "home.Profile",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="threadaction_profile",
    )
    thread = models.OneToOneField(
        "home.Thread",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="threadaction_thread",
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


class Thread_members(models.Model):
    "Generated Model"
    is_admin = models.CharField(
        max_length=256,
    )
    timestamp_joined = models.DateTimeField()
    timestamp_left = models.DateTimeField()
    last_rejoined = models.CharField(
        max_length=256,
    )
    profile = models.OneToOneField(
        "home.Profile",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="thread_members_profile",
    )
    thread = models.OneToOneField(
        "home.Thread",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="thread_members_thread",
    )


class Message(models.Model):
    "Generated Model"
    meaasge = models.CharField(
        max_length=256,
    )
    thread = models.OneToOneField(
        "home.Thread",
        on_delete=models.CASCADE,
        related_name="message_thread",
    )
    sent_by = models.OneToOneField(
        "home.Thread_members",
        on_delete=models.CASCADE,
        related_name="message_sent_by",
    )
    attachment = models.CharField(
        max_length=256,
    )
    is_draft = models.CharField(
        max_length=256,
    )
    is_delevered = models.CharField(
        max_length=256,
    )
    is_read = models.CharField(
        max_length=256,
    )
    timestamp_created = models.DateTimeField()
    timestamp_updated = models.DateTimeField()
    timestamp_read = models.CharField(
        max_length=256,
    )


class HomePage(models.Model):
    "Generated Model"
    body = models.CharField(
        max_length=256,
    )


class MessageAction(models.Model):
    "Generated Model"
    action = models.CharField(
        max_length=256,
    )
    message = models.OneToOneField(
        "home.Message",
        on_delete=models.CASCADE,
        related_name="messageaction_message",
    )
    profile = models.OneToOneField(
        "home.Profile",
        on_delete=models.CASCADE,
        related_name="messageaction_profile",
    )
    timestamp_action = models.DateTimeField()


class CustomerText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )


class ForwordedMessage(models.Model):
    "Generated Model"
    messege = models.OneToOneField(
        "home.Message",
        on_delete=models.CASCADE,
        related_name="forwordedmessage_messege",
    )
    forworded_by = models.OneToOneField(
        "home.Profile",
        on_delete=models.CASCADE,
        related_name="forwordedmessage_forworded_by",
    )
    forworded_to = models.OneToOneField(
        "home.Thread",
        on_delete=models.CASCADE,
        related_name="forwordedmessage_forworded_to",
    )
    timestamp_forworded = models.DateTimeField()
