# Generated by Django 2.2.26 on 2022-08-05 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0001_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("added_profile", models.CharField(max_length=256)),
                ("is_blocked", models.CharField(max_length=256)),
                ("is_favourite", models.CharField(max_length=256)),
                ("timestamp_created", models.CharField(max_length=256)),
                (
                    "added_by",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_added_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerificationCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=256)),
                ("is_verified", models.CharField(max_length=256)),
                ("timestamp_created", models.CharField(max_length=256)),
                ("timestamp_verified", models.CharField(max_length=256)),
                (
                    "sent_to",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verificationcode_sent_to",
                        to="home.Contact",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ThreadAction",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=256)),
                (
                    "timestamp_action",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="threadaction_profile",
                        to="home.ThreadAction",
                    ),
                ),
                (
                    "thread",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="threadaction_thread",
                        to="home.ThreadAction",
                    ),
                ),
            ],
        ),
    ]
