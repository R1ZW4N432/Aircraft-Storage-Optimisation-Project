# 2.scenario_completion_analysis.py

import os
import pandas as pd

# === Configure input/output directories ===
BASE_DIR      = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Import")   # raw timing CSVs
EXPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Export")   # output summaries
os.makedirs(EXPORT_FOLDER, exist_ok=True)

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

# === Compute completion frame for each suitcase ===
combined["Completion_Frame"] = combined["Start Frame"] + combined["Duration"]

# === Helper to count suitcases completed by a cutoff ===
def count_by_frame(df, cutoff):
    return (df["Completion_Frame"] <= cutoff).sum()

# === Group by scenario and calculate metrics ===
summary = (
    combined
    .groupby("Scenario")
    .agg(
        Total_Suitcases      = ("Suitcase Name", "count"),
        Avg_Completion_Frame = ("Completion_Frame", "mean"),
        Earliest_Completion  = ("Completion_Frame", "min"),
        Latest_Completion    = ("Completion_Frame", "max")
    )
    .reset_index()
)

# === Add completed-by-200 metric ===
completed_by_200 = (
    combined
    .groupby("Scenario")
    .apply(lambda df: count_by_frame(df, 200))
    .reset_index(name="Completed_by_200")
)
summary = summary.merge(completed_by_200, on="Scenario")

# === Print to terminal ===
print("\n=== Completion Frame Comparison Table ===")
print(summary.to_string(index=False))

# === Save to CSV ===
completion_path = os.path.join(EXPORT_FOLDER, "Scenario_Completion_Analysis.csv")
summary.to_csv(completion_path, index=False)
print(f"\nSaved completion analysis to:\n    {completion_path}")
