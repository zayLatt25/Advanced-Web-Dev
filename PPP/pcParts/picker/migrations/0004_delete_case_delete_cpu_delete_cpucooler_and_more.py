# Generated by Django 5.1.4 on 2025-01-04 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0003_case_cpu_cpucooler_internalharddrive_memory_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Case",
        ),
        migrations.DeleteModel(
            name="Cpu",
        ),
        migrations.DeleteModel(
            name="CpuCooler",
        ),
        migrations.DeleteModel(
            name="InternalHardDrive",
        ),
        migrations.DeleteModel(
            name="Memory",
        ),
        migrations.DeleteModel(
            name="Motherboard",
        ),
        migrations.DeleteModel(
            name="PowerSupply",
        ),
    ]
