/////////////////////////////////////////////////////////////////////////////////
/// FlyPi v0.97; 2015 05 27 ///
/// Collaboration Tom Baden, Lucia Prieto Godino and Andre Maia Chagas
/// 3D model by Tom Baden (thingyverse ID: tbaden) ///
/// thomas.baden@uni-tuebingen.de ///
/// tombaden.wordpress.com ///
/////////////////////////////////////////////////////////////////////////////////
//// SWITCHES //////////
PartA = 	0; // Base
PartA1=	0; // Base clamps
PartA2 = 	0; // Feet
PartB= 	    1; // Wall
PartB3=	0; // PCB mount
PartC= 	1; // Cam Mount
PartC1= 	0; // Cam Mount Servo
PartC2= 	0; // Cam Mount Cogwheels
PartC3=    0; // Cam V2 Mount 
PartD= 	0; // High Power LED mount
PartE= 	    0; // angled mounting stick
PartF1= 	0; // straight mounting stick, long
PartF2= 	0; // straight mounting stick, short
PartF3= 	0; // straight mounting stick, long 90°
PartG= 	0; // thumbscrew & manipulator links
PartH= 	0; // AdaFruit 8x8 LED Matrix mount
PartI= 	    0; // Adafruit 12 LED Ring mount
PartJ1= 	0; // Mini Petri dish mount
PartJ2= 	0; // Midi Petri dish mount
PartK= 	0; // Diffusor mount
PartL1= 	0; // microscope slide chamber small
PartL2= 	0; // microscope slide chamber big
PartM= 	0; // Fluorescence Excitation light mount
PartN= 	0; // Fluorescence Exitaton tube plug
PartO= 	0; // Fluorescence Emission mount and wheel

/////////////////////////////////////////////////////////////////////////////////
///// KEY VARIABLES ////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////
sep = 30; // How far apart do pieces "float" in the model
Walls = 5; // Global thickness of all walls
Tol = 0.2; // Global gap between all parts that need to slide

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
C_Z2 = 5; // thickness of cmaera mount walls
C_ridge = 2; // width of ridge for camera mount
Cam_Zfloat = 200; // Module B, max height 
CamGroove_X = 12;
CamGroove_Y = 16.1;
CamGroove2_Y = 24;


/////////////////////////////////////////////////////////////////////////////////
/// MODULE A - base   //////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

A_Base_X = P_XY+P_border*2 + Walls + Sidestand;
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
A1_screw_R = 1.5;
A1_offset = 3;

