#include <SerialCommand.h>


#define RedGBPin 6
#define RGreenBPin 4
#define RGBluePin 5
#define peltierEnablePin 13
#define peltierHeatPin1 3
#define peltierCoolPin1 2
#define tempSensorPin A7


//PELTIER variables ////////////////////////

float currTemp;
float newTemp;
float TempTol = 0.5; // tolerance
float highLimit = 40.0; //in Celsius
float lowLimit = 13.0; //in Celsius
int peltOn=0;


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

}//float







void PELT_on(){
  peltOn=1;
  digitalWrite(peltierEnablePin,HIGH);
  Serial.println("pelton");
}//pelt on


void PELT_off(){
  peltOn=0;
  digitalWrite(peltierEnablePin,LOW);
  digitalWrite(peltierHeatPin1, LOW);
  digitalWrite(peltierCoolPin1, LOW);
  analogWrite(RedGBPin, 0);
  analogWrite(RGreenBPin, 0);
  analogWrite(RGBluePin, 0);
  //Serial.println("peltoff");
}//pelt off


    



void TEMP_read(){
  currTemp = checkTemp(tempSensorPin);
  Serial.print("temp: ");
  Serial.println(currTemp);
}//temp read







float HoldTemp(float finalTemp, int tempSensorPin,
               int peltierCoolPin2, int peltierHeatPin2) {
  float temperature, temps;


  temperature = checkTemp(tempSensorPin);
  //Serial.print("temp: ");
  //Serial.println(temperature);
  //Serial.println(temperature);

  if (temperature < (finalTemp - TempTol)) {
    //digitalWrite(peltierEnablePin,HIGH);
    digitalWrite(peltierHeatPin2, HIGH);
    digitalWrite(peltierCoolPin2, LOW);
    analogWrite(RedGBPin, 255);
    analogWrite(RGreenBPin, 0);
    analogWrite(RGBluePin, 0);
  }//end if temperature<finalTemp
  if (temperature > (finalTemp + TempTol)) {
    //digitalWrite(peltierEnablePin,HIGH);
    digitalWrite(peltierHeatPin2, LOW);
    digitalWrite(peltierCoolPin2, HIGH);
    analogWrite(RedGBPin, 0);
    analogWrite(RGreenBPin, 0);
    analogWrite(RGBluePin, 255);
  }//end if temperature > finaTemp

  if ((temperature <= (finalTemp + TempTol)) && (temperature >= (finalTemp - TempTol))) {
    //digitalWrite(peltierEnablePin,LOW);
    //Serial.println("temp reached!");

    digitalWrite(peltierHeatPin2, LOW);
    digitalWrite(peltierCoolPin2, LOW);
    analogWrite(RGreenBPin, 255);
    analogWrite(RedGBPin, 0);
    analogWrite(RGBluePin, 0);

  }// end if temperature < finalTemp && temperature>finalTemp



}


