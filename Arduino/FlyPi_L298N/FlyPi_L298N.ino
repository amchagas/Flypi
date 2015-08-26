//////////////////////////////////////////////////////
/// FLYPI Arduino control by A Chagas and T Baden  ///
/// 2015 Feb, v0.9                                 ///
//////////////////////////////////////////////////////
// Import libraries
#include <Adafruit_NeoPixel.h> // LED Ring
#include <Wire.h> // LED Matrix
#include <Adafruit_LEDBackpack.h> // LED Matrix
#include <Adafruit_GFX.h> // LED Matrix
Adafruit_8x8matrix matrix = Adafruit_8x8matrix();

// Define Pin allocations on Arduino
  //*********************************//
  int control_ledpin = 0;
  int LED1Pin = 10;
  int LED2Pin = 11; // NOT CONFIGURED
  int RedGBPin = 6;
  int RGreenBPin = 4;
  int RGBluePin = 5;
  int RingPin = 7;
  int peltierEnablePin = 13;
  int peltierHeatPin1 = 3;//12
  //int peltierHeatPin2 = 13;//12
  int peltierCoolPin1 = 2;//8
  //int peltierCoolPin2 = 12;//8
  //int HBridgePin = 12;
  int tempSensorPin = A7;//A5 

  int Ring_nPixels = 12;
  int tempToAnalog = 0;
  int analogOut = 0;
  float tempSensVolt = 0;
  float temperature = 0;
  
  unsigned long time1 = 0;
  unsigned long time2 = 0;

  //*********************************//
  int stimDurLight = 6000; //time in milliseconds
  int stimDurHeat = 30000;
  int interStimInterv = 1000; //time in milliseconds
  int numOfTrials = 5;
  float coldTemp = 19.0;//temperature in celsius
  float hotTemp = 29.0; //temperature in celsius
  float TempTol = 0.3; // tolerance 

  float coldTempEmergency = 16.0;//temperature in celsius
  float hotTempEmergency = 40.0; //temperature in celsius


  //********************************//
//create function to control LED ring
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(Ring_nPixels, RingPin, NEO_GRB + NEO_KHZ800);
//set all bytes for serial communication
byte RingModeButton =      0;
byte RingBrighterButton =  0;
byte RingDimmerButton =    0;
byte RingZapButton =       0;
byte RingZapColourButton = 0;
byte MatrixModeButton =    0;
byte MatrixBrighterButton =0;
byte MatrixDimmerButton =  0;
byte RingZapLong       =   0;
byte powerLED1 =           0;
byte powerLED2 =           0;
byte Peltier =             0;
byte flashLED =            0;

int RingBrightness = 1;
byte R_ON =       1;
byte G_ON =       1;
byte B_ON =       1;
int Zap_colour = 1; //[1:7 --> B R G RG RB BG RGB]
byte R_ON_zap =  0;
byte G_ON_zap =  0;
byte B_ON_zap =  1;
int Zap_duration = 500;

// for Rotation stimulus
int RING_rotate = 0;
float RING_rotate_speed = 0.5; // full turns per second
int RING_rotate_duration = 5; // in seconds
int RING_rotate_direction = 0;
int pixel_Pos = 0;
int state = 0;

// for LED ZAP / flash
int powerLED1_timer = 500; 
int powerLED2_timer = 500;
int flashLED_timer = 50;

boolean RING_ON = true;
byte ring_mode =      0;
boolean MATRIX_ON = false;
byte matrix_mode = 0;
byte matrix_brightness = 1; // 0-15
byte matrix_pattern = 0;

boolean Peltier_ON = false;

int LoopDelay = 10; // mainloop delay

int SerialCommand1;
int SerialCommand2;

//matrix stimuli
static const uint8_t PROGMEM // MATRIX PICS
matrix_pattern1[] =
  { B00001111,
    B00001111,
    B00001111,
    B00001111,
    B11110000,
    B11110000,
    B11110000,
    B11110000 },
matrix_pattern2[] =
  { B11110000,
    B11110000,
    B11110000,
    B11110000,
    B00001111,
    B00001111,
    B00001111,
    B00001111 };

////////////////////////////////////////////////////////////////////////////////////

