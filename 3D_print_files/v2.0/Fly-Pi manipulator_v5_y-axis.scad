/// PARAMETERS FOR THE CUSTOMIZER

wall = 3;

X_range = 44; // Length(70) - B_X(20) - 2*wall(6) = 44
Y_range = 35; // Width(70) - C_Y(23) - 4*wall(12) = 38
Z_range = 30; // C_Topheight(40) - D_Z(12) - 2*Wall(6) = 22


Sliding_Gap = 0.1;


Separation_of_pieces = 20; // 

Radius_of_holes = 2.1;
Width_of_boat_slids = 7.4;
Height_of_boat_slids = 3.2;


AFlag=0;
BFlag=0;

CFlag=1;
DFlag=0;
EFlag=0;
E1Flag=0;
KFlag=0;
K1Flag=0;
MFlag=0;
M1Flag=0;

///////////////////////// NOT FOR CUSTOMIZER BELOW HERE

module SEPARATION_OF_CUSTOMIZER_VARIABLES(){
}

sep = Separation_of_pieces; // seperation of pieces
gap = Sliding_Gap; // sliding space //

A_X = X_range+20+2*wall;
A_Y = Y_range+23+4*wall;
A_Z = 15; // 2 mm higher than before
A_Z_lower = 9.5;

A_extrawall = 1; // extra thickness of bottom layer walls
A_beams_Z = 2; // height of support beams

R_main = Radius_of_holes;
R_main_extra = 0.2; // extra radius for non-guiding holes
R_main_head = 4; // radius of screw head for part C
R_knob_in = 4.2; // Radius of Hex boats // M4

R_hex_small = 3.1;// Radius of Hex boats /7 M3
R_screw_small = 1.8; 
R_screw_mini = 1; 
Boatslot_small_height = 3;


Boatslot_width = Width_of_boat_slids; // how wide so that an M4 doesnt rotate?
Boatslot_height = Height_of_boat_slids; // how thick is an M4 boat?


////////////////////////////
//// BOTTOM PART (A)	///////
////////////////////////////
Cam_link = 10;

A_Base_Z = 19;
Airhole_R = 6;
Airhole_R2 = 4;
Airhole_spacing = 13;
Groud_clearance = ((A_Base_Z - Airhole_R*2)/2)/2;

