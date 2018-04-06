//include <global_variables.scad>
include<global_modules.scad>

petrid = 35; // 
petrid_outer = 39; // for lid
//partz=5;
//part_border=4;


module small_petri(){
difference(){
main(petrid,petrid,part_border,partz);
cylinder(d=petrid,h=partz+1,center=true);
}//difference

translate([0,-(-(camx+posx)/2-part_border+1),0]){
//translate([0,(petrid+part_border+posy)/2,0]){
    rotate([0,0,0]){
attachment(posx=posx,
            posy=posy,
            posz = partz,
            negx = negx,
            negy = negy,
            negz = negz,
            screwd = screwd);
}//rotate
}//translate

}//module

//small_petri();
