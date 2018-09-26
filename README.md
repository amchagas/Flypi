#### Flypi - An open source, modular, affordable tool for imaging experiments.


Hi! Thanks for dropping by. This project started during one of the summer courses organized by [Trend in Africa](www.trendinafrica.org). It developed to the current state due to the efforts of many people along the way. In special Tom Baden, Lucia Prieto, and Edwin Cruz. A paper describing the system was published in [Plos Biology](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2002702).

 Version 1.0 was released with the paper and can be found [here](https://github.com/amchagas/Flypi/tree/v1.0.0).

The system can be used for optical microscopy, fluorescence, behavioural tracking, optogenetics, calcium imaging and thermogenetics (see examples recorded with the system below).


##### Further development is being done by [Prometheus Science](wwww.prometheus-science.com)

#### Some samples imaged with the device:


![Fluorescence ZebraFish GFP expressed in heart tissue](example_samples/PLOS_Paper/Zebrafish_heartbeat_GFP.gif)|
![GCamP_ZebraFish](example_samples/PLOS_Paper/GCamP_ZebraFish.jpg)|![Zebra Fish Transmission](example_samples/PLOS_Paper/zebrafish_larva_transmission.gif)
--|---|--
4  |  5 |  6
10         |  11 |  12




### We've created a Forum for users to posts questions and suggestions too! Please take a look [here](http://forum.prometheus-science.com/home/categories/flypi-user-forum)

## Custom PCB

You can order the PCBs and buy the parts to assemble them through the [Kitspace page](https://kitspace.org/boards/github.com/prometheus-science/FlyPi).

## Necessary Libraries:

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

is done via avconv (which is installed with libav-tools).


## SD Card image containing Raspian image with all things installed:
https://www.dropbox.com/sh/bibhy2sgadq30dm/AACD2Rdhmad2QdBi9q-pQfd6a?dl=0