/*
module A_base(){
	translate([0,0,-A_Z_lower])cube([A_X+A_extrawall*2,A_Y+A_extrawall*2,A_Z], center = true);
	translate([0,A_Y/2+A_extrawall+Cam_link/2,-A_Z_lower+Groud_clearance/2])cube([A_X+A_extrawall*2,Cam_link,A_Z+Groud_clearance], center = true);
//translate([-Airhole_spacing,A_Y/2+A_extrawall+Cam_link/2,-A_Z_lower])cube([Cam_link,Cam_link,A_Z], center = true);
}



	

module A_basehole(){
	translate([0,0,-A_Z_lower])cube([A_X-wall*2,A_Y-wall*2,A_Z], center = true);
	translate([0,0,A_Z-13-A_Z_lower]){rotate ([90,0,90]) {cylinder($fn = 50, r = R_main, h = A_X+1+2*A_extrawall, center = true);}} // hole
	translate([0,A_Y/2-wall,A_Z/2-A_Z_lower]){rotate ([90,-15,90]){cylinder($fn = 3, r = wall, h = A_X-2*wall, center = true);}} // slope1
	translate([0,-A_Y/2+wall,A_Z/2-A_Z_lower]){rotate ([90,195,90]){cylinder($fn = 3, r = wall, h = A_X-2*wall, center = true);}} // slope2

	translate([-A_X/2+wall-Boatslot_small_height/2,-M_axis_offset+M_width/2+2*M_wall,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 6, r = R_hex_small, h = Boatslot_small_height, center = true);}} // screwholeHex3
	translate([-A_X/2+wall-Boatslot_small_height/2,-M_axis_offset-M_width/2-2*M_wall,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 6, r = R_hex_small, h = Boatslot_small_height, center = true);}} // screwholeHex4
	translate([-A_X/2+wall/2,-M_axis_offset+M_width/2+2*M_wall,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*wall, center = true);}} // screwhole3
	translate([-A_X/2+wall/2,-M_axis_offset-M_width/2-2*M_wall,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*wall, center = true);}} // screwhole4

	translate([-Airhole_spacing*2,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = Cam_link, center = true );}} // BigLink hole1	
	translate([-Airhole_spacing,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = Cam_link, center = true );}} // BigLink hole2
	translate([0,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = Cam_link, center = true );}} // BigLink hole3
	translate([Airhole_spacing,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = Cam_link, center = true );}} // BigLink hole4
	translate([Airhole_spacing*2,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R, h = Cam_link, center = true );}} // BigLink hole5
	
	translate([-Airhole_spacing*2,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R2, h = Cam_link*2, center = true );}} // BigLink hole1	
	translate([-Airhole_spacing,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R2, h = Cam_link*2, center = true );}} // BigLink hole2
	translate([0,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R2, h = Cam_link*2, center = true );}} // BigLink hole3
	translate([Airhole_spacing,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R2, h = Cam_link*2, center = true );}} // BigLink hole4
	translate([Airhole_spacing*2,A_Y/2+A_extrawall+Cam_link/2,-A_Base_Z/2+Groud_clearance]){rotate ([90,90,0]) {cylinder(r = Airhole_R2, h = Cam_link*2, center = true );}} // BigLink hole5



}
module A_base_beams(){
	translate([0,A_Y/6,-A_Z/2+A_beams_Z/2-A_Z_lower]){cube([A_X,wall,A_beams_Z], center = true);}
	translate([0,-A_Y/6,-A_Z/2+A_beams_Z/2-A_Z_lower]){cube([A_X,wall,A_beams_Z], center = true);}
	translate([A_X/6,0,-A_Z/2+A_beams_Z/2-A_Z_lower]){cube([wall,A_Y,A_beams_Z], center = true);}
	translate([-A_X/6,0,-A_Z/2+A_beams_Z/2-A_Z_lower]){cube([wall,A_Y,A_beams_Z], center = true);}
	translate([A_X/2-wall*2.5,A_Y/2-wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cube([wall*3,wall*3,A_beams_Z], center = true);} // corner1
	translate([-A_X/2+wall*2.5,A_Y/2-wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cube([wall*3,wall*3,A_beams_Z], center = true);} // corner2
	translate([A_X/2-wall*2.5,-A_Y/2+wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cube([wall*3,wall*3,A_beams_Z], center = true);} // corner3
	translate([-A_X/2+wall*2.5,-A_Y/2+wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cube([wall*3,wall*3,A_beams_Z], center = true);} // corner4


}
module A_base_beams_holes(){
	translate([A_X/2-wall*2.5,A_Y/2-wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cylinder($fn = 50, r = R_main, h = A_beams_Z+1, center = true);} // cornerhole1
	translate([-A_X/2+wall*2.5,A_Y/2-wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cylinder($fn = 50, r = R_main, h = A_beams_Z+1, center = true);} // cornerhole2
	translate([A_X/2-wall*2.5,-A_Y/2+wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cylinder($fn = 50, r = R_main, h = A_beams_Z+1, center = true);} // cornerhole3
	translate([-A_X/2+wall*2.5,-A_Y/2+wall*2.5,-A_Z/2-A_Z_lower+A_beams_Z/2]){cylinder($fn = 50, r = R_main, h = A_beams_Z+1, center = true);} // cornerhole4
}

if (AFlag==1){
difference(){A_base();A_basehole();}
difference(){A_base_beams();A_base_beams_holes();}
}

*/
//////////////////////////////
//// MIDDLE PART (B) /////////
//////////////////////////////
B_Y = A_Y -2*wall-2*gap;
B_X = 20;
B_Z = 23;
B_beam_Z = 6; 
/*
module B_base(){
	translate([0,0,sep]){cube([B_X,B_Y,B_Z], center = true);}
	translate([0,A_Y/2-wall,sep-B_Z/2+8+gap]){rotate([90,-15,90]){cylinder($fn = 3, r = wall, h = B_X, center = true);}} // slope1
	translate([0,-A_Y/2+wall,sep-B_Z/2+8+gap]){rotate ([90,195,90]){cylinder($fn = 3, r = wall, h = B_X, center = true);}} // slope2
// 9.75 changed to 8.75 in z translate for slope - fits better - but why? there must be a bug somewhere
}
module B_basehole(){
	translate([0,0,sep]){cube([B_X-2*wall,B_Y-2*wall,B_Z], center = true);}
	translate([0,0,sep-B_Z/2+3.25]){rotate ([90,0,90]){cylinder($fn = 50, r = R_main+R_main_extra, h = A_X+1, center = true);}} //lower holes
	translate([0,0,sep+B_Z/4]){rotate ([90,0,0]){cylinder($fn = 50, r = R_main, h = A_X+1, center = true);}} // upper holes
	translate([B_X/2-wall,0,B_Z/2+sep]){rotate ([90,-15,0]){cylinder($fn = 3, r = wall, h = B_Y-2*wall, center = true);}} // slope3
	translate([-B_X/2+wall,0,B_Z/2+sep]){rotate ([90,195,0]){cylinder($fn = 3, r = wall, h = B_Y-2*wall, center = true);}} // slope4
	//translate([0,-B_Y/2+10,sep+B_Z/4]){rotate ([90,0,90]){cylinder($fn = 50, r = R_screw_small, h = B_X+1, center = true);}} // MMount holes
	translate([0,-B_Y/2+10,sep+B_Z/4]){rotate ([90,0,90]){cylinder($fn = 6, r = R_hex_small, h = B_X+1, center = true);}} // MMount hexholes
}

module B_base_hexslot(){translate([0,0,sep-B_Z/2+B_beam_Z/2]){cube([B_X-2*wall,10,B_beam_Z], center = true);}}
module B_basehole2(){
	translate([0,0,sep-B_Z/2+3.25]){rotate ([90,0,90]){cylinder($fn = 50, r = R_main+R_main_extra, h = A_X+1, center = true);}} // lower holes inner
	translate([-B_X/2+Boatslot_height/2+wall,0,sep-B_Z/2+B_beam_Z/2]){cube([Boatslot_height,Boatslot_width,B_beam_Z], center = true);} //boat1
	translate([B_X/2-Boatslot_height/1.34-wall,0,sep-B_Z/2+B_beam_Z/2]){cube([Boatslot_height*1.1,Boatslot_width,B_beam_Z], center = true);} //boat2 - 10% wider
}

if(BFlag==1){

difference(){B_base();B_basehole();}

difference(){B_base_hexslot();B_basehole2();}
}
*/
//////////////////////////////
// TOP PART (C) ///////////////
//////////////////////////////
C_Y = 23;
C_X = B_X-2*(wall+gap);
C_Z_bottom = 12;
D_Z = 10;
D_Z_extra = 5;
C_Z_top = Z_range + 2*wall + D_Z + D_Z_extra;
C_Z = C_Z_bottom + C_Z_top;


