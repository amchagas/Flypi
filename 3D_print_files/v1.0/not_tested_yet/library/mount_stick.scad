
use<global_variables.scad>
include<global_modules.scad>


module mount_stick(stickl=stickz){
translate([0,0,conntubeh/2-(fity_hole-2*tolerance)/2]){
tube();
translate([conntubed+1.5,0,0]){
tube();
}//translate
translate([-(conntubed+1.5),0,0]){
tube();
}//translate
//cube([],center=true);
}//translate


difference(){
    union(){
        cube([conntubed*3+5,conntubed+3,fity_hole-2*tolerance],center=true);
    //main(partx=conntubed*3+3,party=conntubed+2,part_border=1,partz=fity_hole);
    translate([0,stickl/2,0]){
    cube([fitx_hole-2*tolerance,stickl,fity_hole-2*tolerance],center=true);
    //main(partx=fitx_hole-part_border/2,party=stickl,part_border=2,partz=fity_hole);
}//transalte
}//union
cylinder(d=conntubed-2,h=conntubeh,center=true);
translate([conntubed+1.5,0,0]){
    cylinder(d=conntubed-2,h=conntubeh,center=true);
}//translate
translate([-(conntubed+1.5),0,0]){
    cylinder(d=conntubed-2,h=conntubeh,center=true);
}//translate
}//translate

}//module
//translate([0,0,partz/2]){
//mount_stick(stickl=20);
//}//translate