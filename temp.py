import os 
import json 
import re
import pathlib
import math
from random import random

def process_json_file(file_path):
    # Step 1: Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    new_geo_objects = {}  # Store new geo objects here

    for key, item in list(data.items()):  # Convert to list to safely iterate
        if "_:point" in key and "geo" in item:
            # Generate new geo ID with a random number
            new_geo_id = f"{key}_geo" + str(math.floor(random() * 1000))
            
            # Prepare the new geo object
            new_geo_objects[new_geo_id] = item["geo"]
            new_geo_objects[new_geo_id]["label"] = new_geo_id
            
            # Replace original geo object with reference
            data[key]["geo"] = {"@id": new_geo_id}
            
            # Optionally, add a label to the point if not present
            if "label" not in data[key]:
                data[key]["label"] = "Point_" + str(math.floor(random() * 1000))

    # Update the original dictionary with new geo objects
    data.update(new_geo_objects)
    
    # Step 4: Write the modified data back
    new_file = file_path.replace(".json", "_processed.json")
    with open(new_file, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
current_folder = pathlib.Path(__file__).parent.absolute()
process_json_file(os.path.join(current_folder, "extra_metadata.json"))