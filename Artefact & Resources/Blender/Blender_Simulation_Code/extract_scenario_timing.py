import bpy
import csv
import os

# === CONFIGURATION ===
# Uncomment one of the following scenario names based on the collection you want to extract timing data from:

# SCENARIO_NAME = "Scenario 3 - Side-by-Side"
# SCENARIO_NAME = "Scenario 4 - Organised Chaos"
SCENARIO_NAME = "Scenario 5 - Realistic Chaos"  # Default active option

# This will export the CSV to the same folder where your .blend file is saved
EXPORT_PATH = bpy.path.abspath("//") + f"{SCENARIO_NAME.replace(' ', '_')}_timing_data.csv"

# === GET THE SCENARIO COLLECTION ===
# Blender collections contain all objects (suitcases) used in that scenario
collection = bpy.data.collections.get(SCENARIO_NAME)
if not collection:
    raise ValueError(f"Collection '{SCENARIO_NAME}' not found.")

# === LOOP THROUGH ALL SUITCASES IN THE COLLECTION ===
suitcase_data = []

for obj in collection.objects:
    if "Suitcase" not in obj.name:
        continue  # Skip objects that are not suitcases

    # Ensure the object has animation data
    if not obj.animation_data or not obj.animation_data.action:
        continue  # Skip if not animated

    # Collect all keyframe frames for the location (movement) of the suitcase
    keyframes = []
    for fcurve in obj.animation_data.action.fcurves:
        if fcurve.data_path == "location":
            for kp in fcurve.keyframe_points:
                keyframes.append(int(kp.co.x))  # Get frame number (x axis of the keyframe point)

    if not keyframes:
        continue  # Skip objects with no movement keyframes

    # Find the first and last keyframes
    start_frame = min(keyframes)
    end_frame = max(keyframes)
    duration = end_frame - start_frame

    # Store the extracted data
    suitcase_data.append([obj.name, start_frame, end_frame, duration])

# === EXPORT THE DATA TO A CSV FILE ===
with open(EXPORT_PATH, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Suitcase Name", "Start Frame", "End Frame", "Duration"])
    for row in suitcase_data:
        writer.writerow(row)

# === OUTPUT COMPLETION MESSAGE ===
print(f"Timing data exported successfully to:\n{EXPORT_PATH}")