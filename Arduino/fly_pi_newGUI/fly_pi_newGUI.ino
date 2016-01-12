// Import libraries
#include <Adafruit_NeoPixel.h> // LED Ring
#include <Wire.h> // LED Matrix
#include <Adafruit_LEDBackpack.h> // LED Matrix
#include <Adafruit_GFX.h> // LED Matrix


// Define Pin allocations on Arduino
  //*********************************//
  unsigned int incomingData=0;
  unsigned int address=0;
  unsigned int correction=0;
//  int control_ledpin = 0;
  int LED1Pin = 10;
  int LED2Pin = 11; // NOT CONFIGURED
  int RedGBPin = 6;
  int RGreenBPin = 4;
  int RGBluePin = 5;
  int RingPin = 7;
  int peltierEnablePin = 13;
  int peltierHeatPin1 = 3;//12
  int peltierCoolPin1 = 2;//8
  int tempSensorPin = A7;//A5
  int startFlag = 0;
  //variables needed for peripherical functions
  //ring
  int ring_nPixels = 12;
  int ringOn=0;
  int ringRedHue = 0;
  int ringGreenHue = 0;
  int ringBlueHue = 0;
  int oldRed = 0;
  int oldGreen = 0;
  int oldBlue = 0;
  int ringBright = 0;
  int matBright = 0;
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
  //int stimDurLight = 6000; //time in milliseconds
  //int stimDurHeat = 30000;
  //int interStimInterv = 1000; //time in milliseconds
  //int numOfTrials = 5;
  //float coldTemp = 19.0;//temperature in celsius
  //float hotTemp = 29.0; //temperature in celsius
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
    B11110000 },
matrixPattern2[] =
  { B11110000,
    B11110000,
    B11110000,
    B11110000,
    B00001111,
    B00001111,
    B00001111,
    B00001111 };


void setup()
{ //start serial port
  Serial.begin(115200);
  //Serial.flush();
  //Serial.println("start.");
  //set digital pin modes
  pinMode(LED1Pin, OUTPUT); 
  pinMode(LED2Pin, OUTPUT); 
  pinMode(RedGBPin, OUTPUT);
  pinMode(RGreenBPin, OUTPUT);
  pinMode(RGBluePin, OUTPUT);
  pinMode(peltierEnablePin,OUTPUT);
  pinMode(peltierHeatPin1,OUTPUT);
  //pinMode(peltierHeatPin2,OUTPUT);
  pinMode(peltierCoolPin1,OUTPUT);
  //pinMode(peltierCoolPin2,OUTPUT);
  
  pixels.begin();
 
  // pass in the address for LED Matrix
  matrix.begin(0x70);
  matrix.clear();
  matrix.setBrightness(0); 
  matrix.writeDisplay();
  
}//end void setup
  
