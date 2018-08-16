/*
re written 3d models for the FlyPi. Making it easier to read
and to change. The main idea is simple, taking structures and variables
that are common between parts and making them into modules, 
library files. 


Created by A.M. Chagas 2017 CC BY 4.0
Derived from the original files created by T. Baden


global_variables  file has the variables that will be used 
by other parts
*/

tolerance = 0.1; // Global gap between all parts that need to slide

$fn=20;




//////////////////////////////////////////////////////////////////////////////


//variables related  to square_mount///////////////////////////////////////
//variables for the attachment where parts connect to mounting poles
posx = 18;
posy = 20;
posz = 5;
negx = 10+2*tolerance;
negy = 5+2*tolerance;
negz = posz+1;

screwd = 3.1;//2.95; // diameter of the screw used to fix the parts 

fitx_hole = 10;//x dimension of hole that will fit with the mounting poles
fity_hole = 5; //y dimension of hole that will fit with the mounting poles

fitx = 20; // x dimension of the material that will go around the mounting
          // holes
fity = 22; // y dimension of the material that will go around the mounting
          // holes
mink_dia=0; //sets the diameter of the cylinders used to round pieces up

part_border = 5; //how much larger in x and y  than the actual parts 
                  //being held the printed part is going to be
partx = 25;
party = 25;
offsety = (party+posy)/2+part_border-2;

partz  = 5; //how thick the part printed is going to be

///////raspberry pi///////////////////////////////////////////////////////////
rpiwidth = 56; // Dimensions of the RPi 2 (below also for RPi 2)

rpiholedisy = 49;
rpiholedisx = 58;
rpigrounddist = 4.2;
//////////////////////////////////////////////////////////////////////////

//////////////////CAMERA VARIABLES////////////////////////////////////
// RPi Camera Type
camx = 32.2+2*tolerance;//24 for "classic RPi Cam V1. i.e the one
                        //without the adjustable focus lens";
camy = 32.2+2*tolerance;//25 for "classic RPi Cam V1";



camxoffset = 2.50;// 2.5 for "classic RPi Cam";
cam_pcb_z = 2; // thickness of camera mount
C_Z2 = 5; // thickness of cmaera mount walls
C_ridge = 2; // width of ridge for camera mount
CamGroove_X = 12;
CamGroove_Y = 16.1;
CamGroove2_Y = 24;

MiniGrooveX = 15;

////////////////////////////////////////////////////////////////////////////




//peltier dimensions///////////////////////////////////////////////////////
peltierx = 40+1; // Size of the Peltier
peltiery = 40+1;
peltierz = 3; // Thickness of the Peltier
peltierborder = 12; // Extension in X dimension of base next to Peltier
peltierridge = 1.6; // below Peltier, width of ridge
peltiercable = 3; // thickness of Peltier cable slid
//////////////////////////////////////////////////////////////////////////////

//base///////////////////////////////////////////////////////////////////////
baseextension = 70;
basex=peltierx+2*peltierborder+partz+baseextension;
basey=rpiwidth+2*peltiercable;
basez=19;
stabid=24;

////////////////////////////////////////////////////////////////////



////////markerled////////////////////////////////////////////////////////
markerledd = 7; // diam of RGB LED hole in base
markerledz = 2; // depth beneath surface
markerx = 4; // Module A, viewhole size

///////////////////////////////////////////////////////////////////////////

///connection holes and stick dimensions////////////////////////////
conntubed=11;
conntubeh=16;
conntubed2=8.5;
stickx=10;
sticky=5;
stickz=18;
//18 short stick
//60 medium stick
//120 long stick

//ring
ring_de = 51; //external diameter of the ring
ring_di = 35; //internal diameter of the ring

////////////////////fluorescence tubes//////////////////////////

tubewall = 3;
tubed = 22;
tubeh = 30;
plugh=2;