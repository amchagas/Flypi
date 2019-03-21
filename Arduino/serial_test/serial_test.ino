// Demo Code for SerialCommand Library
// Steven Cogswell
// May 2011

// Import libraries
#include <Servo.h> //servo motor controlling the autofocus
#include <SerialCommand.h>

#include "peltier.h"
#include "ring.h"

//#define arduinoLED 13   // Arduino LED on board

// define ports
#define LED1Pin 10
#define LED2Pin 11 // NOT CONFIGURED

#define servoPin 8
#define servoOnPin 9
//#define peltierEnablePin 13



//Timing Variables////////////////////////
long int millistowait;

//create servo object ****************//
Servo focusServo;
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
  //if (peltOn==1){
  //HoldTemp(newTemp, tempSensorPin,
//               peltierCoolPin1, peltierHeatPin1);
  
  //Serial.print("target: " );
  //Serial.println(newTemp);
  //Serial.print("current: ");
  //Serial.println(checkTemp(tempSensorPin));
  //}//if
               
  sCmd.readSerial();     // We don't do much, just process serial commands
  
}// void loop


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
  //pixels.show();
  
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
  Serial.println("LED2 on");
  digitalWrite(LED2Pin, HIGH);
  waited();
}

void LED2_off() {
  Serial.println("LED2 off");
  digitalWrite(LED2Pin, LOW);
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
