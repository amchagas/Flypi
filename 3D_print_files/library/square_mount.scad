posx = 20;
posy = 22;
posz = 5;
negx = 10;
negy = 5;
negz = posz+1;
screwd=2.95;



$fn=100;

module attachment(posx,posy,posz,negx,negy,negz,screwd){
difference(){
    minkowski()
    {
    cube([posx-4,posy-4,posz-1],center=true);
        cylinder(r=2,h=1, center=true);
        }//minkowski
union(){
    translate([0,posy/5,0]){
    cube([negx,negy,negz],center=true);
    }
    rotate([90,0,0]){
        cylinder(d=screwd,h=posy,center=true,$fn=100);
        }
    }

    }
}

//attachment(posx,posy,posz,negx,negy,negz,screwd);