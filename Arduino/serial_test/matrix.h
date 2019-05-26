
//#define matrix1pin A4
//#define matrix2pin A5

#include <Wire.h> // LED Matrix
#include <Adafruit_LEDBackpack.h> // LED Matrix
#include <Adafruit_GFX.h> // LED Matrix

Adafruit_8x8matrix matrix = Adafruit_8x8matrix();



int matrixOn = 0;
int matrix_brightness=1;

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

void updateMatrix(int brightness, int matOn){  
  matrix.setBrightness(brightness);
  if (matOn == 1){
    matrix.writeDisplay();
    }//if
  }
