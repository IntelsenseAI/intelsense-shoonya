# Generated by Django 3.1.14 on 2022-03-28 06:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("workspaces", "0006_merge_20220328_0340"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workspace",
            name="manager",
        ),
        migrations.AddField(
            model_name="workspace",
            name="managers",
            field=models.ManyToManyField(
                related_name="workspace_managers",
                to=settings.AUTH_USER_MODEL,
                verbose_name="managers",
            ),
        ),
    ]
