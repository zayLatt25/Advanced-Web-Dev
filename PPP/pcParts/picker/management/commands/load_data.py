# START <<<
# Created custom manage.py to load json to db
# TODO: restructure

from django.core.management.base import BaseCommand
from picker.models import Case, CpuCooler, Cpu, InternalHardDrive, Memory, Motherboard, PowerSupply, GPU
import json
import os


class Command(BaseCommand):
    help = "Load data from JSON files into the database."

    # Define the folder where the JSON files are stored
    json_path = os.path.join(os.path.dirname(__file__), "../../static/picker/assets")
    # Normalize the path to make it OS-agnostic
    json_folder = os.path.abspath(json_path)

    # A dictionary mapping file names to their respective models
    files_and_models = {
        "case.json": Case,
        "cpu-cooler.json": CpuCooler,
        "cpu.json": Cpu,
        "internal-hard-drive.json": InternalHardDrive,
        "memory.json": Memory,
        "motherboard.json": Motherboard,
        "power-supply.json": PowerSupply,
        "video-card.json": GPU,
    }

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting data loading process...")

        for file_name, model in self.files_and_models.items():
            file_path = os.path.join(self.json_folder, file_name)

            # Check if the file exists
            if not os.path.exists(file_path):
                self.stdout.write(f"File {file_name} not found in {self.json_folder}. Skipping...")
                continue

            # Load the JSON data
            with open(file_path, 'r') as f:
                data = json.load(f)

            # Load data into the database
            for item in data:
                # Handle each model's specific fields
                if model == Case:
                    model.objects.create(
                        name=item["name"],
                        price=item.get("price"),
                        type=item["type"],
                        color=item.get("color"),
                        psu=item.get("psu"),
                        side_panel=item["side_panel"],
                        external_525_bays=item["external_525_bays"],
                        internal_35_bays=item["internal_35_bays"],
                    )

                elif model == CpuCooler:
                    model.objects.create(
                        name=item["name"],
                        price=item.get("price"),
                        rpm_min=item["rpm"][0] if isinstance(item.get("rpm"), list) else item.get("rpm"),
                        rpm_max=item["rpm"][1] if isinstance(item.get("rpm"), list) and len(item["rpm"]) > 1 else None,
                        noise_level_min=item["noise_level"][0] if "noise_level" in item and isinstance(item["noise_level"], list) else None,
                        noise_level_max=item["noise_level"][1] if "noise_level" in item and isinstance(item["noise_level"], list) else None,
                        color=item.get("color"),
                        size=item.get("size"),
                    )

                elif model == Cpu:
                    model.objects.create(
                        name=item["name"],
                        price=item.get("price"),
                        core_count=item["core_count"],
                        core_clock=item["core_clock"],
                        boost_clock=item["boost_clock"],
                        tdp=item["tdp"],
                        graphics=item.get("graphics"),
                        smt=item["smt"],
                    )

                elif model == InternalHardDrive:
                    model.objects.create(
                        name=item["name"],
                        price=item.get("price"),
                        capacity=item["capacity"],
                        price_per_gb=item["price_per_gb"],
                        type=item["type"],
                        cache=item.get("cache"),
                        form_factor=item["form_factor"],
                        interface=item["interface"],
                    )

                elif model == Memory:
                    model.objects.create(
                        name=item["name"],
                        price=item.get("price"),
                        speed_min=item["speed"][0] if isinstance(item["speed"], list) else item["speed"],
                        speed_max=item["speed"][1] if isinstance(item["speed"], list) and len(item["speed"]) > 1 else None,
                        module_count=item["modules"][0],
                        module_size=item["modules"][1],
                        price_per_gb=item["price_per_gb"],
                        color=item["color"],
                        first_word_latency=item["first_word_latency"],
                        cas_latency=item["cas_latency"],
                    )

                elif model == Motherboard:
                    model.objects.create(
                        name=item["name"],
                        price=item.get("price"),
                        socket=item["socket"],
                        form_factor=item["form_factor"],
                        max_memory=item["max_memory"],
                        memory_slots=item["memory_slots"],
                        color=item.get("color"),
                    )

                elif model == PowerSupply:
                    model.objects.create(
                        name=item["name"],
                        price=item["price"],
                        type=item["type"],
                        efficiency=item["efficiency"],
                        wattage=item["wattage"],
                        modular=item["modular"],
                        color=item.get("color"),
                    )
                
                elif model == GPU:
                    model.objects.create(
                        name=item["name"],
                        price=item["price"],
                        chipset=item["chipset"],
                        memory=item["memory"],
                        core_clock=item["core_clock"],
                        boost_clock=item["boost_clock"],
                        color=item.get("color"), 
                        length=item["length"],
                    )

            self.stdout.write(f"Data for {file_name} loaded successfully.")

        self.stdout.write("Data loading process completed.")

# END <<<