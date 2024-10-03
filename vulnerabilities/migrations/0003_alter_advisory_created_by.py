# Generated by Django 4.0.2 on 2022-02-05 21:56

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("vulnerabilities", "0002_delete_importer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advisory",
            name="created_by",
            field=models.CharField(
                help_text="Fully qualified name of the importer prefixed with themodule name importing the advisory. Eg:vulnerabilities.importers.nginx.NginxImporter",
                max_length=100,
            ),
        ),
    ]
