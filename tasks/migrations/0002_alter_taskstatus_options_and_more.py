# Generated by Django 4.2.6 on 2023-10-21 08:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="taskstatus",
            options={"verbose_name": "TaskStatus", "verbose_name_plural": "TaskStatus"},
        ),
        migrations.RenameField(
            model_name="taskstatus",
            old_name="status",
            new_name="title",
        ),
    ]
