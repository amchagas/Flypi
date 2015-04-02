
#include <Adafruit_NeoPixel.h> // LED Ring

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


int Ring_nPixels = 12;
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(Ring_nPixels, RingPin, NEO_GRB + NEO_KHZ800);

void setup (){
  pinMode(RedGBPin,OUTPUT);
  pinMode(RGreenBPin,OUTPUT);
  pinMode(RGBluePin,OUTPUT);
  pinMode(peltierHeat1,OUTPUT);
  pinMode(peltierHeat2,OUTPUT);
  pinMode(peltierCool1,OUTPUT);
  pinMode(peltierCool2,OUTPUT);
  
  pixels.begin(); //  initialize NeoPixel library (LED Ring).
  Serial.begin(9600);}

void loop (){
//test thermistor
tempRead=analogRead(tempPin);
Serial.println("test temp sensor");
for (int i=0; i<5;i+=1){
Serial.println(tempRead);
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
for (int i = 0; i < Ring_nPixels; i = i+1) { 
   pixels.setPixelColor(i, pixels.Color(5,5,5)); // dim white
}      
pixels.show(); // sends updated pixel color to hardware.
delay(500);
for (int i = 0; i < Ring_nPixels; i = i+1) { 
   pixels.setPixelColor(i, pixels.Color(0,0,0)); // dim white
}      
pixels.show(); // sends updated pixel color to hardware.
delay(500);

//test peltier
Serial.println("test peltier");
digitalWrite (peltierHeat1,LOW);
digitalWrite (peltierHeat2,LOW);
digitalWrite (peltierCool1,LOW);
digitalWrite (peltierCool2,LOW);

//
for (int i=0;i<3;i+=1){
digitalWrite (peltierHeat1,HIGH);
digitalWrite (peltierHeat2,HIGH);
delay(2000);
digitalWrite (peltierHeat1,LOW);
digitalWrite (peltierHeat2,LOW);
delay(1000);
digitalWrite (peltierCool1,HIGH);
digitalWrite (peltierCool2,HIGH);
delay(2000);
digitalWrite (peltierCool1,LOW);
digitalWrite (peltierCool2,LOW);
}


}
