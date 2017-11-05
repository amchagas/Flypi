include<library/square_mount.scad>


tolerance = 0.2; // Global gap between all parts that need to slide
partThick = 5;

screwD = 2.95;

fityHole = 6;
fitxHole = 11;

fity = 22;
fitx = 20;

heatDissX=34.1;
heatDissY=35.1;

difference(){
//positive
cube([heatDissX+8,heatDissY+8,partThick],center=true);
//negative
translate([0,0,partThick-3]){
    cube([heatDissX,heatDissY,partThick],center=true);

}
cube([heatDissX-2,heatDissY-2,partThick],center=true);
}

translate([0,heatDissY/2+fity/2,0]){
    attachment(posx=fitx,
            posy=fity,
            posz=partThick,
            negx=fitxHole+tolerance,
            negy=fityHole+tolerance,
            negz=partThick,
            screwd=screwD);
}