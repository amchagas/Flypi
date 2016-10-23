// Import libraries
#include <Adafruit_NeoPixel.h> // LED Ring
#include <Wire.h> // LED Matrix
#include <Adafruit_LEDBackpack.h> // LED Matrix
#include <Adafruit_GFX.h> // LED Matrix
#include <Servo.h> //servo motor controlling the autofocus

//create servo object ****************//
Servo focusServo;

//************************************//
// Define Pin allocations on Arduino
//*********************************//
String token;
String term1;
String term2;
//String temporary;
int index;
unsigned int incomingData = 0;
//unsigned int address=0;
unsigned int correction = 0;
//  int control_ledpin = 0;
int LED1Pin = 10;
int LED2Pin = 11; // NOT CONFIGURED
int RedGBPin = 6;
int RGreenBPin = 4;
int RGBluePin = 5;
int RingPin = 7;
int servoPin = 8;
int servoOnPin = 9;
int peltierEnablePin = 13;
int peltierHeatPin1 = 3;//12
int peltierCoolPin1 = 2;//8
int tempSensorPin = A7;//A5
int startFlag = 0;

//variables needed for peripherical functions
//ring
int ring_nPixels = 12;
int ringOn = 0;
int ringRedHue = 10;
int ringGreenHue = 10;
int ringBlueHue = 10;
int zapRed = 0;
int zapGreen = 0;
int zapBlue = 0;
int ringBright = 0;
int matBright = 0;
int waitmils = 0;
//peltier
int peltOn = 0;
int tempToAnalog = 0;
int analogOut = 0;
float tempSensVolt = 0;
float temperature = 0;
float newTemp = 30.0;
unsigned long time1 = 0;
unsigned long time2 = 0;
//string incomingData1='';
//*********************************//
float TempTol = 0.5; // tolerance
float highLimit = 40.0; //in Celsius
float lowLimit = 13.0; //in Celsius

//********************************//



//create function to control LED ring
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(ring_nPixels, RingPin, NEO_GRB + NEO_KHZ800);
//create function to control matrix
Adafruit_8x8matrix matrix = Adafruit_8x8matrix();
//matrix stimuli
static const uint8_t PROGMEM // MATRIX PICS
matrixPattern1[] =
{ B00001111,
  B00001111,
  B00001111,
  B00001111,
  B11110000,
  B11110000,
  B11110000,
  B11110000
},
matrixPattern2[] =
{ B11110000,
  B11110000,
  B11110000,
  B11110000,
  B00001111,
  B00001111,
  B00001111,
  B00001111
};


void setup()
{ //start serial port
  Serial.begin(19200);
  //Serial.flush();
  //Serial.println("start.");
  //set digital pin modes
  pinMode(LED1Pin, OUTPUT);
  pinMode(LED2Pin, OUTPUT);
  pinMode(RedGBPin, OUTPUT);
  pinMode(RGreenBPin, OUTPUT);
  pinMode(RGBluePin, OUTPUT);
  pinMode(servoOnPin, OUTPUT);
  pinMode(peltierEnablePin, OUTPUT);
  pinMode(peltierHeatPin1, OUTPUT);
  //pinMode(peltierHeatPin2,OUTPUT);
  pinMode(peltierCoolPin1, OUTPUT);
  //pinMode(peltierCoolPin2,OUTPUT);
  focusServo.attach(servoPin);
  pixels.begin();

  // pass in the address for LED Matrix
  matrix.begin(0x70);
  matrix.clear();
  matrix.setBrightness(0);
  matrix.writeDisplay();
  digitalWrite(servoOnPin, LOW);
  //Serial.println("waited");
}//end void setup

