# Generated by Django 3.1.14 on 2022-04-29 06:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dataset", "0017_auto_20220429_0542"),
    ]

    operations = [
        migrations.RenameField(
            model_name="datasetbase",
            old_name="data_id",
            new_name="id",
        ),
    ]
