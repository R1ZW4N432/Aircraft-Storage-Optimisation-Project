BOARDING SIMULATION (BLENDER)

🧳 Author: Rizwan Khan
📁 File: Cabin_Simulation_baked.blend
📅 Updated: 23 April 2025

------------------------------------------------------------------------

🔍 OVERVIEW
    This Blender file contains 5 animated scenarios demonstrating various aircraft boarding strategies using overhead cabin bins.

------------------------------------------------------------------------

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

------------------------------------------------------------------------

🧭 SCENARIO SWITCHER PANEL (NEW FEATURE)
    
    Location: Blender Sidebar → “Scenario Control” tab
    Script: Included as part of cameras.py and UI registration logic
    
    This panel adds an integrated way to quickly toggle between scenarios.
    
    Each button:
    
    Hides all inactive scenario collections
    Shows only the active layout
    Automatically switches to the correct camera (based on CAMERA_OBJECTS)
    Streamlines the demo experience with smooth, one-click transitions
    This feature was developed for live demos, examiner walkthroughs, and cleaner simulation control.

------------------------------------------------------------------------

📂 SCRIPT INDEX
    
    Within Blender:
        scenario_setup.py → Places cabin and suitcase models for all scenarios
        animate_scenario_1.py → Runs complex logic for Scenario 1
        animate_scenario_2.py → Runs complex logic for Scenario 2
        animate_scenario_3.py → Runs complex logic for Scenario 3
        animate_scenario_4.py → Runs complex logic for Scenario 4
        animate_scenario_5.py → Runs complex logic for Scenario 5
        extract_scenario_timing.py → Exports timing data (CSV)
      🛈     Only keep the relevant SCENARIO_NAME collection visible when exporting.
        cameras.py → Handles camera switching for scenarios and connects to the Scenario Switcher UI (NEW)
    
    Within Python Environment (Visual Studio Code):
        scenario_analysis.py
         → Compares total suitcase counts and average boarding durations across Scenarios 3, 4, and 5.
         → Outputs summary to Scenario_Comparison_Table.csv.
        scenario_completion_analysis.py
         → Calculates when each suitcase finishes boarding and checks how many complete by Frame 200.
         → Outputs earliest, average, and latest frame completion stats to Scenario_Completion_Analysis.csv.
        scenario_advanced_analysis.py
         → Performs detailed analysis per scenario: time to 50% completion, delay ranges, suitcase milestone completions, and storage rates over time.
         → Exports a full metrics table to Advanced_Scenario_Analysis.csv.
        generate_advanced_chart_mini_tables.py
         → Breaks down the advanced metrics CSV into chart-friendly tables:
          • % completion by frame threshold
          • Milestone storage frames
          • Storage progress over time
         → Exports everything into a single .csv for Google Sheets charting.

------------------------------------------------------------------------

🕹️ HOW TO USE

    Open Blender.
    Load FYP_baked.blend and switch to the “Layout” workspace.
    In the Sidebar (N key), go to the Scenario Control tab.
    Use the Scenario Switcher panel:
    Click a button (e.g. Scenario 3)
    It will:
    Show the correct scenario collection
    Hide all others
    Activate the corresponding camera for that layout
    Use the Timeline at the bottom:
    Press Spacebar or drag the scrubber
    Observe suitcase logic, delays, misplacement and retry behaviours

🧠 Markers are placed on the timeline to guide key animation events and milestones.
