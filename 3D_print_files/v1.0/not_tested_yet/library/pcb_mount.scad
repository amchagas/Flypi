include<global_modules.scad>
//include<global_variables.scad>

pcbx=1.6;
pcby=76;
screwheadd=7;
screwheadl =5;
screwl=50;
screwd=3.1;
spacer=15;






module pcb_mount(){
difference(){
    union(){
main(partx=pcbx,
      party=pcby+part_border/2,
      partz=part_border*2+screwheadd);
translate([-spacer/2,+rpiholedisy/2,-part_border-1]){
main(partx=spacer,party=screwd/2,partz=part_border);
}//translate   
translate([-spacer/2,-rpiholedisy/2,-part_border-1]){
main(partx=spacer,party=screwd/2,partz=part_border);
}//translate
    }//union
union(){
translate([0,0,screwheadd+part_border/2]){
main(partx=pcbx+part_border+1,
      party=pcby-15,
      partz=part_border*2+screwheadd);
}//translate
translate([0,0,15-part_border/2]){
cube([pcbx,pcby+tolerance,30],center=true);
}//translate
}//union

translate([(-screwl-screwheadl+part_border)/2+1.5,
           -rpiholedisy/2,
           -part_border+1]){
rotate([0,90,0]){
    screw(screwd,screwl,screwheadd,screwheadl);
    }//rotate
}//translate
translate([(-screwl-screwheadl+part_border)/2+1.5,
           rpiholedisy/2,
           -part_border+1]){
rotate([0,90,0]){
    screw(screwd,screwl,screwheadd,screwheadl);
    }//rotate
}//translate
}//difference
}//module pcb_mount

pcb_mount();