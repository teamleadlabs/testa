# Generated by Django 4.1.13 on 2023-12-19 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vulnerabilities", "0050_copy_qualifiers_temp_back_to_qualifiers"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="package",
            unique_together={("type", "namespace", "name", "version", "qualifiers", "subpath")},
        ),
        migrations.RemoveField(
            model_name="package",
            name="qualifiers_temp",
        ),
    ]
