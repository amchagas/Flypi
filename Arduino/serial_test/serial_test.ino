// Demo Code for SerialCommand Library
// Steven Cogswell
// May 2011

// Import libraries


#include "peltier.h"
#include "ring.h"
#include "matrix.h"
#include "servo.h"


// define ports
#define LED1Pin 10
#define LED2Pin 11 






//Timing Variables////////////////////////
long int millistowait;


////////////////////////////////////////

SerialCommand sCmd;     // The demo SerialCommand object

void setup() {
  pinMode(LED1Pin, OUTPUT);
  pinMode(LED2Pin, OUTPUT);

  pinMode(RedGBPin, OUTPUT);
  pinMode(RGreenBPin, OUTPUT);
  pinMode(RGBluePin, OUTPUT);

  pinMode(servoOnPin, OUTPUT);

  pinMode(peltierEnablePin, OUTPUT);
  pinMode(peltierHeatPin1, OUTPUT);
  pinMode(peltierCoolPin1, OUTPUT);

  focusServo.attach(servoPin);
  // start ring
  pixels.begin();

  Serial.begin(115200);

  // Setup callbacks for SerialCommand commands

  sCmd.addCommand("S1",    SERVO_on);
  sCmd.addCommand("S0",    SERVO_off);
  sCmd.addCommand("M1",    MATRIX_on);
  sCmd.addCommand("M0",    MATRIX_off);
  sCmd.addCommand("M11",    MATRIX_pat1);
  sCmd.addCommand("M12",    MATRIX_pat2);
  sCmd.addCommand("M13",    MATRIX_pat3);
  sCmd.addCommand("M14",    MATRIX_bright);
  

  
  sCmd.addCommand("L11",    LED1_on);          // Turns LED1 on and sets intensity

  //sCmd.addCommand("L12",    LED1_PWM);         // Set intensity LED1

  sCmd.addCommand("L10",    LED1_off);         // Turns LED1 off
  sCmd.addCommand("L21",    LED2_on);          // Turns LED2 on
  
  //sCmd.addCommand("L22",    LED2_PWM);         // Set intensity LED2
  
  sCmd.addCommand("L20",    LED2_off);         // Turns LED2 off
  sCmd.addCommand("R1",     RING_on);          // Turns RING on
  sCmd.addCommand("R0",     RING_off);         // Turns RING off
  sCmd.addCommand("RR",     RED);              // change RED intensity
  sCmd.addCommand("RG",     GREEN);            // change GREEN intensity
  sCmd.addCommand("RB",     BLUE);             // change BLUE intensity
  sCmd.addCommand("P1",     PELT_on);          // Turns PELTIER on
  sCmd.addCommand("P0",     PELT_off);         // Turns PELTIER off
  sCmd.addCommand("ST",     PELT_stemp);       // set PELTIER temperature
  sCmd.addCommand("GT",     TEMP_read);        // get PELTIER temperature
  sCmd.addCommand("TW",     TIME_wait);        // sets time to wait


  sCmd.addCommand("HELLO", sayHello);        // Echos the string argument back
  sCmd.addCommand("P",     processCommand);  // Converts two arguments to integers and echos them back
  sCmd.setDefaultHandler(unrecognized);      // Handler for command that isn't matched  (says "What?")
  Serial.println("Ready");
  newTemp = checkTemp(tempSensorPin);


  pixels.setPixelColor(0, pixels.Color(0,0,0));
  pixels.show();
}

void loop() {
  sCmd.readSerial();     // We don't do much, just process serial commands

}// void loop

///////// servo callbacks ////////////////////////////
void SERVO_on(){
  servoOn = 1;
  int aNumber;
  char *arg;
  arg = sCmd.next();
  digitalWrite(servoOnPin, HIGH);
  if (arg != NULL) {
    focusServo.write(atoi(arg)); //because this is a cont. servo,
    //this will set the velocity, not the pos.
    delay(15);
      
    }// if arg!=NULL
  waited();
  
  }//servo_on
  
void SERVO_off(){
  servoOn = 0;
  digitalWrite(servoOnPin, LOW);
  waited();
  }

/////////matrix callbacks ////////////////////////////
void MATRIX_on(){
  matrixOn = 1;
  
  waited();
  }
  
void MATRIX_off(){
  matrixOn = 0;
  matrix.clear();
  matrix.writeDisplay(); 
  waited();
  }

void MATRIX_bright(){
  matrix.setBrightness(matrix_brightness);
  
  if (matrixOn==1){
    matrix.writeDisplay();
  }
  waited();
  }  
void MATRIX_pat1(){
  
   matrix.clear();
   matrix.drawBitmap(0, 0, matrix_pattern1, 8, 8, LED_ON);
   if (matrixOn == 1){
    matrix.writeDisplay(); // write changes to the display
   }
   waited();
  }
void MATRIX_pat2(){
   
   matrix.clear();
   matrix.drawBitmap(0, 0, matrix_pattern2, 8, 8, LED_ON);
   if (matrixOn == 1){
    matrix.writeDisplay(); // write changes to the display
   }//if
  waited();
  }
