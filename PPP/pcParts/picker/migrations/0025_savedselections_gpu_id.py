# Generated by Django 5.1.4 on 2025-01-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0024_gpu"),
    ]

    operations = [
        migrations.AddField(
            model_name="savedselections",
            name="gpu_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]