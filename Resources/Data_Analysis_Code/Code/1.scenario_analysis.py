# 1.scenario_analysis.py


import os
import pandas as pd

# === Configure input/output directories ===
# BASE_DIR is one level up from this script’s directory
BASE_DIR      = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Import")   # where your raw CSVs live
EXPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Export")   # where summaries will be written
os.makedirs(EXPORT_FOLDER, exist_ok=True)               # create export folder if missing

# === Load each scenario’s timing data ===
scenario_3_path = os.path.join(IMPORT_FOLDER, "Scenario_3_-_Side-by-Side_timing_data.csv")
scenario_4_path = os.path.join(IMPORT_FOLDER, "Scenario_4_-_Organised_Chaos_timing_data.csv")
scenario_5_path = os.path.join(IMPORT_FOLDER, "Scenario_5_-_Realistic_Chaos_timing_data.csv")

scenario_3 = pd.read_csv(scenario_3_path)
scenario_4 = pd.read_csv(scenario_4_path)
scenario_5 = pd.read_csv(scenario_5_path)

# === Tag each DataFrame with its scenario name ===
scenario_3["Scenario"] = "Scenario 3"
scenario_4["Scenario"] = "Scenario 4"
scenario_5["Scenario"] = "Scenario 5"

# === Combine all scenarios into one DataFrame ===
combined = pd.concat([scenario_3, scenario_4, scenario_5], ignore_index=True)

# === Compute summary statistics per scenario ===
summary = (
    combined
    .groupby("Scenario")
    .agg(
        Suitcases     = ("Suitcase Name", "count"),    # total count
        Avg_Duration  = ("Duration", "mean"),           # mean duration
        Min_Duration  = ("Duration", "min"),            # fastest duration
        Max_Duration  = ("Duration", "max")             # slowest duration
    )
    .reset_index()
)

# === Print summary to terminal ===
print("\n=== Scenario Comparison Table ===")
print(summary.to_string(index=False))

# === Save the summary as CSV in Export folder ===
comparison_path = os.path.join(EXPORT_FOLDER, "Scenario_Comparison_Table.csv")
summary.to_csv(comparison_path, index=False)
print(f"\nSaved comparison table to:\n    {comparison_path}")