module C_base(){
	translate([0,0,2*sep+C_Z/2]){cube([B_X,C_Y,C_Z_top], center = true);} // upper
	translate([0,0,2*sep]){cube([C_X,C_Y,C_Z_bottom], center = true);} // lower
	translate([B_X/2-wall,0,B_Z/4+gap+2*sep-0.5]){rotate ([90,-15,0]){cylinder($fn = 3, r = wall, h = C_Y, center = true);}} // slope3
	translate([-B_X/2+wall,0,B_Z/4+gap+2*sep-0.5]){rotate ([90,195,0]){cylinder($fn = 3, r = wall, h = C_Y, center = true);}} // slope4
}
module C_basehole(){
	translate([0,0,2*sep+C_Z/2]){cube([B_X-2*wall,C_Y,C_Z_top-2*wall+2*gap], center = true);} // top hole
	translate([0,0,2*sep+C_Z_bottom/2 + C_Z_top/2]){rotate ([0,0,0]){cylinder($fn = 50, r = R_main, h = C_Z_top+3, center = true);}} // vertical hole
	translate([0,0,2*sep]){rotate ([0,0,0]){cylinder($fn = 50, r = R_main_head, h = C_Z_bottom, center = true);}} // vertical hole from bottom

	translate([0,0,2*sep]){rotate ([90,0,0]){cylinder($fn = 50, r = R_main+R_main_extra, h = A_X+1, center = true);}} // lower hole
	translate([0,-C_Y/2+Boatslot_height/2+wall,2*sep]){cube([Boatslot_width,Boatslot_height,C_Z_bottom], center = true);} // boat1
	translate([0,C_Y/2-Boatslot_height/2-wall,2*sep]){cube([Boatslot_width,Boatslot_height*1.1,C_Z_bottom], center = true);} // boat2 - 10% wider
	translate([B_X/2-wall,+C_Y/2,2*sep+C_Z_bottom+C_Z_top/2-2*wall]){
		rotate ([0,0,15]){cylinder($fn = 3, r = wall, h = C_Z_top-2*wall, center = true);}} //slope5
	translate([-B_X/2+wall,+C_Y/2,2*sep+C_Z_bottom+C_Z_top/2-2*wall]){
		rotate ([0,0,-75]){cylinder($fn = 3, r = wall, h = C_Z_top-2*wall, center = true);}} // slope6 

