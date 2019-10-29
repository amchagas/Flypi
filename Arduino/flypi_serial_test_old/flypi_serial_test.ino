unsigned int incomingData=0;
unsigned int address = 0;
unsigned int correction = 0;
unsigned int bytesAvail=0;
int temp=0;
int tempAdd=A0;
long int time1=0;
long int time2=0;
//int setTemp=0;

void setup() {
  Serial.begin(115200);
  Serial.flush();
  Serial.println("started port");
  
}

void loop() {
  // put your main code here, to run repeatedly: 
         // send data only when you receive data:
        //bytesAvail=Serial.available();
        if(Serial.available() > 0) {
                incomingData = Serial.parseInt();
                // say what you got:
                //Serial.print("I received: ");
                //Serial.println(incomingData);
                if (incomingData==99000){
                Serial.println ("starting protocol");}
                
                if (incomingData<1000){
                  if(incomingData==31){Serial.println("led1on");}
                  if(incomingData==32){Serial.println("led1off");}
                  if(incomingData==35){Serial.println("led2on");}
                  if(incomingData==36){Serial.println("led1off");}
                  if (incomingData==39){Serial.println("matrixon");}
                  if (incomingData==40){Serial.println("matrixoff");}
                  if (incomingData==41){Serial.println("matpattern1");}
                  if (incomingData==42){Serial.println("matpattern2");}
                  if (incomingData==44){Serial.println("ringOn");}
                  if (incomingData==45){Serial.println("ringOff");}
                  
                 }
                 else{                   
                   address=incomingData*0.001;
                   Serial.println(address);
                   if (address==43){Serial.println("matrix bright: ");}
                   if (address==34){Serial.println("led1zap: ");}
                   if (address==38){Serial.println("led2zap: ");}
                   if (address==52){Serial.println("RingZap: ");}
                   if(address==49){Serial.println("Ring red hue: ");}
                   if(address==50){Serial.println("Ring green hue: ");}
                   if(address==51){Serial.println("Ring blue hue: ");}
                   if(address==46){Serial.println("Ring bright: ");}
                   if(address==47){Serial.println("Ring rotation: ");}
                   if(address==55){Serial.println("peltier temp: ");}        
                   correction=incomingData-(address*1000);
                   Serial.println(correction);
            }
            
                  
                
        }
        temp=analogRead(A0);
        //Serial.print("temperature");
        Serial.println(temp);

        time1=millis();
        while(time2-time1<500){time2=millis();}
        
}
  /* events to detect
  matrix:
  pattern1
  pattern2
  brightness
  on 
  off
  
  ring
  on
  off
  zap
  zap dur
  red
  green
  blue
  brightness
  rot left
  rot right
  rot speed
  
  led1
  on 
  off
  zap
  zap dur*/
 
  