void loop() {

  if (Serial.available() > 0) {
    
    token = Serial.readStringUntil('>');
    //delay(5);
    index = token.indexOf('<');
    term1 = token.substring(0,index);
    //Serial.println(term1);
    term2 = token.substring(index+1);
    //Serial.println(term2);
  }
    
  //timing
  if (term1 == "TIM") {
    //Serial.println(term2);
    waitmils = term2.toInt();
    waiting(waitmils);
    Serial.println("waited");
    }

  //check temp sensor
  if (term1 == "TEM") 
    {  temperature = checkTemp(tempSensorPin);
        if (term2.toInt()!=99){newTemp=term2.toInt();}
       Serial.println(temperature);
       if (peltOn == 1) {
          HoldTemp(newTemp, tempSensorPin, peltierCoolPin1, peltierHeatPin1);
    }

    if (temperature >= highLimit || temperature <= lowLimit) {
      digitalWrite (peltierEnablePin, LOW);
      digitalWrite(peltierHeatPin1, LOW);
      digitalWrite(peltierCoolPin1, LOW);
      digitalWrite(RedGBPin, HIGH);
      digitalWrite(RGreenBPin, HIGH);
      digitalWrite(RGBluePin, HIGH);
      peltOn = 0;
    }//end if temperature >=...
    Serial.println("waited");
  }//end if incomingData==99

  //***************SERVO******************////
  if (term1 == "SER") {
    if (term2.toInt() == 90) {
      digitalWrite(servoOnPin, LOW);
      
    }
    else {
      digitalWrite(servoOnPin, HIGH);
      focusServo.write(term2.toInt()); //because this is a cont. servo,
      //this will set the velocity, not the pos.
      delay(15);
      //correction = 0;
    }//else
  Serial.println("waited");}//end servo

  //////////////////////////////////////////////////
  //LED1
  if (term1 == "LD1") {
    if (term2.toInt()==1){digitalWrite(LED1Pin, HIGH);}
    if (term2.toInt() == 0) {digitalWrite(LED1Pin, LOW);}
  Serial.println("waited");}

  //LED2
  if (term1 == "LD2") {
    if (term2.toInt()==1){digitalWrite(LED2Pin, HIGH);}
    if (term2.toInt() == 0) {digitalWrite(LED2Pin, LOW);}
  Serial.println("waited");} 
 
  //MATRIX
  if (term1 == "MAT"){
    if (term2.toInt() == 0) { 
      //matrix off
      matrix.clear();
      matrix.writeDisplay();// write changes to the display
      } 
    if (term2.toInt() == 1) {
      // matrix pattern 1
      matrix.clear();
      matrix.drawBitmap(0, 0, matrixPattern1, 8, 8, LED_ON);
      matrix.writeDisplay();// write changes to the display
      } 

    if (term2.toInt() == 2) {
      //matrix pattern 2
      matrix.clear();
      matrix.drawBitmap(0, 0, matrixPattern2, 8, 8, LED_ON);
      matrix.writeDisplay();
      }

    if (term2.toInt() == 3) {
      //matrix pattern 3
      for (int j = 0; j < 2 ; j = j + 1) {
        for (int i = 0; i < 4; i = i + 1) {
          matrix.clear();
          if (i == 0) {
            matrix.drawLine(0, 0, 0, 7, LED_ON);  matrix.drawLine(1, 0, 1, 7, LED_ON);
            matrix.drawLine(4, 0, 4, 7, LED_ON);  matrix.drawLine(5, 0, 5, 7, LED_ON);
            }
          if (i == 1) {
            matrix.drawLine(1, 0, 1, 7, LED_ON);  matrix.drawLine(2, 0, 2, 7, LED_ON);
            matrix.drawLine(5, 0, 5, 7, LED_ON);  matrix.drawLine(6, 0, 6, 7, LED_ON);
            }
          if (i == 2) {
            matrix.drawLine(2, 0, 2, 7, LED_ON);  matrix.drawLine(3, 0, 3, 7, LED_ON);
            matrix.drawLine(6, 0, 6, 7, LED_ON);  matrix.drawLine(7, 0, 7, 7, LED_ON);
            }
          if (i == 3) {
            matrix.drawLine(3, 0, 3, 7, LED_ON);  matrix.drawLine(4, 0, 4, 7, LED_ON);
            matrix.drawLine(7, 0, 7, 7, LED_ON);  matrix.drawLine(0, 0, 0, 7, LED_ON);
            }
          matrix.writeDisplay(); // write changes to the display

          time1 = millis();
          time2 = time1;
          while (time2 - time1 < 100) {time2 = millis();}//end while
        }//end for i
      }//end for j
    }//end if incomingData==3
  Serial.println("waited");}//end if term1 == MAT
  
  if (term1=="MAB") {
    //set brightness of the matrix
    if (term2.toInt() == 0) {
      matrix.clear();
      matrix.writeDisplay();}
    else {
      matrix.setBrightness(term2.toInt());
      matrix.writeDisplay();}
    Serial.println("waited");}


  //RING
  if (term1=="RIN"){
    if (term2.toInt() == 1) { //ring on
      ringOn = 1;
      updateRing(ringRedHue, ringGreenHue, ringBlueHue);
      pixels.show();}
    if (term2.toInt() == 0) { //ring off
      incomingData = 0;
      ringOn = 0;
      updateRing(0, 0, 0);
      pixels.show();}
  Serial.println("waited");}//end if "RIN"


//  if (term1=="G"){
//    //oldRed = ringRedHue;
//    ringGreenHue=term2.toInt();
//    updateRing(ringRedHue, ringGreenHue, ringBlueHue);
//    pixels.show();
//  }//end if term1=="G"
//   if (term1=="B"){
//    //oldRed = ringRedHue;
//    ringBlueHue=term2.toInt();
//    updateRing(ringRedHue, ringGreenHue, ringBlueHue);
//    pixels.show();
//  }//end if term1=="G"
  
  if (term1=="RRE"){
    //oldRed = ringRedHue;
    ringRedHue=term2.toInt();
    updateRing(ringRedHue, ringGreenHue, ringBlueHue);
    if (ringOn == 1) { 
      //if the ring is on
      //show the update
      pixels.show();}//end if ringOn==1
  Serial.println("waited");}//end if term1=="RRE"


  if (term1 == "RGR") { //ring green
    //oldGreen = ringGreenHue;
    //set the brightness of the green channel
    ringGreenHue=term2.toInt();
    updateRing(ringRedHue, ringGreenHue, ringBlueHue);
    if (ringOn == 1) {
      pixels.show();}
  Serial.println("waited");}//end if term1== "RGR"

  if (term1 == "RBL") { //ring blue
    //oldBlue = ringBlueHue;
    ringBlueHue = term2.toInt();
    updateRing(ringRedHue, ringGreenHue, ringBlueHue);
    if (ringOn == 1) {pixels.show();}

  Serial.println("waited");}//end if RBL

  if (term1 == "RAL") { //ring all together
    ringBlueHue = term2.toInt();
    ringGreenHue = term2.toInt();
    ringRedHue = term2.toInt();
    updateRing(ringRedHue, ringGreenHue, ringBlueHue);
    if (ringOn == 1) {
      pixels.show();
    }
  Serial.println("waited");}

  if (term1=="RZAR") {zapRed = term2.toInt();Serial.println("waited");}
  if (term1=="RZAG") {zapGreen = term2.toInt();Serial.println("waited");}
  if (term1=="RZAB") {zapBlue = term2.toInt();Serial.println("waited");}
  if (term1=="RZAT") {    
    if (ringOn == 1) {
      updateRing(zapRed, zapGreen, zapBlue);
      pixels.show();
      waiting(term2.toInt());
      updateRing(ringRedHue, ringGreenHue, ringBlueHue);
      pixels.show();      
    }//end if ring on
  Serial.println("waited");}
      //zapRed = pow(2,zapRed);
//      zapGreen = term2.substring(4,7);
//      zapBlue = term2.substring(2,3);
    
    


  

  if (term1 == "RRT") { //ring rotation
    time1 = millis();
    time2 = time1;
    while (time2 - time1 < 1000) {
      time2 = millis();
      if (term2.toInt() > 500) { //check to see which side to turn
        for (int i = 0; i < ring_nPixels; i = i + 2) {
          pixels.setPixelColor(i, pixels.Color(ringRedHue, ringGreenHue, ringBlueHue));
          if (i < ring_nPixels) {
            pixels.setPixelColor(i + 1, pixels.Color(0, 0, 0)); //end if
          }

        }//end for
        pixels.show();//update ring hardware
        delay(term2.toInt() - 450);
        for (int i = 0; i < ring_nPixels; i = i + 2) {
          pixels.setPixelColor(i, pixels.Color(0, 0, 0));
          if (i < ring_nPixels) {
            pixels.setPixelColor(i + 1, pixels.Color(ringRedHue, ringGreenHue, ringBlueHue)); //end if
          }
        }//end for
        pixels.show();//update ring hardware
        delay(term2.toInt() - 450);
      }//end if correction>500

      if (term2.toInt() < 500) {
        for (int i = ring_nPixels; i >= 0; i = i - 2) {
          pixels.setPixelColor(i, pixels.Color(0, 0, 0));
          if (i > 0) {
            pixels.setPixelColor(i + 1, pixels.Color(ringRedHue, ringGreenHue, ringBlueHue)); //end if
          }

        }//end for
        pixels.show();//update ring hardware

        delay(term2.toInt() - 350);
        for (int i = ring_nPixels; i >= 0; i = i - 2) {
          pixels.setPixelColor(i, pixels.Color(ringRedHue, ringGreenHue, ringBlueHue));
          if (i > 0) {
            pixels.setPixelColor(i + 1, pixels.Color(0, 0, 0)); //end if
          }
        }//end for
        pixels.show();//update ring hardware
        delay(term2.toInt() - 350);
      }//end if correction<500
      //correction = 0;
    }//end while


  Serial.println("waited");
  }//end if address==RRT

  //PELTIER
  if (term1 == "PEL") { //Peltier on
  if (term2.toInt()==1){
    //incomingData = 0;
    digitalWrite(peltierEnablePin, HIGH);
    peltOn = 1;
  }
  
  if (term2.toInt() == 0) { //Peltier off
//    incomingData = 0;
    digitalWrite(peltierEnablePin, LOW);
    digitalWrite(peltierHeatPin1, LOW);
    digitalWrite(peltierCoolPin1, LOW);
    digitalWrite(RedGBPin, LOW);
    digitalWrite(RGreenBPin, LOW);
    digitalWrite(RGBluePin, LOW);
    peltOn = 0;
  }
  Serial.println("waited");}
  
  if (term1 == "PET") {newTemp = term2.toInt();
  Serial.println("waited");}

}//end void loop




