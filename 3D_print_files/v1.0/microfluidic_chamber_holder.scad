

/*holder for a microfluidic chamber.
The holder is lifted in the air, so that a light source can be slid below it */

//chamber
chamX = 75;
chamY = 25;
chamZ = 5;
offsetZ = 2;
offsetX = 3;


//holder
difference(){
    cube([chamX+offsetX,chamY+offsetX,chamZ/2],center=true);
    translate([0,0,0.5]){
    cube([chamX+(offsetX/3),chamY+(offsetX/3),chamZ/3],center=true);}
}

//feet
translate([chamX/2-(offsetX/2),chamY/2-(offsetX/2),-chamZ/2-(offsetZ/2)]){
cube([5,5,5],center=true);}

translate([-chamX/2+(offsetX/2),-chamY/2+(offsetX/2),-chamZ/2-(offsetZ/2)]){
cube([5,5,5],center=true);}

translate([chamX/2-(offsetX/2),-chamY/2+(offsetX/2),-chamZ/2-(offsetZ/2)]){
cube([5,5,5],center=true);}

translate([-chamX/2+(offsetX/2),chamY/2-(offsetX/2),-chamZ/2-(offsetZ/2)]){
cube([5,5,5],center=true);}

