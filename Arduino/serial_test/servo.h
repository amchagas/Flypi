

#include <Servo.h> //servo motor controlling the autofocus
#include <SerialCommand.h>

#define servoPin 8
#define servoOnPin 9




int servoOn = 0;



//create servo object ****************//
Servo focusServo;