//run things once
void setup(){ 
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
  
  //set the analog output scale depending 
  //on the temperature range used
  tempToAnalog = 255/((hotTemp-coldTemp)+20);

  // begin serial communication
  Serial.begin(9600);
  //Serial.setTimeout(500);

  //  initialize NeoPixel library (LED Ring).
  pixels.begin(); 
  // pass in the address for LED Matrix
  matrix.begin(0x70);  

  }// END SETUP

//run things forever
void loop(){ 

  // SET ALL BUTTONS TO ZERO
  RingModeButton  =      0;
  RingBrighterButton =   0;
  RingDimmerButton =     0;
  RingZapButton =        0;
  RingZapColourButton =  0;
  MatrixModeButton =     0;
  MatrixBrighterButton = 0;
  MatrixDimmerButton =   0;
   
  //RingZapLong = 0;
  //powerLED1 = 0;
  //powerLED2 = 0;  
  //flashLED = 0;
  
  // LISTEN FOR SERIAL COMMANDS from GUI
  
  if(Serial.available() > 0) {
     int SerialCommand1 = Serial.parseInt(); 
    
    // addressing LED ring
    if (SerialCommand1==11) { RingModeButton =       1; }  
    if (SerialCommand1==12) { RingBrighterButton =   1; }  
    if (SerialCommand1==13) { RingDimmerButton =     1; } 
    if (SerialCommand1==14) { RingZapButton =        1; } 
    if (SerialCommand1==15) { RingZapColourButton =  1; } 
    if (SerialCommand1==16) { RingZapLong =    1; } 
    if (SerialCommand1==17) { RingZapLong =    0; } 
    if (SerialCommand1==18) { RING_rotate = 1; RING_rotate_direction = 0; } // Rotation1
    if (SerialCommand1==19) { RING_rotate = 1; RING_rotate_direction = 1; } // Rotation2
             
    // addressing power LED1
    if (SerialCommand1==21) { powerLED1 = 1; }  
    if (SerialCommand1==22) { powerLED1 = 0; }  
    if (SerialCommand1==23) { powerLED1 = 2; powerLED1_timer = 500; } 
 
    // addressing power LED2
    if (SerialCommand1==31) { powerLED2 = 1; }  
    if (SerialCommand1==32) { powerLED2 = 0; }  
    if (SerialCommand1==33) { powerLED2 = 2; powerLED2_timer = 500; } 
    
    // addressing Peltier
    if (SerialCommand1==41) { Peltier = 0; }  // OFF
    if (SerialCommand1==42) { // COLD
      Peltier = 1; 
      int SerialCommand2 = Serial.parseInt();   // reads ColdSet Temp from python GUI
      coldTemp = float(SerialCommand2);
    } 
    if (SerialCommand1==43) { // HOT
      Peltier = 2;
      int SerialCommand2 = Serial.parseInt();   // reads HotSet Temp from python GUI
      hotTemp = float(SerialCommand2); 
    } 
  
    // addressing LED Matrix
    if (SerialCommand1==51) { MatrixModeButton =       1; }  
    if (SerialCommand1==52) { MatrixBrighterButton =   1; }  
    if (SerialCommand1==53) { MatrixDimmerButton =     1; } 
 
    // MarkerLED Flashes
    if (SerialCommand1==91) { flashLED = 1; flashLED_timer = 100; } 
    if (SerialCommand1==92) { flashLED = 2; flashLED_timer = 100; } 
    if (SerialCommand1==93) { flashLED = 3; flashLED_timer = 100; }     
    
    
  
    // update Temp
    if (SerialCommand1==99) { // update Temp
      temperature = checkTemp(tempSensorPin);
      int temp_serial = temperature;      
      Serial.print(temp_serial,DEC);
    }// else { Serial.print("SC"); Serial.println(SerialCommand1,DEC); }
  }
  
  ////////////////////////////////////////////////////////
  // END SERIAL READ /////////////////////////////////////
  ////////////////////////////////////////////////////////
  
  // LED RING CONTROL //
  
  /// 1) MODE
  if (RingModeButton == 1) { ring_mode+=1;
    if (ring_mode>4) {ring_mode = 0;  }}
  if (ring_mode==0) { R_ON = 0; G_ON = 0; B_ON = 0; RING_ON = false; } // OFF
  if (ring_mode==1) { R_ON = 1; G_ON = 1; B_ON = 1; RING_ON = true; } // White
  if (ring_mode==2) { R_ON = 1; G_ON = 0; B_ON = 0; RING_ON = true; } // RED
  if (ring_mode==3) { R_ON = 0; G_ON = 1; B_ON = 0; RING_ON = true; } // Green
  if (ring_mode==4) { R_ON = 0; G_ON = 0; B_ON = 1; RING_ON = true; } // Blue 
  
  /// 2) BRIGHTNESS
  if (RingBrighterButton == 1) { RingBrightness+=10; 
    if (RingBrightness>255) {RingBrightness = 255;  }}
  if (RingDimmerButton == 1) { RingBrightness-=10; 
    if (RingBrightness<1) {RingBrightness = 1;  }}    
 
  /// 3) CHR ZAPPER
  if (RingZapButton == 1) {
    if (Zap_colour == 1) {R_ON_zap = 0; G_ON_zap = 0; B_ON_zap = 1;}
    if (Zap_colour == 2) {R_ON_zap = 1; G_ON_zap = 0; B_ON_zap = 0;}
    if (Zap_colour == 3) {R_ON_zap = 0; G_ON_zap = 1; B_ON_zap = 0;}
    if (Zap_colour == 4) {R_ON_zap = 1; G_ON_zap = 1; B_ON_zap = 0;}
    for (int i = 0; i < Ring_nPixels; i = i+1) {
       pixels.setPixelColor(i, pixels.Color(R_ON_zap*255,G_ON_zap*255,B_ON_zap*255)); // ADD BRIGHT BLUE
    }
    pixels.show(); // This sends the updated pixel color to the hardware.
    delay (Zap_duration);
  }
  
  /// 4) ZAP MODE
  if (RingZapColourButton == 1) { Zap_colour+=1; if (Zap_colour>4) { Zap_colour = 1; }}
    

  // 5) LED RING EXECUTE
  if (RING_ON == true && RingZapLong == 0 ) {
    if (RING_rotate==0) {
      for (int i = 0; i < Ring_nPixels; i = i+1) {  
         pixels.setPixelColor(i, pixels.Color(RingBrightness*R_ON,RingBrightness*G_ON,RingBrightness*B_ON)); // Normal
       }
    }       
    pixels.show(); // sends updated pixel color to hardware.
  }  
  if (RING_ON == true && RingZapLong == 1 ) {
    for (int i = 0; i < Ring_nPixels; i = i+1) {
       pixels.setPixelColor(i, pixels.Color(R_ON_zap*255,G_ON_zap*255,B_ON_zap*255)); // ZAP 
     }
    pixels.show(); // sends updated pixel color to hardware.
  }  
  if (RING_ON == false && RingZapLong == 1 ) {
    for (int i = 0; i < Ring_nPixels; i = i+1) {
       pixels.setPixelColor(i, pixels.Color(R_ON_zap*255,G_ON_zap*255,B_ON_zap*255)); // ZAP 
    }
    pixels.show(); // sends updated pixel color to hardware.
  }      
  if (RING_ON == false && RingZapLong == 0 ) {
    for (int i = 0; i < Ring_nPixels; i = i+1) {
       pixels.setPixelColor(i, pixels.Color(0,0,0)); // OFF
    }
    pixels.show(); // sends updated pixel color to hardware.
  }   
   
  // 5b) LED RING ROTATE
  if (RING_rotate==1) { // ROTATING RING
    int SwitchDelay = 1000/(Ring_nPixels*RING_rotate_speed); 
    int nSwitches = int(RING_rotate_duration * 1000/SwitchDelay); // goes for Rotate_duration seconds
    for (int j = 0; j < nSwitches; j = j+1) { 
       if (RING_rotate_direction==0) { state+=1; }
       if (RING_rotate_direction==1) { state-=1; }
       if (state>3) { state = 0; };
       if (state<0) { state = 3; };
       pixel_Pos = state;
      
       for (int i = 0; i < Ring_nPixels; i = i+1) { 
          pixel_Pos+=1;
          
          if (pixel_Pos == 1) { 
             pixels.setPixelColor(i, pixels.Color(RingBrightness/2*R_ON,RingBrightness/2*G_ON,RingBrightness/2*B_ON)); }// Rotate ON px 
          if (pixel_Pos == 2) { 
             pixels.setPixelColor(i, pixels.Color(RingBrightness*R_ON,RingBrightness*G_ON,RingBrightness*B_ON)); }// Rotate ON px 
          if (pixel_Pos == 3) { 
             pixels.setPixelColor(i, pixels.Color(RingBrightness/2*R_ON,RingBrightness/2*G_ON,RingBrightness/2*B_ON)); }// Rotate ON px 
          if (pixel_Pos == 4) {  // Rotate ON px 
             pixels.setPixelColor(i, pixels.Color(0,0,0));
             pixel_Pos = 0;
          }
       }
       pixels.show(); // sends updated pixel color to hardware.
       delay(SwitchDelay);
    }
    RING_rotate = 0;
  }     
    
  
  
  ////////////////////////////////////////////////////////////////////////
  
  // 6) POWER LED CONTROL ///
  if (powerLED1 == 2) {digitalWrite(LED1Pin,HIGH); delay(powerLED1_timer); powerLED1 = 0; }  
  if (powerLED1 == 1) {digitalWrite(LED1Pin,HIGH); } else { digitalWrite(LED1Pin,LOW); } 

  if (powerLED2 == 2) {digitalWrite(LED2Pin,HIGH); delay(powerLED2_timer); powerLED2 = 0; }  
  if (powerLED2 == 1) {digitalWrite(LED2Pin,HIGH); } else { digitalWrite(LED2Pin,LOW); } 

  ///////////////////////////////////////////////////////////////////////
  
  // 7) PELTIER
  if (Peltier == 0) { // KILL PELTIER
     Peltier_ON = false;   
     analogWrite(RedGBPin,0);
     analogWrite(RGreenBPin,0);
     analogWrite(RGBluePin,0);
     digitalWrite(peltierEnablePin,LOW);
     digitalWrite(peltierHeatPin1,LOW);
     //digitalWrite(peltierHeatPin2,LOW);
     digitalWrite(peltierCoolPin1,LOW);
     //digitalWrite(peltierCoolPin2,LOW);
  }
  if (Peltier == 1) { // GO TO LOW T
   Peltier_ON = true;
   HoldTemp(coldTemp,tempSensorPin, peltierEnablePin,peltierCoolPin1,peltierHeatPin1,tempToAnalog);
  }  
  if (Peltier == 2) { // GO TO HIGH T
    Peltier_ON = true; 
    HoldTemp(hotTemp,tempSensorPin, peltierEnablePin,peltierCoolPin1,peltierHeatPin1,tempToAnalog);
  }    
  ///////////////////////////////////////////////////////////////////////
  
  // 10) LED Matrix

  
  /// 1) Read Matrix Mode
  if (MatrixModeButton == 1) { matrix_mode+=1; if (matrix_mode>3) {matrix_mode = 0;}}
  if (matrix_mode==0) { MATRIX_ON = false; } // OFF
  if (matrix_mode>0) { matrix_pattern = 1; MATRIX_ON = true; } // 
  
  /// 2) Read Matrix Brightness
  if (MatrixBrighterButton == 1) { matrix_brightness+=1;
    if (matrix_brightness>15) {matrix_brightness = 15;  }}
  if (MatrixDimmerButton == 1) { matrix_brightness-=1;
    if (matrix_brightness<1) {matrix_brightness = 1;  }}  
    
  /// EXECUTE MATRIX  
  if (MATRIX_ON == true) {
     matrix.setBrightness(matrix_brightness);
     if (matrix_mode == 1) { // quartiles1
       matrix.clear();
       matrix.drawBitmap(0, 0, matrix_pattern1, 8, 8, LED_ON);
       matrix.writeDisplay(); // write changes to the display
     }
     if (matrix_mode == 2) { // quartiles2
       matrix.clear();
       matrix.drawBitmap(0, 0, matrix_pattern2, 8, 8, LED_ON);
       matrix.writeDisplay(); // write changes to the display
     }
     if (matrix_mode == 3) { // Stripes
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
         delay(100); }
     }
  } else { // ie Matrix not ON
    matrix.clear();
    matrix.writeDisplay(); // write changes to the display
    
  }   
  
  ///////////////////////////////////////////////////////////////////////
  
  // 9) Flash LEDs
  if (flashLED == 1) {analogWrite(RedGBPin,255); delay(flashLED_timer); analogWrite(RedGBPin,0); flashLED = 0; } // RED
  if (flashLED == 2) {analogWrite(RGreenBPin,255); delay(flashLED_timer); analogWrite(RGreenBPin,0); flashLED = 0; } // GREEN
  if (flashLED == 3) {analogWrite(RGBluePin,255); delay(flashLED_timer); analogWrite(RGBluePin,0); flashLED = 0; } // Blue  
  
  ///////////////////////////////////////////////////////////////////////
  
  delay(LoopDelay);
} // END MEIN LOOP


