

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
    

This files describes the a holder for a light diffuser)

*/
include<global_modules.scad>
use<global_variables.scad>


Link_Opening = 1;
partx = 40;
party = 40;
partz=4.5;

diffuserx = 38.5+tolerance;
diffusery = 38.5+tolerance;

module diffusor(){
difference(){
    union(){
    main(party=party-mink_dia,partx=partx-mink_dia,partz=partz);
    translate([0,-(-(camx+posx)/2-part_border+1),0]){
sideattachment(posz=partz);
}//translate
}//union
    cube([diffuserx,diffusery,partz+10],center=true);
}//difference
}//module

diffusor();