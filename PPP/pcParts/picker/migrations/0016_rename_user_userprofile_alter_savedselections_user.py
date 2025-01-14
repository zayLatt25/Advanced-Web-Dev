# Generated by Django 5.1.4 on 2025-01-05 01:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0015_savedselections"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="UserProfile",
        ),
        migrations.AlterField(
            model_name="savedselections",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="saved_selections",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
