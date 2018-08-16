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
    

This files describes the base of the frame.
*/

include <global_modules.scad>
include <global_variables.scad>

$fn=100;

module tube(tubede=conntubed, 
              tubedi=conntubed2, 
              tubeh=conntubeh){
    difference(){
        cylinder(d=tubede,h=tubeh,center=true);
        cylinder(d=tubedi,h=tubeh+1,center=true);
    }//difference

}//module


module circholes(){
    cylinder(d=conntubed,h=basey+5,center=true);
    translate([0,conntubed+1,0]){
    cylinder(d=conntubed+tolerance,h=basey+5,center=true);
    }
    translate([0,-conntubed-1,0]){
    cylinder(d=conntubed+tolerance,h=basey+5,center=true);
    }

    }//module
    
module stabi(){
    union(){
    difference(){
    cylinder(d=stabid,h=2*part_border-peltiercable,center=true);
    
    translate([stabid/2-(stabid/2)/2,0,0]){
    cube([stabid/2,partz,20],center=true);
        }
    }//translate
    }//difference
}//module


/*
module roundbase(){
    //minkowski(){
    cube([basex,basey,basez],center=true);
      //  cylinder(d=1,h=1,center=true);
      //  rotate([90,0,0]){
    //cylinder(d=1,h=1,center=true);
     //   }//rotate
     //          rotate([0,90,0]){
    //cylinder(d=1,h=1,center=true);
     //   }rotate
    //}//minkowski
    }
*/
module base(){
union(){   
difference(){

    union(){
        cube([basex,basey,basez],center=true);
    //roundbase();
    //stabilizer1
    translate([0,-(basey-(2*part_border-peltiercable))/2,basez/2]){
    rotate([90,-90,0]){
    stabi();
    }//rotate
    }//translate


    //stabilizer2
    translate([0,(basey-(2*part_border-peltiercable))/2,basez/2]){
    rotate([90,-90,0]){
    stabi();
    }//rotate
    }//translate
    }//union
    
    union(){
    //wall slit
    cube([partz,basey-2*part_border-peltiercable,150],center=true);

    //connecting holes
    translate([basex/2,0,0]){
    rotate([0,90,0]){
    circholes();
    }//rotate
    }//translate

    translate([peltierx/2+partz+conntubed,0,0]){
    rotate([90,90,0]){
    circholes();
    }//rotate
    }//translate

    //peltier
    translate([(basex-peltierx)/2-peltierborder,0,basez/2-peltierz/2]){
    cube([peltierx+2*tolerance,peltiery+2*tolerance,peltierz+1],center=true);
    }//translate
    
    //peltier cable1
    translate([0,peltiery/2-peltiercable/2,basez/2-peltierz/2]){
    cube([basey,peltiercable+2*tolerance,peltiercable+2*tolerance],center=true);
    }//translate
    
    //peltier cable2
    translate([0,-(peltiery/2-peltiercable/2),basez/2-peltierz/2]){
    cube([basey,peltiercable+2*tolerance,peltiercable+2*tolerance],center=true);
    }//translate

    //marker led hole
    translate([0,0,basez/2-markerledd/2-markerledz]){
    rotate([0,90,0]){
    cylinder(d = markerledd, h = basey, center = true );
    }//rotate
    }//translate

    //marker led window
    translate([peltierx/2-7,0,basez/2]){
    cube([markerx,markerx,10],center=true);
    }//translate

    //hole below peltier
    translate([(basex-peltierx)/2-peltierborder,0,19/2-peltierz/2]){
    cube([peltierx-peltierridge*2,peltiery-peltierridge*2,50], center = true );
    }//translate

    //cleaning up material from the back part
    translate([-basex/2-stabid/2,0,5]){
    cube([basex,basey,15],center=true);
    }//translate
    translate([-basex/2+(basey-13)/2+5,0,5]){
    cube([basey-13,basey-10,35],center=true);
    }//translate

}//union
}//difference
}//union
}//module
//stabi();
//base();