// Demo Code for SerialCommand Library
// Steven Cogswell
// May 2011

// Import libraries
#include <Adafruit_NeoPixel.h> // LED Ring
#include <Wire.h> // LED Matrix
#include <Adafruit_LEDBackpack.h> // LED Matrix
#include <Adafruit_GFX.h> // LED Matrix
#include <Servo.h> //servo motor controlling the autofocus
#include <SerialCommand.h>

//#define arduinoLED 13   // Arduino LED on board

// define ports
#define LED1Pin 10
#define LED2Pin 11 // NOT CONFIGURED
#define RedGBPin 6
#define RGreenBPin 4
#define RGBluePin 5
#define RingPin 7
#define servoPin 8
#define servoOnPin 9
#define peltierEnablePin 13
#define peltierHeatPin1 3
#define peltierCoolPin1 2
#define tempSensorPin A7

//Timing Variables////////////////////////
long int millistowait;


//////////////////////////////////////////

//RING variables//////////////////////////
int ring_nPixels = 12;
int ringOn = 0;
int ringRedHue = 10;
int ringGreenHue = 10;
int ringBlueHue = 10;
int zapRed = 0;
int zapGreen = 0;
int zapBlue = 0;
int zapWhite = 0;
int ringBright = 0;

//create function to control LED ring/////////
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(ring_nPixels, RingPin, NEO_GRB + NEO_KHZ800);
//////////////////////////////////////////////


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
  sCmd.addCommand("L11",    LED1_on);          // Turns LED1 on
  sCmd.addCommand("L10",    LED1_off);         // Turns LED1 off
  sCmd.addCommand("L21",    LED2_on);          // Turns LED2 on
  sCmd.addCommand("L20",    LED2_off);         // Turns LED2 off
  sCmd.addCommand("R1",     RING_on);          // Turns RING on
  sCmd.addCommand("R0",     RING_off);         // Turns RING off
  sCmd.addCommand("RR",     RED);              // change RED intensity
  //sCmd.addCommand("RG",     GREEN);            // change GREEN intensity
  //sCmd.addCommand("RB",     BLUE);             // change BLUE intensity
  //sCmd.addCommand("P1",     PELT_on);          // Turns PELTIER on
  //sCmd.addCommand("P0",     PELT_off);         // Turns PELTIER off
  //sCmd.addCommand("PT",     PELT_stemp);       // Change PELTIER temperature
  //sCmd.addCommand("TR",     TEMP_read);        // reads temperature sensor
  sCmd.addCommand("TW",     TIME_wait);        // sets time to wait
  
  
  sCmd.addCommand("HELLO", sayHello);        // Echos the string argument back
  sCmd.addCommand("P",     processCommand);  // Converts two arguments to integers and echos them back
  sCmd.setDefaultHandler(unrecognized);      // Handler for command that isn't matched  (says "What?")
  Serial.println("Ready");
}

void loop() {
  sCmd.readSerial();     // We don't do much, just process serial commands
}// void loop

void updateRing(int hue1, int hue2, int hue3) {
  for (int i = 0; i < ring_nPixels; i++) {
    pixels.setPixelColor(i, pixels.Color(hue1, hue2, hue3));
  }
}


void LED1_on() {
  Serial.println("LED1 on");
  digitalWrite(LED1Pin, HIGH);
}

void LED1_off() {
  Serial.println("LED1 off");
  digitalWrite(LED1Pin, LOW);
}

void LED2_on() {
  Serial.println("LED2 on");
  digitalWrite(LED2Pin, HIGH);
}

void LED2_off() {
  Serial.println("LED2 off");
  digitalWrite(LED2Pin, LOW);
}

void RING_on() {
  Serial.println("ring on");
  pixels.show();
}

void RING_off() {
  Serial.println("ring off");
  updateRing(0, 0, 0);
  pixels.show();}


void RED(){
  int aNumber;
  char *arg;
  arg = sCmd.next();
  if (arg != NULL) {
     aNumber = atoi(arg);
     updateRing(aNumber, ringGreenHue, ringBlueHue);
  
  }//if

}//red

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
    //wait amount of time
    while ((time1 - time2) < aNumber) {
    time1 = millis();
     } //done waiting
    Serial.println("done");
    
  }//if
  
  }//time_wait

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
