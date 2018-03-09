

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
    

This files describes the a wheel holder for the light filters and the holder for the wheel.
*/

include<global_modules.scad>
use<global_variables.scad>


partx = 30;
party = 35;
partz = 4.5;
mainholed=17;
wheeld = 60;
wheelh = 1.2;
wheelholed = 18;
pivotholeoffset = 15;
pivotd = 6;
pivoth=8;
spacerh=0.5;



module wheelholes(){
translate([0,pivotholeoffset,0]){  
cylinder(d = wheelholed, h = wheelh+1, center = true );
}//translate
translate([0,-pivotholeoffset,0]){  
cylinder(d = wheelholed, h = wheelh+1, center = true );
}//translate
translate([-pivotholeoffset,0,0]){  
cylinder(d = wheelholed, h = wheelh+1, center = true );
}//translate
translate([pivotholeoffset,0,0]){  
cylinder(d = wheelholed, h = wheelh+1, center = true );
}//translate
}//module

module filter_mount(){
difference(){
main();
union(){
cylinder(d=mainholed,h=partz+10,center=true);
    translate([0,pivotholeoffset,0]){
        cylinder(d=pivotd+tolerance,h=partz+10,center=true);
        }//translate
    }//union
}//difference


//wheel
translate([0,(party+wheeld/2)-6,-partz/2+wheelh/2]){
    difference(){
    union(){
        cylinder(d=wheeld, h=wheelh, center = true );
        translate([0,0,(wheelh+spacerh)/2]){
            cylinder(d=pivotd+1, h=spacerh, center = true );
            }//translate
        translate([0,0,(pivoth+wheelh)/2]){
            cylinder(d=pivotd-tolerance,h=pivoth, center = true );
            }//translate
       
        }//union
    wheelholes();
    }//difference
    
}//translate

translate([-(camx+posx)/2-part_border+1,0,0]){
    rotate([0,0,90]){
attachment(posz=partz);
    }//rotate
}//translate
}//module

//filter_mount();
