import bpy
import math

# === CONFIG ===
CURRENT_CABIN_GAP = 0.0
OPTIMISED_CABIN_GAP = 0.0

CURRENT_SUITCASE_GAP = 0.0
OPTIMISED_SUITCASE_GAP = -0.2

CURRENT_SUITCASE_OFFSET = 0.23
OPTIMISED_SUITCASE_OFFSET = 0.22

SUITCASE_Z = 0.0
CABIN_Z = 1.3
SUITCASE_Y_OFFSET = -0.8

CABIN_SOURCE_NAMES = {
    "Current": "CurrentCabin",
    "Optimised": "OptimisedCabin"
}

# === SCENARIOS ===
SCENARIOS = {
    "Scenario 1 - Current Only": {
        "cabin_type": "Current",
        "cabin_length": 1.45,
        "cabin_gap": CURRENT_CABIN_GAP,
        "suitcase_count": 3,
        "suitcase_gap": CURRENT_SUITCASE_GAP,
        "suitcase_offset": CURRENT_SUITCASE_OFFSET,
        "suitcase_rotation_deg": 0,
        "y_offset": 0.0,
    },
    "Scenario 2 - Optimised Only": {
        "cabin_type": "Optimised",
        "cabin_length": 1.10,
        "cabin_gap": OPTIMISED_CABIN_GAP,
        "suitcase_count": 4,
        "suitcase_gap": OPTIMISED_SUITCASE_GAP,
        "suitcase_offset": OPTIMISED_SUITCASE_OFFSET,
        "suitcase_rotation_deg": 90,
        "y_offset": 5.0,
    },
    "Scenario 3 - Side-by-Side": {
        "combined": True,
        "y_offset": 10.0,
    },
    "Scenario 4 - Random Layout": {
        "combined": True,
        "y_offset": 15.0,
    }
}

def duplicate_object(obj, new_name):
    new_obj = obj.copy()
    new_obj.data = obj.data.copy()
    new_obj.name = new_name
    return new_obj

def create_scenario_collection(name):
    if name in bpy.data.collections:
        bpy.data.collections.remove(bpy.data.collections[name])
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection

def place_cabins_and_suitcases(cfg, cabin_type, x_offset, collection):
    base_cabin = bpy.data.objects.get(CABIN_SOURCE_NAMES[cabin_type])
    base_suitcase = bpy.data.objects.get("Suitcase")
    if not base_cabin or not base_suitcase:
        print(f"Missing model(s): {cabin_type} or Suitcase")
        return

    suitcase_length = 0.45
    cabin_length = cfg["cabin_length"]
    cabin_gap = cfg["cabin_gap"]
    suitcase_gap = cfg["suitcase_gap"]
    suitcase_offset = cfg.get("suitcase_offset", 0.0)
    suitcase_rotation_deg = cfg.get("suitcase_rotation_deg", 0)
    count = cfg["suitcase_count"]
    y = cfg["y_offset"]

    for i in range(3):
        cabin_x = x_offset + i * (cabin_length + cabin_gap)

        cabin = duplicate_object(base_cabin, f"{cabin_type}Cabin_{i+1}")
        cabin.location = (cabin_x, y, CABIN_Z)
        collection.objects.link(cabin)

        group_width = count * suitcase_length + (count - 1) * suitcase_gap
        group_start = cabin_x - group_width / 2

        for j in range(count):
            sx = group_start + j * (suitcase_length + suitcase_gap)
            sx += suitcase_offset

            suitcase = duplicate_object(base_suitcase, f"{cabin_type}Suitcase_{i+1}_{j+1}")
            suitcase.location = (sx, y + SUITCASE_Y_OFFSET, SUITCASE_Z)
            suitcase.rotation_euler = (0, 0, math.radians(suitcase_rotation_deg))
            collection.objects.link(suitcase)

def setup_scenario(name, cfg):
    collection = create_scenario_collection(name)

    if cfg.get("combined"):
        current_cfg = {
            "cabin_length": 1.45,
            "cabin_gap": CURRENT_CABIN_GAP,
            "suitcase_count": 3,
            "suitcase_gap": CURRENT_SUITCASE_GAP,
            "suitcase_offset": CURRENT_SUITCASE_OFFSET,
            "suitcase_rotation_deg": 0,
            "y_offset": cfg["y_offset"],
        }
        optimised_cfg = {
            "cabin_length": 1.10,
            "cabin_gap": OPTIMISED_CABIN_GAP,
            "suitcase_count": 4,
            "suitcase_gap": OPTIMISED_SUITCASE_GAP,
            "suitcase_offset": OPTIMISED_SUITCASE_OFFSET,
            "suitcase_rotation_deg": 90,
            "y_offset": cfg["y_offset"],
        }

        # Place current cabins on the left
        place_cabins_and_suitcases(current_cfg, "Current", x_offset=0.0, collection=collection)
        # Place optimised cabins offset to the right
        place_cabins_and_suitcases(optimised_cfg, "Optimised", x_offset=6.0, collection=collection)

    else:
        setup_scenario_standard(cfg["cabin_type"], cfg, collection)

def setup_scenario_standard(cabin_type, cfg, collection):
    place_cabins_and_suitcases(cfg, cabin_type, x_offset=0.0, collection=collection)

# === RUN ===
for scenario, cfg in SCENARIOS.items():
    setup_scenario(scenario, cfg)
