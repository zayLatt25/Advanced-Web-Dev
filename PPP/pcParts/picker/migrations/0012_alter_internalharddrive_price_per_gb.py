# Generated by Django 5.1.4 on 2025-01-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0011_alter_memory_speed_max_alter_memory_speed_min"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internalharddrive",
            name="price_per_gb",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
