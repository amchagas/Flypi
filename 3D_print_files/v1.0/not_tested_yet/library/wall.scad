use<cam_mount_waveshare.scad>
//include<global_variables.scad>
include <global_modules.scad>



screwh=10;
screwdi=2.9;
screwde=screwdi+2.4;
wallx=90;
longstick= 95;


module wall(){
translate([rpigrounddist,0,(screwh/2)-1]){
rpiholes();
}//translate



difference(){

union(){    
//main wall
main(partx=wallx,party=basey-part_border);

//rectangular link
translate([peltierz*2,0,0]){
main(partx=wallx,party=rpiwidth/2-part_border/2,partz=partz);  
}//translate

//connection to base
translate([wallx/2+(peltierz+partz)*2,0,0]){
main(partx=partz+tolerance,party=(basey)/2+part_border,partz=partz);
}//translate
//triangular neck
translate([-(basey-2*part_border-mink_dia),0,0]){
rotate([0,0,-60]){
    minkowski(){
cylinder(d=basey-part_border-mink_dia,h=partz,$fn=3, center=true);
        sphere(d=mink_dia,center=true);
    }//minkowski


}//rotate
}//translate


//camerapole
translate([-wallx/2-(basey-part_border/2),0,0]){
    main(partx=longstick,party=fity_hole-part_border,partz=fitx_hole-part_border);
}//translate

}//union

union(){
    
    //cutout of wall
translate([0,0,(partz/2+1)]){
    main(partx=wallx-part_border*4, party=basey-4*part_border, partz=10);
}//translate

//marker led hole
translate([wallx/2+basez/2+markerledd/4,0,0]){
cylinder(d=markerledd+2*tolerance,h=partz+30,center=true);

}//translate
//temp sensor hole
translate([(wallx+partz)/2,((basey)/2+part_border)/5,0]){
//minkowski(){
cube([partz-mink_dia,2.5*partz-mink_dia,30],center=true);
//sphere(d=mink_dia,center=true);
//}//
    }//translate
}//union
}//difference

}//module wall

wall();