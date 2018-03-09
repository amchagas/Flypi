# Flypi

#### This is the repository for the flypi project 




### Users interested in the release described in the Plos Biology Paper (http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2002702) should follow this link: https://github.com/amchagas/Flypi/tree/v1.0.0 

### further development is being done on the following fork: https://github.com/prometheus-science/Flypi/commit/ac9aac55044f0e4dddc3e00e41459db75cc05826 They will be incorporated as releases here once they are stable.

### We've created a Forum for users to posts questions and suggestions too! Please take a look at http://forum.prometheus-science.com/home/categories/flypi-user-forum 

## necessary libraries:

LED Ring from Adafruit:
https://github.com/adafruit/Adafruit_NeoPixel

LED Matrix from Adafruit:
https://github.com/adafruit/Adafruit-LED-Backpack-Library


gpac library:
sudo apt-get update
sudo apt-get install gpac

libav library:
sudo apt-get update
sudo apt-get install libav-tools


update pyserial library:
sudo pip3 install --upgrade serial

## *.h264 conversion to *.avi:



## *.h264 conversion to *.avi:

is done via avconv (which is installed with libav-tools).

## SD Card image containing Raspian image with all things installed:
https://www.dropbox.com/sh/bibhy2sgadq30dm/AACD2Rdhmad2QdBi9q-pQfd6a?dl=0

## outdated:
## conversion from h264 to mp4 ()
MP4Box -add filename.h264 filename.mp4

//from here we need to convert it to a series of images (like *.avi) to be read on 
//imagej. We are doing this right now using a software called streamclip, that unfortunately does not work on linux. --> we are going to find a better solution for this!
##d end of outdated
