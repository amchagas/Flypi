/////////////////////////////////////////////////////////////////////////////////
/// FlyPi v0.97; 2015 05 27 ///
/// Collaboration Tom Baden, Lucia Prieto Godino and Andre Maia Chagas
/// 3D model by Tom Baden (thingyverse ID: tbaden) ///
/// thomas.baden@uni-tuebingen.de ///
/// tombaden.wordpress.com ///
/// Modified FlyPi_v29 by Ian Cavén 2017-10-24 for selectable assembly layout and other improvements 
/////////////////////////////////////////////////////////////////////////////////
//// SWITCHES //////////
PartA = 	1; // Base
PartA1 =	1; // Base clamps
PartA2 = 	1; // Feet
PartB =     1; // Wall
PartB3 =	1; // PCB mount

// Only the next two lines need to be set to control whether and which of the camera mounts are shown
show_camera_mount = 1;  
use_servo_focus = false;     // Set to true for PartC1 otherwise false for PartC
PartC = 	show_camera_mount && !use_servo_focus ? 1 : 0; // Cam Mount
PartC1 = 	show_camera_mount && use_servo_focus ? 1 : 0; // Cam Mount Servo - only use PartC or PartC1

PartC2_1 = 	1; // Cam Mount Cogwheel 1 - will only be made if use_servo_focus is true
PartC2_2 = 	1; // Cam Mount Cogwheel 2 - will only be made if use_servo_focus is true
PartD = 	1; // High Power LED mount
PartE =     1; // angled mounting stick
PartF1 = 	1; // straight mounting stick, long
PartF2 = 	1; // straight mounting stick, short
PartF3 = 	1; // straight mounting stick, long 90°
PartG = 	1; // thumbscrew & manipulator links
PartH = 	1; // AdaFruit 8x8 LED Matrix mount
PartI = 	1; // Adafruit 12 LED Ring mount
PartJ1 = 	1; // Mini Petri dish mount
PartJ2 = 	1; // Midi Petri dish mount
PartK = 	1; // Diffusor mount
PartL1 = 	1; // microscope slide chamber small
PartL2= 	1; // microscope slide chamber big
PartM = 	1; // Fluorescence Excitation light mount
PartN = 	1; // Fluorescence Exitaton tube plug
PartO = 	1; // Fluorescence Emission mount and wheel

/////////////////////////////////////////////////////////////////////////////////
///// KEY VARIABLES ////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

// Set the assembly_location variable to one of the following two values to move the parts 
// to their location in the exploded view or their location when printing all parts
EXPLODED_VIEW = 0;
PRINTABLE_LAYOUT = 1;
assembly_location = EXPLODED_VIEW;
max_print_bounds = [285, 150, 155];  // X, Y, Z: the maximum bounding box supported by the printer
printing_batch_number = 2;  // Either 0, 1 or 2
connect_parts = (assembly_location == PRINTABLE_LAYOUT);   // Connect parts with bridges when printing a batch as a single part

// Make a layout guide for the maximum print bounding box
CHECKING_LAYOUT = false;
if (CHECKING_LAYOUT && assembly_location == PRINTABLE_LAYOUT)
{
    difference() {
        cube([max_print_bounds[0]+1, max_print_bounds[1]+1, 1], center=true); 
        cube([max_print_bounds[0], max_print_bounds[1], 1], center=true);
    }
}

sep = 30; // How far apart do pieces "float" in the model
MINIMUM_PRINT_LAYOUT_SEPARATION = 5;       // Minimum distance between parts for the print layout
MINIMUM_WIRE_SIZE = 2;  // Depends on the printer and the material
Walls = 5; // Global thickness of all walls
Tol = 0.2; // Global gap between all parts that need to slide
corner_radius = 4; // Round corner radius

// Base and mainwall details
T_cableZ = 4; // Module A, height of thermistor cable slid
T_cableY = 12; // Module A,width of thermistor cable slid
T_cable_offset = 8; // Module A, lateral displacement of thermistor cable slid
MarkerLED_R = 3+Tol; // Module A, radius of RGB LED hole in base
MarkerLED_Z = 2; // Module A, depth beneath surface
MarkerLED_XY = 4; // Module A, viewhole size
Sidestand = 70; // Module A, extension in X dimension at the back of the base
Sidestand_thickness = Walls; // Module A, thickness of extension at back of base
Borders = 15; // Module B, thickness of borders on the back (saves plastic)
Walls_thinning = 4; // Module B, how much thinner than "Walls" is thin part (saves plastic)

//Peltier dimensions
P_XY = 40+1; // Size of the Peltier
P_Z = 3; // Thickness of the Peltier
P_border = 12; // Extension in X dimension of base next to Peltier
P_ridge = 2; // below Peltier, width of ridge
P_cable = 3; // thickness of Peltier cable slid

//Raspberry Pi type (mounting parameters)
RPi_Width = 56+Walls*2; // Dimensions of the RPi 2 (below also for RPi 2)
RPi_groundZ = 17; // 65; for RPi B (not RPi B+)
RPi_holedist_Y = 49/2; // 15.5; // for RPi B (not RPi B+)
RPi_holedist_Yb = 49/2; //-10; // for RPi B (not RPi B+)
RPi_holedist_Z = 58; //54.5; // for RPi B (not RPi B+)
Tube_wall = 1.5;
S_hole_R = 1.5;
S_mount_R = 4;
Mount_h = 19; // RPi2 mount

// RPi Camera Type
Cam_X = 32.2;//24 for "classic RPi Cam. i.e the one without the adjustable focus lens";
Cam_Y = 32.2;//25 for "classic RPi Cam";
Cam_X_offset = 0;// 2.5 for "classic RPi Cam";
C_Z = 2; // thickness of camera mount
C_Z2 = 5; // thickness of camera mount walls
C_ridge = 2; // width of ridge for camera mount
Cam_Zfloat = 200; // Module B, max height 
CamGroove_X = 12;
CamGroove_Y = 16.1;
CamGroove2_Y = 24;

OPTICAL_AXIS_OFFSET_X = Cam_X/2+P_border-Walls;
PELTIER_AXIS_OFFSET_X = P_XY/2+P_border-Walls;

// Default number of faces 
$fn=100;

/////////////////////////////////////////////////////////////////////////////////
/// Utility function to create a arched wire bridge between two points to be 
/// for printing mutliple parts in a single assembly
/////////////////////////////////////////////////////////////////////////////////
module arch_bridge(bridge_radius, arch_scale=1)
{
    min_wire_width = MINIMUM_WIRE_SIZE; // This value is dependent on the printer and the material used
    scale([1, 1, arch_scale])
    rotate([0, -90, 0])
    intersection() 
    {
        linear_extrude(height = min_wire_width) {
            difference() {
               circle(r=bridge_radius);
               circle(r=bridge_radius-min_wire_width /2);
             }
         }
         translate([bridge_radius, 0, min_wire_width]) cube([bridge_radius*2, bridge_radius*2, min_wire_width*2], center=true);
     }
 }
 
/////////////////////////////////////////////////////////////////////////////////
/// MODULE A - base   //////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

A_Base_X = (PELTIER_AXIS_OFFSET_X + Walls)*2 + Sidestand;
A_Base_Y = RPi_Width;
A_Base_Z = 19;
A_Wall_X = Walls;
A_Wall_Y = A_Base_Y;
A_Wall_Y_long = 10;
A_Wall_Z = RPi_groundZ+RPi_holedist_Z+25;
A_Wall_Z_long = Cam_Zfloat+Walls;
A_extramount_Z = 100;
Stabiliser_R = 12;
Airhole_R = 6;
Airhole_spacing = 13;
Airhole_center_Z = -A_Base_Z/2-P_Z/2;  // The height at which the airhole is centered w.r.t. the inside thickness
A1_screw_R = 1.5;
A1_offset = 3;
PartA_batch = 0;    // The printing batch that PartA belongs to
PartA_locations = [[0,0,0], [0, A_Base_X/4, A_Base_Z]];
PartA_rotations = [[0,0,0], [0, 0, 90]];