void loop(){ 

  if(Serial.available() > 0) {
    //store data into a variable
    incomingData = Serial.parseInt();
    //Serial.println(incomingData);
  }
  
    if (incomingData<1000){
      //check temp sensor
      if(incomingData==99){
        temperature=checkTemp(tempSensorPin);
        Serial.println(temperature);
        if (peltOn==1){
          HoldTemp(newTemp,tempSensorPin,peltierCoolPin1,peltierHeatPin1);}
        if (temperature>=highLimit || temperature<=lowLimit){
          digitalWrite (peltierEnablePin,LOW);
          digitalWrite(peltierHeatPin1,LOW);
          digitalWrite(peltierCoolPin1,LOW);
          digitalWrite(RedGBPin,HIGH);
          digitalWrite(RGreenBPin,HIGH);
          digitalWrite(RGBluePin,HIGH);
          peltOn=0; 
          //newTemp = (highLimit+lowLimit)/2; 
      }//end if temperature >=...
    }//end if incomingData==99
      //LED1
      if(incomingData==31){digitalWrite(LED1Pin,HIGH);}
      if(incomingData==32){digitalWrite(LED1Pin,LOW);}
      //LED2
      if(incomingData==35){digitalWrite(LED2Pin,HIGH);}
      if(incomingData==36){digitalWrite(LED2Pin,LOW);} 

      //MATRIX
      if (incomingData==40){//matrix off
        matrix.clear();
        matrix.writeDisplay();} // write changes to the display
      if (incomingData==41){// matrix pattern1
       matrix.clear();
       matrix.drawBitmap(0, 0, matrixPattern1, 8, 8, LED_ON);
       matrix.writeDisplay();} // write changes to the display
     
      if (incomingData==42){//matrix pattern2
        matrix.clear();
        matrix.drawBitmap(0, 0, matrixPattern2, 8, 8, LED_ON);
        matrix.writeDisplay();}
      if (incomingData==39){
        for (int j=0; j<2 ; j=j+1){
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
          matrix.writeDisplay(); // write changes to the display
         time1=millis();
         time2=time1;
         while(time2-time1<100){time2=millis();}//end while
         }//end for i
       }//end for j
      }//end if incomingData==39
         
      //RING         
      if (incomingData==44){//ring on
          incomingData=0;
          //Serial.println("ringOn");
          ringOn=1;
          updateRing(ringRedHue,ringGreenHue,ringBlueHue);
          pixels.show();}
      if (incomingData==45){//ring off
          incomingData=0;
          ringOn=0;
          updateRing(0,0,0);
          pixels.show();}
          
      //PELTIER
      if (incomingData==53){//Peltier on
        digitalWrite(peltierEnablePin,HIGH);
        peltOn = 1;}      
      if (incomingData==54){//Peltier off
        digitalWrite(peltierEnablePin,LOW);
        digitalWrite(peltierHeatPin1,LOW);
        digitalWrite(peltierCoolPin1,LOW);
        digitalWrite(RedGBPin,LOW);
        digitalWrite(RGreenBPin,LOW);
        digitalWrite(RGBluePin,LOW);
        peltOn = 0;}      
                   
      }//end if incoming data<100
    else{//if incoming data >1000
      //if the incoming data is bigger than 1000
      // we will have "graded values", such as brightness,
      //temperature, velocities and etc.
      //In this part of the code, we deal with this values

      //get the biggest two digits in the number
      address=incomingData*0.001;
      
      //get the three remaining digits in the number
      //our actual graded value
      correction=incomingData-(address*1000);
      //set the incoming data to zero
      incomingData=0;
      
//      //MATRIX
//      if (address==43){//matrix brightness slider
//        //set brightness of the matrix
//        //if (correction==0){
//         //matrix.clear();
//         //matrix.writeDisplay();}
//        //else{
//        matrix.setBrightness(correction);}//}
//      if (address==34){Serial.println("led1zap: ");}
//      if (address==38){Serial.println("led2zap: ");}
     
     
      //RING

      if(address==49){//ring red
        oldRed= ringRedHue;
        //set the brightness of the red channel
        ringRedHue=correction;
        updateRing(ringRedHue,ringGreenHue,ringBlueHue);
        if(ringOn==1){//if the ring is on
          //and show the updat
          pixels.show();}//end if ringOn==1
        }//end if address==49


      if (address==50){//ring green
        //set the brightness of the green channel
        oldGreen= ringGreenHue;       
        ringGreenHue=correction;
        updateRing(ringRedHue,ringGreenHue,ringBlueHue);
        if(ringOn==1){
          pixels.show();}}
          
      if (address==46){//ring blue
        oldBlue= ringBlueHue;
        ringBlueHue=correction;
          updateRing(ringRedHue,ringGreenHue,ringBlueHue);
        if(ringOn==1){      
          pixels.show();}}
      if (address==51){//ring all together
        ringBlueHue=correction;
        ringGreenHue=correction;
        ringRedHue=correction;
          updateRing(ringRedHue,ringGreenHue,ringBlueHue);
        if(ringOn==1){pixels.show();}}
        
      if (address==52){//ring zap
          if(ringOn==1){
          updateRing(ringRedHue,ringGreenHue,ringBlueHue);
          pixels.show();
          delay(correction);
          //Serial.println(oldRed);
          //measure time without blocking the arduino board
          //time1=millis();
          //time2=time1;
          //while(time2-time1<correction){time2=millis();}
          //Serial.println("done");
          //loop through all pixels in ring to update their colours
          updateRing(oldRed,oldGreen,oldBlue);
          //update ring hardware
          pixels.show();}//end if ring on
        }
     
      if (address==47){
      //ring rotation
        time1=millis();
        time2=time1;
        while(time2-time1<1000){
          time2=millis();
          if (correction>500){//check to see which side to turn
          for(int i=0;i<ring_nPixels;i=i+2){
            pixels.setPixelColor(i, pixels.Color(ringRedHue,ringGreenHue,ringBlueHue));
            if(i<ring_nPixels){pixels.setPixelColor(i+1,pixels.Color(0,0,0));}//end if
     
            }//end for   
         pixels.show();//update ring hardware
         delay(correction-450);
          for(int i=0;i<ring_nPixels;i=i+2){
            pixels.setPixelColor(i, pixels.Color(0,0,0));
            if(i<ring_nPixels){pixels.setPixelColor(i+1,pixels.Color(ringRedHue,ringGreenHue,ringBlueHue));}//end if
            }//end for
          pixels.show();//update ring hardware
          delay(correction-450);
        }//end if correction>500
        
        if(correction<500){
          for(int i=ring_nPixels;i>=0;i=i-2){
            pixels.setPixelColor(i, pixels.Color(0,0,0));
            if(i>0){pixels.setPixelColor(i+1,pixels.Color(ringRedHue,ringGreenHue,ringBlueHue));}//end if
     
            }//end for   
         pixels.show();//update ring hardware
         
         //Serial.print("correction: ");
         //Serial.println(correction);
         delay(correction-350);
          for(int i=ring_nPixels;i>=0;i=i-2){
            pixels.setPixelColor(i, pixels.Color(ringRedHue,ringGreenHue,ringBlueHue));
            if(i>0){pixels.setPixelColor(i+1,pixels.Color(0,0,0));}//end if
            }//end for
          pixels.show();//update ring hardware
          delay(correction-350);
        }//end else
        }//end while
          
        
      }//end if address==47
        

      if(address==55){
        newTemp=correction;}
       
       
//
address = 0;
correction = 0;
}//end else incomingData>1000
    }//end void loop
               