module A(){
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Base_Z/2]){cube([A_Base_X,A_Base_Y,A_Base_Z], center = true );} // BASE
	translate([-P_XY/2-P_border-Walls/2,A_Base_Y/2-Walls+Tol/2,0]){rotate ([90,0,0]) {cylinder($fn = 50, r = Stabiliser_R, h = Walls*2-Tol, center = true );}} // Support1	
	translate([-P_XY/2-P_border-Walls/2,-A_Base_Y/2+Walls-Tol/2,0]){rotate ([90,0,0]) {cylinder($fn = 50, r = Stabiliser_R, h = Walls*2-Tol, center = true );}} // Support2	
}
module A_sub(){
	translate([0,0,-P_Z/2]){cube([P_XY+2*Tol,P_XY+2*Tol,P_Z], center = true );} // Peltier groove
	translate([-A_Base_Y/4,(P_XY+2*Tol)/2-(P_cable+2*Tol)/2,-P_Z/2]){cube([A_Base_Y,P_cable+2*Tol,P_Z], center = true );} // Peltier cable1
	translate([-A_Base_Y/4,-(P_XY+2*Tol)/2+(P_cable+2*Tol)/2,-P_Z/2]){cube([A_Base_Y,P_cable+2*Tol,P_Z], center = true );} // Peltier cable1
	translate([-A_Base_Y/2,0,-MarkerLED_R-MarkerLED_Z]){rotate ([0,90,0]) {cylinder($fn = 50, r = MarkerLED_R, h = A_Base_Y, center = true );}} // MarkerLed HOLE
	translate([-P_XY/2-MarkerLED_XY/2-1,0,-MarkerLED_Z]){cube([MarkerLED_XY,MarkerLED_XY,2*MarkerLED_Z], center = true );} // MarkerLed opening
	translate([0,0,-A_Base_Z/2]){cube([P_XY-P_ridge*2,P_XY-P_ridge*2,A_Base_Z], center = true );} // Peltier below
	translate([-A_Base_X/2-Walls,0,-A_Base_Z/2]){cube([Sidestand-Walls*3,A_Base_Y-Walls*2,A_Base_Z], center = true );} // Sidestand Hole
	translate([-A_Base_X/2-Walls/2-Walls,0,-A_Base_Z/2+Sidestand_thickness]){cube([Sidestand-Walls*2,A_Base_Y,A_Base_Z], center = true );} // Sidestand Hole shallow
	translate([-P_XY/2-P_border-Walls/2,0,-A_Base_Z/2]){cube([Walls+Tol*2,A_Base_Y-Walls*4,A_Base_Z], center = true );} // Wall_linkhole
	translate([-P_XY/2-P_border-A_Wall_X/2,0,A_Wall_Z/2]){cube([A_Wall_X+Tol*2,A_Wall_Y,A_Wall_Z], center = true );} // Sidestand_slot
	translate([Airhole_spacing,0,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([0,0,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([-Airhole_spacing,0,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([+A_Base_Y/2,0,-A_Base_Z/2]){rotate ([0,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([0,-Airhole_spacing,-A_Base_Z/2]){rotate ([0,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([0,Airhole_spacing,-A_Base_Z/2]){rotate ([0,90,0]) {cylinder(r = Airhole_R, h = A_Base_Y, center = true );}} // Air holes
	translate([-(P_XY/2-A1_offset),P_XY/2+A1_offset,-Walls]){rotate ([0,0,0]) {cylinder($fn=20, r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
	translate([-(P_XY/2-A1_offset),-(P_XY/2+A1_offset),-Walls]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
	translate([(P_XY/2-A1_offset),P_XY/2+A1_offset,-Walls]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
	translate([(P_XY/2-A1_offset),-(P_XY/2+A1_offset),-Walls]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls*2, center = true );}} // screwhole
}
if (PartA==1){difference(){A();A_sub();}}

/////////////////////////////////////////////////////////////////////////////////
//// MODULE A1 - thermistor /Peltier clamps /////
/////////////////////////////////////////////////////////////////////////////////

module A1(){
	translate([P_XY/2-A1_offset,P_XY/2+A1_offset,Walls*2]){cube([A1_offset*2,A1_offset*5,Walls/3], center = true );} // clamp
	translate([P_XY/2-A1_offset,P_XY/2+A1_offset*3,Walls*2-Walls/3]){cube([A1_offset*2,A1_offset,Walls/3], center = true );} // clamp
	translate([P_XY/2-A1_offset,-P_XY/2-A1_offset,Walls*2]){cube([A1_offset*2,A1_offset*5,Walls/3], center = true );} // clamp
	translate([P_XY/2-A1_offset,-P_XY/2-A1_offset*3,Walls*2-Walls/3]){cube([A1_offset*2,A1_offset,Walls/3], center = true );} // clamp
	translate([-P_XY/2+A1_offset,-P_XY/2-A1_offset,Walls*2]){cube([A1_offset*2,A1_offset*5,Walls/3], center = true );} // clamp
	translate([-P_XY/2+A1_offset,-P_XY/2-A1_offset*3,Walls*2-Walls/3]){cube([A1_offset*2,A1_offset,Walls/3], center = true );} // clamp
      translate([-P_XY/2+A1_offset,P_XY/2+A1_offset/4,Walls*2]){cube([A1_offset*2,A1_offset*6.5,Walls/3], center = true );} // Thermistor clamp
	translate([-P_XY/2+A1_offset,P_XY/2+A1_offset*3,7]){cube([A1_offset*2,A1_offset,5], center = true );} // Thermistor clamp footbig
	translate([-P_XY/2+A1_offset,P_XY/2-A1_offset*2.5,Walls*2-Walls/3]){cube([A1_offset*2,A1_offset,Walls/3], center = true );} // clamp
}
module A1_sub(){
	translate([-(P_XY/2-A1_offset),P_XY/2+A1_offset,Walls*2]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls/2, center = true );}} // screwhole
	translate([-(P_XY/2-A1_offset),-(P_XY/2+A1_offset),Walls*2]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls/2, center = true );}} // screwhole
	translate([(P_XY/2-A1_offset),P_XY/2+A1_offset,Walls*2]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls/2, center = true );}} // screwhole
	translate([(P_XY/2-A1_offset),-(P_XY/2+A1_offset),Walls*2]){rotate ([0,0,0]) {cylinder($fn=20,r = A1_screw_R, h = Walls/2, center = true );}} // screwhole
}
if (PartA1==1) {difference(){A1();A1_sub();}}

/////////////////////////////////////////////////////////////////////////////////
/// MODULE A2 - basefeet   /////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

A_Foot_Z = 30;
A_Foot_Groove_Z = 3;
A_Foot_Corners_XY = 10;

module A2(){
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2-sep]){cube([A_Base_X+Walls,A_Base_Y+Walls,A_Foot_Z], center = true );} // Main foot
	
}
module A2_sub(){
	//translate([0,0,-A_Foot_Z/2-sep]){cube([P_XY-P_ridge*2,P_XY-P_ridge*2,A_Foot_Z], center = true );} // Peltier below
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Groove_Z/2-sep]){cube([A_Base_X+Tol,A_Base_Y+Tol,A_Foot_Groove_Z], center = true );} // BASE

	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2-sep]){cube([A_Base_X-Walls,A_Base_Y-Walls,A_Foot_Z], center = true );} // Main Hole
	
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2+Walls/2-sep]){cube([A_Base_X-Walls-A_Foot_Corners_XY,A_Base_Y*2,A_Foot_Z-Walls], center = true );} // CornerCut Hole1
	translate([-A_Base_X/2+P_XY/2+P_border,0,-A_Foot_Z/2+Walls/2-sep]){cube([A_Base_X*2,A_Base_Y-Walls-A_Foot_Corners_XY,A_Foot_Z-Walls], center = true );}  // CornerCut Hole2


}
if (PartA2==1){difference(){A2();A2_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE B - main wall //////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

module B(){
	translate([-P_XY/2-P_border-A_Wall_X/2,0,A_Wall_Z/2+sep]){cube([A_Wall_X,A_Wall_Y,A_Wall_Z], center = true );} // WALL
	translate([-P_XY/2-P_border-A_Wall_X/2,0,A_Wall_Z_long/2+sep]){cube([A_Wall_X,A_Wall_Y_long,A_Wall_Z_long], center = true );} // WALL_extra
	translate([-P_XY/2-P_border-A_Wall_X/2,0,0.5+sep-A_Base_Z/2]){cube([Walls,A_Base_Y-Walls*4-Tol*2,A_Base_Z], center = true );} // WALL_link
	translate([-P_XY/2-P_border-A_Wall_X/2,0,A_Wall_Z+sep-A_Wall_Y/999]){rotate ([0,270,0]) {cylinder($fn = 3, r = A_Wall_Y/2, h = Walls, center = true );}} // WALL_rounding top
}
module B2(){
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h,RPi_holedist_Yb,RPi_groundZ+sep]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_bottom
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h,RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z+sep]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_top
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h,-RPi_holedist_Yb,RPi_groundZ+sep]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_bottom
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h,-RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z+sep]){rotate ([0,90,0]) {cylinder(r = S_mount_R, h = Mount_h, center = true );}} // m hole_top
}
module B_sub(){
	translate([-A_Base_Y/4,(P_XY+2*Tol)/2-(P_cable+2*Tol)/2+P_cable/2,-P_Z/2+sep]){cube([A_Base_Y,P_cable*2+2*Tol,P_Z], center = true );} // Peltier cable1
	translate([-A_Base_Y/4,-(P_XY+2*Tol)/2+(P_cable+2*Tol)/2-P_cable/2,-P_Z/2+sep]){cube([A_Base_Y,P_cable*2+2*Tol,P_Z], center = true );} // Peltier cable2
	translate([-A_Base_Y/4,T_cable_offset,T_cableZ/2+Tol+sep]){cube([A_Base_Y,T_cableY,T_cableZ+2*Tol], center = true );} // thermistor cable
	translate([-A_Base_Y/2,0,-MarkerLED_R-MarkerLED_Z+sep]){rotate ([0,90,0]) {cylinder($fn = 50, r = MarkerLED_R, h = A_Base_Y, center = true );}} // MarkerLed HOLE
	translate([-P_XY/2-P_border-A_Wall_X/2-(Walls-Walls_thinning)/2,0,A_Wall_Z/2+sep]){cube([Walls_thinning,A_Wall_Y-Borders,A_Wall_Z-Borders], center = true );} // Save Material	
}
module B2_sub(){
	translate([-P_XY/2-P_border+Walls-Mount_h,RPi_holedist_Yb,RPi_groundZ+sep]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // m hole_bottom
	translate([-P_XY/2-P_border+Walls-Mount_h,RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z+sep]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // 
	translate([-P_XY/2-P_border+Walls-Mount_h,-RPi_holedist_Yb,RPi_groundZ+sep]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // m hole_bottom
	translate([-P_XY/2-P_border+Walls-Mount_h,-RPi_holedist_Y,RPi_groundZ+RPi_holedist_Z+sep]){rotate ([0,90,0]) {cylinder($fn = 50, r = S_hole_R, h = Mount_h+Walls, center = true );}} // 
}
if (PartB==1){difference(){B();B_sub();}}
if (PartB==1){difference(){B2();B2_sub();}}

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

module B3(){
	translate([-P_XY/2-P_border-Ard_holder_X/2-2*sep,0,RPi_groundZ+sep+Ard_z_extra/2]){cube([Ard_holder_X,Ard_holder_Y,Ard_holder_Z], center = true );} // Holder
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h-2*sep+Mount2_h/2,RPi_holedist_Yb,RPi_groundZ+sep-S_mount_R/2+Foot_Z_extra/2]){cube([Mount2_h,S_mount_R*2,S_mount_R+Foot_Z_extra], center = true );} // foot
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h-2*sep+Mount2_h/2,-RPi_holedist_Yb,RPi_groundZ+sep-S_mount_R/2+Foot_Z_extra/2]){cube([Mount2_h,S_mount_R*2,S_mount_R+Foot_Z_extra], center = true );} // foot
}
module B3_sub(){
	translate([-P_XY/2-P_border-Ard_holder_X/2-2*sep,0,RPi_groundZ+Ard_holder_Z/2-Fritzing_Z_depth/2+sep]){cube([Fritzing_X+Tol,Fritzing_Y+2*Tol,Fritzing_Z_depth+Ard_z_extra], center = true );} // slot
	translate([-P_XY/2-P_border-Ard_holder_X/2-2*sep,0,RPi_groundZ+sep+Ard_holder_Z/2]){cube([Ard_holder_X,Fritzing_Y-2,Ard_z_extra], center = true );} // Holder
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h-2*sep+Mount2_h/2,RPi_holedist_Yb,RPi_groundZ+sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = Mount2_h+5, center = true );}} // m hole_bottom
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h-2*sep+Mount2_h/2,-RPi_holedist_Yb,RPi_groundZ+sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = Mount2_h+5, center = true );}} // m hole_bottom
    translate([-P_XY/2-P_border+1.7*Walls-Mount_h-2*sep+Mount2_h-LShape_Length/2,RPi_holedist_Yb-S_mount_R+LShape_Width/2,RPi_groundZ+sep-S_mount_R/2+Foot_Z_extra/2]){cube([LShape_Length,LShape_Width,S_mount_R+Foot_Z_extra], center = true );} // L-Shape
	translate([-P_XY/2-P_border+1.7*Walls-Mount_h-2*sep+Mount2_h-LShape_Length/2,-RPi_holedist_Yb+S_mount_R-LShape_Width/2,RPi_groundZ+sep-S_mount_R/2+Foot_Z_extra/2]){cube([LShape_Length,LShape_Width,S_mount_R+Foot_Z_extra], center = true );} // L-Shape    
}
if (PartB3==1){difference(){B3();B3_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE C - camera mount /////////////////////////
/////////////////////////////////////////////////////////////////////////////////

MiniGrooveX = 15;

module C(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat+sep]){cube([Cam_X+Walls*2,Cam_Y+Walls*2,Walls*1.5], center = true );} // Cam_mount
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat+sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls*1.5], center = true );} // Cam_link
}
module C_sub(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat+sep+Walls*0.75-C_Z/2]){cube([Cam_X+Tol*2,Cam_Y+Tol*2,C_Z], center = true );} // Cam_hole_ridge
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2,0,Cam_Zfloat+sep+C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cam_cable_groove
	translate([sep+Cam_X_offset+Cam_X/2-MiniGrooveX/2-C_ridge,-Cam_Y/2+C_ridge/2,Cam_Zfloat+sep+C_Z2/2]){cube([MiniGrooveX,C_ridge,C_Z2+Walls/2], center = true );} // mini groove
	translate([sep+Cam_X_offset-Cam_X/2+CamGroove_X/2,0,Cam_Zfloat+sep+C_Z2/2]){cube([CamGroove_X,CamGroove2_Y,C_Z2+Walls/2], center = true );} // Cam_bmup_groove
	translate([sep+Cam_X_offset,0,Cam_Zfloat+sep]){cube([Cam_X-C_ridge*2,Cam_Y-C_ridge*2,Walls*3], center = true );} // Cam_hole
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat+sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // Cam_link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat+sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // screwhole
}
if (PartC==1){difference(){C();C_sub();}}


