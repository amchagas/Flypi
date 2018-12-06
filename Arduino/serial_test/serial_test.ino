// Demo Code for SerialCommand Library
// Steven Cogswell
// May 2011

#include <SerialCommand.h>


#define arduinoLED 13   // Arduino LED on board
const int arraysize = 200;

SerialCommand sCmd;     // The demo SerialCommand object
char message[arraysize];
char temp;
//const char out;

void setup() {
  pinMode(arduinoLED, OUTPUT);      // Configure the onboard LED for output
  digitalWrite(arduinoLED, LOW);    // default to LED off

  Serial.begin(115200);

  // Setup callbacks for SerialCommand commands
  sCmd.addCommand("LED1ON",    LED1_on);          // Turns LED1 on
  sCmd.addCommand("LED1OFF",   LED1_off);         // Turns LED1 off
  sCmd.addCommand("LED1",      LED1_PWM);          // Turns LED on
  sCmd.addCommand("LED2ON",    LED2_on);          // Turns LED2 on
  sCmd.addCommand("LED2OFF",   LED2_off);         // Turns LED2 off
  sCmd.addCommand("HELLO", sayHello);        // Echos the string argument back
  sCmd.addCommand("PROT", protocol);
  sCmd.addCommand("P",     processCommand);  // Converts two arguments to integers and echos them back
  sCmd.setDefaultHandler(unrecognized);      // Handler for command that isn't matched  (says "What?")

  Serial.println("Ready");
}

void loop() {
  sCmd.readSerial();     // We don't do much, just process serial commands
}

void protocol() {
  Serial.println("protocol");
  char *arg;
  //char *test;
  temp = '9';
  //const char out;
  int i = 0;


  while (1) {

    //Serial.println(arg);
    arg = sCmd.next();
    if (arg==NULL){}
    for (i;i<=length(*arg);i++ ){
      message[i] = *arg[i];}
    i = i + length(*arg);
    if (i == arraysize) {
      i + 0;
      break;
    }//if i==arraysize

  }//while
  for (int j = 0; j < arraysize; j++) {
    //Serial.println(j);
    Serial.println(message[j]);


    if (message[j] == '9') {
      Serial.println("done.");
    }//if message[j]==1

  }
}//protocol


void LED1_on() {
  Serial.println("LED1 on");
  digitalWrite(arduinoLED, HIGH);
}

void LED1_off() {
  Serial.println("LED1 off");
  digitalWrite(arduinoLED, LOW);
}

void LED1_PWM() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  aNumber = atoi(arg);
  Serial.print("LED1 ");
  Serial.println(aNumber);

  //test=arg;
  digitalWrite(arduinoLED, LOW);
}

void LED2_on() {
  Serial.println("LED1 on");
  digitalWrite(arduinoLED, HIGH);
}

void LED2_off() {
  Serial.println("LED1 off");
  digitalWrite(arduinoLED, LOW);
}

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
