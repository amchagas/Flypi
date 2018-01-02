
/* mount for the LED ring used in the FlyPi

Created by AM Chagas 2017 CC BY 4.0

Since rings from different manufactures have different dimensions
users can change ring_de and ring_di to fit the dimensions of their rings

All variables in mm.


The repository for this project can be found under
https://github.com/prometheus-science/Flypi

Derived from the work of T Baden (www.github.com/amchagas/Flypi)
*/

//import modules and variables
include<global_modules.scad>
//include<global_variables.scad>

//ring_de = 51; //external diameter of the ring
//ring_di = 35; //internal diameter of the ring
//adafruit 12 led ring: 
//de = 37
//di = 23

//aliexpress ring
//de=51;
//di=35;
partz1=4;
partz2=0.5;
//part_border=3;



//$fn=100; //number of "sides" in the cylinders

//offsety =(ring_de+part_border+fity)/2;

module ring(ring_de1=ring_de,ring_di=ring_di){
    union(){


//make the main structure with the circular hole
difference(){
//positives:
//imported from square_mount file
    union(){
main(partx=ring_de,party=ring_de1,part_border=part_border,partz=partz);
    translate([0,-(-(camx+posx)/2-part_border-1),0]){
//create the attachment that will connect the part with the moutnting poles
//translate([0,offsety,0]){
attachment(posx=fitx,
            posy=fity,
            posz=partz  ,
            negx=negx,
            negy=negy,
            negz=partz+5,
            screwd=screwd);

}//translate
}//union

//negatives

cylinder(d=ring_de1,h=partz+5,center=true);

}//difference

//make the base of the main structure with smaller circular hole

translate([0,0,-(partz-partz2)/2]){
    
difference(){
main(partx=ring_de1,party=ring_de1,part_border=part_border,partz=partz2);


union(){
cylinder(d=ring_di,h=partz+5,center=true); 
    translate([0,ring_di/2,0]){
        cylinder(d=15,h=10,center=true);
        }//translate
    }//union
}//difference
}//translate


}//union
}//module


//ring(ring_de=ring_de,ring_di=ring_di);