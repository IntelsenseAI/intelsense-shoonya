# Generated by Django 3.1.14 on 2022-04-04 06:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0016_project_maximum_annotators"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="maximum_annotators",
            new_name="required_annotators_per_task",
        ),
    ]