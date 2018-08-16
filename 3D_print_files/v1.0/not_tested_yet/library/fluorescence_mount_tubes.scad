/*excitation light mount









*/

include<global_modules.scad>
//include<global_variables.scad>
partx=35;
party=50;
//part_border=5;
//partz=5;




module threecylinders(cylinderd,middlewall,cylinderh){
    union(){
    translate([0,0,(cylinderh/2)-partz*2]){
    cylinder(d=cylinderd+middlewall,h=cylinderh,center=true);
    }
    
	translate([0,-tubed+part_border/2+1,(tubeh/2)-partz*2]){
        rotate ([45,0,0]) {
            cylinder(d=cylinderd,h=cylinderh,center=true);
            }//rotate
            }//translate 
	translate([0,+tubed-part_border/2-1,(tubeh/2)-partz*2]){
        rotate ([-45,0,0]) {
            cylinder(d=cylinderd,h=cylinderh,center=true);
            }//rotate
            }//translate
        }//union
    }//module



module threetubes(tubed,tubewall,tubeh){
    union(){
    difference(){
    union(){
    translate([0,0,(tubeh/2)-2]){
        rotate ([0,0,0]) {
            cylinder(d=tubed+tubewall,h=tubeh,center=true);
            }//rotate
            }//translate
	translate([0,-tubed+part_border/2+1,(tubeh/2)-partz*2]){
        rotate ([45,0,0]) {
            cylinder(d=tubed+tubewall,h=tubeh,center=true);
            }//rotate
            }//translate 
	translate([0,+tubed-part_border/2-1,(tubeh/2)-partz*2]){
        rotate ([-45,0,0]) {
            cylinder(d=tubed+tubewall,h=tubeh,center=true);
            }//rotate
            }//translate
            
        }//union
        
        union(){
    translate([0,0,(tubeh/2)]){
        rotate ([0,0,0]) {
            cylinder(d=tubed,h=tubeh+50,center=true);
            }//rotate
            }//translate
	translate([0,-tubed+part_border/2+1,(tubeh/2)-partz*2]){
        rotate ([45,0,0]) {
            cylinder(d=tubed,h=tubeh+50,center=true);
            }//rotate
            }//translate 
	translate([0,+tubed-part_border/2-1,(tubeh/2)-partz*2]){
        rotate ([-45,0,0]) {
            cylinder(d=tubed,h=tubeh+50,center=true);
            }//rotate
            }//translate
 translate([0,0,-((tubeh/2))]){
            cube([tubed+tubewall*2,2*tubed+tubewall*2+10,tubeh],center=true);
            }//translate
        }//union
    }//difference
}//union
    }//module



module fluor_tube_mount(){
union(){
translate([-(camx+posx)/2-part_border+1,0,0]){
rotate([0,0,90]){
attachment(posx,posy,partz,negx,negy,negz,screwd);
}//rotate
}//translate


difference(){
main(partx=partx,party=party,partz=partz);
union(){
threecylinders(cylinderd=tubed,
                middlewall=0,
                cylinderh=tubeh+5);
    translate([0,0,tubeh]){
cube([tubed,tubed-tubewall/2,tubeh],center=true);
    }
}//union
}//difference


threetubes(tubed,tubewall,tubeh);



}
}//module

//fluor_tube_mount();
