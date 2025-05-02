# 4.generate_chart_mini_tables.py

import os
import pandas as pd

# === Configure input/output directories ===
BASE_DIR      = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXPORT_FOLDER = os.path.join(BASE_DIR, "CSVs_Export")   # where the advanced CSV lives and where we'll write the mini-tables
os.makedirs(EXPORT_FOLDER, exist_ok=True)

# === Load the advanced scenario analysis CSV ===
input_file = os.path.join(EXPORT_FOLDER, "Advanced_Scenario_Analysis.csv")
df = pd.read_csv(input_file)

# === Chart 2: % Complete by Frame Threshold (LONG format) ===
frame_thresholds = [200, 300, 400]
chart2_rows = []
for _, row in df.iterrows():
    for t in frame_thresholds:
        chart2_rows.append({
            "Scenario": row["Scenario"],
            "Frame Threshold": t,
            "% Complete": row[f"%_By_Frame_{t}"]
        })
chart2_df_long = pd.DataFrame(chart2_rows)

# === Chart 2: Wide Format (for plotting) ===
chart2_wide_data = {"Frame Threshold": frame_thresholds}
for scen in df["Scenario"].unique():
    chart2_wide_data[scen] = [
        df.loc[df["Scenario"] == scen, f"%_By_Frame_{t}"].values[0]
        for t in frame_thresholds
    ]
chart2_df_wide = pd.DataFrame(chart2_wide_data)

# === Chart 3: Milestone Completion Frames ===
milestones = [3, 6, 9, 12, 15, 18, 21]
milestone_data = {"Suitcase Milestone": milestones}
for _, row in df.iterrows():
    milestone_data[row["Scenario"]] = [
        row[f"Frame_Suitcase_{m}"] for m in milestones
    ]
chart3_df = pd.DataFrame(milestone_data)

# === Chart 4: Cumulative Storage Progress (counts by 50-frame intervals) ===
storage_cols = sorted(
    [c for c in df.columns if c.startswith("Stored_0to")],
    key=lambda c: int(c.split("0to")[-1])
)
frame_values = [int(c.split("0to")[-1]) for c in storage_cols]
chart6_data = {"Frame": frame_values}
for _, row in df.iterrows():
    chart6_data[row["Scenario"]] = [row[c] for c in storage_cols]
chart6_df = pd.DataFrame(chart6_data)

# === Write all mini-tables to CSV ===
output_path = os.path.join(EXPORT_FOLDER, "Advanced_Chart_Mini_Tables.csv")
with open(output_path, "w") as f:
    f.write("Table for Chart 2: % Complete by Frame Threshold (Long Format)\n")
    chart2_df_long.to_csv(f, index=False)
    f.write("\nTable for Chart 2: % Complete by Frame Threshold (Wide Format)\n")
    chart2_df_wide.to_csv(f, index=False)
    f.write("\nTable for Chart 3: Milestone Completion Frames\n")
    chart3_df.to_csv(f, index=False)
    f.write("\nTable for Chart 4: Cumulative Storage Progress\n")
    chart6_df.to_csv(f, index=False)

print(f"Extended mini-tables saved to: {output_path}")
