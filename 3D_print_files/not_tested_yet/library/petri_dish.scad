//use <global_variables.scad>
include<global_modules.scad>



petrid = 58.8; // 
petrid_outer = 58.8; // for lid


module petri(){
difference(){
main(partx = petrid,party=petrid,part_border=part_border,partz=partz);
cylinder(d=petrid+tolerance,h=partz+10,center=true);
}//difference

//translate([0,-(-(camx+posx)/2-part_border+1),0]){
translate([0,(petrid+part_border+posy)/2,0]){
    rotate([0,0,0]){
attachment(posx=posx,
            posy=posy,
            posz=partz+mink_dia,
            negx=negx,
            negy=negy,
            negz=negz,
            screwd=screwd);
}//rotate
}//translate
}//module

//petri();
