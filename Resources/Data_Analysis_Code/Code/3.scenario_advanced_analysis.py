# 3. advanced_scenario_analysis.py

import os
import pandas as pd

# === Configure input/output directories ===
BASE_DIR      = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Import")   # raw timing CSVs
EXPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Export")   # output summaries
os.makedirs(EXPORT_FOLDER, exist_ok=True)

# === Load each scenario’s timing data ===
scenario_3 = pd.read_csv(os.path.join(
    IMPORT_FOLDER, "Scenario_3_-_Side-by-Side_timing_data.csv"))
scenario_4 = pd.read_csv(os.path.join(
    IMPORT_FOLDER, "Scenario_4_-_Organised_Chaos_timing_data.csv"))
scenario_5 = pd.read_csv(os.path.join(
    IMPORT_FOLDER, "Scenario_5_-_Realistic_Chaos_timing_data.csv"))

# === Tag each DataFrame with its scenario name ===
scenario_3["Scenario"] = "Scenario 3"
scenario_4["Scenario"] = "Scenario 4"
scenario_5["Scenario"] = "Scenario 5"

# === Combine all scenarios into one DataFrame ===
combined = pd.concat([scenario_3, scenario_4, scenario_5], ignore_index=True)

# === Compute completion frame for each suitcase ===
combined["Completion_Frame"] = combined["Start Frame"] + combined["Duration"]

# === Function to compute advanced metrics for a single scenario ===
def calculate_metrics(df):
    df_sorted = df.sort_values("Completion_Frame").reset_index(drop=True)
    total = len(df_sorted)

    # Time to 50% completion
    halfway_idx = int(total / 2)
    time_to_half = df_sorted.loc[halfway_idx, "Completion_Frame"]

    # Delay range (max - min)
    delay_range = df_sorted["Completion_Frame"].max() - df_sorted["Completion_Frame"].min()

    # Final delay vs average
    final_delay = df_sorted["Completion_Frame"].max() - df_sorted["Completion_Frame"].mean()

    # Milestone frames every 3 suitcases
    milestone_frames = {
        f"Frame_Suitcase_{i}": df_sorted.loc[i - 1, "Completion_Frame"]
        for i in range(3, total + 1, 3)
    }

    # Percent under key frames
    pct_200 = (df_sorted["Completion_Frame"] <= 200).sum() / total
    pct_300 = (df_sorted["Completion_Frame"] <= 300).sum() / total
    pct_400 = (df_sorted["Completion_Frame"] <= 400).sum() / total

    # Storage counts in 50-frame bins up to 700
    bins = list(range(0, 701, 50))
    rate_series = pd.cut(df_sorted["Completion_Frame"], bins=bins).value_counts().sort_index()
    storage_rate = {
        f"Stored_0to{bins[i+1]}": int(rate_series.iloc[i])
        for i in range(len(rate_series))
    }

    return {
        "Time_to_50pct": time_to_half,
        "Delay_Range": delay_range,
        "Final_Delay_vs_Avg": final_delay,
        "%_By_Frame_200": pct_200,
        "%_By_Frame_300": pct_300,
        "%_By_Frame_400": pct_400,
        **milestone_frames,
        **storage_rate
    }

# === Compute metrics for each scenario and assemble DataFrame ===
results = []
for scenario_name in combined["Scenario"].unique():
    df_scen = combined[combined["Scenario"] == scenario_name]
    metrics = calculate_metrics(df_scen)
    metrics["Scenario"] = scenario_name
    results.append(metrics)

advanced_df = pd.DataFrame(results)

# === Reorder columns to put 'Scenario' first ===
cols = ["Scenario"] + [c for c in advanced_df.columns if c != "Scenario"]
advanced_df = advanced_df[cols]

# === Save the advanced analysis CSV ===
advanced_path = os.path.join(EXPORT_FOLDER, "Advanced_Scenario_Analysis.csv")
advanced_df.to_csv(advanced_path, index=False)
print(f"Advanced scenario metrics saved to:\n    {advanced_path}")
