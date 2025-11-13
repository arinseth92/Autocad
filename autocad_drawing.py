"""
AutoCAD Serpentine Coil Pattern Generator - FINAL VERSION
This is the complete, working version with all fixes applied.

Specifications:
- Total width: 1 meter (horizontal)
- Total height: 5 meters (vertical)
- Tube width: 0.2 meters
- Pitch: 0.2 meters
- Arc radius: 0.1 meters
- Pattern: Vertical serpentine coil (1m × 5m)
"""

import win32com.client
import math
import sys

def connect_to_autocad():
    """Connect to AutoCAD and return acad, doc, mspace objects"""
    print("Connecting to AutoCAD...", flush=True)
    
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        print("✓ Connected to AutoCAD", flush=True)
    except:
        acad = win32com.client.Dispatch("AutoCAD.Application")
        print("✓ Created new AutoCAD instance", flush=True)
    
    acad.Visible = True
    
    try:
        doc = acad.ActiveDocument
    except:
        doc = acad.Documents.Add()
        print("✓ Created new document", flush=True)
    
    mspace = doc.ModelSpace
    return acad, doc, mspace


def to_variant(x, y, z):
    """Convert coordinates to AutoCAD variant format"""
    import win32com.client
    return win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, [x, y, z])


def draw_loop(model, start_y, loop_num, width, pitch, arc_radius, direction_right):
    """Draw a single horizontal loop with semicircular arc"""
    
    if direction_right:
        # Draw line from left to right
        p1 = to_variant(0, start_y, 0)
        p2 = to_variant(width, start_y, 0)
        model.AddLine(p1, p2)
        
        # Draw arc at right side (bottom to top)
        center = to_variant(width, start_y + arc_radius, 0)
        model.AddArc(center, arc_radius, -math.pi / 2, math.pi / 2)
        
        next_x = width
        next_y = start_y + pitch
    else:
        # Draw line from right to left
        p1 = to_variant(width, start_y, 0)
        p2 = to_variant(0, start_y, 0)
        model.AddLine(p1, p2)
        
        # Draw arc at left side (top to bottom)
        center = to_variant(0, start_y + arc_radius, 0)
        model.AddArc(center, arc_radius, math.pi / 2, 3 * math.pi / 2)
        
        next_x = 0
        next_y = start_y + pitch
    
    if loop_num % 5 == 0:  # Print progress every 5 loops
        print(f"  Completed {loop_num} loops...", flush=True)
    
    return next_x, next_y


def main():
    """Main function"""
    
    # Parameters (in meters)
    WIDTH = 1.0
    HEIGHT = 5.0
    TUBE_WIDTH = 0.2
    PITCH = 0.2
    
    print("\n" + "="*60, flush=True)
    print("  AUTOCAD SERPENTINE COIL GENERATOR", flush=True)
    print("="*60, flush=True)
    print(f"\nParameters:", flush=True)
    print(f"  Width: {WIDTH}m", flush=True)
    print(f"  Height: {HEIGHT}m", flush=True)
    print(f"  Pitch: {PITCH}m", flush=True)
    print(f"  Tube Width: {TUBE_WIDTH}m\n", flush=True)
    
    try:
        # Connect to AutoCAD
        acad, doc, mspace = connect_to_autocad()
        
        # Calculate parameters
        arc_radius = TUBE_WIDTH / 2.0
        num_loops = int(HEIGHT / PITCH)
        
        print(f"\nDrawing {num_loops} loops...\n", flush=True)
        
        # Draw all loops
        current_x = 0
        current_y = 0
        
        for i in range(num_loops):
            direction_right = (i % 2 == 0)
            current_x, current_y = draw_loop(
                mspace, current_y, i + 1, WIDTH, PITCH, arc_radius, direction_right
            )
        
        # Draw boundary rectangle
        print("\nAdding boundary rectangle...", flush=True)
        mspace.AddLine(to_variant(0, 0, 0), to_variant(WIDTH, 0, 0))
        mspace.AddLine(to_variant(WIDTH, 0, 0), to_variant(WIDTH, HEIGHT, 0))
        mspace.AddLine(to_variant(WIDTH, HEIGHT, 0), to_variant(0, HEIGHT, 0))
        mspace.AddLine(to_variant(0, HEIGHT, 0), to_variant(0, 0, 0))
        
        # Zoom to fit
        print("Zooming to fit...", flush=True)
        try:
            acad.ZoomExtents()
        except:
            acad.ZoomAll()
        
        print("\n" + "="*60, flush=True)
        print("  ✓ SUCCESS! Drawing completed!", flush=True)
        print("="*60, flush=True)
        print(f"\n  Loops drawn: {num_loops}", flush=True)
        print(f"  Size: {WIDTH}m × {HEIGHT}m", flush=True)
        print(f"\n  Check AutoCAD to see the vertical serpentine pattern!", flush=True)
        print("\n" + "="*60 + "\n", flush=True)
        
    except Exception as e:
        print("\n" + "="*60, flush=True)
        print("  ✗ ERROR", flush=True)
        print("="*60, flush=True)
        print(f"\n  {e}\n", flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if _name_ == "_main_":
    main()
