include<global_variables.scad>




    union(){
    translate([0,0,-1]){
    cylinder(d=tubed+tubewall,h=1,center=true);
    }//translate
    cylinder(d=tubed-tolerance,h=plugh,center=true);
    }
