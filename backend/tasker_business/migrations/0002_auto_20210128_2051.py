# Generated by Django 2.2.17 on 2021-01-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasker_business", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="businessphoto",
            name="photo",
        ),
        migrations.RemoveField(
            model_name="businessphoto",
            name="tasker",
        ),
        migrations.RemoveField(
            model_name="taskeravailability",
            name="tasker",
        ),
        migrations.RemoveField(
            model_name="taskerskill",
            name="category",
        ),
        migrations.RemoveField(
            model_name="taskerskill",
            name="description",
        ),
        migrations.RemoveField(
            model_name="taskerskill",
            name="name",
        ),
        migrations.RemoveField(
            model_name="taskerskill",
            name="rate",
        ),
        migrations.RemoveField(
            model_name="taskerskill",
            name="tasker",
        ),
        migrations.RemoveField(
            model_name="timeslot",
            name="date",
        ),
        migrations.RemoveField(
            model_name="timeslot",
            name="start_time",
        ),
    ]