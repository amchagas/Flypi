include<global_variables.scad>




$fn=50;

module screw(screwd,screwl,screwheadd,screwheadl){
cylinder(d=screwd+2*tolerance,h=screwl,center=true);
translate([0,0,screwl/2+screwheadl/2]){
cylinder(d=screwheadd,h=screwheadl,center=true);
}//translate
}//module screw


module rpiholes(){
translate([rpiholedisx/2,rpiholedisy/2,0]){
tube(tubede=screwde,tubedi=screwd,tubeh=screwh+partz/2);
}//translate

translate([rpiholedisx/2,-rpiholedisy/2,0]){
tube(tubede=screwde,tubedi=screwd,tubeh=screwh+partz/2);
}//translate

translate([-rpiholedisx/2,-rpiholedisy/2,0]){
tube(tubede=screwde,tubedi=screwd,tubeh=screwh+partz/2);
}//translate

translate([-rpiholedisx/2,rpiholedisy/2,0]){
tube(tubede=screwde,tubedi=screwd,tubeh=screwh+partz/2);
}//translate
}//module

module tube(tubede=conntubed, 
              tubedi=conntubed2, 
              tubeh=conntubeh){
    difference(){
        cylinder(d=tubede,h=tubeh,center=true);
        cylinder(d=tubedi,h=tubeh+1,center=true);
    }//difference

}//module
/*
module stabi(){
    
    difference(){
    cylinder(d=stabid,h=2*part_border-peltiercable,center=true);
    
    translate([stabid/2-(stabid/2)/2,0,0]){
    cube([stabid/2,partz,20],center=true);
    }//translate
    }//difference
}//module

module circholes(){
    cylinder(d=conntubed,h=basey+5,center=true);
    translate([0,conntubed+1,0]){
    cylinder(d=conntubed+tolerance,h=basey+5,center=true);
    }
    translate([0,-conntubed-1,0]){
    cylinder(d=conntubed+tolerance,h=basey+5,center=true);
    }

    }//module
    
 */   
module attachment(posx=posx,
                    posy=posy,
                    posz=posz,
                    negx=negx,
                    negy=negy,
                    negz=negz,
                    screwd=screwd){
    
difference(){
    //minkowski(){
    cube([posx-mink_dia,posy-mink_dia,posz-mink_dia],center=true);
      //  sphere(d=mink_dia, center=true);
        
        //}//minkowski
union(){
    translate([0,posy/5,0]){
      // minkowski(){
    cube([negx-mink_dia,negy-mink_dia,posz+mink_dia],center=true);
      // sphere(d=mink_dia,center=true);
        //    }//minkowski
    }//translate
    translate([0,posy/2,0]){
    rotate([90,0,0]){
        cylinder(d=screwd,h=posy/2,center=true,$fn=100);
        }//rotate
    }//translate
}//union

    }//difference

}//module


module main(partx=partx,
              party=party,
              partz=partz){
    
    
  //  minkowski(){

    cube([partx+2*part_border-mink_dia,
          party+2*part_border-mink_dia,
          partz],center=true);
    //rotate([0,90,0]){
    //sphere(d=mink_dia, center=true);    
    //}
    //rotate([90,0,0]){
    //cylinder(r=mink_dia,h=1, center=true);    
    //}
    //cylinder(r=mink_dia,h=1, center=true);
//}//minkowski

    
    }
  
module combined(){
    //main(partx,party,part_border,partz-1);
    main();
    translate([0,(party+posy)/2+part_border-2,0]){
    attachment(posx,posy,posz,negx,negy,negz,screwd);
    }//translate   
       
} 

       
module sideattachment(posx=posx,
                        posy=posy,
                        posz=posz,
                        negx=negx,
                        negy=negy,
                        negz=negz,
                        screwd=screwd){
    
difference(){
    //minkowski()
    {
    cube([posx-mink_dia,posy-mink_dia,posz],center=true);
      //  sphere(d=mink_dia, center=true);
    //    }//minkowski
union(){
    translate([5,posy/5,0]){
   // minkowski(){
        cube([negx+10-mink_dia,negy-mink_dia,negz],center=true);
     //   sphere(d=mink_dia,center=true);
       // }
    }//translate
    translate([0,posy/2,0]){
    rotate([90,0,0]){
        cylinder(d=screwd,h=posy/2,center=true,$fn=100);
        }//rotate
    }//translate
}//union

    }//difference

}//module

//sideattachment();
//combined();
//main();
//minkowski(){
//attachment();
//    sphere(d=1,center=true);
}
//main();