/////////////////////////////////////
/// MANUAL PELTIER Control

float HoldTemp(float finalTemp,int tempSensorPin,int peltierEnablePin,int peltierCoolPin1,int peltierHeatPin1,int tempToAnalog){
   float temperature, temps;
   int analogOut;
   temperature = checkTemp(tempSensorPin); 
   analogOut = convert_analog(coldTemp,temperature,tempToAnalog);
   
   if (temperature>hotTempEmergency){Peltier_ON = false; }      
   if (temperature<coldTempEmergency){Peltier_ON = false; }      
      
   if (Peltier_ON == true ) {
     if (temperature<finalTemp-TempTol){ 
       digitalWrite(peltierEnablePin,HIGH);
       digitalWrite(peltierHeatPin1,HIGH);
       //digitalWrite(peltierHeatPin2,HIGH);
       digitalWrite(peltierCoolPin1,LOW);
       //digitalWrite(peltierCoolPin2,LOW);
       analogWrite(RedGBPin,255);
       analogWrite(RGreenBPin,0);
       analogWrite(RGBluePin,0);
     }
     if (temperature>finalTemp+TempTol){
       digitalWrite(peltierEnablePin,HIGH);
       digitalWrite(peltierHeatPin1,LOW);
       //digitalWrite(peltierHeatPin2,LOW);
       digitalWrite(peltierCoolPin1,HIGH);
       //digitalWrite(peltierCoolPin2,HIGH);
       analogWrite(RedGBPin,0);
       analogWrite(RGreenBPin,0);
       analogWrite(RGBluePin,255);
     }
     if (temperature<finalTemp+TempTol && temperature>finalTemp-TempTol  ){
       //digitalWrite(peltierHeatPin,LOW);
       //digitalWrite(peltierCoolPin,LOW);
       digitalWrite(peltierEnablePin,HIGH);
       digitalWrite(peltierHeatPin1,LOW);
       //digitalWrite(peltierHeatPin2,LOW);
       digitalWrite(peltierCoolPin1,LOW);
       //digitalWrite(peltierCoolPin2,LOW);
       analogWrite(RGreenBPin,255);
     
       if (finalTemp==hotTemp) { analogWrite(RedGBPin,50); }
       if (finalTemp==coldTemp) { analogWrite(RGBluePin,50); }
     }
   }  
}






