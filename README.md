# Flypi
This is the repository for the flypi project. If you are looking for the original version of this device, as published in http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2002702, please go to the following fork: https://github.com/amchagas/Flypi


### If you have questions or comments about this device and its applications, please take a look at the User Forum: http://forum.prometheus-science.com/home/categories/flypi-user-forum

# necessary libraries:

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

# *.h264 conversion to *.avi:
is done via avconv (which is installed with libav-tools).

# SD Card image containing Raspian image with all things installed:
https://www.dropbox.com/sh/bibhy2sgadq30dm/AACD2Rdhmad2QdBi9q-pQfd6a?dl=0

# outdated:
# conversion from h264 to mp4 ()
MP4Box -add filename.h264 filename.mp4

//from here we need to convert it to a series of images (like *.avi) to be read on 
//imagej. We are doing this right now using a software called streamclip, that unfortunately does not work on linux. --> we are going to find a better solution for this!
# end of outdated
