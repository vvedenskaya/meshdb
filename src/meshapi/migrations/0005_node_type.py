# Generated by Django 4.2.10 on 2024-03-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meshapi", "0004_device_ip_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="node",
            name="type",
            field=models.CharField(
                choices=[
                    ("Standard", "Standard"),
                    ("Hub", "Hub"),
                    ("Supernode", "Supernode"),
                    ("POP", "Pop"),
                    ("AP", "Ap"),
                    ("Remote", "Remote"),
                ],
                default="Standard",
                help_text="The type of node this is, controls the icon used on the network map",
            ),
        ),
    ]
