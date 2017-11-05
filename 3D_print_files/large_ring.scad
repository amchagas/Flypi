
use<library/square_mount.scad>


tolerance = 0.1; // Global gap between all parts that need to slide

screw_d = 2.95;

fity_hole = 6;
fitx_hole = 11;

fity = 22;
fitx = 20;

ring_de = 51;
ring_di = 35;
part_border = 5;
part_thick = 5;



module ring(diame,height){
    
    cylinder(d=diame,h=height,center=true,$fn=100);
  
}


difference(){
//positives:
$fn=100;
minkowski()
{
cube([ring_de+part_border-2,ring_de+part_border-2,part_thick-1],center=true);
  cylinder(r=2,h=1, center=true);


}//minkowski
//negatives
ring(ring_de,part_thick+5);
}

translate([0,0,-part_thick/2]){
difference(){
minkowski()
{
cube([ring_de+part_border-2,ring_de+part_border-2,0.5],center=true);
  cylinder(r=2,h=0.5, center=true);


}//minkowski
union(){
ring(ring_di,part_thick+5);
    translate([0,ring_di/2,0]){
        cylinder(d=5,h=10,center=true,$fn=100);
        }//translate
    }//union
}//difference
}//translate




translate([0,ring_de/2+fity/2,-0.25]){
attachment(posx=fitx,
            posy=fity,
            posz=part_thick+0.5,
            negx=fitx_hole+tolerance,
            negy=fity_hole+tolerance,
            negz=part_thick+5,
            screwd=screw_d);
}

//ring();