/////////////////////////////////////////////////////////////////////////////////
///// MODULE C1 - camera mount with servo ////
/////////////////////////////////////////////////////////////////////////////////

Servo_Y = 12.2;
Servo_X = 23.7;
Servo_X_offset = 5.5;
// height of Servo is 29 in total, which is counted from the bottom
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

module C1(){
	translate([sep+Cam_X_offset,-2*sep-Walls/2-Servo_Y/2,Cam_Zfloat+sep]){cube([Cam_X+Walls*2,Cam_Y+Servo_Y+Walls*3,Walls*1.5], center = true );} // Cam_mount
	translate([sep-P_XY/4-P_border/2-Walls,-2*sep,Cam_Zfloat+sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls*1.5], center = true );} // Cam_link

}
module C1_sub(){
	translate([sep+Cam_X_offset,-2*sep,Cam_Zfloat+sep+Walls*0.75-C_Z/2]){cube([Cam_X+Tol*2,Cam_Y+Tol*2,C_Z], center = true );} // Cam_hole_ridge
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2,-2*sep,Cam_Zfloat+sep+C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cam_cable_groove
	translate([sep+Cam_X_offset+Cam_X/2-MiniGrooveX/2-C_ridge,-Cam_Y/2+C_ridge/2-2*sep,Cam_Zfloat+sep+C_Z2/2]){cube([MiniGrooveX,C_ridge,C_Z2+Walls/2], center = true );} // mini groove
	translate([sep+Cam_X_offset-Cam_X/2+CamGroove_X/2,-2*sep,Cam_Zfloat+sep+C_Z2/2]){cube([CamGroove_X,CamGroove2_Y,C_Z2+Walls/2], center = true );} // Cam_bmup_groove
	translate([sep+Cam_X_offset,-2*sep,Cam_Zfloat+sep]){cube([Cam_X-C_ridge*2,Cam_Y-C_ridge*2,Walls*3], center = true );} // Cam_hole
	translate([sep-P_XY/2-P_border-Walls/2,-2*sep,Cam_Zfloat+sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // Cam_link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,-2*sep,Cam_Zfloat+sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // screwhole
      translate([sep+Cam_X_offset-Servo_X_offset,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+sep]){cube([Servo_X+Tol,Servo_Y+Tol,Walls*3], center = true );} // Servo_hole
 translate([sep+Cam_X_offset-Servo_X_offset+Servo_X/2,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+sep]){cylinder( $fn=50, r = 4, h = 100, center = true );} // Servo_cablegroove

}
if (PartC1==1){difference(){C1();C1_sub();}}

module C2(){
      for (i = [0 : cogwheel_nteeth/3]) {
		translate([sep+Cam_X_offset,-2*sep,Cam_Zfloat+2*sep]){rotate ([0,0,(i+0.5)*360/cogwheel_nteeth]) {cylinder($fn = 3, r = cogwheel_R, h = cogwheel_Z, center = true );}} // cogs wheel 1
		translate([sep+Cam_X_offset,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+2*sep]){rotate ([0,0,i*360/cogwheel_nteeth]) {cylinder($fn = 3, r = cogwheel_R, h = cogwheel_Z, center = true );}} // cogs wheel 2
	}
}
module C2_sub(){
	translate([sep+Cam_X_offset,-2*sep,Cam_Zfloat+2*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = cogwheel_R_inner1, h = cogwheel_Z+1, center = true );}} // Cam_cog Lens hole 
	translate([sep+Cam_X_offset,-2*sep,Cam_Zfloat+2*sep+cogwheel_Z2/2+1]){rotate ([0,0,0]) {cylinder($fn = 50, r = cogwheel_R2, h = cogwheel_Z-cogwheel_Z2+1, center = true );}} // Cam_cog main hole
	
	translate([sep+Cam_X_offset,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+2*sep+cogwheel_Z2/2+1]){rotate ([0,0,0]) {cylinder($fn = 50, r = cogwheel_R2, h = cogwheel_Z - cogwheel_Z2+1, center = true );}} // Servo_cog main hole
	translate([sep+Cam_X_offset,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+2*sep]){rotate ([0,0,0]) {cylinder($fn = 12, r = cogwheel_R_inner2, h = cogwheel_Z+1, center = true );}} // Servo_cog mount hole
	translate([sep+Cam_X_offset,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+2*sep-cogwheel_cross_Z/2]){cube([cogwheel_cross_Length,cogwheel_cross_Width,cogwheel_cross_Z], center = true);} // Servo_cog cross1
	translate([sep+Cam_X_offset,-2*sep-Servo_Y/2-Cam_Y/2-Walls,Cam_Zfloat+2*sep-cogwheel_cross_Z/2]){cube([cogwheel_cross_Width,cogwheel_cross_Length,cogwheel_cross_Z], center = true);} // Servo_cog cross2

}
if (PartC2==1){difference(){C2();C2_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE C3 - camera mount /////////////////////////
/////////////////////////////////////////////////////////////////////////////////

MiniGrooveX = 15;

module C3(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat+sep]){cube([Cam_X+Walls*2,Cam_Y+Walls*2,Walls*1.5], center = true );} // Cam_mount
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat+sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls*1.5], center = true );} // Cam_link
}
module C3_sub(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat+sep+Walls*0.75-C_Z/2]){cube([Cam_X+Tol*2,Cam_Y+Tol*2,C_Z], center = true );} // Cam_hole_ridge
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2,0,Cam_Zfloat+sep+C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cam_cable_groove
	translate([sep+Cam_X_offset+Cam_X/2-MiniGrooveX/2-C_ridge,-Cam_Y/2+C_ridge/2,Cam_Zfloat+sep+C_Z2/2]){cube([MiniGrooveX,C_ridge,C_Z2+Walls/2], center = true );} // mini groove
	translate([sep+Cam_X_offset-Cam_X/2+CamGroove_X/2,0,Cam_Zfloat+sep+C_Z2/2]){cube([CamGroove_X,CamGroove2_Y,C_Z2+Walls/2], center = true );} // Cam_bmup_groove
	translate([sep+Cam_X_offset,0,Cam_Zfloat+sep]){cube([Cam_X-C_ridge*2,Cam_Y--1.5,Walls*3], center = true );} // Cam_hole
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat+sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // Cam_link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat+sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // screwhole
}
if (PartC3==1){difference(){C3();C3_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE D - high power LED mount  /////////
/////////////////////////////////////////////////////////////////////////////////

Tube_wall = 1.5;
LED_holder_inside = 35+2*Tol;
LED_holder_outside = 35+2*Tol+2*Walls;
LED_holder_ridge = 3;

module D(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat]){cube([Cam_X+Walls*2,Cam_Y+Walls*2,Walls*1.5], center = true );} // Cam_mount
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls*1.5], center = true );} // Cam_link
}
module D_sub(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat]){cylinder(r = Excit_hole_R+Tube_wall+Tol, h = Walls*2, center = true );} 
	translate([sep+Cam_X_offset,0,Cam_Zfloat+Walls*0.4]){cube([LED_holder_inside,LED_holder_inside,Walls], center = true );} // LED_holder_groove2
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // Cam_link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // screwhole
}
if (PartD==1){difference(){D();D_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE E - angled pillars  //////////////////////////
/////////////////////////////////////////////////////////////////////////////////

E_Y_extra = 35;
E_Z_extra = 40;
E_extra_angle = -40;
E_extra_angle2 = -30;

module E(){
		translate([-P_XY/2-P_border-Walls/2,2*sep,Cam_Zfloat]){cube([3*Walls,A_Wall_Y_long+2*Walls,Walls*1.5], center = true );} // Cam_link
		translate([-P_XY/2-P_border-Walls/2,2*sep+E_Y_extra/2,Cam_Zfloat]){cube([Walls,A_Wall_Y_long+2*Walls+E_Y_extra,Walls*1.5], center = true );} // Arm
            translate([-P_XY/2-P_border-A_Wall_X/2,2*sep+E_Y_extra-sin(E_extra_angle)*E_Z_extra-10,Cam_Zfloat+E_Z_extra/2-5]) {rotate ([E_extra_angle,0,0]) {cube([A_Wall_X,A_Wall_Y_long,E_Z_extra], center = true );}} // W_extra1
		translate([-P_XY/2-P_border-A_Wall_X/2,2*sep+E_Y_extra-15-sin(E_extra_angle2)*E_Z_extra-10,Cam_Zfloat+E_Z_extra/2-3]) {rotate ([E_extra_angle2,0,0]) {cube([A_Wall_X,A_Wall_Y_long*0.6,E_Z_extra], center = true );}} // W_extra2
}
module E_sub(){
	translate([-P_XY/2-P_border-Walls/2,2*sep,Cam_Zfloat]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*10], center = true );} // Cam_link_hole
	translate([-Cam_X/2-CamGroove_X-15,2*sep,Cam_Zfloat]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 100, center = true );}} // screwhole
}
if (PartE==1){difference(){E();E_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE F1 - extra pillar stick 1 //////////////////
/////////////////////////////////////////////////////////////////////////////////

F_Plug_X = 15;
Airhole_R2 = 4;

module F1(){
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep,A_extramount_Z/2+10-A_Base_Z/2]){cube([A_Wall_Y_long,A_Wall_X,A_extramount_Z+20+A_Base_Z], center = true );} // low_mount
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep,-A_Base_Z/2]){cube([A_Wall_Y_long*4,A_Wall_X,A_Base_Z], center = true );} // low_mount
	translate([Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole1
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole2
	translate([-Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole3
}
module F1_sub(){
	translate([Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
	translate([-Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
}
if (PartF1==1){difference(){F1();F1_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE F2 - extra pillar stick 2 (mini)    ////
/////////////////////////////////////////////////////////////////////////////////

Ministick_Z = 15;

module F2(){
	translate([2*sep,-A_Base_Y/2-A_Wall_X/2-sep,Ministick_Z/2-A_Base_Z/2]){cube([A_Wall_Y_long,A_Wall_X,A_Base_Z+Ministick_Z], center = true );} // low_mount
	translate([2*sep,-A_Base_Y/2-A_Wall_X/2-sep,-A_Base_Z/2]){cube([A_Wall_Y_long*4,A_Wall_X,A_Base_Z], center = true );} // low_mount
	translate([2*sep+Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole1
	translate([2*sep,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole2
	translate([2*sep-Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole3
}
module F2_sub(){
	translate([2*sep+Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
	translate([2*sep,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
	translate([2*sep-Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
}
if (PartF2==1){difference(){F2();F2_sub();}}


/////////////////////////////////////////////////////////////////////////////////
///// MODULE F1 - extra pillar stick 1 //////////////////
/////////////////////////////////////////////////////////////////////////////////


module F3(){
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep,A_extramount_Z/2.5+-A_Base_Z]){
        cube([A_Wall_Y_long,A_Wall_X,A_extramount_Z/2], center = true );} // low_mount
    
    translate([0,A_Base_Y/2-A_Wall_X*17,A_extramount_Z/2.5+13-A_Base_Z/2]){
        rotate([90,0,0]){
        cube([A_Wall_Y_long,A_Wall_X,A_extramount_Z/4], center = true );}} // 90°
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep,-A_Base_Z/2]){cube([A_Wall_Y_long*4,A_Wall_X,A_Base_Z], center = true );} // low_mount
	translate([Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole1
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole2
	translate([-Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = F_Plug_X, center = true );}} // Plug hole3
}
module F3_sub(){
	translate([Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
	translate([0,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
	translate([-Airhole_spacing,-A_Base_Y/2-A_Wall_X/2-sep+F_Plug_X/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = F_Plug_X*2, center = true );}} // Air holes
}
if (PartF3==1){difference(){F3();F3_sub();}}

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

module G(){
	translate([Airhole_spacing,A_Base_Y/2+sep+G_Plug_X1/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = G_Plug_X1, center = true );}} // Air holes
	translate([0,A_Base_Y/2+sep+G_Plug_X2/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = G_Plug_X2, center = true );}} // Air holes
	translate([-Airhole_spacing,A_Base_Y/2+sep+G_Plug_X3/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tol, h = G_Plug_X3, center = true );}} // Air holes
	translate([2*sep,2*sep,-A_Base_Z+G_thumb_Z/2]){rotate ([0,0,0]) {cylinder(r = G_thumb_outer, h = G_thumb_Z, center = true );}} // thumbscrew
	translate([2*sep,2*sep,-A_Base_Z+G_thumb_ridge_Z/2]){rotate ([0,0,0]) {cylinder(r = G_thumb_ridge, h = G_thumb_ridge_Z, center = true );}} // thumbscrew
}
module G_sub(){
	translate([Airhole_spacing,A_Base_Y/2+sep+G_Plug_X1/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = G_Plug_X1, center = true );}} // Air holes
	translate([0,A_Base_Y/2+sep+G_Plug_X2/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = G_Plug_X2, center = true );}} // Air holes
	translate([-Airhole_spacing,A_Base_Y/2+sep+G_Plug_X3/2,-A_Base_Z/2]){rotate ([90,90,0]) {cylinder(r = Airhole_R-Tube_wall, h = G_Plug_X3, center = true );}} // Air holes
	translate([2*sep,2*sep,-A_Base_Z+G_thumb_Z/2]){rotate ([0,0,0]) {cylinder(r = G_thumb_inner-3*Tol, h = G_thumb_Z, center = true );}} // thumbtop
	translate([2*sep,2*sep,-A_Base_Z+G_thumb_Z-G_thumb_inner_Z/2]){rotate ([0,0,0]) {cylinder(r = G_thumb_inner+Tol/2, h = G_thumb_inner_Z, center = true );}} // thumbhead
}
if (PartG==1){difference(){G();G_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE H - Adafruit 8x8 Matrix mount /////
/////////////////////////////////////////////////////////////////////////////////

Matrix_XY = 32;
Matrix_screwdistY = 28;
Matrix_screwdistX = 37;
Smini_hole_R = 1;

module H(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-2*sep]){cube([Cam_X+Walls*2,Cam_Y+Walls*2,Walls], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat-2*sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls], center = true );} // LINK
}
module H_sub(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-2*sep]){cube([Matrix_XY+Tol*2,Matrix_XY+Tol*2,Walls], center = true );} // Main hole
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2,0,Cam_Zfloat-2*sep+C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cable_groove
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2-3,0,Cam_Zfloat-2*sep]){rotate ([0,0,0]) {cylinder(r = CamGroove_X/4, h = Walls, center = true );}} // Cable thre
	translate([sep+Matrix_screwdistX/2,Matrix_screwdistY/2,Cam_Zfloat-2*sep]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole1
	translate([sep-Matrix_screwdistX/2,Matrix_screwdistY/2,Cam_Zfloat-2*sep]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole2
	translate([sep+Matrix_screwdistX/2,-Matrix_screwdistY/2,Cam_Zfloat-2*sep]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole3
	translate([sep+-Matrix_screwdistX/2,-Matrix_screwdistY/2,Cam_Zfloat-2*sep]){rotate ([0,0,0]) {cylinder(r = Smini_hole_R, h = 10, center = true );}} // Matrix_screwhole4
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat-2*sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat-2*sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
}
if (PartH==1){difference(){H();H_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE I - Adafruit 16LED ring mount //////
/////////////////////////////////////////////////////////////////////////////////

R_LEDring = 40/2;

module I(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-sep]){cube([Cam_X+Walls*4,Cam_Y+Walls*4,Walls], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat-sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls], center = true );} // LINK
}
module I_sub(){
	translate([sep,0,Cam_Zfloat-sep]){rotate ([0,0,0]) {cylinder(r = R_LEDring-Tol, h = Walls, center = true );}} // Main hole
	translate([sep,0,Cam_Zfloat-sep+1]){rotate ([0,0,0]) {cylinder(r = R_LEDring+Tol, h = Walls, center = true );}} // Main hole
	translate([sep,R_LEDring/2+1.5,Cam_Zfloat-sep+1]){rotate ([0,0,0]) {cylinder(r = R_LEDring/2, h = Walls, center = true );}} // extra sidegrooves1
	translate([sep,-R_LEDring/2-1.5,Cam_Zfloat-sep+1]){rotate ([0,0,0]) {cylinder(r = R_LEDring/2, h = Walls, center = true );}} // extra sidegrooves2
	translate([sep-R_LEDring/2-1.5,0,Cam_Zfloat-sep+1]){rotate ([0,0,0]) {cylinder(r = R_LEDring/2, h = Walls, center = true );}} // extra sidegrooves3
	translate([sep+R_LEDring/2+1.5,0,Cam_Zfloat-sep+1]){rotate ([0,0,0]) {cylinder(r = R_LEDring/2, h = Walls, center = true );}} // extra sidegrooves4
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2,0,Cam_Zfloat-sep+C_Z2/2]){cube([CamGroove_X,CamGroove_Y,C_Z2+Walls/2], center = true );} // Cable_groove
	translate([sep+Cam_X_offset-Cam_X/2-CamGroove_X/2-3,0,Cam_Zfloat-sep]){rotate ([0,0,0]) {cylinder(r = CamGroove_X/4, h = Walls, center = true );}} // Cable thread
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat-sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat-sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
}
if (PartI==1){difference(){I();I_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE J - mini petri dish mount ///////////////
/////////////////////////////////////////////////////////////////////////////////

Petri_R = 35/2; // 
Petri_R_outer = 39/2; // for lid

module J(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-3*sep]){cube([Cam_X+Walls*2,Cam_Y+Walls*2,Walls], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat-3*sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls], center = true );} // LINK
}
module J_sub(){
	translate([sep,0,Cam_Zfloat-3*sep]){rotate ([0,0,0]) {cylinder(r = Petri_R_outer+Tol, h = Walls, center = true );}} // Main hole
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat-3*sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat-3*sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
}
if (PartJ1==1){difference(){J();J_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE J2 - midi petri dish mount /////////////
/////////////////////////////////////////////////////////////////////////////////

Petri2_R = 58.8/2; // 
Petri2_R_outer = 58.8/2; // for lid

module J2(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-4*sep]){cube([Walls+Petri2_R*2,Walls+Petri2_R*2,Walls], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat-4*sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls], center = true );} // LINK
}
module J2_sub(){
	translate([sep,0,Cam_Zfloat-4*sep]){rotate ([0,0,0]) {cylinder(r = Petri2_R+Tol, h = Walls, center = true );}} // Main hole
	translate([sep-P_XY/2-P_border-Walls/2,0,Cam_Zfloat-4*sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*1.5], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat-4*sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
}
if (PartJ2==1){difference(){J2();J2_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE K - diffuser mount /////////////////////////
/////////////////////////////////////////////////////////////////////////////////

Link_Opening = 1;
Diffuser_XY = 45;
Diffuser_XY_inner = 38.5+2*Tol;

module K(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-5*sep]){cube([Diffuser_XY,Diffuser_XY,Walls], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls,0,Cam_Zfloat-5*sep]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls], center = true );} // LINK
}
module K_sub(){
	translate([sep+Cam_X_offset,0,Cam_Zfloat-5*sep]){cube([Diffuser_XY_inner,Diffuser_XY_inner,Walls], center = true );} // Main_hole
	translate([sep-P_XY/2-P_border-Walls/2,-5*Link_Opening,Cam_Zfloat-5*sep]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol+10*Link_Opening,Walls*1.5], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,0,Cam_Zfloat-5*sep]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
}
if (PartK==1){difference(){K();K_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE L1 - small microsc. sl. chamber  //
/////////////////////////////////////////////////////////////////////////////////

Plug_R = 1.5;
Chamber1_Z = 1;
Slide1_Y = 25;
Slide1_X = Slide1_Y+10;
Slide1_Z = 1.5;

module L1(){
	translate([4*sep,0,0]){cube([Slide1_X,Slide1_Y,Chamber1_Z+Slide1_Z], center = true );} // Main 
	translate([4*sep,0,sep]){cube([Slide1_X,Slide1_Y,1], center = true );} // Lid 
	translate([4*sep+Slide1_Y/2+2.5,0,Chamber1_Z+sep]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = Slide1_Z, center = true );}} // Plug 
	translate([4*sep-Slide1_Y/2-2.5,0,Chamber1_Z+sep]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = Slide1_Z, center = true );}} // Plug 
}
module L1_sub(){
	translate([4*sep,0,0]){rotate ([0,0,0]) {cylinder(r = Slide1_Y/2-2, h = Chamber1_Z+Slide1_Z, center = true );}} // Main hole
	translate([4*sep,0,sep]){rotate ([0,0,0]) {cylinder(r = Slide1_Y/2-2, h = Chamber1_Z+Slide1_Z, center = true );}} // Lid hole
      translate([4*sep,0,Chamber1_Z]){cube([Slide1_Y+7*Tol,Slide1_X,Chamber1_Z+Slide1_Z], center = true );} // Lid groove 
	translate([4*sep+Slide1_Y/2+2.5,0,Chamber1_Z/2]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R+Tol, h = Slide1_Z*2, center = true );}} // Plug hole
	translate([4*sep-Slide1_Y/2-2.5,0,Chamber1_Z/2]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R+Tol, h = Slide1_Z*2, center = true );}} // Plug hole
}
if (PartL1==1){difference(){L1();L1_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE L2 - big microsc. sl. chamber  /////
/////////////////////////////////////////////////////////////////////////////////

Chamber2_Z = 1;
Slide2_Y = 50;
Slide2_X = Slide2_Y+10;
Slide2_Z = 1.5;

module L2(){
	translate([6*sep,0,0]){cube([Slide2_X,Slide2_Y,Chamber2_Z+Slide2_Z], center = true );} // Main 
	translate([6*sep,0,sep]){cube([Slide2_X,Slide2_Y,1], center = true );} // Lid 
	translate([6*sep+Slide2_Y/2+2.5,0,Chamber2_Z+sep]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = Slide2_Z, center = true );}} // Plug 
	translate([6*sep-Slide2_Y/2-2.5,0,Chamber2_Z+sep]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R, h = Slide2_Z, center = true );}} // Plug 
}
module L2_sub(){
	translate([6*sep,0,0]){rotate ([0,0,0]) {cylinder(r = Slide2_Y/2-2, h = Chamber2_Z+Slide2_Z, center = true );}} // Main hole
	translate([6*sep,0,sep]){rotate ([0,0,0]) {cylinder(r = Slide2_Y/2-2, h = Chamber2_Z+Slide2_Z, center = true );}} // Lid hole   
	translate([6*sep,0,Chamber2_Z]){cube([Slide2_Y+7*Tol,Slide2_X,Chamber2_Z+Slide2_Z], center = true );} // Lid groove 
	translate([6*sep+Slide2_Y/2+2.5,0,Chamber2_Z/2]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R+Tol, h = Slide2_Z*2, center = true );}} // Plug hole
	translate([6*sep-Slide2_Y/2-2.5,0,Chamber2_Z/2]){rotate ([0,0,0]) {cylinder( $fn = 50, r = Plug_R+Tol, h = Slide2_Z*2, center = true );}} // Plug hole
}
if (PartL2==1){difference(){L2();L2_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE M - fluor.excitation LED mount ////
/////////////////////////////////////////////////////////////////////////////////

Excit_hole_R = 11;
Excit_XY = 50;
Excit_tube_h = 40;
Excit_focal_depth = 5; // how far below base is focal point 
Vert_tube_h = 30;

module M(){
	translate([sep+Cam_X_offset,4*sep,Cam_Zfloat-5*sep-Walls/4]){cube([Excit_XY,Excit_XY,Walls/2], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls,4*sep,Cam_Zfloat-5*sep+Walls/2]){cube([P_XY/2+P_border+2*Walls,A_Wall_Y_long+2*Walls,Walls*2], center = true );} // LINK
	translate([sep,4*sep,Cam_Zfloat-5*sep+Vert_tube_h/2]){rotate ([0,0,0]) {cylinder(r = Excit_hole_R+Tube_wall, h = Vert_tube_h, center = true );}} // Vert_tube
	translate([sep,4*sep,Cam_Zfloat-5*sep-Excit_focal_depth-Walls/2]){rotate ([45,0,0]) {cylinder(r = Excit_hole_R+Tube_wall, h = Excit_tube_h*2, center = true );}} // Excit_tube	
	translate([sep,4*sep,Cam_Zfloat-5*sep-Excit_focal_depth-Walls/2]){rotate ([-45,0,0]) {cylinder(r = Excit_hole_R+Tube_wall, h = Excit_tube_h*2, center = true );}} // Excit_tbe	
}
module M_sub(){
	translate([sep,4*sep,Cam_Zfloat-5*sep+Vert_tube_h/2]){rotate ([0,0,0]) {cylinder(r = Excit_hole_R, h = Vert_tube_h*2, center = true );}} // Main hole	
	translate([sep,4*sep,Cam_Zfloat-5*sep-Excit_focal_depth-Walls/2]){rotate ([45,0,0]) {cylinder(r = Excit_hole_R, h = Excit_tube_h*2, center = true );}} // Excit_tube	
	translate([sep,4*sep,Cam_Zfloat-5*sep-Excit_focal_depth-Walls/2]){rotate ([-45,0,0]) {cylinder(r = Excit_hole_R, h = Excit_tube_h*2, center = true );}} // Excit_tube	
	translate([sep+Cam_X_offset,4*sep,Cam_Zfloat-5*sep-Walls/2-Excit_tube_h]){cube([Excit_XY,Excit_XY*2,Excit_tube_h*2], center = true );} // cut_below
	translate([sep-P_XY/2-P_border-Walls/2,4*sep,Cam_Zfloat-5*sep+Walls]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*3], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,4*sep,Cam_Zfloat-5*sep+Walls/2]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
}
if (PartM==1){difference(){M();M_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE N - fluor. excitation LED plug //////
/////////////////////////////////////////////////////////////////////////////////

N_Z1 = 2;
N_Z2 = 4; 

module N(){
	translate([sep,4*sep,Cam_Zfloat-3*sep+N_Z1/2]){rotate ([0,0,0]) {cylinder(r = Excit_hole_R+Tube_wall, h = N_Z1, center = true );}} // lid
	translate([sep,4*sep,Cam_Zfloat-3*sep-N_Z1/2]){rotate ([0,0,0]) {cylinder(r = Excit_hole_R-Tol, h = N_Z2, center = true );}} // plug	
}
module N_sub(){
	translate([sep,4*sep,Cam_Zfloat-3*sep-N_Z1/2]){rotate ([0,0,0]) {cylinder(r = Excit_hole_R-Tol-Tube_wall, h = N_Z2, center = true );}} // plug	
}
if (PartN==1){difference(){N();N_sub();}}

/////////////////////////////////////////////////////////////////////////////////
///// MODULE O - fluor emission filter mount /////
/////////////////////////////////////////////////////////////////////////////////

Emiss_hole_R = 8.5;
Emiss_Wheel_R = 30;
Emiss_pivot_hole_R = 3;
Emiss_pivot_hole_offset = 15;
Emiss_wheel_hole_R = Emiss_hole_R+0.5;
Emiss_wheel_h = 1;
Spacer_Z = 0.5;
Emiss_wheel_peg_Z = 8;

module O(){
	translate([sep+Cam_X_offset,4*sep,Cam_Zfloat-6*sep-Walls/4]){cube([Excit_XY,Excit_XY,Walls/2], center = true );} // Main
	translate([sep-P_XY/4-P_border/2-Walls*2,4*sep,Cam_Zfloat-6*sep-Walls/2]){cube([P_XY/2+P_border,A_Wall_Y_long+2*Walls,Walls], center = true );} // LINK
	translate([sep,4*sep+Emiss_pivot_hole_offset,Cam_Zfloat-5.5*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_Wheel_R, h = Emiss_wheel_h, center = true );}} // Wheel
	translate([sep,4*sep+Emiss_pivot_hole_offset,Cam_Zfloat-5.5*sep-Spacer_Z/2-Emiss_wheel_h/2]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_pivot_hole_R+1, h = Spacer_Z, center = true );}} // Wheel_peg_spacer	
	translate([sep,4*sep+Emiss_pivot_hole_offset,Cam_Zfloat-5.5*sep-Emiss_wheel_peg_Z/2]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_pivot_hole_R-Tol, h = Emiss_wheel_peg_Z, center = true );}} // Wheel_peg		
	


}
module O_sub(){
	translate([sep,4*sep,Cam_Zfloat-6*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_hole_R, h = Walls, center = true );}} // Main hole	
	translate([sep,4*sep+Emiss_pivot_hole_offset,Cam_Zfloat-6*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_pivot_hole_R, h = Walls, center = true );}} // screw pivot hole	
	translate([sep-P_XY/2-P_border-Walls/2,4*sep,Cam_Zfloat-6*sep-Walls]){cube([Walls+Tol*2,A_Wall_Y_long+2*Tol,Walls*3], center = true );} // link_hole
	translate([sep-Cam_X/2-CamGroove_X-15,4*sep,Cam_Zfloat-6*sep-Walls/2]){rotate ([0,90,0]) {cylinder(r = S_hole_R, h = 20, center = true );}} // link_screwhole
	translate([sep,4*sep,Cam_Zfloat-5.5*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_wheel_hole_R, h = Walls, center = true );}} // Wheel hole 1	
      translate([sep,4*sep+Emiss_pivot_hole_offset*2,Cam_Zfloat-5.5*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_wheel_hole_R, h = Walls, center = true );}} // Wheel hole 2
      translate([sep-Emiss_pivot_hole_offset,4*sep+Emiss_pivot_hole_offset,Cam_Zfloat-5.5*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_wheel_hole_R, h = Walls, center = true );}} // Wheel hole 3
      translate([sep+Emiss_pivot_hole_offset,4*sep+Emiss_pivot_hole_offset,Cam_Zfloat-5.5*sep]){rotate ([0,0,0]) {cylinder($fn = 50, r = Emiss_wheel_hole_R, h = Walls, center = true );}} // Wheel hole 4
}
if (PartO==1){difference(){O();O_sub();}}
