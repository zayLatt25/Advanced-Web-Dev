# Generated by Django 5.1.4 on 2025-01-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0019_alter_case_internal_35_bays"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cpu",
            name="core_count",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
