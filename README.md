# Autocad
Assessment: PyAutoCAD Serpentine 
Geometry Automation 
Objective 
Create a Python script using PyAutoCAD that automatically generates a serpentine coil pattern 
inside AutoCAD. 
The script should draw a serpentine similar to the one shown in the reference image, following 
strict geometric parameters and proper engineering units. 
Task Details 
1. Geometry Requirements 
The candidate must generate a serpentine pattern with the following specifications: 
Parameter 
Total Height 
Tube Width 
Pitch (Center-to-Center 
Distance) 
Overall Length (Horizontal Run) 
2. Drawing Logic 
Value 
1 meter 
0.2 
meters 
0.2 
meters 
5 meters 
The serpentine pattern consists of repeated “U-shaped” loops: 
● Start at bottom-left corner. 
● Draw vertical rise of 1 meter. 
● Draw semicircle/top arc. 
● Draw vertical fall of 1 meter. 
● Shift by pitch to create next loop. 
● Continue until the total length (5m) is filled. 
The candidate must calculate: 
● Number of loops = floor( total_length / pitch ) 
● Proper arc radius = tube_width / 2 = 0.1 m 
● Geometry must stay inside an outer 5m × 1m boundary box 
Technical Requirements 
1. Use Correct Units 
● Use meters consistently throughout the script. 
● Ensure AutoCAD drawing units are handled properly (e.g., 1 unit = 1 meter). 
● No arbitrary hardcoding in pixels or arbitrary scale factors. 
2. Use PyAutoCAD Correctly 
● Connect to AutoCAD application. 
● Create a modelspace reference. 
● Draw using functions like: 
○ model.AddLine() 
○ model.AddArc() 
○ model.AddPolyline() 
3. Script Must Be Modular 
● Code should use functions such as: 
○ draw_loop(start_point) 
○ draw_serpentine(length, height, pitch, width) 
4. Code Quality Requirements 
● Clean variable names 
● No magic numbers 
● Proper comments explaining geometry 
● Reusable and readable structure 
● Error handling (e.g., if AutoCAD is not running) 
Expected Output 
The script must produce: 
● A clean serpentine coil pattern exactly 5m long and 1m tall. 
● All loops evenly spaced at 0.2m pitch. 
● Smooth top arcs with radius 0.1m. 
● Pattern that visually matches the provided reference image.
