use<global_modules.scad>
//include<global_variables.scad>


part_thick = 5;
part_border = 5;


fityHole = 6;
fitxHole = 11;

fity = 22;
fitx = 20;

heatDissX=34.1;
heatDissY=35.1;
module heat_diss(){
difference(){
//positive
    union(){
    main(heatDissX,heatDissY,part_border,part_thick);
    translate([0,-(-(camx+posx)/2-part_border+1),0]){

    attachment(posx=fitx,
            posy=fity,
            posz=part_thick,
            negx=fitxHole+tolerance,
            negy=fityHole+tolerance,
            negz=part_thick+1,
            screwd=screwd);
}//translate
}//union

//negative
translate([0,0,part_thick-3]){
    cube([heatDissX+tolerance*2,heatDissY+tolerance*2,part_thick],center=true);

}
cube([heatDissX-3,heatDissY-3,part_thick+2],center=true);
}
}//module
//heat_diss();