// function to get the temperature in °C by reading the AD22100 output
//to the analog in
float checkTemp(int pinToRead) {
  float temps = 0;
  float volts;
  float baseLine;
  for (int i = 0; i < 6; i++) {
    baseLine = analogRead(pinToRead);
    //temps = ((baseLine*(5.0 / 1023.0)) - 1.375) / 0.0225;
    //convert the value into volts
    volts = baseLine * (4750.0 / 1024);
    //convert the volt value into temperature (celsius)
    // the AD22100 has 200°C span (-50 to 150) for 4.5 V
    //therefore we need to subtract -1.375 to compensate
    //for this -50° offset
    temps = temps + ((volts - 1375) / 22.5);
    //delay(15);
  }//end for loop

  temps = temps / 5.0;
  //return the result of the function
  return temps;
}

/////////////////////////////////////
/// MANUAL PELTIER Control

float HoldTemp(float finalTemp, int tempSensorPin,
               int peltierCoolPin1, int peltierHeatPin1) {
  float temperature, temps;
  temperature = checkTemp(tempSensorPin);
  //Serial.print("temp: ");
  //Serial.println(temperature);
  //Serial.println(temperature);

  if (temperature < (finalTemp - TempTol)) {
    //digitalWrite(peltierEnablePin,HIGH);
    digitalWrite(peltierHeatPin1, HIGH);
    digitalWrite(peltierCoolPin1, LOW);
    analogWrite(RedGBPin, 255);
    analogWrite(RGreenBPin, 0);
    analogWrite(RGBluePin, 0);
  }//end if temperature<finalTemp
  if (temperature > (finalTemp + TempTol)) {
    //digitalWrite(peltierEnablePin,HIGH);
    digitalWrite(peltierHeatPin1, LOW);
    digitalWrite(peltierCoolPin1, HIGH);
    analogWrite(RedGBPin, 0);
    analogWrite(RGreenBPin, 0);
    analogWrite(RGBluePin, 255);
  }//end if temperature > finaTemp
  if ((temperature <= (finalTemp + TempTol)) && (temperature >= (finalTemp - TempTol))) {
    //digitalWrite(peltierEnablePin,LOW);
    //Serial.println("temp reached!");
    digitalWrite(peltierHeatPin1, LOW);
    digitalWrite(peltierCoolPin1, LOW);
    analogWrite(RGreenBPin, 255);
    analogWrite(RedGBPin, 0);
    analogWrite(RGBluePin, 0);
  }// end if temperature < finalTemp && temperature>finalTemp
  //if (finalTemp<temperature) { analogWrite(RedGBPin,50); }
  //if (finalTemp>temperature) { analogWrite(RGBluePin,50); }


}

void updateRing(int hue1, int hue2, int hue3) {
  for (int i = 0; i < ring_nPixels; i++) {
    pixels.setPixelColor(i, pixels.Color(hue1, hue2, hue3));
  }
}

void waiting(int millistowait) {
  long int time3=0;
  long int time4=0;
  int flag = 1;
  int index;
  String token1;
  time3 = millis();
  time4 = time3;
  //wait amount of time
  while ((time4 - time3) < millistowait) {
    //Serial.flush();
    //Serial.println("waiting");
    //Serial.println(millistowait);
    time4 = millis();
    //Serial.println(time4);
  } //done waiting
  
  //handshake
//  while(flag==1){
//    Serial.println("waited");
//    token1=Serial.readStringUntil('>');
//    index = token.indexOf('<');
//    if (token.substring(0,index)=="END"){flag=0;}
//  }
  //Serial.flush();
}
