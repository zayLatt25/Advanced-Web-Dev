# Generated by Django 5.1.4 on 2025-01-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0013_alter_internalharddrive_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="powersupply",
            name="efficiency",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]