///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////

//function to convert the input temp signal and convert to analog out
//this function might be obsolete and might disappear in future iterations
int convert_analog(float minTemp, float temp,int tempToAnalog){
  int analogOut = (temp-minTemp)*tempToAnalog;
  return analogOut;}
  
// function to get the temperature in °C by reading the AD22100 output
//to the analog in
float checkTemp(int pinToRead){
  float temps;
  float volts;
  int baseLine;  
  baseLine = analogRead(pinToRead);
  //temps = ((baseLine*(5.0 / 1023.0)) - 1.375) / 0.0225;
  //convert the value into volts
  volts = (baseLine/1023.0) * 5;
  //convert the volt value into temperature (celsius)
  // the AD22100 has 200°C span (-50 to 150) for 4.5 V
  //therefore we need to subtract -1.375 to compensate 
  //for this -50° offset
  temps = (volts - 1.375) / 0.0225;
  //return the result of the function
  return temps; 
}

//function to send increasing voltage commands to the analog out port
//this is used to calibrate the camera using different LED "brightnesses".
void calibrationLight(int LEDPin){
  analogWrite(LEDPin,63);//25% of light
  delay(10);
  analogWrite(LEDPin,127);//50% of light
  delay(10);
  analogWrite(LEDPin,190);//75% of light
  delay(10);
  analogWrite(LEDPin,255);//100% of light
  delay(10);
  analogWrite(LEDPin,0);//100% of light
  delay(10);
}
