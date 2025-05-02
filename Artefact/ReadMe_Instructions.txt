FINAL YEAR PROJECT – BOARDING SIMULATION (BLENDER)

🧳 Author: Rizwan Khan
📁 File: FYP_baked.blend
📅 Updated: 23 April 2025

---

🔍 OVERVIEW
This Blender file contains 5 animated scenarios demonstrating various aircraft boarding strategies using overhead cabin bins.

---

🎬 SCENARIO INDEX (Arranged on the Y-Axis)

Scenario 1 – Current Only
▶ Location: Y = 0
▶ Layout: 3 suitcases per bin (CurrentCabin)
▶ Notes: Sequential boarding with uniform timing

Scenario 2 – Optimised Only
▶ Location: Y = 5
▶ Layout: 4 suitcases per bin (OptimisedCabin)
▶ Notes: Side-entry boarding with tighter layout

Scenario 3 – Side-by-Side
▶ Location: Y = 10
▶ Layout: Left: Current, Right: Optimised
▶ Notes: Simultaneous boarding for side-by-sde visual comparison

Scenario 4 – Organised Chaos
▶ Location: Y = 15
▶ Notes: Random boarding, staggered entry without misplacement

Scenario 5 – Realistic Chaos 
- (Misplacement + Conflict Logic)
▶ Location: Y = 21
▶ Notes:
    - Includes misplacement and rerouting (2_2 suitcase logic)
    - Suitcases delayed if bins are in use
    - Most realistic simulation scenario

--- 

🕹️ HOW TO USE

1. Open Blender.
2. Switch to the “Layout” workspace.
3. Use Timeline controls to preview animation.
4. Press Play (spacebar) or drag scrubber to observe:
   - Suitcase movement logic
   - Conflict resolution in Scenario 5
   - Delays between animations

🧠 TIP: Markers are placed on the timeline to guide important events.

---

📂 SCRIPT INDEX
Within Blender:
- scenario_setup.py → Places cabin and suitcase models for all scenarios
- animate_scenario_1.py → Runs complex logic for Scenario 1
- animate_scenario_2.py → Runs complex logic for Scenario 2
- animate_scenario_3.py → Runs complex logic for Scenario 3
- animate_scenario_4.py → Runs complex logic for Scenario 4
- animate_scenario_5.py → Runs complex logic for Scenario 5
- extract_scenario_timing.py → Exports timing data (CSV)
    - Ensure the correct ** SCENARIO_NAME ** collection is visible/uncommented to get the respective CSV.

Within Python Environment (Visual Studio Code)
- 1. scenario_analysis.py
    → Compares total suitcase counts and average boarding durations across Scenarios 3, 4, and 5. Outputs a clean summary table (Scenario_Comparison_Table.csv) for presentation or Google Sheets visualisation.

- 2. scenario_completion_analysis.py
    → Calculates when each suitcase finishes boarding and checks how many complete by Frame 200. Outputs earliest, average, and latest completion frames for each scenario (Scenario_Completion_Analysis.csv).

- 3. scenario_advanced_analysis.py
    → Performs detailed analysis per scenario: time to 50% completion, delay ranges, suitcase milestone completions, and storage rates over time. Exports this to a full metrics table (Advanced_Scenario_Analysis.csv).

- 4. generate_advanced_chart_mini_tables.py
    → Breaks down the advanced metrics CSV into smaller, chart-friendly tables. These include % completion by frame threshold, milestone storage frames, and storage progress across time intervals. Exports all to a single .csv for charting.

---

