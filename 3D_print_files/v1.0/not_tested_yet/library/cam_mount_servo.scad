/* Part library for the frame of the FlyPi.
Written by AM Chagas, CC By 4.0 -

First publication: 21.12.2017

Derived from the work of T. Baden 2015.

The complete library was rewriten from scratch to:
    - Be modular, each part is described and contained in one file
    - common variables and modules are contained in "global files", so that they can be called from other files, and there is no need to re-write code.
    - edges are made more circular, with Minkowsky calls, which makes rendering slower, but should lead to nicer prints.
    - to facilitate larger scale production. 

This was originally published as part of the product development for Prometheus Science (www.prometheus-science.com). Questions and inquires can be directed to the FlyPi Forum:
      www.prometheus-science.com/en_GB/forums/forum/flypi-user-forum/
    

This files describes the mount part for the camera and servo motor to control the lens distance from camera.

*/
use<cam_mount_waveshare.scad>
include<global_variables.scad>
//use<library/MCAD-dev/gears/involute_gears.scad>

$fn=100;
//sep = 0; // How far apart do pieces "float" in the model
//Walls = 5; // Global thickness of all walls
//Tol = 0.2; // Global gap between all parts that need to slide
servox = 23.7;
servoy=12.2;
servoxoffset=5.5;
// height of Servo is 29 in total, which is counted from the bottom


cogwheeld = 28.2;
cogwheel_R2 = 10.5;
cogwheelh = 10;
//cogwheel_Z2 = 4;
cogwheel_nteeth = 30; // should be divisible by 3
cogwheeldinner1 = 14+tolerance; // camera radius
//cogwheel_R_inner2 = 3.7+Tol/2; // servo axis radius
servocrossz = 3;
servocrossx = 4.5+tolerance;
servocrossy = cogwheel_R2*2-1;






module servoMount(){
translate([0,-(camy+posx)/2-part_border,0]){
 difference(){
 minkowski(){
cube([camx+2*part_border-mink_dia,
      servoy+2*part_border-mink_dia,
      partz],center=true);
  sphere(d=mink_dia,center=true);
}//minkowski
union(){
    translate([-servoxoffset,0,0]){
cube([servox,servoy,partz+5],center=true);
       translate([(servox)/2,0,0]){
cylinder( d = 8, h = partz+5, center = true );
    }//translate
}//translate
}//union
}//difference
}//translate

}//module servo mount



module cogWheel(){

 for (i = [1 : cogwheel_nteeth/3]) {
		rotate ([0,0,(i+0.5)*360/cogwheel_nteeth]) {cylinder($fn = 3, d = cogwheeld, h = cogwheelh, center = true );} // cogs wheel 1
    }

}
module wheels(){
rotate([0,180,0]){
translate([0,50,0]){
difference(){
cogWheel();
union(){
    translate([0,0,-servocrossz]){
cylinder(d=cogwheeldinner1+5,h=cogwheelh,center=true);
cylinder(d=cogwheeldinner1-5,h=cogwheelh-5,center=true);
    }
translate([0,0,servocrossz]){

cube([servocrossx,servocrossy,servocrossz+0.1], center = true);
cube([servocrossy,servocrossx,servocrossz+0.1], center = true);
}//translate
}//union
}//difference
translate([0,2.5*cogwheeldinner1,0]){
 difference(){
cogWheel();
     union(){
   cylinder(d=cogwheeldinner1,h=cogwheelh+1,center=true);
         translate([0,0,-2.5]){
   cylinder(d=cogwheeldinner1+5,h=cogwheelh-5,center=true);
     }//translate
     }//union
 
 }//difference
}//translate
}//translate
}//rotate
}//module

module camera_servo(){
translate([0,0,-(partz)/2]){
camera(part_border=part_border);
servoMount();

}
}