#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:53:17 2019

@author: andre
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtCore import QTimer
import time
import subprocess
import os
from flypi_GUI import Ui_MainWindow
import pyqtgraph as pg




try:
    import serial
    serialAvail = True
    print ("serial lib loaded.")

except ImportError:
    serialAvail = False
    print ("serial module not available!")
    print ("user interface will not control flypi!")


loadSerial = 1




class allcallbacks(Ui_MainWindow):
        #connect callbacks
    def __init__(self,dialog):  
        
        self.basePath = "/home/pi/Desktop/flypi_output/" 
        
        self.timer = QTimer()
        self.led2onflag = 0
        self.led1onflag = 0
        self.mat1onflag = 0
        self.peltonflag = 0
        self.camon = 0
        Ui_MainWindow.__init__(self)
        #load camera library
        try:
            # picamera module
            import picamera
            #picameraAvail = True
            ##setup camera
            self.cam = picamera.PiCamera()
            self.cam.led = False
            self.cam.exposure_mode = "fixedfps"
            self.cam.exposure_compensation = 0
            self.cam.brightness = 50
            self.cam.awb_mode = "auto"
            self.camFlag=1

        except ImportError:
            #picameraAvail = False
            print ("picamera module not available!")
            self.camFlag=0
        
        #load serial port  
        self.primer = "TW 1"
        if loadSerial == 1 and serialAvail == True:
            # for Arduino Uno from RPi
            #self.ser = serial.Serial('/dev/ttyACM0', 115200)
            # for Arduino Nano from RPi
            self.ser = serial.Serial('/dev/ttyUSB0', 115200)
            if self.ser.in_waiting != 0:
                print(self.ser.readline())
            #while self.ser.in_waiting==0:
            #    print("init")
            #    print(self.ser.readline())
            #    self.primer = "TW 1"
        else:
            self.ser=None
            print ("Arduino not being controlled")
            
        self.setupUi(dialog)
        
        #camera callbacks connection
        self.camonbutton.clicked.connect(self.camonbutton_callback)
        self.zoombar.valueChanged.connect(self.zoom_callback)
        self.windowbar.valueChanged.connect(self.window_callback)
        self.horizontalbar.valueChanged.connect(self.horizontal_callback)
        self.verticalbar.valueChanged.connect(self.vertical_callback)
        self.rotationbar.valueChanged.connect(self.rotation_callback)
        self.brightnessbar.valueChanged.connect(self.brightness_callback)
        self.contrastbar.valueChanged.connect(self.contrast_callback)
        self.exposurebar.valueChanged.connect(self.exposure_callback)
        self.fpsbar.valueChanged.connect(self.fps_callback)
        self.binbar.valueChanged.connect(self.bin_callback)
        self.modebox.activated.connect(self.mode_callback)
        self.whitebalancebox.activated.connect(self.whitebalance_callback)
        self.colourbox.activated.connect(self.colour_callback)
        self.resolutionbox.activated.connect(self.resolution_callback)
        self.to_avibutton.clicked.connect(self.to_avibutton_callback)
        self.photobutton.clicked.connect(self.photobutton_callback)
        self.timelapsebutton.clicked.connect(self.timelabpsebutton_callback)
        self.videobutton.clicked.connect(self.videobutton_callback)
        self.flipimagebox.clicked.connect(self.flipimage_callback)
        #self.autoexposurebox.clicked.connect(self.autoe )
        
        #protocol callbacks
        self.runbutton.clicked.connect(self.runUpdate)
        #led1 callbacks
        self.led1onbutton.clicked.connect(self.led1On)
        self.led1pulsebutton.clicked.connect(self.led1pulse)
        self.led1slider.valueChanged.connect(self.led1bright)
        
        
        #led2 callbacks
        self.led2onbutton.clicked.connect(self.led2On)
        self.led2pulsebutton.clicked.connect(self.led2pulse)
        self.led2slider.valueChanged.connect(self.led2bright)
        
        #ring callbacks
        self.ringonbutton.clicked.connect(self.ringonupdate)
        self.ringpulsebutton.clicked.connect(self.ringpulseupdate)
        self.redslider.valueChanged.connect(self.redupdate)
        self.greenslider.valueChanged.connect(self.greenupdate)
        self.blueslider.valueChanged.connect(self.blueupdate)
        self.allslider.valueChanged.connect(self.allupdate)
        
        #peltier callbacks
        self.peltonbutton.clicked.connect(self.peltieroncallback)
        self.tempslider.valueChanged.connect(self.peltierslidercallback)
        #self.tempclosedloop.toggled.connect(self.peltiergettempcallback)
        self.logtempcheck.clicked.connect(self.peltierlogtemp)
        

        #matrix callbacks
        self.matrixonbutton.clicked.connect(self.matrixoncallback)
        self.matrixpat1.clicked.connect(self.matpat1callback)
        self.matrixpat2.clicked.connect(self.matpat2callback)
        self.matrixpat3.clicked.connect(self.matpat3callback)
        self.matrixslider.valueChanged.connect(self.matbrightcallback)
        
        #servo callbacks
        self.servobutton.clicked.connect(self.servoupdatecallback)
        self.servoslider.valueChanged.connect(self.servovelcallback)
    


    ################## peltier functions ######################################
    def peltieroncallback(self):
        #print("here")
        self.tempgraph.clear()
        flag = 1
        output = list()
        if self.peltonbutton.isChecked() and flag==1:
            self.peltonflag = 1
            flag = 0
            temp = float(self.peltiergettempcallback())
            self.y = [temp for i in range(10)]
            self.x = list(range(0,10))

            theTitle = "pyqtgraph plot"
            self.plot = self.tempgraph.plot(self.x, self.y)
            
            print ("pelt on")
            
            self.timer.timeout.connect(self.peltierloop)
            self.timer.start(250)   # ms
            output.append("P1 ")
            
            
          
        else:
            flag=1
            self.timer.stop()
            self.peltonflag = 0
            output.append("P0")
        self.runCommands(allcom=output)
        return
    
    def peltierslidercallback(self):
        value = self.tempslider.value()
        self.desiredtempbar.setValue(value)
        
        if self.peltonflag == 1:
            self.peltieroncallback()       
        return
    
    def peltiergettempcallback(self):
        output = "GT"
        self.output1(command=output)
        haltFlag = 1
        while haltFlag==1:
            test=self.ser.readline()
            if test[0:-2]!='d'.encode('utf-8') and test[0:-2]!='Ready'.encode('utf-8'):
                haltFlag=0
                actual_temp = test.decode()
                
                self.actualtempbar.setValue(int(actual_temp[0:2]))
        return actual_temp
    
    def peltierloop(self):
        actual_temp = self.peltiergettempcallback()  
        self.y.pop(0)
        self.y.append(float(actual_temp))
        self.plot.setData(self.x,self.y) 
        self.tempgraph.setYRange(min = min(self.y)-2, max = max(self.y)+2)
        
        if self.tempclosedloop.toggled:
            set_temp = self.tempslider.value()
            output = "ST " + str(set_temp)
            self.output1(command=output)
        
        if self.logtempcheck.isChecked():
            self.peltierlogtemp(actual_temp)

        
        
    
    def peltierlogtemp(self,temp):
        
        
        if self.logtempcheck.isChecked():
            folderPath = self.create_folder(
                      folderPath="/home/pi/Desktop/flypi_output/",
                      folderName="temperatures")
            
            
            fid = self.create_file(
                    filePath=folderPath+"/",
                    fileName="templog_"+time.strftime('%Y-%m-%d') + ".txt")
            
            fid.write(time.strftime('%Y-%m-%d-%H-%M-%S') + (','))
            fid.write(str(temp)+(',\r\n')) 
            fid.close()
    
    ################## Servo functions ########################################
    def servoupdatecallback(self):
        flag = 1
        if self.servobutton.isChecked() and flag==1:
            flag=0
            value = self.servoslider.value()
            print ("servo on")
            output = "S1 " + str(value)
            
          
        else:
            flag=1
            print("servo off")
            output = "S0"
        self.output1(command = output)
        return
    
    def servovelcallback(self):
        value = self.servoslider.value()
        self.servobar.setValue(value)
        return
    
    ################## Matrix functions #######################################
    def matrixoncallback(self):
        flag = 1
        if self.matrixonbutton.isChecked() and flag==1:
            flag=0
            self.mat1onflag=1
            value = self.matrixslider.value()
            print ("matrix on")
            output = "M1 " + str(value/10)
          
        else:
            flag=1
            self.mat1onflag=0
            print("matrix off")
            output = "M0"
        self.output1(command = output)
        return
    
    def matpat1callback(self):
        self.output1(command = "M11")
        return
    
    def matpat2callback(self):
        self.output1(command = "M12")
        return
    
    def matpat3callback(self):
        self.output1(command = "M13")
        return
    
    def matbrightcallback(self):
        value = self.matrixslider.value()
        print(value)
        self.matbrightindicator.setValue(value)
        if self.mat1onflag == 1:    
            self.output1(command = "M1 " + str(value))
        return
    
    ################## LED1 functions #########################################
    
    def led1On(self):
        flag = 1
        
        if self.led1onbutton.isChecked() and flag==1:
            flag=0
            
            self.led1onflag=1
            value = self.led1slider.value()
            value = int(value *(255./100.))
            output = "L11 " + str(value)
            
            
        else:
            self.led1onflag=0
            flag=1
            
            output = "L10"
        
            
        self.output1(command = output)
        

        return
    
    def led1pulse(self):
        value = int(self.led1pulsebrightness.text())
        value = int(int(value) *(255./100.))
        time = self.led1pulseduration.text()
        if time == "zap in ms":
            time = str(500)
            #print("you didn't set a value!")
            
        if self.led1onflag==1:
            last = "L11"
        else:
            last = "L10"
        if loadSerial==1 and serialAvail==1:
            allcom = [self.primer, "L11 " + str(value),"TW "+time,last]
            self.runCommands(allcom=allcom)
            
        print("pulse")
        return
    
    def led1bright(self):
        self.l1value = self.led1slider.value()
        
        self.led1brightindicator.setValue(self.l1value)
        if self.led1onflag==1:
            self.led1On()
        return  
        
    ################## LED2 functions #########################################
    
    def led2On(self):
        flag = 1
        if self.led2onbutton.isChecked() and flag==1:
            flag=0
            self.led2onflag = 1
            value = self.led2slider.value()
            value = int(int(value) *(255./100.))
            print ("led2 on")
            output = "L21 " + str(value)
          
        else:
            flag=1
            self.led2onflag = 0
            print("led2 off")
            output = "L20"
        if loadSerial==1 and serialAvail==1:
            self.output1(command = output)
        return
        
    def led2pulse(self):
        value = self.led2pulsebrightness.text()
        value = int(int(value) *(255./100.))
        time = self.led2pulseduration.text()
        if time == "zap in ms":
            time = str(500)
            #print("you didn't set a value!")
        
        if self.led2onflag==1:
            last = "L21"
        else:
            last = "L20"

        allcom = [self.primer, "L21 " + str(value),"TW "+time,last]
        if loadSerial==1 and serialAvail==1:
            self.runCommands(allcom=allcom)
        print("pulse")
        return
    
    def led2bright(self):
        value = self.led2slider.value()
        self.led2brightindicator.setValue(value)
        if self.led2onflag ==1:
            self.led2On()
        return

    
    ############# Ring functions ##############################################

    def redupdate(self):
        print(self.redslider.value())
        value = self.redslider.value()
        self.redindicator.setValue(value)
        value = int(value *(255./100.))
        #print(value)
        if loadSerial == 1:

            output = "RR " + str(value)
            self.output1(command = output)
        return
                

    def greenupdate(self):
        print(self.greenslider.value())
        value = self.greenslider.value()
        self.greenindicator.setValue(value)
        value = int(value *(255./100.))
        if loadSerial == 1:

            output = "RG " + str(value)
            self.output1(command = output)
        return

    def blueupdate(self):
        print(self.blueslider.value())
        value = self.blueslider.value()
        self.blueindicator.setValue(value)
        value = int(value *(255./100.))
        if loadSerial == 1:
            
            
            output = "RB " + str(value)
            self.output1(command = output)
        return        
                
    def allupdate(self):
        value = self.allslider.value()
        
        self.redslider.setValue(value)
        self.greenslider.setValue(value)
        self.blueslider.setValue(value)
        self.redindicator.setValue(value)
        self.greenindicator.setValue(value)
        self.blueindicator.setValue(value)
        self.allindicator.setValue(value)
        return
                
    def ringpulseupdate(self):
        print("zap")
        if self.ringonbutton.isChecked():
            print(self.redpulse.text())
            print(self.greenpulse.text())
            print(self.bluepulse.text())
            print(self.ringpulsedurinput.text())
            if loadSerial == 1:
                output = list()
                output.append("RR " + self.redpulse.text())
                output.append("RG " + self.greenpulse.text())                
                output.append("RB " + self.bluepulse.text())          
                output.append("TW " + self.ringpulsedurinput.text())
                output.append("RR " + str(self.redslider.value()))
                output.append("RG " + str(self.greenslider.value()))
                output.append("RB " + str(self.blueslider.value()))
                self.runCommands(allcom=output)
        return

    def ringonupdate(self):
        
        if loadSerial == 1:
            if self.ringonbutton.isChecked():
                output = "R1"
                print("ring ON")
            else:
                output = "R0" 
                print("ring OFF")
            self.output1(command = output)
        return


    ############# Protocol functions ##########################################
    def runUpdate(self):
        totalDur = 0
        if self.runbutton.isChecked():
            print("run")
            allcom = list()
            if self.protled1button.isChecked():
                allcom.append(str('L11 ' + str(self.led1box1.text())))
                
            if self.protled2button.isChecked():
                allcom.append(str('L21 ' + str(self.led2box1.text())))
                
            if self.protringbutton.isChecked():
                allcom.append('R1')
                allcom.append(str('RR '+ str(self.redinput1.text())))
                allcom.append(str('RG '+ str(self.greeninput1.text())))
                allcom.append(str('RB '+ str(self.blueinput1.text())))

            if self.protpeltierbutton.isChecked():
                allcom.append('P1')
                allcom.append(str('ST '+str(self.peltinput1.text())))
                allcom.append(str('GT'))
                breaktime = int(self.timeinput1.text())
                # test this code for using the peltier in protocol
                # the idea is to give more read and set commands during the 
                # execution phase of the protocol, so that the peltier temperature
                # is more accurate.
                
                #for i in range(int(breaktime)/4):
                #    allcom.append(str('ST '+str(self.peltinput1.text())))
                #    allcom.append(str('GT'))
                #    allcom.append(str('TW '+str(int(breaktime/4))))
            #else:        
            #    allcom.append(str('TW '+str(self.timeinput1.text())))
            allcom.append(str('TW '+str(self.timeinput1.text())))
            totalDur = totalDur + int(self.timeinput1.text())

            if self.protled1button.isChecked():
                allcom.append(str('L11 ' + str(self.led1box2.text())))
            if self.protled2button.isChecked():
                allcom.append(str('L21 ' + str(self.led2box2.text())))
            if self.protringbutton.isChecked():
                allcom.append('R1')
                allcom.append(str('RR '+ str(self.redinput2.text())))
                allcom.append(str('RG '+ str(self.greeninput2.text())))
                allcom.append(str('RB '+ str(self.blueinput2.text())))

            if self.protpeltierbutton.isChecked():
                allcom.append('P1')
                allcom.append(str('ST '+str(self.peltinput2.text())))
                allcom.append(str('GT'))

            allcom.append(str('TW '+str(self.timeinput2.text())))
            totalDur = totalDur + int(self.timeinput2.text())
            
            if self.protled1button.isChecked():
                allcom.append(str('L11 ' + str(self.led1box3.text())))
            if self.protled2button.isChecked():
                allcom.append(str('L21 ' + str(self.led2box3.text())))
            if self.protringbutton.isChecked():
                allcom.append('R1')
                allcom.append(str('RR '+ str(self.redinput3.text())))
                allcom.append(str('RG '+ str(self.greeninput3.text())))
                allcom.append(str('RB '+ str(self.blueinput3.text())))

            if self.protpeltierbutton.isChecked():
                allcom.append('P1')
                allcom.append(str('ST '+str(self.peltinput3.text())))
                allcom.append(str('GT'))

            allcom.append(str('TW '+str(self.timeinput3.text())))
            totalDur = totalDur + int(self.timeinput3.text())
            
            if self.protled1button.isChecked():
                allcom.append(str('L11 ' + str(self.led1box4.text())))
            if self.protled2button.isChecked():
                allcom.append(str('L21 ' + str(self.led2box4.text())))

            if self.protringbutton.isChecked():
                allcom.append('R1')
                allcom.append(str('RR '+ str(self.redinput4.text())))
                allcom.append(str('RG '+ str(self.greeninput4.text())))
                allcom.append(str('RB '+ str(self.blueinput4.text())))

            if self.protpeltierbutton.isChecked():
                allcom.append('P1')
                allcom.append(str('ST '+str(self.peltinput4.text())))
                allcom.append(str('GT'))

            allcom.append(str('TW '+str(self.timeinput4.text())))
            totalDur = totalDur + int(self.timeinput4.text())


            if self.protled1button.isChecked():
                allcom.append(str('L11 ' + str(self.led1box5.text())))
            if self.protled2button.isChecked():
                allcom.append(str('L21 ' + str(self.led2box5.text())))
            if self.protringbutton.isChecked():
                allcom.append('R1')
                allcom.append(str('RR '+ str(self.redinput5.text())))
                allcom.append(str('RG '+ str(self.greeninput5.text())))
                allcom.append(str('RB '+ str(self.blueinput5.text())))
            if self.protpeltierbutton.isChecked():
                allcom.append('P1')
                allcom.append(str('ST '+str(self.peltinput5.text())))
                allcom.append(str('GT'))

            allcom.append(str('TW '+str(self.timeinput5.text())))
            totalDur = totalDur + int(self.timeinput5.text())
            
            allcom.append(str('TW '+str(self.itiinput.text())))
            totalDur = totalDur + int(self.itiinput.text())

            reps = int(self.repinput.text())
            totalDur = totalDur*reps

            #add 1 sec buffer
            totalDur=totalDur+1000
            #convert milliseconds to seconds
            totalDur = totalDur/1000.0
            if totalDur<2.:
                totalDur = 2


            x=1
            print(allcom)
            if self.checkBox.isChecked():                
                # because we needed a fast solution
                # bits from the camera functions are copied here
                self.camon = 1
                #res = self.resolutionbox.value 
                size = self.windowbar.value()
                self.cam.resolution = (1920,1080)
                self.cam.preview_window = (0, 0, size, size)
                self.zoombar.setValue (1)
                self.horizontalbar.setValue (0) 
                self.verticalbar.setValue (0) 
                self.cam.zoom = (self.horizontalbar.value(),
                                 self.verticalbar.value(),
                                 self.zoombar.value(),
                                 self.zoombar.value())
                self.cam.start_preview()
                self.cam.preview.fullscreen = False
                time.sleep(1)
                self.durationbox.setValue(totalDur)
                videoPath = self.create_folder(folderPath=self.basePath,
                               folderName='videos/')
                
                self.cam.start_recording(output = videoPath +
                                'video_' +
                                time.strftime('%Y-%m-%d-%H-%M-%S') + '.h264',
                                format = "h264",)
                                #resize = (1920,1080))
                #wait a second so the camera adjusts
                
                
                
                #self.videobutton_callback()
            print(self.redinput5.text())    
            for i in range(reps):
                if i+1==reps:
                    allcom.append('R0')
                    allcom.append('P0')
                    allcom.append('L10')
                    allcom.append('L20')
                
                #self.runCommands(allcom=allcom)
                
                for command in allcom:
                    haltFlag=1
                    self.ser.write(str(command+'\n').encode('utf-8'))
                    self.ser.flush()
                    x=x+1
                    while self.ser.in_waiting==0:
                        x=x
                    while haltFlag==1:
                        test=self.ser.readline()
                        #print(test[0:-2])
                        if test[0:-2]=='d'.encode('utf-8') or test[0:-2]=='Ready'.encode('utf-8'):
                            haltFlag=0
                        else:
                            print(test)
                            print("ops")
            self.cam.stop_recording()
            print("done.")
            self.runbutton.setChecked(False)
        return
   
    ################## Camera functions #######################################    
    def camonbutton_callback(self,Camera):
        flag = 1
        if self.camonbutton.isChecked() and flag==1:
            flag=0
            #print(self.colourbox.itemData(1))
            print ("cam on")
            
            if self.camFlag==1:
                self.camon = 1
                #res = self.resolutionbox.value 
                size = self.windowbar.value()
                self.cam.resolution = (2592, 1944)
                self.cam.preview_window = (0, 0, size, size)
                self.zoombar.setValue (1)
                self.horizontalbar.setValue (0) 
                self.verticalbar.setValue (0) 
                self.cam.zoom = (self.horizontalbar.value(),
                                 self.verticalbar.value(),
                                 self.zoombar.value(),
                                 self.zoombar.value())
                self.cam.start_preview()

                self.cam.preview.fullscreen = False
                #wait a second so the camera adjusts
                time.sleep(1)
                return
        
        else:
            flag=1
            print("cam off")
            if self.camFlag==1:
                self.camon = 0
                self.cam.stop_preview()
                

    def photobutton_callback(self,Camera):
        #print(self.photobutton.isChecked())
        if self.camFlag==1 and self.camon==1:
            print("photo")
            
            photoPath = self.create_folder(folderPath=self.basePath,
                               folderName='snaps/')

            # Camera warm-up time
            time.sleep(1)
            self.cam.capture(photoPath + 'snap_' +
                        time.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg')
        return

    def timelabpsebutton_callback(self,Camera):
        if self.camFlag==1 and self.camon==1:
            x = 1
            print("time lapse")
            dur = self.durationbox.text()
            ntl = self.intervalbox.text()
            
            alltlpath = self.basePath + 'time_lapses/'            
            thistlpath = self.create_folder(folderPath=alltlpath,
                               folderName=time.strftime("%Y-%m-%d-%H-%M-%S")+"/")
            
            # Camera warm-up time
            time.sleep(1)
            totalphotos = int(float(dur)/float(ntl))
            for i in range(totalphotos):
                self.cam.capture(thistlpath + '/TL' + str(x)+'.jpg')
                x = x + 1
                print("photo " + str(x-1) + " out of " + str(totalphotos))
                time.sleep(float(dur)/float(ntl))
            print ("done")
        return

    def videobutton_callback(self):
        if self.camFlag==1:
            dur = self.durationbox.text()
            print(dur)
            
            videoPath = self.create_folder(folderPath=self.basePath,
                               folderName='videos/')

            #it seems that the raspi-cam doesn't like shooting videos at full res.
            #so the softw. will automatically use a lower resolution for videos
            if self.resolutionbox.currentText() == "2592x1944":
                resVal = "2592x1944" 
                self.resolutionbox.setCurrentText ("1920x1080")
                
                if self.camFlag == 1:
                    self.cam.resolution = (1920, 1080)
                
                if self.fpsbar.value()<30:
                    self.fpsbar.setValue(30)
                print ("impossible to record at 2592X1944,")
                print ("due to camera limitations.")
                print("dropping to next possible resolution")


            print("recording for: " + str(dur) + " secs")
            self.cam.start_recording(output = videoPath +
                                'video_' +
                                time.strftime('%Y-%m-%d-%H-%M-%S') + '.h264',
                                format = "h264",)
                                #resize = (1920,1080))
            self.cam.wait_recording(float(dur))
            self.cam.stop_recording()
            print("done.")
            #here we restore the preview resolution if it was the maximal one.
            if resVal == "2592x1944":
                if self.camFlag==1:
                    self.cam.resolution = (2592, 1944)
            return

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)  
                  
    def to_avibutton_callback(self):
        
        options = QtWidgets.QFileDialog.Options()
        #fname = QFileDialog.getOpenFileName(QtWidgets.QDialog(), 'Open file', 
        #    '/home/',"Image files (*.jpg *.gif)")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QDialog(), 'open file',
                                "","h264 Files (*.h264);;Python Files (*.py)", options=options)
        
        print("filename: "+fileName)
        if fileName == '':
            print ('no files selected')
            return
        fps = self.fpsbar.value()
        fps = "-r" + str(fps)

        print (fileName)
        print ("converting video to avi")
        outname = os.path.splitext(fileName)[0]+".avi"
        lastInd=fileName.rindex("/")
        files = os.listdir(fileName[0:lastInd])
        outCore = outname.rindex("/")
        print ("out: " + outname[outCore+1:])
        if outname[outCore+1:] in files:
            print ("file is already converted! Skipping...")
            print("done.")
            return
        command = ['MP4Box', '-add', fileName, outname]
        subprocess.call(command,shell=False)
        print("done.")
        return


    def fps_callback(self,Camera):
        self.fpslcd.setProperty("intValue",self.fpsbar.value())
        if self.camFlag==1:
            self.cam.framerate = (self.fpsbar.value())
        return
    
    def exposure_callback(self,Camera):
        self.exposurelcd.setProperty("intValue",self.exposurebar.value())
        print(self.exposurebar.value())
        if self.camFlag==1:
            self.cam.exposure_compensation = (self.exposurebar.value())
        return
    
    def flipimage_callback(self,Camera):
        if self.flipimagebox.isChecked():
            if self.camFlag == 1:
                self.cam.hflip = True
        else:
            if self.camFlag == 1:    
                self.cam.hflip = False
        return
    
    def brightness_callback(self,Camera):
        self.brightnesslcd.setProperty("intValue",self.brightnessbar.value())
        if self.camFlag==1:
            self.cam.brightness = (self.brightnessbar.value())
        return    
    
    def rotation_callback(self,Camera):
        self.rotationlcd.setProperty("intValue",self.rotationbar.value())
        if self.camFlag==1:
            self.cam.rotation = (self.rotationbar.value())
        return
    
    def contrast_callback(self,Camera):
        self.contrastlcd.setProperty("intValue",self.contrastbar.value())
        if self.camFlag==1:
            self.cam.contrast = (self.contrastbar.value())
        return
    
    def window_callback(self,Camera):
        print(self.windowbar.value())
        self.windowlcd.setProperty("intValue",self.windowbar.value())
        if self.camFlag==1:
            self.cam.preview_window = (0, 0, self.windowbar.value(), self.windowbar.value())       
        return
    def colour_callback(self,Camera):
        print(self.colourbox.currentText())
        if self.camFlag==1:
            if self.colourbox.currentText() != "":
                if self.colourbox.currentText() == "BW":
                    self.cam.color_effects = (128, 128)
                elif self.colourbox.currentText() == "RED":
                    self.cam.color_effects = (0, 255)
                elif self.colourbox.currentText() == "BLUE":
                    self.cam.color_effects = (255, 0)
                elif self.colourbox.currentText() == "GREEN":
                    self.cam.color_effects = (0, 0)
                else:
                    self.cam.color_effects = None
            
        
    def zoom_callback(self, Camera):
        self.zoomlcd.setProperty("intValue", self.zoombar.value())
        if self.zoombar.value==1:
            self.horizontalbar.setValue(0)
            self.verticalbar.setValue(0)
        if self.camFlag==1:
            if self.zoombar.value()==1:
                self.cam.zoom = (0, 0, 1, 1)
                self.horizontalbar.setValue(0)
                self.verticalbar.setValue(0)
            elif self.zoombar.value()!=0:
                zoomSide = 1. / self.zoombar.value()
                edge = (1 - zoomSide)#*0.5
                self.cam.zoom = ((self.horizontalbar.value() / 100.0) * edge,
                                    (self.verticalbar.value() / 100.0) * edge,
                                     1 / self.zoombar.value(),
                                     1 / self.zoombar.value() )    
    
    def horizontal_callback(self,Camera):
        self.horizontallcd.setProperty("intValue",self.horizontalbar.value())
        if self.zoombar.value == 1:
            if self.camFlag == 1:
                self.cam.zoom = (0, 0, 1, 1)
            self.horizontalbar.setValue(50)
            self.verticalbar.setValue(50)
        else:
            zoomSide = 1. / self.zoombar.value()
            edge = (1 - zoomSide)#*0.5
            self.cam.zoom = ((self.horizontalbar.value() / 100.0) * edge,
                             (self.verticalbar.value() / 100.0) * edge,
                              1 / self.zoombar.value(),
                              1 / self.zoombar.value())
        
    
    def vertical_callback(self,Camera):
        self.verticallcd.setProperty("intValue",self.verticalbar.value())
        if self.zoombar.value() == 1:
            if self.camFlag == 1:
                self.cam.zoom = (0, 0, 1, 1)
            self.horizontalbar.setValue(50)
            self.verticalbar.setValue(50)
        else:
            zoomSide = 1. / self.zoombar.value()
            edge = (1 - zoomSide)#*0.5
            self.cam.zoom = ((self.horizontalbar.value() / 100.0) * edge,
                             (self.verticalbar.value() / 100.0) * edge,
                              1 / self.zoombar.value(),
                              1 / self.zoombar.value())
        
    def bin_callback(self,Camera):
        self.binlcd.setProperty("intValue",self.binbar.value())
        resVal = self.resolutionbox.currentText()
        print("here")
        print(self.binbar.value())
        if self.binbar.value() == 1:
            ind = resVal.find("x")
            print(resVal[ind:])
            if self.camFlag == 1 and int(resVal[:ind]) >= 1920:
                self.cam.resolution = (int(resVal[0:ind]), int(resVal[ind+1:]))
                self.cam.framerate = (15)
                self.fpsbar.setValue(15)
                #self.FPSVar.set(15)
        if self.binbar.value() == 2:
            if self.camFlag==1:
                self.cam.resolution = (1296, 972)
                self.cam.framerate = (42)
            self.fpsbar.setValue (42)
            
        if self.binbar.value() == 4:
            self.fpsbar.setValue(90)
            if self.camFlag==1:
                self.cam.resolution = (640, 480)
                self.cam.framerate = (90)
            
            
        
    def whitebalance_callback(self,Camera):
        print(self.whitebalancebox.currentText())
        if self.camFlag==1:
            if self.whitebalancebox.currentText() == "green":
                self.cam.awb_mode = "off"
                self.cam.awb_gains = (1, 1)
            elif self.whitebalancebox.currentText() == "red":
                self.cam.awb_mode = "off"
                self.cam.awb_gains = (8.0, 0.9)
            elif self.whitebalancebox.currentText() == "blue":
                self.cam.awb_mode = "off"
                self.cam.awb_gains = (0.9, 8.0)
            elif self.whitebalancebox.currentText() == "off":
                self.cam.awb_mode = "off"
            else:
                self.cam.awb_mode = self.whitebalancebox.currentText()
    
    def resolution_callback(self,Camera):
        text = self.resolutionbox.currentText()
        index = text.find('x')
        values = [int(text[0:index]),int(text[index+1:])]
        if self.camFlag==1:
            if int(text[:index]) == 2592:
                self.cam.framerate = (15)
                self.fpsbar.setValue(15)
            self.cam.resolution = (int(text[0:index]),int(text[index+1:]))
        return values
        
    def mode_callback(self,Camera):
         print(self.modebox.currentText())
         if self.camFlag==1:
             if self.cam.image_effect != self.modebox.currentText():
                 self.cam.image_effect = self.modebox.currentText()
    
    
    def camConv2(self,Camera):

        
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","h264 Files (.h264)", options=options)

        if fileName == '':
            print ('no files selected')
            return
        fps = self.fpsbar.value()
        fps = "-r" + str(fps)

        print (fileName)
        print ("converting video to avi")
        outname = os.path.splitext(fileName)[0]+".avi"
        lastInd=fileName.rindex("/")
        files = os.listdir(fileName[0:lastInd])
        outCore = outname.rindex("/")
        print ("out:" + outname[outCore:])
        if outname[outCore+1:] in files:
            print ("file is already converted! Skipping...")
            print("done.")
            return
        command = ['MP4Box', '-add', fileName, outname]
        #command = ['ffmpeg', '-i', fileName,"-b",str(self.bitRate) ,"-pix_fmt","nv12","-f:v","-vcodec rawvideo", outname]
        subprocess.call(command,shell=False)
        print("done.")
        return
    
    

        
    ################## support functions ########################################################
    def output1(self,command = "TW 1"):
        if loadSerial == 1:
            self.ser.write(str(command+' \n').encode('utf-8'))
            #self.ser.flush()
        else:
            print("serial not loaded")
            
        return
    
    def runCommands(self,allcom=['P0','R0','L1 0','L2 0','S0']): 
        x=1
        for command in allcom:
            haltFlag=1
            
            #self.output1(command=command)
            
            self.ser.write(str(command+'\n').encode('utf-8'))
            self.ser.flush()
            x=x+1
            while self.ser.in_waiting==0:
                x=x
            while haltFlag==1:
                test=self.ser.readline()
                #print(test[0:-2])
                if test[0:-2]=='d'.encode('utf-8') or test[0:-2]=='Ready'.encode('utf-8'):
                    haltFlag=0
                else:
                    print(test)
                    print("ops")
    
        return

    def create_folder(self,
                      folderPath="/home/pi/Desktop/flypi_output/",
                      folderName="output1"):
        absPath = folderPath+folderName
        #print(os.path.exists(absPath))
        if not os.path.exists(absPath):
            #if not, create it:
            os.makedirs(absPath)
            os.chown(absPath, 1000, 1000)
        return absPath
    
    def create_file(self,
                    filePath="/home/pi/Desktop/flypi_output/output1/",
                    fileName="file1"+time.strftime('%Y-%m-%d') + ".txt"):
        #check if the file already exists
        if os.path.isfile(filePath + fileName) == False:
            #if it does not exist, create it
            fh = open(filePath + fileName, "w")
        else:
            #open file and append to it
            fh = open(filePath + fileName, "a")



        return fh    

       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = allcallbacks(dialog)
    dialog.show()
    sys.exit(app.exec_())
