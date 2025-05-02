import bpy
import math

# === CONFIG ===
SCENARIO_NAME = "Scenario 1 - Current Only"
CABIN_HEIGHT = 1.45                  # Raised slightly above cabin base
Z_LIFT_FRAMES = 20
ROTATE_FRAMES = 10
SLIDE_IN_FRAMES = 20
DELAY_BETWEEN = 20

ROTATION_ANGLE_RAD = math.radians(90)  # Rotate suitcase 90° around X axis

# === Get the collection for Scenario 1 ===
collection = bpy.data.collections.get(SCENARIO_NAME)
if not collection:
    raise ValueError(f"Collection '{SCENARIO_NAME}' not found.")

# === Filter all suitcases in the Scenario 1 collection ===
suitcases = [obj for obj in collection.objects if "Suitcase" in obj.name]

# === Animate each suitcase ===
for index, suitcase in enumerate(sorted(suitcases, key=lambda o: o.location.x)):
    start_frame = index * DELAY_BETWEEN
    frame1 = start_frame
    frame2 = frame1 + Z_LIFT_FRAMES
    frame3 = frame2 + ROTATE_FRAMES
    frame4 = frame3 + SLIDE_IN_FRAMES

    # Step 1: Keyframe at ground position
    suitcase.keyframe_insert(data_path="location", frame=frame1)
    suitcase.keyframe_insert(data_path="rotation_euler", frame=frame1)

    # Step 2: Lift up
    suitcase.location.z = CABIN_HEIGHT
    suitcase.keyframe_insert(data_path="location", frame=frame2)

    # Step 3: Rotate flat
    suitcase.rotation_euler = (ROTATION_ANGLE_RAD, 0, 0)
    suitcase.keyframe_insert(data_path="rotation_euler", frame=frame3)

    # Step 4: Slide into cabin (backward along Y)
    suitcase.location.y += 1.05
    suitcase.keyframe_insert(data_path="location", frame=frame4)