// function to get the temperature in °C by reading the AD22100 output
//to the analog in
float checkTemp(int pinToRead){
  float temps = 0;
  float volts;
  float baseLine;  
  for (int i=0; i<6; i++){
    baseLine = analogRead(pinToRead);
    //temps = ((baseLine*(5.0 / 1023.0)) - 1.375) / 0.0225;
    //convert the value into volts
    volts = baseLine * (4750.0/1024);
    //convert the volt value into temperature (celsius)
    // the AD22100 has 200°C span (-50 to 150) for 4.5 V
    //therefore we need to subtract -1.375 to compensate 
    //for this -50° offset
    temps = temps + ((volts - 1375) / 22.5);
    //delay(15);
  }//end for loop
    
  temps = temps/5.0;
    //return the result of the function
  return temps; 
}

/////////////////////////////////////
/// MANUAL PELTIER Control

float HoldTemp(float finalTemp,int tempSensorPin,
               int peltierCoolPin1,int peltierHeatPin1){
   float temperature, temps;
   temperature = checkTemp(tempSensorPin);
   //Serial.print("temp: ");
   //Serial.println(temperature);   
   //Serial.println(temperature);
   
     if (temperature<(finalTemp-TempTol)){ 
       //digitalWrite(peltierEnablePin,HIGH);
       digitalWrite(peltierHeatPin1,HIGH);
       digitalWrite(peltierCoolPin1,LOW);
       analogWrite(RedGBPin,255);
       analogWrite(RGreenBPin,0);
       analogWrite(RGBluePin,0);
     }//end if temperature<finalTemp
     if (temperature>(finalTemp+TempTol)){
       //digitalWrite(peltierEnablePin,HIGH);
       digitalWrite(peltierHeatPin1,LOW);
       digitalWrite(peltierCoolPin1,HIGH);
       analogWrite(RedGBPin,0);
       analogWrite(RGreenBPin,0);
       analogWrite(RGBluePin,255);
     }//end if temperature > finaTemp
     if ((temperature<=(finalTemp+TempTol)) && (temperature>=(finalTemp-TempTol))){
       //digitalWrite(peltierEnablePin,LOW);
       //Serial.println("temp reached!");
       digitalWrite(peltierHeatPin1,LOW);
       digitalWrite(peltierCoolPin1,LOW);
       analogWrite(RGreenBPin,255);
       analogWrite(RedGBPin,0);
       analogWrite(RGBluePin,0);
          }// end if temperature < finalTemp && temperature>finalTemp
       //if (finalTemp<temperature) { analogWrite(RedGBPin,50); }
       //if (finalTemp>temperature) { analogWrite(RGBluePin,50); }

     
}

void updateRing(int hue1,int hue2,int hue3){
  //Serial.println("update ring");
  for(int i=0;i<ring_nPixels;i++){
  pixels.setPixelColor(i, pixels.Color(hue1,hue2,hue3));} 
}

