# START <<<

import json
import os

# Define the folder where the JSON files are stored
json_folder = "static/picker/assets"

# List of file names
json_files = ["cpu.json", "cpu-cooler.json", "case.json", "internal-hard-drive.json", 
              "memory.json", "motherboard.json", "power-supply.json", "video-card.json"]

data = {}

# Read each JSON file
for file_name in json_files:
    with open(os.path.join(json_folder, file_name), 'r') as f:
        data[file_name.split('.')[0]] = json.load(f)
        print(f"Loaded {file_name}")
# END <<<