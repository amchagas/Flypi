/*this is a small test suite for the flypi.
  it is mainly used to make sure all parts connected to the 
  arduino are working properly. It acomplishes that by 
  turning each component on and off individually
  
  Written by A. Chagas and T. Baden*/
  
//import libraries for the LED ring
#include <Adafruit_NeoPixel.h> // LED Ring

//set pins
int tempPin=A7;
int tempRead=0;
int RedGBPin = 6;
int RGreenBPin = 4;
int RGBluePin = 5;
int RingPin = 7;
int peltierHeat1 =3;
int peltierHeat2 =13;
int peltierCool1 =2;
int peltierCool2 =12;

//set the number of LEDs in the ring
int Ring_nPixels = 12;
//create function to control LED ring
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(Ring_nPixels, RingPin, NEO_GRB + NEO_KHZ800);

//things that are ran once
void setup (){
  //set the mode for the pins
  pinMode(RedGBPin,OUTPUT);
  pinMode(RGreenBPin,OUTPUT);
  pinMode(RGBluePin,OUTPUT);
  pinMode(peltierHeat1,OUTPUT);
  pinMode(peltierHeat2,OUTPUT);
  pinMode(peltierCool1,OUTPUT);
  pinMode(peltierCool2,OUTPUT);
  

  //initialize NeoPixel library (LED Ring).
  pixels.begin(); 
  //begin the serial port
  Serial.begin(9600);}

//start infinite loop
void loop (){
  
  //make sure everything is off
  digitalWrite(RedGBPin,LOW);
  digitalWrite(RGreenBPin,LOW);
  digitalWrite(RGBluePin,LOW);
  digitalWrite (peltierHeat1,LOW);
  digitalWrite (peltierHeat2,LOW);
  digitalWrite (peltierCool1,LOW);
  digitalWrite (peltierCool2,LOW);
  
  //test thermistor
  Serial.println("test temp sensor");
  for (int i=0; i<5;i+=1){
    //read the analog pin
    tempRead=analogRead(tempPin);
    //print it out for user
    Serial.println(tempRead);
    //1.5 sec interval
    delay(1500);}

  //test RGB
  Serial.println("test rgb led");
  digitalWrite(RedGBPin,HIGH);
  delay(500);
  digitalWrite(RedGBPin,LOW);
  delay(500);
  digitalWrite(RGreenBPin,HIGH);
  delay(500);
  digitalWrite(RGreenBPin,LOW);
  delay(500);
  digitalWrite(RGBluePin,HIGH);
  delay(500);
  digitalWrite(RGBluePin,LOW);
  delay(500);

  //test led ring
  Serial.println("test led ring");
    //change all LEDs in ring
    for (int i = 0; i < Ring_nPixels; i = i+1) { 
      // dim white
      pixels.setPixelColor(i, pixels.Color(5,5,5)); 
    }      
  // sends updated pixel color to hardware.  
  pixels.show(); 
  delay(500);
  for (int i = 0; i < Ring_nPixels; i = i+1) { 
    // dim white
    pixels.setPixelColor(i, pixels.Color(0,0,0)); 
   }      
  // sends updated pixel color to hardware.
  pixels.show(); 
  delay(500);

  //test peltier
  Serial.println("test peltier");

  //make it heat up and cool down three times
  for (int i=0;i<3;i+=1){
    //turn on the heat (assuming peltier has the correct side up)
    digitalWrite (peltierHeat1,HIGH);
    digitalWrite (peltierHeat2,HIGH);
    delay(2000);

    Serial.print("temperature: ");
    //print out temperature as read out by analog pin
    //make sure temperature sensor is working, before
    //blindly trusting these values
    Serial.println(analogRead(tempPin));
    //turn off the heat
    digitalWrite (peltierHeat1,LOW);
    digitalWrite (peltierHeat2,LOW);
    delay(1000);
    //turn on the cooling
    digitalWrite (peltierCool1,HIGH);
    digitalWrite (peltierCool2,HIGH);
    delay(2000);
    Serial.print("temperature: ");
    //print out temperature as read out by analog pin
    //make sure temperature sensor is working, before
    //blindly trusting these values
    Serial.println(analogRead(tempPin));
    //turn off the cooling
    digitalWrite (peltierCool1,LOW);
    digitalWrite (peltierCool2,LOW);
    }

}//end void loop
