
include<global_variables.scad>
include<global_modules.scad>

linkx=40;
module angled_stick(){
//rotate([0,0,90]){
difference(){
union(){
attachment();




translate([linkx/2+negx/2,0,0]){
cube([linkx,part_border,partz],center=true);    
    }//translate

translate([linkx/2+2*part_border,0,linkx/2-0.5*part_border]){  
rotate([0,295,0]){
cube([linkx,part_border,partz],center=true); 
}//rotate
}//translate

translate([linkx+2*part_border,0,linkx/2-4]){
rotate([0,305,0]){
cube([linkx,part_border,8],center=true); 
}//rotate
}//translate
}//union
rotate([90,0,0]){
cylinder(d=screwd,h=part_border+1,center=true);
}//rotate
translate([0,-posy/2-part_border/2,0]){
cube([posx,20,30],center=true);

}//translate
}//difference

}//angled_stick
