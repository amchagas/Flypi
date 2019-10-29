






#define RingPin 7

int ring_nPixels = 12;
int ringOn = 0;
int ringRedHue = 10;
int ringGreenHue = 10;
int ringBlueHue = 10;
int zapRed = 0;
int zapGreen = 0;
int zapBlue = 0;
int zapWhite = 0;
int ringBright = 0;



//create function to control LED ring/////////
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(ring_nPixels, RingPin, NEO_GRB + NEO_KHZ800);




/////////ring functions //////////////////////////////
void updateRing(int hue1, int hue2, int hue3, int ringOn) {
  for (int i = 0; i < ring_nPixels; i++) {
    pixels.setPixelColor(i, pixels.Color(hue1, hue2, hue3));
    
  }//for
  if (ringOn==1){
    pixels.show();
    }//if
}//void