module A(){
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Base_Z/2]){cube([A_Base_X,A_Base_Y,A_Base_Z], center = true );} // BASE
	translate([-P_XY/2-P_border-Walls/2,A_Base_Y/2-Walls+Tol/2,0]){rotate ([90,0,0]) {cylinder($fn = 50, r = Stabiliser_R, h = Walls*2-Tol, center = true );}} // Support1	
	translate([-P_XY/2-P_border-Walls/2,-A_Base_Y/2+Walls-Tol/2,0]){rotate ([90,0,0]) {cylinder($fn = 50, r = Stabiliser_R, h = Walls*2-Tol, center = true );}} // Support2	
}
module A_sub(){
	translate([0,0,-P_Z/2]){cube([P_XY+2*Tol,P_XY+2*Tol,P_Z], center = true );} // Peltier groove
	translate([-A_Base_Y/4,(P_XY+2*Tol)/2-(P_cable+2*Tol)/2,-P_Z/2]){cube([A_Base_Y,P_cable+2*Tol,P_Z], center = true );} // Peltier cable1
	translate([-A_Base_Y/4,-(P_XY+2*Tol)/2+(P_cable+2*Tol)/2,-P_Z/2]){cube([A_Base_Y,P_cable+2*Tol,P_Z], center = true );} // Peltier cable2
	translate([-A_Base_Y/2,0,-MarkerLED_R-MarkerLED_Z]){rotate ([0,90,0]) {cylinder($fn = 50, r = MarkerLED_R, h = A_Base_Y, center = true );}} // MarkerLed HOLE
	translate([-P_XY/2-MarkerLED_XY,0,-MarkerLED_Z]){cube([MarkerLED_XY,MarkerLED_XY,2*MarkerLED_Z], center = true );} // MarkerLed opening
	translate([0,0,-A_Base_Z/2]){cube([P_XY-P_ridge*2,P_XY-P_ridge*2,A_Base_Z], center = true );} // Peltier below
	translate([-A_Base_X/2-Walls,0,-A_Base_Z/2]){cube([Sidestand-Walls*3,A_Base_Y-Walls*2,A_Base_Z], center = true );} // Sidestand Hole
	translate([-A_Base_X/2-Walls/2-Walls,0,-A_Base_Z/2+Sidestand_thickness]){cube([Sidestand-Walls*2,A_Base_Y,A_Base_Z], center = true );} // Sidestand Hole shallow
	translate([-P_XY/2-P_border-Walls/2,0,-A_Base_Z/2]){cube([Walls+Tol*2,A_Base_Y-Walls*4,A_Base_Z], center = true );} // Wall_linkhole
	translate([-P_XY/2-P_border-A_Wall_X/2,0,A_Wall_Z/2]){cube([A_Wall_X+Tol*2,A_Wall_Y,A_Wall_Z], center = true );} // Sidestand_slot
	translate([Airhole_spacing,0,Airhole_center_Z]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([0,0,Airhole_center_Z]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([-Airhole_spacing,0,Airhole_center_Z]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([+A_Base_Y/2,0,Airhole_center_Z]){rotate ([0,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([0,-Airhole_spacing,Airhole_center_Z]){rotate ([0,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([0,Airhole_spacing,Airhole_center_Z]){rotate ([0,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([-(P_XY/2-A1_offset),P_XY/2+A1_offset,-Walls]){rotate ([0,0,0]) {cylinder($fn=20, r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
	translate([-(P_XY/2-A1_offset),-(P_XY/2+A1_offset),-Walls]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
	translate([(P_XY/2-A1_offset),P_XY/2+A1_offset,-Walls]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
	translate([(P_XY/2-A1_offset),-(P_XY/2+A1_offset),-Walls]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
}
show_PartA = PartA==1 && (printing_batch_number == PartA_batch || assembly_location == EXPLODED_VIEW);
if (show_PartA) {translate(PartA_locations[assembly_location]) rotate(PartA_rotations[assembly_location]) difference(){A();A_sub();}}

/////////////////////////////////////////////////////////////////////////////////
//// MODULE A1 - thermistor /Peltier clamps /////
/////////////////////////////////////////////////////////////////////////////////

module clamp()
{
    difference()
    {
        union(){
            cube([A1_offset*2,A1_offset*5,Walls/3], center = true );
            translate([0,A1_offset*2,-Walls/3]){cube([A1_offset*2,A1_offset,Walls/3], center = true );} // clamp
        }
        cylinder($fn=20,r = A1_screw_R, h = Walls/2, center = true ); // screwhole
    }
   
}

// The thermistor clamp has a larger foot
module thermistor_clamp()
{
    difference()
    {
        union(){
            translate([0, -3*A1_offset/4, 0]) cube([A1_offset*2,A1_offset*6.5,Walls/3], center = true );
            translate([0,A1_offset*2, 7-Walls*2]){cube([A1_offset*2,A1_offset,5], center = true );} // clamp
        }
        cylinder($fn=20,r = A1_screw_R, h = Walls/2, center = true ); // screwhole
    }
   
}

clamp1_locations = [[P_XY/2-A1_offset,P_XY/2+A1_offset,Walls*2], [-A_Base_X+10,PartA_locations[1][1]+P_XY/2-A1_offset-Walls,Walls/6]];
clamp2_locations = [[-(P_XY/2-A1_offset),P_XY/2+A1_offset,Walls*2], [-A_Base_X+10,PartA_locations[1][1]+P_XY/2-2*(A1_offset+Walls),Walls/6]];
clamp3_locations = [[-(P_XY/2-A1_offset),-(P_XY/2+A1_offset),Walls*2], [-A_Base_X+10,PartA_locations[1][1]+P_XY/2-3*(A1_offset+Walls),Walls/6]];
clamp4_locations = [[P_XY/2-A1_offset,-(P_XY/2+A1_offset),Walls*2], [-A_Base_X+10,PartA_locations[1][1]+P_XY/2-4*(A1_offset+Walls),Walls/6]];

clamp1_rotations = [[0,0,0], [0,180,90]];
clamp2_rotations = [[0,0,0], [0,180,90]];
clamp3_rotations = [[0,0,180], [0,180,90]];
clamp4_rotations = [[0,0,180], [0,180,90]];

show_PartA1 = PartA1==1 && (printing_batch_number == PartA_batch || assembly_location == EXPLODED_VIEW);
if (show_PartA1) {
    translate(clamp1_locations[assembly_location]) rotate(clamp1_rotations[assembly_location]) clamp();
    translate(clamp2_locations[assembly_location]) rotate(clamp2_rotations[assembly_location]) thermistor_clamp();
    translate(clamp3_locations[assembly_location]) rotate(clamp3_rotations[assembly_location]) clamp();
    translate(clamp4_locations[assembly_location]) rotate(clamp4_rotations[assembly_location]) clamp();
}

// Add in wire bridges to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartA1 && show_PartA2)
{
    translate([-Walls*3/2-MINIMUM_WIRE_SIZE*3, -Walls/2-2*(A1_offset+Walls), -Walls/6]) 
    translate(clamp4_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 6*(A1_offset+Walls)+MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
    
    for (clamp_index = [0, 1, 2, 3]) {
        translate([-Walls*3/2-MINIMUM_WIRE_SIZE*2, clamp_index*(A1_offset+Walls)-Walls/2, -Walls/6]) 
        translate(clamp4_locations[assembly_location])  
            cube([MINIMUM_WIRE_SIZE*3, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
    }

    translate([-Walls*3/2-MINIMUM_WIRE_SIZE*2, 4*(A1_offset+Walls)-Walls/2, -Walls/6]) 
    translate(clamp4_locations[assembly_location])  
        cube([30, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);

    // Add in the wire bridge to the angled stick as well
    translate([-Walls*3/2-MINIMUM_WIRE_SIZE*2, -2*(A1_offset+Walls)-Walls/2, -Walls/6]) 
    translate(clamp4_locations[assembly_location])  
        cube([6, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);

}

/////////////////////////////////////////////////////////////////////////////////
/// MODULE A2 - basefeet   /////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

A_Foot_Z = 30;
A_Foot_Groove_Z = 3;
A_Foot_Corners_XY = 10;
PartA2_locations = [[0,0,0], [-A_Base_Y-MINIMUM_PRINT_LAYOUT_SEPARATION, A_Base_X/4, A_Foot_Z+sep]];
PartA2_rotations = [[0,0,0], [0, 0, 90]];


module A2(){
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2-sep]){cube([A_Base_X+Walls,A_Base_Y+Walls,A_Foot_Z], center = true );} // Main foot
	
}
module A2_sub(){
	translate([0,0,-A_Foot_Z/2-sep]){cube([P_XY-P_ridge*2,P_XY-P_ridge*2,A_Foot_Z], center = true );} // Peltier below
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Groove_Z/2-sep]){cube([A_Base_X+Tol,A_Base_Y+Tol,A_Foot_Groove_Z], center = true );} // BASE

	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2-sep]){cube([A_Base_X-Walls,A_Base_Y-Walls,A_Foot_Z], center = true );} // Main Hole
	
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2+Walls/2-sep]){cube([A_Base_X-Walls-A_Foot_Corners_XY,A_Base_Y*2,A_Foot_Z-Walls], center = true );} // CornerCut Hole1
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2+Walls/2-sep]){cube([A_Base_X*2,A_Base_Y-Walls-A_Foot_Corners_XY,A_Foot_Z-Walls], center = true );}  // CornerCut Hole2


}
show_PartA2 = PartA2==1 && (printing_batch_number == PartA_batch || assembly_location == EXPLODED_VIEW);
if (show_PartA2) {translate(PartA2_locations[assembly_location]) rotate(PartA2_rotations[assembly_location]) difference(){A2();A2_sub();}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartA2 && show_PartA)
{
    translate([A_Base_X/4, P_XY/2+P_border-MINIMUM_WIRE_SIZE, -A_Foot_Z-sep]) 
    translate(PartA2_locations[assembly_location])  
        cube([10, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE B - main wall //////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

PartB_batch = 1;    // The printing batch that PartB belongs to
PartB_locations = [[-(P_XY/2+P_border), 0, sep], [-A_Wall_Y*1.75-6, A_Wall_Y/2+6, 0]];
PartB_rotations = [[0,0,0], [0,90,0]];

module B(){
	translate([-A_Wall_X/2,0,A_Wall_Z/2]){cube([A_Wall_X,A_Wall_Y,A_Wall_Z], center = true );} // WALL
	translate([-A_Wall_X/2,0,A_Wall_Z_long/2]){cube([A_Wall_X,A_Wall_Y_long,A_Wall_Z_long], center = true );} // WALL_extra
	translate([-A_Wall_X/2,0,0.5-A_Base_Z/2]){cube([Walls,A_Base_Y-Walls*4-Tol*2,A_Base_Z], center = true );} // WALL_link
	translate([-A_Wall_X/2,0,A_Wall_Z-A_Wall_Y/999]){rotate ([0,270,0]) {cylinder($fn = 3, r = A_Wall_Y/2, h = Walls, center = true );}} // WALL_rounding top
}
module B2(){
	translate([1.7*Walls-Mount_h,RPi_holedist_Yb,RPi_groundZ]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_bottom
	translate([1.7*Walls-Mount_h,RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_top
	translate([1.7*Walls-Mount_h,-RPi_holedist_Yb,RPi_groundZ]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_bottom
	translate([1.7*Walls-Mount_h,-RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_top
}
module B_sub(){
	translate([-A_Base_Y/4,(P_XY+2*Tol)/2-(P_cable+2*Tol)/2+P_cable/2,-P_Z/2]){cube([A_Base_Y,P_cable*2+2*Tol,P_Z], center = true );} // Peltier cable1
	translate([-A_Base_Y/4,-(P_XY+2*Tol)/2+(P_cable+2*Tol)/2-P_cable/2,-P_Z/2]){cube([A_Base_Y,P_cable*2+2*Tol,P_Z], center = true );} // Peltier cable2
	translate([-A_Base_Y/4,T_cable_offset,T_cableZ/2+Tol]){cube([A_Base_Y,T_cableY,T_cableZ+2*Tol], center = true );} // thermistor cable
	translate([-A_Base_Y/2,0,-MarkerLED_R-MarkerLED_Z]){rotate ([0,90,0]) {cylinder($fn = 50, r = MarkerLED_R, h = A_Base_Y, center = true );}} // MarkerLed HOLE
	translate([-A_Wall_X/2-(Walls-Walls_thinning)/2,0,A_Wall_Z/2]){cube([Walls_thinning,A_Wall_Y-Borders,A_Wall_Z-Borders], center = true );} // Save Material	
}
module B2_sub(){
	translate([Walls-Mount_h,RPi_holedist_Yb,RPi_groundZ]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // m hole_bottom
	translate([Walls-Mount_h,RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // 
	translate([Walls-Mount_h,-RPi_holedist_Yb,RPi_groundZ]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // m hole_bottom
	translate([Walls-Mount_h,-RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // 
}
show_PartB = PartB==1 && (printing_batch_number == PartB_batch || assembly_location == EXPLODED_VIEW);
if (show_PartB){translate(PartB_locations[assembly_location]) rotate(PartB_rotations[assembly_location]) difference(){B();B_sub();}}
if (show_PartB){translate(PartB_locations[assembly_location]) rotate(PartB_rotations[assembly_location]) difference(){B2();B2_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE B3 - Arduino/Fritzing holder ////////
/////////////////////////////////////////////////////////////////////////////////

Fritzing_X = 1.65;
Fritzing_Y = 76.75;
Fritzing_Z_depth = 3;
Mount2_h = 25;
Mount2_Z = 4;
Ard_holder_X = Walls*2 + Fritzing_X;
Ard_holder_Y = Fritzing_Y + 2*Walls;
Ard_z_extra = 5;
Ard_holder_Z = 2*S_mount_R+Ard_z_extra;
Foot_Z_extra = 2;
LShape_Length = 6;
LShape_Width = 3;

PartB3_locations = [[-P_XY/2-P_border-2*sep, 0, RPi_groundZ + sep], [P_XY/2+P_border+Ard_holder_X, 60, Ard_holder_Z/2-Ard_z_extra/2]];
PartB3_rotations = [[0,0,0], [0, 0, 90]];

module B3(){
	translate([-Ard_holder_X/2,0,Ard_z_extra/2]){cube([Ard_holder_X,Ard_holder_Y,Ard_holder_Z], center = true );} // Holder
	translate([1.7*Walls-Mount_h+Mount2_h/2,RPi_holedist_Yb,Ard_z_extra/2]){cube([Mount2_h,S_mount_R*2,Ard_holder_Z], center = true );} // foot
	translate([1.7*Walls-Mount_h+Mount2_h/2,-RPi_holedist_Yb,Ard_z_extra/2]){cube([Mount2_h,S_mount_R*2,Ard_holder_Z], center = true );} // foot
}
module B3_sub(){
	translate([-Ard_holder_X/2,0,Ard_holder_Z/2-Fritzing_Z_depth/2]){cube([Fritzing_X+Tol,Fritzing_Y+2*Tol,Fritzing_Z_depth+Ard_z_extra], center = true );} // slot
	translate([-(Ard_holder_X-Mount2_h)/2,0,Ard_holder_Z/2]){cube([Ard_holder_X+Mount2_h+1,Fritzing_Y-2,Ard_z_extra], center = true );} // Holder
	translate([1.7*Walls-Mount_h+Mount2_h/2,RPi_holedist_Yb,0]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = Mount2_h+5, center = true );}} // m hole_bottom
	translate([1.7*Walls-Mount_h+Mount2_h/2,-RPi_holedist_Yb,0]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = Mount2_h+5, center = true );}} // m hole_bottom
    translate([1.7*Walls-Mount_h+Mount2_h-LShape_Length/2,RPi_holedist_Yb-S_mount_R+LShape_Width/2,0]){cube([LShape_Length,LShape_Width,Ard_holder_Z], center = true );} // L-Shape
	translate([1.7*Walls-Mount_h+Mount2_h-LShape_Length/2,-RPi_holedist_Yb+S_mount_R-LShape_Width/2,0]){cube([LShape_Length,LShape_Width,Ard_holder_Z], center = true );} // L-Shape    
}
show_PartB3 = PartB3==1 && (printing_batch_number == PartB_batch || assembly_location == EXPLODED_VIEW);
if (show_PartB3){translate(PartB3_locations[assembly_location]) rotate(PartB3_rotations[assembly_location]) difference(){B3();B3_sub();}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartB3 && show_PartB)
{
    translate([-Ard_holder_Y/2-25, -MINIMUM_WIRE_SIZE, -Ard_holder_Z/2+Ard_z_extra/2]) 
    translate(PartB3_locations[assembly_location])  
        cube([30, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}
////////////////////////////////////////////////////////////////////////////////
///// Common modules for mount configurations   /////
/////////////////////////////////////////////////////////////////////////////////
module Mount(X_dim, Y_dim, thickness = Walls, Y_extension=0, link_thickness=Walls){
    thickness = thickness/2;  // Will be increased again by the minkowski operation
    link_thickness = link_thickness - thickness;  // Will be scaled up again by the minkowski operation
    x_thickness_adj = 2*(Walls - corner_radius);
    y_thickness_adj = 2*(Walls - corner_radius);
    y_sep = Y_extension > 0 ? -2*sep-Y_extension/2 : 0;
    minkowski()
    {
        union() {
            translate([X_dim/2+P_border,0,-(link_thickness - thickness)/2]){cube([X_dim+x_thickness_adj,Y_dim+Y_extension+y_thickness_adj,thickness], center = true );} 
            translate([(-3*A_Wall_X+P_border+P_XY/2+x_thickness_adj)/2+Walls, Y_extension/2, 0]) {
                cube([A_Wall_X+2*Walls+OPTICAL_AXIS_OFFSET_X+x_thickness_adj,A_Wall_Y_long+y_thickness_adj,link_thickness], center = true );  // LINK
            } 
        }
        cylinder(r=corner_radius, h=thickness, center=true);
    }
}

module Mount_link_holes(link_thickness=Walls)
{
    translate([-(A_Wall_X+Tol)/2, 0, 0]){cube([A_Wall_X+Tol,A_Wall_Y_long+2*Tol,link_thickness*1.5], center = true );} // link_hole
    translate([-(A_Wall_X+Tol)*1.5, 0, 0]) rotate ([0,90,0]) cylinder(r = S_hole_R, h = (A_Wall_X+Tol)*2, center = true ); // screwhole    
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE C - camera mount /////////////////////////
/////////////////////////////////////////////////////////////////////////////////

MiniGrooveX = 15;
Cam_Z = Walls*1.5;
PartC_batch = 0;    // The printing batch that PartC belongs to
PartC_locations = [[sep+Cam_X_offset, 0, 2*sep+Cam_Zfloat], [-A_Base_X/2-P_XY/2-3, A_Base_Y*0.5+5, Cam_Z/2]];
PartC_rotations = [[0,0,0], [0, 0, 0]];

module C_sub(){
	translate([OPTICAL_AXIS_OFFSET_X,0,Walls*0.75-C_Z/2]){cube([Cam_X+Tol*2,Cam_Y+Tol*2,C_Z], center = true );} // Cam_hole_ridge
	translate([OPTICAL_AXIS_OFFSET_X-Cam_X/2-CamGroove_X/2,0,C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cam_cable_groove
	translate([OPTICAL_AXIS_OFFSET_X+Cam_X/2-MiniGrooveX/2-C_ridge,-Cam_Y/2+C_ridge/2,C_Z2/2]){cube([MiniGrooveX,C_ridge,C_Z2+Walls/2], center = true );} // mini groove
	translate([OPTICAL_AXIS_OFFSET_X+-Cam_X/2+CamGroove_X/2,0,C_Z2/2]){cube([CamGroove_X,CamGroove2_Y,C_Z2+Walls/2], center = true );} // Cam_bump_groove
	translate([OPTICAL_AXIS_OFFSET_X,0,0]){cube([Cam_X-C_ridge*2,Cam_Y-C_ridge*2,Walls*3], center = true );} // Cam_hole
    Mount_link_holes();
}
show_PartC = PartC==1 && (printing_batch_number == PartC_batch || assembly_location == EXPLODED_VIEW);
if (show_PartC){translate(PartC_locations[assembly_location]) rotate(PartC_rotations[assembly_location]) {difference(){Mount(Cam_X, Cam_Y, Cam_Z, 0, Cam_Z);C_sub();}}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartC && show_PartA2)
{
    translate([Cam_X/2, Cam_Y-12, -Cam_Z/2]) 
    translate(PartC_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 
              10,
              MINIMUM_WIRE_SIZE],
             center=false);
}


/////////////////////////////////////////////////////////////////////////////////
///// MODULE C1 - camera mount with servo ////
/////////////////////////////////////////////////////////////////////////////////

Servo_Y = 12.2;
Servo_X = 23.7;
Servo_X_offset = 5.5;
// height of Servo is 29 in total, which is counted from the bottom
PartC1_locations = [[sep+Cam_X_offset, -(Servo_Y+Walls)/2, 2*sep+Cam_Zfloat], [-A_Base_X/2-P_XY/2-3, A_Base_Y*0.5-2, Cam_Z/2]];
PartC1_rotations = [[0,0,0], [0, 0, 0]];

module C1_sub(){
    translate([0, (Servo_Y+Walls)/2, 0]) C_sub();
    translate([Servo_X+Servo_X_offset-Walls/2,-Cam_Y/2-Walls/2,0]){cube([Servo_X+Tol,Servo_Y+Tol,Cam_Z*2], center = true );} // Servo_hole
    translate([Servo_X+Servo_X_offset+Servo_X/2-Walls/2,-Cam_Y/2-Walls/2,0]){cylinder( $fn=50, r = 4, h = 100, center = true );} // Servo_cablegroove

}
show_PartC1 = PartC1==1 && (printing_batch_number == PartC_batch || assembly_location == EXPLODED_VIEW);
if (show_PartC1){translate(PartC1_locations[assembly_location]) rotate(PartC1_rotations[assembly_location]) {difference(){Mount(Cam_X, Cam_Y, Cam_Z, Servo_Y+Walls, Cam_Z);C1_sub();}}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartC1 && show_PartA2)
{
    translate([Cam_X/2, Cam_Y-12, -Cam_Z/2]) 
    translate(PartC_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 
              10,
              MINIMUM_WIRE_SIZE],
             center=false);
}

///////////////////////////
//  Cogwheel design using involute teeth
//
//////////////////////////
cogwheel_R = 14.1;
cogwheel_R2 = 10.5;
cogwheel_Z = 10;
cogwheel_Z2 = 4;
cogwheel_nteeth = 30; // should be divisible by 3
cogwheel_R_inner1 = 7+Tol; // camera radius
cogwheel_R_inner2 = 3.7+Tol/2; // servo axis radius
cogwheel_cross_Z = 3;
cogwheel_cross_Width = 4.5+Tol;
cogwheel_cross_Length = cogwheel_R2*2-1;

include <MCAD/involute_gears.scad>
// Gear parameter description from: http://www.thingiverse.com/thing:3575
/*
    Parametric Involute Spur Gears take the following parameters:
    number_of_teeth
    circular_pitch or diametral_pitch: controls the size of the teeth (and hence the size of the gear).
    The circular pitch is in units of pi/180 mm (according to a comment by the author on Thingiverse).
    pressure_angle: controls the shape of the teeth.
    clearance: The gap between the root between teeth and the teeth point on a meshing gear.
    gear_thickness: the thickness of the gear plate.
    rim_thickness: the thickness of the gear at the rim (including the teeth).
    rim_width: radial distance from the root of the teeth to the inside of the rim.
    hub_thickness: the thickness of the section around the bore.
    hub_diameter
    bore_diameter: size of the hole in the middle
    circles: the number of circular holes to cut in the gear plate.
    backlash: the space between this the back of this gears teeth and the front of its meshing gear's teeth when the gear is correctly spaced from it.
    twist: for making helical gears.
    involute_facets: the number of facets in one side of the involute tooth shape. If this is omitted it will be 1/4 of $fn. If $fn is not set, it will be 5.
*/

module cogwheel(bore_radius)
{
    pressure_angle = 22; // degrees
    pitch_circle_diameter = 2*cogwheel_R*15/16;
    gear_thickness = cogwheel_Z2;  
    rim_thickness = cogwheel_Z;
    bore_diameter = 2*bore_radius;
    hub_diameter = 0;  
    cutout_circles = 0;  // Symmetrically balanced circles on the inside of the gear
    circular_pitch = 180 * pitch_circle_diameter/cogwheel_nteeth;  // in units of pi/180 mm
    
    gear (number_of_teeth=cogwheel_nteeth, circular_pitch=circular_pitch,
          pressure_angle=pressure_angle,
          clearance=0.05*(pi/180)*circular_pitch,  // Formula derived from info. in Ivan Law's book "Gears and Gear Cutting"
          bore_diameter= bore_diameter,
          gear_thickness = gear_thickness,
          rim_thickness = rim_thickness,
          rim_width=cogwheel_R/8,
          hub_diameter=hub_diameter,  
          hub_thickness = cogwheel_Z,
          circles=cutout_circles,                   
          involute_facets=10);
}

PartC2_1_locations = [[sep+Cam_X_offset,-2*sep,Cam_Zfloat+2*sep-cogwheel_Z2-1], 
                      [-A_Base_Y, -1.5*cogwheel_R+2, 0]];
PartC2_1_rotations = [[0, 0, 0], 
                      [0, 0, 45]]; // Rotate the cross engraving away from horizontal and vertical so a wire may be attached
PartC2_2_locations = [[sep+Cam_X_offset,-3*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+2*sep-cogwheel_Z2-1], 
                      [-A_Base_Y, -3.5*cogwheel_R, 0]];
PartC2_2_rotations = [[0, 0, 180/cogwheel_nteeth], 
                      [0, 0, 180/cogwheel_nteeth]];

show_PartC2_1 = PartC2_1==1 && use_servo_focus && (printing_batch_number == PartC_batch || assembly_location == EXPLODED_VIEW);
if (show_PartC2_1)
{
    translate(PartC2_1_locations[assembly_location]) rotate(PartC2_1_rotations[assembly_location]) 
    difference()
    {
        cogwheel(cogwheel_R_inner1);
        translate([0,0,cogwheel_cross_Z+0.5]){cube([cogwheel_cross_Length,cogwheel_cross_Width, cogwheel_cross_Z+1], center = true);} // Servo_cog cross1
        translate([0,0,cogwheel_cross_Z+0.5]){cube([cogwheel_cross_Width,cogwheel_cross_Length,cogwheel_cross_Z+1], center = true);} // Servo_cog cross2    
  }
}

show_PartC2_2 = PartC2_2==1 && use_servo_focus && (printing_batch_number == PartC_batch || assembly_location == EXPLODED_VIEW);
if (show_PartC2_2)
{
    translate(PartC2_2_locations[assembly_location]) rotate(PartC2_2_rotations[assembly_location]) cogwheel(cogwheel_R_inner2);
}

// Add in wire bridges to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartC2_1 && show_PartC2_2)
{
    translate(PartC2_2_locations[assembly_location]) translate([0, cogwheel_R+0.25, 0]) arch_bridge(cogwheel_R/2+1.5, 3);
    if (show_PartA2)
    {
        translate(PartC2_2_locations[assembly_location]) translate([0, -cogwheel_R+0.25, 0]) arch_bridge(cogwheel_R/2, 3);
    }
}


/////////////////////////////////////////////////////////////////////////////////
///// MODULE D - high power LED mount  /////////
/////////////////////////////////////////////////////////////////////////////////

D_X = Cam_X;
D_Y = Cam_Y;
D_Z = Walls * 1.5;
Tube_wall = 1.5;
LED_holder_inside = 35+2*Tol;
LED_holder_outside = 35+2*Tol+2*Walls;
LED_holder_ridge = 3;
PartD_batch = 2; // The printing batch that PartD belongs to
PartD_locations = [[sep+Cam_X_offset, 0, Cam_Zfloat], [-OPTICAL_AXIS_OFFSET_X-5, -A_Base_Y+14, D_Z/2]];
PartD_rotations = [[0,0,0], [0, 0, 0]];


module D_sub(){
	translate([D_X/2+P_border,0,0]){cylinder(r = Excit_hole_R+Tube_wall+Tol, h = D_Z*1.5, center = true );} 
	translate([D_X/2+P_border,0,Walls*0.4]){cube([LED_holder_inside,LED_holder_inside,D_Z/2], center = true );} // LED_holder_groove2
    Mount_link_holes(D_Z);
}

show_PartD = PartD==1 && (printing_batch_number == PartD_batch || assembly_location == EXPLODED_VIEW);
if (show_PartD){translate(PartD_locations[assembly_location]) rotate(PartD_rotations[assembly_location]) difference(){Mount(D_X, D_Y, D_Z, 0, D_Z);D_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE E - angled pillars  //////////////////////////
/////////////////////////////////////////////////////////////////////////////////

E_Y_extra = 35;
E_Z_extra = 40;
E_extra_angle = -40;
E_extra_angle2 = -30;
PartE_batch = 0; // The printing batch that PartE belongs to
PartE_locations = [[-P_XY/2-P_border-A_Wall_X/2, 2*sep, Cam_Zfloat], [-A_Base_X+10, 0, Walls*1.5/2]];
PartE_rotations = [[0,0,0], [0, 0, 180]];

module E(){
		translate([0,0,0]){cube([A_Wall_X+2*Walls,A_Wall_Y_long+2*Walls,Walls*1.5], center = true );} // Cam_link
		translate([0,E_Y_extra/2,0]){cube([Walls,A_Wall_Y_long+2*Walls+E_Y_extra,Walls*1.5], center = true );} // Arm
        translate([0,E_Y_extra-sin(E_extra_angle)*E_Z_extra-10,E_Z_extra/2-5]) {rotate ([E_extra_angle,0,0]) {cube([A_Wall_X,A_Wall_Y_long,E_Z_extra], center = true );}} // W_extra1
		translate([0,E_Y_extra-15-sin(E_extra_angle2)*E_Z_extra-10,E_Z_extra/2-3]) {rotate ([E_extra_angle2,0,0]) {cube([A_Wall_X,A_Wall_Y_long*0.6,E_Z_extra], center = true );}} // W_extra2
}
module E_sub(){
	translate([0, 0, 0]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*10], center = true );} // Cam_link_hole
	//translate([-Cam_X/2-CamGroove_X-15,2*sep,Cam_Zfloat]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = false );}} // screwhole
}
show_PartE = PartE==1 && (printing_batch_number == PartE_batch || assembly_location == EXPLODED_VIEW);
if (show_PartE){translate(PartE_locations[assembly_location]) rotate(PartE_rotations[assembly_location]) difference(){E();E_sub();}}

// The wire bridge for the angled pillar was connected to the clamps in a section above

/////////////////////////////////////////////////////////////////////////////////
///// MODULE F1 - extra pillar stick 1 //////////////////
/////////////////////////////////////////////////////////////////////////////////

F_Plug_X = 15;
Airhole_R2 = 4;

module pillar_stick(stick_length)
{
    difference() {	
        union() {
            translate([0,0, stick_length/2]){cube([A_Wall_Y_long,A_Wall_X,stick_length+A_Base_Z], center = true );} // low_mount
            translate([0,0,0]){cube([A_Wall_Y_long*4,A_Wall_X,A_Base_Z], center = true );} // low_mount
            
            // The air hole tubes sit just below the center line of the base, since the center line of the holes needed to be adjusted for the peltier grove
            translate([Airhole_spacing,F_Plug_X/2,-P_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole1
            translate([0,F_Plug_X/2,-P_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole2
            translate([-Airhole_spacing,F_Plug_X/2,-P_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole3
        }
        union() {
            translate([Airhole_spacing,F_Plug_X/2,-P_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
            translate([0,F_Plug_X/2,-P_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
            translate([-Airhole_spacing,F_Plug_X/2,-P_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
        }  
    }        
}

PartF_batch = 1; // The printing batch that PartF1, PartF2, PartF3 belong to
PartF1_locations = [[0, -A_Base_Y/2-A_Wall_X/2-sep, -A_Base_Z/2], [-A_extramount_Z-30, -A_Wall_Y_long-8, A_Wall_X/2]];
PartF1_rotations = [[0,0,0], [90, 0, 90]];
show_PartF1 = PartF1==1 && (printing_batch_number == PartF_batch || assembly_location == EXPLODED_VIEW);
if (show_PartF1){translate(PartF1_locations[assembly_location]) rotate(PartF1_rotations[assembly_location]) pillar_stick(A_extramount_Z+20); }

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartF1 && show_PartB)
{
    translate([-A_Wall_X/2-15, -A_Wall_Y/2-10, 0]) 
    translate(PartB_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 30, MINIMUM_WIRE_SIZE], center=false);
}
/////////////////////////////////////////////////////////////////////////////////
///// MODULE F2 - extra pillar stick 2 (mini)    ////
/////////////////////////////////////////////////////////////////////////////////

Ministick_Z = 15;
PartF2_locations = [[2*sep, -A_Base_Y/2-A_Wall_X/2-sep, -A_Base_Z/2], [115, 60, A_Wall_X/2]];
PartF2_rotations = [[0,0,0], [90, 0, 0]];

show_PartF2 = PartF2==1 && (printing_batch_number == PartF_batch || assembly_location == EXPLODED_VIEW);
if (show_PartF2){translate(PartF2_locations[assembly_location]) rotate(PartF2_rotations[assembly_location]) pillar_stick(Ministick_Z); }

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartF2 && show_PartB3)
{
    translate([Ard_holder_Y/2, -MINIMUM_WIRE_SIZE, -Ard_holder_Z/2+Ard_z_extra/2]) 
    translate(PartB3_locations[assembly_location])  
        cube([10, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}
/////////////////////////////////////////////////////////////////////////////////
///// MODULE F1 - extra pillar stick 3 (right angle) //////////////////
/////////////////////////////////////////////////////////////////////////////////
horizontal_length = 28;
PartF3_locations = [[-2*sep, -A_Base_Y/2-A_Wall_X/2-sep, -A_Base_Z/2], [-80, -A_Wall_Y_long-40, A_Wall_X/2]];
PartF3_rotations = [[0,0,0], [90, 0, 270]];
show_PartF3 = PartF3==1 && (printing_batch_number == PartF_batch || assembly_location == EXPLODED_VIEW);
if (show_PartF3){
    translate(PartF3_locations[assembly_location]) rotate(PartF3_rotations[assembly_location]) {
        translate([0, (horizontal_length-A_Wall_X)/2, 53]){rotate([90,0,0]){ cube([A_Wall_Y_long, A_Wall_X, horizontal_length], center = true );}} // 90°
        pillar_stick(41); 
    }
}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartF3 && show_PartF1)
{
    translate([A_Wall_X, -A_Wall_Y_long*2, -A_Wall_X/2]) 
    translate(PartF1_locations[assembly_location])  
        cube([40, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE G - links and thumbscrews //////////
/////////////////////////////////////////////////////////////////////////////////

G_Plug_X1 = 22; // tight fit
G_Plug_X2 = 32; // 1 cm extra
G_Plug_X3 = 42; // 2 cm extra
G_thumb_outer = 4;
G_thumb_ridge = 6;
G_thumb_ridge_Z = 5;
G_thumb_inner = 5.5/2;
G_thumb_inner_Z = 3;
G_thumb_Z = 10;

PartG_batch = 1; // The printing batch that PartG belongs to
PartG_print_location_X = -A_Base_X/2-P_XY/2+Walls*2;
PartG_manipulator1_locations = [[Airhole_spacing, A_Base_Y/2+sep, A_Base_Z/2], [PartG_print_location_X+2 * Airhole_spacing, -Airhole_R/2-2, 0]];
PartG_manipulator1_rotations = [[0,0,0], [90, 0, 0]];
PartG_manipulator2_locations = [[0, A_Base_Y/2+sep, A_Base_Z/2], [PartG_print_location_X, -Airhole_R/2-2, 0]];
PartG_manipulator2_rotations = [[0,0,0], [90, 0, 0]];
PartG_manipulator3_locations = [[-Airhole_spacing, A_Base_Y/2+sep, A_Base_Z/2], [PartG_print_location_X-2*Airhole_spacing, -Airhole_R/2-2, 0]];
PartG_manipulator3_rotations = [[0,0,0], [90, 0, 0]];
PartG_thumbscrew_locations = [[2*Airhole_spacing, A_Base_Y/2+sep, A_Base_Z/2], [PartG_print_location_X+4*Airhole_spacing, -Airhole_R*1.5-2, Airhole_R-Tol]];
PartG_thumbscrew_rotations = [[0,0,0], [0, 0, 0]];

module manipulator_link(link_length)
{
    translate([0,link_length/2,0]) rotate ([90,90,0]) {
        difference(){
            cylinder(r = Airhole_R-Tol, h = link_length, center = true );
            cylinder(r = Airhole_R-Tube_wall, h = link_length, center = true );
        }
    } 
}

module thumbscrew()
{
    translate([0,G_thumb_ridge,(G_thumb_Z-G_thumb_inner_Z)/2]) {
        difference(){
            union() {
                translate([0,0,-A_Base_Z/2+G_thumb_Z/2]) cylinder(r = G_thumb_outer, h = G_thumb_Z, center = true ); // thumbscrew
                translate([0,0,-A_Base_Z/2+G_thumb_ridge_Z/2]) cylinder(r = G_thumb_ridge, h = G_thumb_ridge_Z, center = true ); // thumbscrew
            }
            union() {
                translate([0,0,G_thumb_Z/2]) cylinder(r = G_thumb_inner-3*Tol, h = G_thumb_Z, center = true ); // thumbtop
                translate([0,0,G_thumb_Z-G_thumb_inner_Z/2]) cylinder(r = G_thumb_inner+Tol/2, h = G_thumb_inner_Z, center = true ); // thumbhead
            }
      }
    } 
}

show_PartG = PartG==1 && (printing_batch_number == PartG_batch || assembly_location == EXPLODED_VIEW);
if (show_PartG){translate(PartG_manipulator1_locations[assembly_location]) rotate(PartG_manipulator1_rotations[assembly_location]) manipulator_link(G_Plug_X1);}
if (show_PartG){translate(PartG_manipulator2_locations[assembly_location]) rotate(PartG_manipulator2_rotations[assembly_location]) manipulator_link(G_Plug_X2);}
if (show_PartG){translate(PartG_manipulator3_locations[assembly_location]) rotate(PartG_manipulator3_rotations[assembly_location]) manipulator_link(G_Plug_X3);}
if (show_PartG){translate(PartG_thumbscrew_locations[assembly_location]) rotate(PartG_thumbscrew_rotations[assembly_location]) thumbscrew();}

// Add in wire bridges to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartG && show_PartB)
{
    for (index = [0:3])
    {
        translate([-A_Wall_X/2+18.5+index*2*Airhole_spacing, -A_Wall_Y/2-6, 0]) 
        translate(PartB_locations[assembly_location])  
            cube([MINIMUM_WIRE_SIZE, 6, MINIMUM_WIRE_SIZE], center=false);
    }
}

//////////////////////////////////////////////////////////////////////////////////
///// MODULE H - Adafruit 8x8 Matrix mount /////
/////////////////////////////////////////////////////////////////////////////////

Matrix_XY = 32;
Matrix_screwdistY = 28;
Matrix_screwdistX = 37;
Smini_hole_R = 1;
PartH_batch = 1; // The printing batch that PartH belongs to
PartH_locations = [[sep+Cam_X_offset, 0, Cam_Zfloat-2*sep], [10, -Cam_Y*1.5, Walls/2]];
PartH_rotations = [[0,0,0], [0, 0, 0]];

module H_sub(){
    translate([PELTIER_AXIS_OFFSET_X, 0, 0])
    {
        translate([0,0,0]){cube([Matrix_XY+Tol*2,Matrix_XY+Tol*2,Walls], center = true );} // Main hole
        translate([-Cam_X/2-CamGroove_X/2,0,C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cable_groove
        translate([-Cam_X/2-CamGroove_X/2-3,0,0]){rotate ([0,0,0]) {cylinder(r = CamGroove_X/4, h = Walls, center = true );}} // Cable through-hole
        translate([Matrix_screwdistX/2,Matrix_screwdistY/2,0]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole1
        translate([-Matrix_screwdistX/2,Matrix_screwdistY/2,0]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole2
        translate([Matrix_screwdistX/2,-Matrix_screwdistY/2,0]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole3
        translate([-Matrix_screwdistX/2,-Matrix_screwdistY/2,0]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole4
    }
    Mount_link_holes();
}
show_PartH = PartH==1 && (printing_batch_number == PartH_batch || assembly_location == EXPLODED_VIEW);
if (show_PartH){translate(PartH_locations[assembly_location]) rotate(PartH_rotations[assembly_location]) difference(){Mount(Cam_X, Cam_Y);H_sub();}}

// PartH is connected to PartI below

/////////////////////////////////////////////////////////////////////////////////
///// MODULE I - Adafruit 16LED ring mount //////
/////////////////////////////////////////////////////////////////////////////////

R_LEDring = 40/2;
PartI_batch = 1; // The printing batch that PartI belongs to
PartI_locations = [[sep+Cam_X_offset, 0, Cam_Zfloat-sep], [0, 10, Walls/2]];
PartI_rotations = [[0,0,0], [0, 0, 0]];

module I_sub(){
    translate([PELTIER_AXIS_OFFSET_X, 0, 0])
    {
        translate([0,0,0]){rotate ([0,0,0]) {cylinder(r = R_LEDring-Tol, h = Walls, center = true );}} // Main hole
        translate([0,0,1]){rotate ([0,0,0]) {cylinder(r = R_LEDring+Tol, h = Walls, center = true );}} // Main hole
        translate([0,0,1]){rotate ([0,0,0]) {cube([R_LEDring*2+Walls*3.5, 2*Walls, C_Z2/2+Walls/2], center = true );}} // extra sidegrooves1
        translate([0,0,1]){rotate ([0,0,90]) {cube([R_LEDring*2+Walls*3.5, 2*Walls, C_Z2/2+Walls/2], center = true );}} // extra sidegrooves2
        translate([Cam_X_offset-Cam_X/2-CamGroove_X/2,0,C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cable_groove
        translate([Cam_X_offset-Cam_X/2-CamGroove_X/2-3,0,0]){rotate ([0,0,0]) {cylinder(r = CamGroove_X/4, h = Walls, center = true );}} // Cable thread
    }
    Mount_link_holes();
}
show_PartI = PartI==1 && (printing_batch_number == PartH_batch || assembly_location == EXPLODED_VIEW);
if (show_PartI){translate(PartI_locations[assembly_location]) rotate(PartI_rotations[assembly_location]) difference(){Mount(Cam_X, Cam_Y);I_sub();}}

// Connecting PartH to PartI
if (connect_parts && show_PartH && show_PartI)
{
    translate([P_XY*0.75, P_XY/2, -A_Wall_X/2]) 
    translate(PartH_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 20, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE J - mini petri dish mount ///////////////
/////////////////////////////////////////////////////////////////////////////////

Petri_R = 35/2; // 
Petri_R_outer = 39/2; // for lid
PartJ_batch = 1; // The printing batch that PartJ1 and PartJ2 belong to
PartJ1_locations = [[sep+Cam_X_offset, 0, Cam_Zfloat-3*sep], [-Cam_X*2+10, -Cam_Y*1.5, Walls/2]];
PartJ1_rotations = [[0,0,0], [0, 0, 0]];

module J_sub(){
	translate([PELTIER_AXIS_OFFSET_X,0,0]){rotate ([0,0,0]) {cylinder(r = Petri_R_outer+Tol, h = Walls, center = true );}} // Main hole
    Mount_link_holes();
}
show_PartJ1 = PartJ1==1 && (printing_batch_number == PartJ_batch || assembly_location == EXPLODED_VIEW);
if (show_PartJ1){translate(PartJ1_locations[assembly_location]) rotate(PartJ1_rotations[assembly_location]) difference(){Mount(Cam_X, Cam_Y);J_sub();}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartJ1 && show_PartF3)
{
    translate([A_Wall_X+Walls/2, -A_Wall_Y_long*2+4, -A_Wall_X/2]) 
    translate(PartF3_locations[assembly_location])  
        cube([30, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

// Connect PartJ1 to PartI
if (connect_parts && show_PartJ1 && show_PartI)
{
    translate([P_XY+5, P_XY/2-5, -A_Wall_X/2]) 
    translate(PartJ1_locations[assembly_location])  
        cube([28, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE J2 - midi petri dish mount /////////////
/////////////////////////////////////////////////////////////////////////////////

Petri2_R = 58.8/2; // 
PartJ2_locations = [[sep+Cam_X_offset, 0, Cam_Zfloat-4*sep], [Cam_X*2, -2, Walls/2]];
PartJ2_rotations = [[0,0,0], [0, 0, 0]];

module J2_sub(){
	translate([PELTIER_AXIS_OFFSET_X+Petri2_R/2,0,0]){rotate ([0,0,0]) {cylinder(r = Petri2_R+Tol, h = Walls, center = true );}} // Main hole
    Mount_link_holes();

}
show_PartJ2 = PartJ2==1 && (printing_batch_number == PartJ_batch || assembly_location == EXPLODED_VIEW);
if (show_PartJ2){translate(PartJ2_locations[assembly_location]) rotate(PartJ2_rotations[assembly_location]) difference(){Mount(Petri2_R*2, Petri2_R*2);J2_sub();}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartJ2 && show_PartI)
{
    translate([-20, -Petri2_R, -A_Wall_X/2]) 
    translate(PartJ2_locations[assembly_location])  
        cube([40, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}


/////////////////////////////////////////////////////////////////////////////////
///// MODULE K - diffuser mount /////////////////////////
/////////////////////////////////////////////////////////////////////////////////

Link_Opening = A_Wall_Y_long;
Diffuser_XY = 45;
Diffuser_XY_inner = 38.5+2*Tol;
PartK_batch = 0; // The printing batch that PartK belongs to
PartK_locations = [[sep+Cam_X_offset, 0, Cam_Zfloat-5*sep], [A_Base_X/2-5, 0, Walls/2]];
PartK_rotations = [[0,0,0], [0, 0, 90]];

module K_sub(){
    translate([PELTIER_AXIS_OFFSET_X+(Diffuser_XY/2-Walls)/2,0,0]){cube([Diffuser_XY_inner,Diffuser_XY_inner,Walls], center = true );} // Main_hole
    translate([-(A_Wall_X+Tol)/2,-Link_Opening,0]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol+2*Link_Opening,Walls*1.5], center = true );} // link opening slot
    
    Mount_link_holes();
}
show_PartK = PartK==1 && (printing_batch_number == PartK_batch || assembly_location == EXPLODED_VIEW);
if (show_PartK){translate(PartK_locations[assembly_location]) rotate(PartK_rotations[assembly_location]) difference(){Mount(Diffuser_XY, Diffuser_XY);K_sub();}}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartK && show_PartA)
{
    translate([A_Base_X/4-MINIMUM_WIRE_SIZE, P_XY/2, -A_Base_Z]) 
    translate(PartA_locations[assembly_location])  
        cube([10, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE L1 - small microsc. sl. chamber  //
/////////////////////////////////////////////////////////////////////////////////

Plug_R = 1.25;
Chamber_Z = 1;
Slide1_Y = 25;
Slide1_X = Slide1_Y+10;
Slide1_Z = 1.5;
lid_thickness = 1;
PartL_batch = 0; // The printing batch that PartL1 and PartL2 belong to
PartL1_chamber_locations = [[sep*4, 0, 4*sep], [A_Base_X/2+Diffuser_XY/2+Slide1_X/2+4, Diffuser_XY/2, Slide1_Z/2]];
PartL1_chamber_rotations = [[0,0,0], [0, 0, 0]];
PartL1_lid_locations = [[sep*4, 0, 5*sep], [A_Base_X/2+Diffuser_XY/2+Slide1_X/2+4, Slide1_Y+Diffuser_XY/2+5, 0]];
PartL1_lid_rotations = [[180,0,0], [0, 0, 0]];

module slide_chamber_lid(size)
{
    translate([0,0,lid_thickness/2])
    difference() {
        union() {
            translate([0,0,0]){cube([size[0],size[1],lid_thickness], center = true );} // Lid 
            translate([size[1]/2+2.75,0,Chamber_Z]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = size[2], center = true );}} // Plug 
            translate([-size[1]/2-2.75,0,Chamber_Z]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = size[2], center = true );}} // Plug 
       }
        union() {
            translate([0,0,0]){rotate ([0,0,0]) {cylinder(r = Slide1_Y/2-2, h = Chamber_Z+size[2], center = true );}} // Lid hole
        } 
    }
}

module slide_chamber(size)
{
    translate([0,0,Chamber_Z/2])
    difference() {
        union() {
            translate([0,0,0]){cube([size[0],size[1],Chamber_Z+size[2]], center = true );} // Main 
            translate([size[1]/2+2.75,0,Chamber_Z]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = size[2], center = true );}} // Plug 
            translate([-size[1]/2-2.75,0,Chamber_Z]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = size[2], center = true );}} // Plug 
       }
        union() {
            translate([0,0,0]){rotate ([0,0,0]) {cylinder(r = size[1]/2-2, h = Chamber_Z+size[2], center = true );}} // Main hole
            translate([0,0,size[2]]){cube([size[1]+7*Tol,size[0],Chamber_Z+size[2]], center = true );} // Lid groove
            translate([size[1]/2+2.75,0,Chamber_Z/2]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R+Tol, h = size[2]*3, center = true );}} // Plug hole goes right through
            translate([-size[1]/2-2.75,0,Chamber_Z/2]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R+Tol, h = size[2]*3, center = true );}} // Plug hole goes right through
       } 
    }
}

show_PartL1 = PartL1==1 && (printing_batch_number == PartL_batch || assembly_location == EXPLODED_VIEW);
if (show_PartL1) {
    translate(PartL1_chamber_locations[assembly_location]) rotate(PartL1_chamber_rotations[assembly_location]) slide_chamber([Slide1_X,Slide1_Y, Slide1_Z]);
    translate(PartL1_lid_locations[assembly_location]) rotate(PartL1_lid_rotations[assembly_location]) slide_chamber_lid([Slide1_X,Slide1_Y,Slide1_Z]);
}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartL1 && show_PartK)
{
    // Connect the slide chamber lid to PartK
    translate([-Slide1_X/2-5, Slide1_Y/2-MINIMUM_WIRE_SIZE*3-corner_radius, 0]) 
    translate(PartL1_lid_locations[assembly_location])  
        cube([5, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
    
    // Connect the slide chamber to to PartK
    translate([-Slide1_X/2-10, Slide1_Y/2-MINIMUM_WIRE_SIZE*3-corner_radius, -Slide1_Z/2]) 
    translate(PartL1_chamber_locations[assembly_location])  
        cube([10, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE L2 - big microsc. sl. chamber  /////
/////////////////////////////////////////////////////////////////////////////////

Chamber2_Z = 1;
Slide2_Y = 50;
Slide2_X = Slide2_Y+10;
Slide2_Z = 1.5;
PartL2_chamber_locations = [[sep*4, 0, 6*sep], [A_Base_X/2-5, -Diffuser_XY+3, Slide2_Z/2]];
PartL2_chamber_rotations = [[0,0,0], [0, 0, 90]];
PartL2_lid_locations = [[sep*4, 0, 7*sep], [A_Base_X/2+Diffuser_XY/2+Slide1_X/2+8, -Diffuser_XY+3, 0]];
PartL2_lid_rotations = [[180,0,0], [0, 0, 90]];

show_PartL2 = PartL2==1 && (printing_batch_number == PartL_batch || assembly_location == EXPLODED_VIEW);
if (show_PartL2) {
    translate(PartL2_chamber_locations[assembly_location]) rotate(PartL2_chamber_rotations[assembly_location]) slide_chamber([Slide2_X,Slide2_Y, Slide2_Z]);
    translate(PartL2_lid_locations[assembly_location]) rotate(PartL2_lid_rotations[assembly_location]) slide_chamber_lid([Slide2_X,Slide2_Y,Slide2_Z]);
}

// Add in wire bridge to the nearby parts (note that the location of the bridges is sensitive to the location of the parts being connected)
if (connect_parts && show_PartL2 && show_PartA)
{
    // Connect the slide chamber to PartA
    translate([-PartL2_chamber_locations[assembly_location][0]/2, -PartL2_chamber_locations[assembly_location][1]/2+Walls, -Slide2_Z/2]) 
    translate(PartL2_chamber_locations[assembly_location])  
        cube([10, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
    
    // Connect the slide chamber lid to the slide chamber
    translate([-Slide2_Y/2-10, -PartL2_lid_locations[assembly_location][1]/2+Walls, 0]) 
    translate(PartL2_lid_locations[assembly_location])  
        cube([10, MINIMUM_WIRE_SIZE, MINIMUM_WIRE_SIZE], center=false);
}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE M - fluor.excitation LED mount ////
/////////////////////////////////////////////////////////////////////////////////

Excit_hole_R = 11;
Excit_XY = 50;
Excit_tube_h = 40;
Excit_focal_depth = 5; // how far below base is focal point 
Vert_tube_h = 30;
PartM_batch = 2; // The printing batch that PartM belongs to
PartM_locations = [[sep, 4*sep, Cam_Zfloat-5*sep], [-Excit_XY*2, 0, Walls/2]];
PartM_rotations = [[0,0,0], [0, 0, 0]];

module ExcitationTube(focal_depth)
{
    cylinder(r = Excit_hole_R+Tube_wall, h = Vert_tube_h+focal_depth*sqrt(2), center = false );
}

module M(){
    translate([0, 0, Walls/2]) Mount(Excit_XY, Excit_XY, thickness = Walls/2, Y_extension=0, link_thickness=Walls*2);
    
    // Add the tubes
    translate([OPTICAL_AXIS_OFFSET_X, 0, 0]) rotate ([0,0,0]) ExcitationTube(0); // Vert_tube
    translate([OPTICAL_AXIS_OFFSET_X, 0, -Excit_focal_depth+Tube_wall]) rotate ([45,0,0]) ExcitationTube(Excit_focal_depth);  
    translate([OPTICAL_AXIS_OFFSET_X, 0, -Excit_focal_depth+Tube_wall]) rotate ([-45,0,0]) ExcitationTube(Excit_focal_depth); 
}

module M_sub(){
	translate([OPTICAL_AXIS_OFFSET_X,0, Vert_tube_h/2]){rotate ([0,0,0]) {cylinder(r = Excit_hole_R, h = Vert_tube_h*2, center = true );}} // Main hole	
	translate([OPTICAL_AXIS_OFFSET_X,0, -Excit_focal_depth-Walls/2+Tube_wall*2*sqrt(2)]){rotate ([45,0,0]) {cylinder(r = Excit_hole_R, h = Excit_tube_h+Excit_focal_depth, center = false );}} // Excit_tube	
	translate([OPTICAL_AXIS_OFFSET_X,0, -Excit_focal_depth-Walls/2+Tube_wall*2*sqrt(2)]){rotate ([-45,0,0]) {cylinder(r = Excit_hole_R, h = Excit_tube_h+Excit_focal_depth, center = false );}} // Excit_tube	
	translate([OPTICAL_AXIS_OFFSET_X,0,-Walls/2-Excit_tube_h]){cube([Excit_hole_R*3,Excit_hole_R*4,Excit_tube_h*2], center = true );} // cut_below
    Mount_link_holes(link_thickness=Walls*2);
}

show_PartM = PartM==1 && (printing_batch_number == PartM_batch || assembly_location == EXPLODED_VIEW);
if (show_PartM){translate(PartM_locations[assembly_location]) rotate(PartM_rotations[assembly_location]) difference(){M();M_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE N - fluor. excitation LED plug //////
/////////////////////////////////////////////////////////////////////////////////

N_Z1 = 3;
N_Z2 = 5; 
PartN_batch = 2; // The printing batch that PartN belongs to
PartN1_locations = [[sep+OPTICAL_AXIS_OFFSET_X, 4*sep-(Excit_hole_R+Tube_wall)*2-5, Cam_Zfloat-3*sep+N_Z1/2], [0, 50, N_Z1*1.5]];
PartN1_rotations = [[0,0,0], [180, 0, 0]];
PartN2_locations = [[sep+OPTICAL_AXIS_OFFSET_X, 4*sep+(Excit_hole_R+Tube_wall)*2+5, Cam_Zfloat-3*sep+N_Z1/2], [0, +(Excit_hole_R+Tube_wall)*2+55, N_Z1*1.5]];
PartN2_rotations = [[0,0,0], [180, 0, 0]];

module N(){
	translate([0,0,N_Z1]) cylinder(r = Excit_hole_R+Tube_wall, h = N_Z1, center = true ); // lid
	cylinder(r = Excit_hole_R-Tol, h = N_Z2, center = true ); // plug	
}
module N_sub(){
	cylinder(r = Excit_hole_R-Tol-Tube_wall, h = N_Z2, center = true ); // plug	
}
show_PartN = PartN==1 && (printing_batch_number == PartN_batch || assembly_location == EXPLODED_VIEW);
if (show_PartN){translate(PartN1_locations[assembly_location]) rotate(PartN1_rotations[assembly_location]) difference(){N();N_sub();}}
if (show_PartN){translate(PartN2_locations[assembly_location]) rotate(PartN2_rotations[assembly_location]) difference(){N();N_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE O - fluor emission filter mount /////
/////////////////////////////////////////////////////////////////////////////////

Emiss_hole_R = 8;
Emiss_Wheel_R = 26.5; //30;
Emiss_pivot_hole_R = 3;
Emiss_wheel_hole_offset = OPTICAL_AXIS_OFFSET_X;
Emiss_pivot_hole_offset =  OPTICAL_AXIS_OFFSET_X + Emiss_Wheel_R/2 + Emiss_hole_R/2;
Emiss_wheel_hole_R = Emiss_hole_R+0.5;
Emiss_wheel_h = 2;
Spacer_R = Emiss_pivot_hole_R+2;
Spacer_Z = 0.5;
Emiss_wheel_peg_Z = 8;

PartO_batch = 2; // The printing batch that PartO belongs to
PartO_filter_wheel_mount_locations = [[sep+Cam_X_offset, 4*sep, Cam_Zfloat-2*sep], [Excit_XY*2, 0, Walls/2]];
PartO_filter_wheel_mount_rotations = [[0,0,0], [180, 0, 180]];
PartO_filter_wheel_locations = [[sep+Cam_X_offset+Emiss_pivot_hole_offset, 4*sep, Cam_Zfloat-1.5*sep], [0, 5, Emiss_wheel_h/2]];
PartO_filter_wheel_rotations = [[0,0,0], [180, 0, 45]];

module filter_wheel()
{
    difference() {
        union() {
            cylinder($fn = 50, r = Emiss_Wheel_R, h = Emiss_wheel_h, center = true ); // Wheel
            translate([0, 0, -Spacer_Z/2-Emiss_wheel_h/2]) cylinder($fn = 50, r = Spacer_R, h = Spacer_Z, center = true ); // Wheel_peg_spacer	
            translate([0, 0, -Emiss_wheel_peg_Z/2])        cylinder($fn = 50, r = Emiss_pivot_hole_R-Tol, h = Emiss_wheel_peg_Z, center = true ); // Wheel_peg
        }
        // Make four holes for the filters
        for ( wheel_hole_angle = [0, 90, 180, 270] ) {
            rotate ([0,0,wheel_hole_angle])  translate([Emiss_Wheel_R*5/8,0,0]) cylinder($fn = 50, r = Emiss_wheel_hole_R, h = Walls, center = true );
        }
    }
}

module filter_wheel_mount()
{
    difference(){
        // The mount is flipped upside down from the "normal" orientation
        rotate([180,0,0]) Mount(Excit_XY, Excit_XY, thickness = Walls/2, Y_extension=0, link_thickness=Walls);

        union() {
            // Make the holes in the mount and link
            translate([Emiss_wheel_hole_offset, 0, 0]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_hole_R, h = Walls*1.5, center = true );}} // Main hole	
            translate([Emiss_pivot_hole_offset, 0, 0]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_pivot_hole_R, h = Walls*1.5, center = true );}} // screw pivot hole	
            Mount_link_holes(link_thickness=Walls);
        }
    }
}

show_PartO = PartO==1 && (printing_batch_number == PartO_batch || assembly_location == EXPLODED_VIEW);
if (show_PartO){
    translate(PartO_filter_wheel_mount_locations[assembly_location]) rotate(PartO_filter_wheel_mount_rotations[assembly_location]) filter_wheel_mount();
    translate(PartO_filter_wheel_locations[assembly_location]) rotate(PartO_filter_wheel_rotations[assembly_location]) filter_wheel();
}

// Connecting parts in batch #2 to the filter wheel
if (connect_parts && show_PartM && show_PartO)  // Connect the LED tube mount to the filter wheel
{
    translate([-Emiss_Wheel_R-18.5, -MINIMUM_WIRE_SIZE/2, -(Emiss_wheel_h)/2]) 
    translate(PartO_filter_wheel_locations[assembly_location])  
        cube([19, MINIMUM_WIRE_SIZE, Emiss_wheel_h], center=false);
}

if (connect_parts && show_PartO)  // Connect the wheel to the filter wheel mount
{
    translate([Emiss_Wheel_R-0.5, -MINIMUM_WIRE_SIZE/2, -(Emiss_wheel_h)/2]) 
    translate(PartO_filter_wheel_locations[assembly_location])  
        cube([19, MINIMUM_WIRE_SIZE, Emiss_wheel_h], center=false);
}

if (connect_parts && show_PartO && show_PartD)  // Connect the wheel to the High Power LED mount
{
    translate([-MINIMUM_WIRE_SIZE/2, -Emiss_Wheel_R-16.5, -(Emiss_wheel_h)/2]) 
    translate(PartO_filter_wheel_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 17, Emiss_wheel_h], center=false);
}

if (connect_parts && show_PartO && show_PartN)  // Connect the wheel to the fluor. excitation LED plugs
{
    translate([-MINIMUM_WIRE_SIZE/2, Emiss_Wheel_R-0.5, -(Emiss_wheel_h)/2]) 
    translate(PartO_filter_wheel_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 8, Emiss_wheel_h], center=false);
    
    translate([-MINIMUM_WIRE_SIZE/2, Emiss_Wheel_R-0.5+(Excit_hole_R+Tube_wall)*2+5, -(Emiss_wheel_h)/2]) 
    translate(PartO_filter_wheel_locations[assembly_location])  
        cube([MINIMUM_WIRE_SIZE, 8, Emiss_wheel_h], center=false);

}

