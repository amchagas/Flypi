//stage components
//include <global_variables.scad>
include <base.scad>
include <mount_stick.scad>
include <cam_mount_waveshare.scad>
include <filter_mount.scad>
include <large_ring.scad>
include <heat_dissipator_led.scad>
include <wall.scad>
include <mini_petri_dish.scad>
include <petri_dish.scad>
include <pcb_mount.scad>
include <cam_mount_servo.scad>
include <fluorescence_mount_tubes.scad>

translate([0,0,basez/2]){

base();

}
translate([45,basey/2+10,fity_hole/2]){
mount_stick(stickl=20);
}

translate([0,basey/2+10,fity_hole/2]){
mount_stick(stickl=100);
}

/*
translate([-45,40,fity_hole/2]){
mount_stick(stickl=50);
}
*/

translate([0,-60,partz/2]){
camera();
}

translate([basex,0,partz/2]){
filter_mount();
}

translate([90,-100,partz/2]){
fluor_tube_mount();
}

translate([50,100,partz/2]){
ring();
}

translate([-50,100,partz/2]){
heat_diss();
}


translate([50,200,partz/2]){
wall();    
}


translate([0,-70,0]){
small_petri();
}

translate([-90,0,0]){
petri();
}

translate([0,0,70]){
camera_servo();
}
