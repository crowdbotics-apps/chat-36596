# Generated by Django 2.2.26 on 2022-08-05 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_homepage_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerText",
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
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="MessageAction",
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
                ("timestamp_action", models.DateTimeField()),
                (
                    "message",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messageaction_message",
                        to="home.Message",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messageaction_profile",
                        to="home.Profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ForwordedMessage",
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
                ("timestamp_forworded", models.DateTimeField()),
                (
                    "forworded_by",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forwordedmessage_forworded_by",
                        to="home.Profile",
                    ),
                ),
                (
                    "forworded_to",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forwordedmessage_forworded_to",
                        to="home.Thread",
                    ),
                ),
                (
                    "messege",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forwordedmessage_messege",
                        to="home.Message",
                    ),
                ),
            ],
        ),
    ]