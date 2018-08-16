

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
    

This files describes the a holder for a picamera. (from waveshare)
*/


use<global_modules.scad>
include<global_variables.scad>

module camera(){
difference(){
    union(){
    main(camx,camy,part_border,partz);
	translate([-(camx+posx)/2-part_border+1,0,0]){
        rotate([0,0,90]){
        attachment(posx,posy,posz,
                    negx,negy,negz,
                    screwd);}
                }
            }//union

union(){
	
    translate([0,0,partz*0.75-cam_pcb_z/2]){
    cube([camx,camy,cam_pcb_z], center = true);
        } // Cam_hole_ridge
	
    translate([-camx/2-CamGroove_X/2,0,0+C_Z2/2]){
        cube([CamGroove_X,CamGroove_Y,C_Z2+partz/2], center = true );
        } // Cam_cable_groove
	
    translate([camx/2-MiniGrooveX/2-C_ridge,-camy/2+C_ridge/2,0+C_Z2/2]){
        cube([MiniGrooveX,C_ridge,C_Z2+partz/2], center = true );} // mini groove
	
    translate([-camx/2+CamGroove_X/2,0,0+C_Z2/2]){
        cube([CamGroove_X,CamGroove2_Y,C_Z2+partz/2], center = true );
        } // Cam_bmup_groove
	

  cube([camx-C_ridge*2,camy-C_ridge*2,partz*3], center=true);
}//union
}//difference
}//module camera


//camera();