void MATRIX_pat3(){
  for (int i = 0; i < 4; i = i+1) {
     matrix.clear();
     if (i==0) { 
        matrix.drawLine(0,0, 0,7, LED_ON);  matrix.drawLine(1,0, 1,7, LED_ON);
        matrix.drawLine(4,0, 4,7, LED_ON);  matrix.drawLine(5,0, 5,7, LED_ON); }          
     if (i==1) { 
        matrix.drawLine(1,0, 1,7, LED_ON);  matrix.drawLine(2,0, 2,7, LED_ON);
        matrix.drawLine(5,0, 5,7, LED_ON);  matrix.drawLine(6,0, 6,7, LED_ON); }          
     if (i==2) { 
        matrix.drawLine(2,0, 2,7, LED_ON);  matrix.drawLine(3,0, 3,7, LED_ON);
        matrix.drawLine(6,0, 6,7, LED_ON);  matrix.drawLine(7,0, 7,7, LED_ON); }          
      if (i==3) { 
        matrix.drawLine(3,0, 3,7, LED_ON);  matrix.drawLine(4,0, 4,7, LED_ON);
        matrix.drawLine(7,0, 7,7, LED_ON);  matrix.drawLine(0,0, 0,7, LED_ON); }          
     if (matrixOn==1){
      matrix.writeDisplay(); // write changes to the display
     }//if matrix on
     delay(100); }
  waited();
  }

/////////ring callbacks //////////////////////////////



void RING_on() {
  //Serial.println("ring on");
  ringOn = 1;
  updateRing(ringRedHue, ringGreenHue, ringBlueHue,ringOn);
  waited();
}

void RING_off() {
  //Serial.println("ring off");

  updateRing(0, 0, 0, ringOn);
  ringOn=0;
  waited();
  pixels.show();

  }


void RED(){
  int aNumber;
  char *arg;
  arg = sCmd.next();
  if (arg != NULL) {
     ringRedHue = atoi(arg);
     updateRing(ringRedHue, ringGreenHue, ringBlueHue,ringOn);
     waited();
  }//if

}//red

void GREEN(){
  int aNumber;
  char *arg;
  arg = sCmd.next();
  if (arg != NULL) {
     ringGreenHue = atoi(arg);
     updateRing(ringRedHue, ringGreenHue, ringBlueHue,ringOn);
     waited();
  }//if

}//red

void BLUE(){
  int aNumber;
  char *arg;
  arg = sCmd.next();
  if (arg != NULL) {
     //Serial.println("here");
     ringBlueHue = atoi(arg);
     updateRing(ringRedHue, ringGreenHue, ringBlueHue,ringOn);
     waited();
  }//if

}//red


////// LED functions ////////////////////////////////

void LED1_on() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  if (arg != NULL) {
     aNumber = atoi(arg);
     analogWrite(LED1Pin, aNumber);
     waited();
  }//if

}//led1_on

void LED1_off() {
  //Serial.println("LED1 off");
  analogWrite(LED1Pin, 0);
  waited();
}

void LED2_on() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  if (arg != NULL) {
     aNumber = atoi(arg);
     analogWrite(LED2Pin, aNumber);
     waited();
  }//if
}

void LED2_off() {
  //Serial.println("LED2 off");
  analogWrite(LED2Pin, 0);
  waited();
}


////////////////////////

//Peltier callbacks/////////////////


void PELT_on(){
  peltOn=1;
  digitalWrite(peltierEnablePin,HIGH);
  waited();
  //Serial.println("pelton");
}//pelt on


void PELT_off(){
  peltOn=0;
  digitalWrite(peltierEnablePin,LOW);
  digitalWrite(peltierHeatPin1, LOW);
  digitalWrite(peltierCoolPin1, LOW);
  analogWrite(RedGBPin, 0);
  analogWrite(RGreenBPin, 0);
  analogWrite(RGBluePin, 0);
  //Serial.println("waited()peltoff");
  waited();
}//pelt off

//peltier func (requiring scmd)
void PELT_stemp(){
   int aNumber;
   char *arg;
   arg = sCmd.next();
   if (arg != NULL) {
      newTemp = atoi(arg);
   }
   waited();

}

void TEMP_read(){
  currTemp = checkTemp(tempSensorPin);
  //Serial.print("temp: ");
  Serial.println(currTemp);
  waited();
}//temp read


///////////////////////////////////////
// timing functions /////////////////

void TIME_wait(){

  int aNumber;
  //int time1;
  //int time2;
  char *arg;
  long int time1=0;
  long int time2=0;

  time1 = millis();
  time2 = time1;

  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atoi(arg);
    //Serial.println(aNumber);
    //wait amount of time
    while ((time1 - time2) < aNumber) {
    time1 = millis();
     } //done waiting


  }//if
  waited();
  }//time_wait


/////////////////////////////////////////



void sayHello() {

  char *arg;
  arg = sCmd.next();    // Get the next argument from the SerialCommand object buffer
  if (arg != NULL) {    // As long as it existed, take it
    Serial.print("Hello ");
    Serial.println(arg);
  }
  else {
    Serial.println("Hello, whoever you are");
  }
}


void processCommand() {
  int aNumber;
  char *arg;

  Serial.println("We're in processCommand");
  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atoi(arg);    // Converts a char string to an integer
    Serial.print("First argument was: ");
    Serial.println(aNumber);
  }
  else {
    Serial.println("No arguments");
  }

  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atol(arg);
    Serial.print("Second argument was: ");
    Serial.println(aNumber);
  }
  else {
    Serial.println("No second argument");
  }
}

// This gets set as the default handler, and gets called when no other command matches.
void unrecognized(const char *command) {
  Serial.println("What?");
}

void waited(){
  Serial.println("d");
  }