	translate([0,0,2*sep+C_Z-C_Z_bottom/2-10]){rotate ([90,0,90]){cylinder($fn = 6, r = R_hex_small, h = B_X+1, center = true);}} // MMount hexholes

}

if(CFlag==1){
difference(){C_base();C_basehole();}
}

//////////////////////////////
// TOP DRIVE INSET (D) ///////
//////////////////////////////
/*
D_X = C_X; 
D_Y = C_Y;
D_X_holder = 20;
D_Y_holder = 25;
D_Y_holder_slid = 4;
D_Z_holder_slid = 1;

module D_base(){
	translate([0,2*sep,2*sep+C_Z/2]){cube([D_X,D_Y,D_Z+D_Z_extra], center = true);} // axis
	translate([B_X/2-wall,2*sep+D_Y/2+gap,2*sep+C_Z/2]){rotate ([0,0,15]){cylinder($fn = 3, r = wall, h = D_Z+D_Z_extra, center = true);}} // slope5
	translate([-B_X/2+wall,2*sep+D_Y/2+gap,2*sep+C_Z/2]){rotate ([0,0,-75]){cylinder($fn = 3, r = wall, h = D_Z+D_Z_extra, center = true);}} // slope6
	translate([D_X_holder/2-D_X/2-wall,2*sep+D_Y/2+D_Y_holder/2+3,2*sep+C_Z/2]){cube([D_X_holder,D_Y_holder,D_Z], center = true);} // holder part
	translate([D_X_holder/2-D_X/2-wall,2*sep+1.5+D_Y_holder/2,2*sep+C_Z/2]){cube([D_X_holder,3,D_Z+D_Z_extra], center = true);} // extra thick holder part1
	translate([0,2*sep+1,2*sep+C_Z/2]){cube([D_X,D_Y+2,D_Z+D_Z_extra], center = true);} // extra thick holder part2

}
module D_basehole(){
	translate([0,2*sep+D_Y/2-C_Y/2,2*sep+C_Z/2+2*wall]){rotate ([0,0,0]){cylinder($fn = 50, r = R_main+R_main_extra, h = C_Z_top+1, center = true);}} // vertical hole
	translate([0,2*sep,2*sep+C_Z/2]){cube([Boatslot_width,50,Boatslot_height], center = true );}
	translate([D_X_holder/2-D_X/2-wall,2*sep+D_Y/2+D_Y_holder/2+3,2*sep+C_Z/2]){cube([D_X_holder,D_Y_holder,D_Z_holder_slid+Sliding_Gap], center = true);} // holder part


}


if(DFlag==1){
difference(){D_base();D_basehole();}
}


//////////////////////////////
// Electrode holder (E1) ///////
//////////////////////////////

E1_plugdepth = 5;
E1_Wall = 3;

E1_Z = 10;
E1_Z_extra = 12;
E1_X_extra = 2 + D_Y_holder_slid + wall*2;
E1_Y = 15;


E1_gap_X = D_Y_holder_slid;

module E1_base(){
	translate([0,-2*sep+E1_plugdepth/2,2*sep+C_Z/2]){cube([Boatslot_width-gap,E1_plugdepth,Boatslot_height-gap], center = true );} // plug
	translate([0,-2*sep-E1_plugdepth/2+E1_Wall/2,2*sep+C_Z/2-E1_Z_extra/2]){cube([B_X,E1_Wall,E1_Z+E1_Z_extra], center = true );} // EndWall
	translate([-E1_X_extra/2-B_X/2,-2*sep-E1_plugdepth/2+E1_Wall/2,2*sep+C_Z/2-E1_Z_extra]){cube([E1_X_extra,E1_Wall,E1_Z], center = true );} // EndWall_link_left
	translate([E1_X_extra/2+B_X/2,-2*sep-E1_plugdepth/2+E1_Wall/2,2*sep+C_Z/2-E1_Z_extra]){cube([E1_X_extra,E1_Wall,E1_Z], center = true );} // EndWall_link_right
	translate([-E1_X_extra-B_X/2+wall/2,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){cube([wall,E1_Y,E1_Z], center = true );} // outer_arm_left
	translate([E1_X_extra+B_X/2-wall/2,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){cube([wall,E1_Y,E1_Z], center = true );} // outer_arm_right
	translate([-E1_X_extra-B_X/2+wall/2+wall+D_Y_holder_slid,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){cube([wall,E1_Y,E1_Z], center = true );} // inner_arm_left
	translate([E1_X_extra+B_X/2-wall/2-wall-D_Y_holder_slid,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){cube([wall,E1_Y,E1_Z], center = true );} // inner_arm_right


	translate([-E1_X_extra-B_X/2+wall/2,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 50, r = E1_Z/2, h = wall, center = true);}} // Round_inner_left
	translate([E1_X_extra+B_X/2-wall/2,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 50, r = E1_Z/2, h = wall, center = true);}} // Round_inner_right
	translate([-E1_X_extra-B_X/2+wall/2+wall+D_Y_holder_slid,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 50, r = E1_Z/2, h = wall, center = true);}} // Round_outer_left
	translate([E1_X_extra+B_X/2-wall/2-wall-D_Y_holder_slid,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 50, r = E1_Z/2, h = wall, center = true);}} // Round_outer_right
}


module E1_basehole(){
	translate([-E1_X_extra-B_X/2,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 50, r = R_main+R_main_extra, h = 20, center = true);}} // outer_hole_left
	translate([E1_X_extra+B_X/2,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 50, r = R_main+R_main_extra, h = 20, center = true);}} // outer_hole_right

	translate([-E1_X_extra-B_X/2+wall*2+1+D_Y_holder_slid,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 6, r = Width_of_boat_slids/2, h = 2*wall, center = true);}} // hex_left
	translate([E1_X_extra+B_X/2-wall*2-1-D_Y_holder_slid,-2*sep-E1_plugdepth/2+E1_Wall/2+E1_Y/2+E1_Y/2,2*sep+C_Z/2-E1_Z_extra]){rotate ([0,90,0]){cylinder($fn = 6, r = Width_of_boat_slids/2, h = 2*wall, center = true);}} // hex_right


	
}


if (E1Flag==1){
difference(){E1_base();E1_basehole();}
}

//////////////////////////////
// Electrode holder (E) ///////
//////////////////////////////

E_Z_link = D_Z;
E_X_link = 15;
E_Z_platform = 25;
E_Y_platform = 20; 
E_X_side = 15;

module E_link(){
	translate([2*sep+E_X_link/2,2*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2]){cube([E_X_link,D_Y_holder_slid-2*gap,E_Z_link], center = true);} // holder
	translate([2*sep+E_X_link,2*sep+D_Y/2+D_Y_holder/2+E_Y_platform/2-D_Y_holder_slid/2+gap,2*sep+C_Z/2]){
		cube([wall,E_Y_platform,E_Z_platform], center = true);} // bottom platform
	translate([2*sep+E_X_link+E_X_side/2,2*sep+D_Y/2+D_Y_holder/2+gap,2*sep+C_Z/2]){
		cube([E_X_side,D_Y_holder_slid,E_Z_platform], center = true);} // side1
	translate([2*sep+E_X_link+E_X_side/2+wall/4+gap/2,3.5*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2]){
		cube([E_X_side-wall/2-gap,D_Y_holder_slid,E_Z_platform], center = true);} // side2
}
module E_link_hole(){
	translate([2*sep+5,2*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2]){rotate ([90,0,0]){cylinder($fn = 50, r = R_main, h = D_Y_holder+1, center = true);}} // slid hole
	translate([2*sep,2*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2+E_Z_link/2]){rotate ([90,0,0]){
		cylinder($fn = 3, r = R_main*2.5, h = D_Y_holder+1, center = true);}} // edge top
	translate([2*sep,2*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2-E_Z_link/2]){rotate ([90,0,0]){
		cylinder($fn = 3, r = R_main*2.5, h = D_Y_holder+1, center = true);}} // edge bottom}
	translate([2*sep+E_X_link+E_X_side-wall-R_knob_in/2,2*sep+D_Y/2+D_Y_holder/2-wall/2,2*sep+C_Z/2+E_Z_platform/4]){
		rotate ([90,30,0]){cylinder($fn = 6, r = R_hex_small, h = wall, center = true);}}  //platform hexhole top
	translate([2*sep+E_X_link+E_X_side-wall-R_knob_in/2,2*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2+E_Z_platform/4]){
		rotate ([90,30,0]){cylinder($fn = 6, r = R_hex_small-0.6, h = wall*2, center = true);}}  //platform hexhole top_thinning
	translate([2*sep+E_X_link+E_X_side-wall-R_knob_in/2,3.5*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2+E_Z_platform/4]){
		rotate ([90,0,0]){cylinder($fn = 50, r = R_screw_small, h = wall*2, center = true);}} // platform roundhole top
	translate([2*sep+E_X_link+E_X_side-wall-R_knob_in/2,2*sep+D_Y/2+D_Y_holder/2-wall/2,2*sep+C_Z/2-E_Z_platform/4]){
		rotate ([90,30,0]){cylinder($fn = 6, r = R_hex_small, h = wall, center = true);}} // platformhexhole bottom
	translate([2*sep+E_X_link+E_X_side-wall-R_knob_in/2,2*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2-E_Z_platform/4]){
		rotate ([90,30,0]){cylinder($fn = 6, r = R_hex_small-0.6, h = wall*2, center = true);}} // platformhexhole bottom_thinning
	translate([2*sep+E_X_link+E_X_side-wall-R_knob_in/2,3.5*sep+D_Y/2+D_Y_holder/2,2*sep+C_Z/2-E_Z_platform/4]){
		rotate ([90,0,0]){cylinder($fn = 50, r = R_screw_small, h = wall*2, center = true);}} // platform roundhole bottom
}


if (EFlag==1){
difference(){E_link();E_link_hole();}
}

/////////////////////////////////////////
////// MANUAL KNOB (K1) ////////////////
////////////////////////////////////////

K_Z = 14;
K_hole_Z = 10;
R_knob = 6;

R_knobgroove = 4;
R_knobhead = 9; // only if dont use motors

K_groove_width = 4.5;//4.5;
K_groove_depth = 4.5;//4.5;
K_groove_length = 20;

module knob(){
	translate([-sep-A_X*0.67,-sep-A_Y*0.67,-A_Z_lower]){cylinder($fn = 50, r = R_knob, h = K_Z, center = true);}// knob itself
	translate([-sep-A_X*0.67,-sep-A_Y*0.67,-A_Z_lower+K_Z-K_groove_depth/2]){cylinder($fn = 8, r = R_knobhead, h = K_Z+K_groove_depth, center = true);} // head
} 

module knobhole(){
	translate([-sep-A_X*0.67,-sep-A_Y*0.67,-K_Z/2+K_hole_Z/2-A_Z_lower]){cylinder($fn = 6, r = R_knob_in, h = K_hole_Z, center = true);} // hexgroove in bottom

}

if(K1Flag==1){
difference(){knob();knobhole();}
}


/////////////////////////////////////////
////// MOTOR KNOB (K1) ////////////////
////////////////////////////////////////

module knob2(){
	translate([-sep-A_X*0.67,-2*sep-A_Y*0.67,-A_Z_lower]){cylinder($fn = 50, r = R_knob, h = K_Z, center = true);}// knob itself
} 

module knobhole2(){
	translate([-sep-A_X*0.67,-2*sep-A_Y*0.67,-K_Z/2+K_hole_Z/2-A_Z_lower]){cylinder($fn = 6, r = R_knob_in, h = K_hole_Z, center = true);} // hexgroove in bottom
	translate([-sep-A_X*0.67,-2*sep-A_Y*0.67,-A_Z_lower+K_Z/2-K_groove_depth/2]){cylinder($fn = 50, r = R_knobgroove, h = K_groove_depth, center = true);} // groundgroove in top
	translate([-sep-A_X*0.67,-2*sep-A_Y*0.67,-A_Z_lower+K_Z/2-K_groove_depth/2]){cube([K_groove_length,K_groove_width,K_groove_depth], center = true);} // groove 1
	translate([-sep-A_X*0.67,-2*sep-A_Y*0.67,-A_Z_lower+K_Z/2-K_groove_depth/2]){cube([K_groove_width,K_groove_length,K_groove_depth], center = true);} // groove 2

}

if (KFlag==1){
difference(){knob2();knobhole2();}
}


///////////////////////////////////////
/// MOTOR MOUNT Bottom (M1) ///////////
///////////////////////////////////////

M_wall = 2;
M_height = 12.6+2*M_wall+2*gap;
M_width = 23.7+2*M_wall+2*gap;
M_depth = 6;
M_linklength = 18;
M_linkheight = 10;
M_linkplate1_width = M_width+18;
M_linkplate2_width = M_width+6;
M_axis_offset = 4.8 + gap; // distance of motor axis from center of long axis
module M1_base(){
	translate([-sep-A_X,-M_axis_offset,M_height/2-A_Z/2+(A_Z-13)/2-A_Z_lower]){cube([M_depth,M_width,M_height+A_Z-13], center = true);} // chassis
	translate([-sep+M_linklength/2+M_depth/2-A_X,-M_axis_offset,M_linkheight/2-A_Z/2+(A_Z-13)/2-A_Z_lower]){
		cube([M_linklength,M_width,M_linkheight+A_Z-13], center = true);}// link
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset,-A_Z_lower]){
		cube([M_wall,M_linkplate1_width,A_Z], center = true);} // linkplate 1
	translate([-sep-M_depth/2+M_wall/2-A_X,-M_axis_offset,M_height/2-A_Z/2+(A_Z-13)/2-A_Z_lower]){
		cube([M_wall,M_linkplate2_width,M_height+A_Z-13], center = true);} // linkplate 2
}
module M1_hole(){
	translate([-sep-A_X,-M_axis_offset,-A_Z_lower+(A_Z-13)]){cube([M_depth,M_width-2*M_wall+2*gap,M_height-2*M_wall+2*gap], center = true);}
	translate([-sep-A_X,-M_axis_offset,-A_Z_lower+A_Z]){cube([M_depth,M_linkplate1_width,A_Z], center = true);} // cut away top
	translate([-sep+M_linklength/2+M_depth/2-A_X,-M_axis_offset,(A_Z-13)/2-A_Z_lower]){cube([M_linklength,M_width-2*M_wall,A_Z+A_Z-13], center = true);} // link hole
	translate([-sep-A_X-M_depth/2+M_wall/2,-M_axis_offset+M_width/2,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_mini, h = 4*M_wall, center = true);}} // screwhole1
	translate([-sep-A_X-M_depth/2+M_wall/2,-M_axis_offset-M_width/2,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_mini, h = 4*M_wall, center = true);}} // screwhole2
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset+M_width/2+2*M_wall,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*M_wall, center = true);}} // screwhole3 - at base
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset+M_width/2+2*M_wall+1,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*M_wall, center = true);}} // screwhole3l - at base
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset+M_width/2+2*M_wall-1,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*M_wall, center = true);}} // screwhole3r - at base
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset-M_width/2-2*M_wall,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*M_wall, center = true);}} // screwhole4 - at base
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset-M_width/2-2*M_wall+1,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*M_wall, center = true);}} // screwhole4l - at base
	translate([-sep+M_linklength+M_wall-A_X,-M_axis_offset-M_width/2-2*M_wall-1,A_Z-13-A_Z_lower]){
		rotate ([90,0,90]) {cylinder($fn = 50, r = R_screw_small, h = 2*M_wall, center = true);}} // screwhole4r - at base
}
// M_height-2*M_wall+2*gap


if (MFlag==1){
difference (){M1_base();M1_hole();}
}

///////////////////////////////////////
/// MOTOR MOUNT Top (M2) //////////////
///////////////////////////////////////

M_linklength2 = 15;
gap2 = 0.2; // extra gap for the mounting link, div by 2

module M2_base(){
	translate([0,-sep-A_Y,sep+B_Z/4+M_axis_offset]){cube([B_X+2*M_wall+gap2,M_depth,M_width+7], center = true);} // chassis
	translate([0,-sep-M_depth/2+M_wall/2-A_Y,sep+B_Z/4+M_axis_offset]){cube([M_height,M_wall,M_linkplate_width], center = true);} // linkplate2
	translate([0,-sep+M_linklength/2+M_depth/2-A_Y,sep+B_Z/4]){cube([B_X+2*M_wall+gap2,M_linklength,M_linkheight], center = true);} // link1
	translate([0,-sep+M_linklength+M_linklength2/2+M_depth/2-M_wall/2-A_Y,sep+B_Z/4]){cube([B_X+2*M_wall+gap2,M_linklength2+M_wall,M_linkheight], center = true);} // link2
}
module M2_hole(){
	translate([0,-sep-A_Y,sep+B_Z/4+M_axis_offset]){cube([M_height-2*M_wall+2*gap,M_depth,M_width-2*M_wall+2*gap], center = true);} // hole
	translate([0,-sep+M_linklength/2+M_depth/2-A_Y,sep+B_Z/4]){cube([B_X-wall+gap2,M_linklength,M_linkheight], center = true);} // link gap
	translate([0,-sep+M_linklength+M_linklength2/2+M_depth/2-A_Y,sep+B_Z/4]){cube([B_X+2*gap+gap2,M_linklength2,M_linkheight], center = true);} // link gap2
	translate([0,-sep-A_Y,sep+B_Z/4+M_axis_offset+M_width/2]){rotate ([90,0,0]){cylinder($fn = 50, r = R_screw_mini, h = M_depth, center = true);}} // screwhole1
	translate([0,-sep-A_Y,sep+B_Z/4+M_axis_offset-M_width/2]){rotate ([90,0,0]){cylinder($fn = 50, r = R_screw_mini, h = M_depth, center = true);}} // screwhole2
	translate([0,-sep+M_linklength+10+gap2+M_depth/2-A_Y,sep+B_Z/4]){rotate ([90,0,90]){cylinder($fn = 50, r = R_screw_small, h = 100, center = true);}} // MMount holes
	translate([0,-sep+M_linklength+10+gap2+M_depth/2-A_Y,sep+B_Z/4+1]){rotate ([90,0,90]){cylinder($fn = 50, r = R_screw_small, h = 100, center = true);}} // MMount holes
	translate([0,-sep+M_linklength+10+gap2+M_depth/2-A_Y,sep+B_Z/4-1]){rotate ([90,0,90]){cylinder($fn = 50, r = R_screw_small, h = 100, center = true);}} // MMount holes
}

if (M1Flag==1){
difference (){M2_base();M2_hole();}
}

*/

