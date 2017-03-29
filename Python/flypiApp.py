import tkinter as tk
import os

#import serial module
try:
    import serial
    serialAvail = True
 
except ImportError:
    serialAvail = False
    print ("serial module not available!")
    print ("user interface will not control flypi!")


class flypiApp:
    #filepath for output:
    basePath = '/home/pi/Desktop/flypi_output/'
    

    #use these flags to make whole pieces of the GUI disappear

    cameraFlag = 1
    ringFlag = 1

    led1Flag = 1
    led2Flag = 1
    matrixFlag = 1
    peltierFlag = 1
    autofocusFlag = 1

    
    protocolFlag = 1
    quitFlag = 1

    #############adresses for all arduino components:
    ##LED1##
    led1OnAdd = "LD1<1>>"
    led1OffAdd = "LD1<0>>"
    led1ZapDurAdd = "LD1"

    ##LED2##
    led2OnAdd = "LD2<1>>"
    led2OffAdd = "LD2<0>>"
    led2ZapDurAdd = "LD2"

    ##MATRIX##
    #matOnAdd = "39"
    matOffAdd = "MAT<0>>"
    matPat1Add = "MAT<1>>"
    matPat2Add = "MAT<2>>"
    matPat3Add = "MAT<3>>"
    matBrightAdd = "MAB"

    ##RING##
    ringOnAdd = "RIN<1>>"
    ringOffAdd = "RIN<0>>"
    ringRedAdd = "RRE"
    ringGreenAdd = "RGR"
    ringBlueAdd = "RBL"
    ringAllAdd = "RAL"
    ringZapAdd = "RZA"
    ringRotAdd = "RRT"

    ##PELTIER##
    peltOnAdd = "PEL<1>>"
    peltOffAdd = "PEL<0>>"
    peltTempAdd = "TEM"

    ##autofocus##
    autoFocusAdd = "SER"

    #row4Frame = tk.Frame()
    def __init__(self, master, ser=""):

        #create base path for storing files, temperature curves, etc:
        if not os.path.exists(self.basePath):
            #os.chdir('/home/pi/Desktop/')
            os.mkdir(self.basePath)
            os.chown(self.basePath, 1000, 1000)

        #create dictionary to store all classes that will be used
        usedClasses = dict() 

        ##create the mainframe
        frame = tk.Frame()
        frame.grid(row=0, column=0, rowspan=1, columnspan=1)
        
        row1Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        row2Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        row3Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        row4Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        
        if serialAvail == True:
            # for Arduino Uno from RPi
            #self.ser = serial.Serial('/dev/ttyACM0', 115200)
            # for Arduino Nano from RPi
            self.ser = serial.Serial('/dev/ttyUSB0', 115200)

        ##show the pieces of the GUI
        ##depending on which flags are on (see above):
        

        
        ###CAMERA###
        if self.cameraFlag == 1:
            
            
            import Camera
            self.frameCam = tk.Frame(master=row2Frame, bd=3)
            self.frameCam.pack(side="top")
            self.Camera = Camera.Camera(parent=self.frameCam,
                                        label="CAMERA",
                                        basePath=self.basePath)

            usedClasses["camera"] = self.Camera
        else:
            usedClasses["camera"] = 0
        ###LED1###
        if self.led1Flag == 1:
            import LED
            
            self.frameLed1 = tk.Frame(row1Frame, bd=3)
            self.frameLed1.grid(row=0, column=0, sticky="NW")

            self.LED1 = LED.LED(parent=self.frameLed1, label="LED 1",
                          onAdd=self.led1OnAdd, offAdd=self.led1OffAdd,
                          zapDurAdd=self.led1ZapDurAdd, ser=self.ser,
                          #prot=self.prot,
                          #protFrame=self.frameProt,
                          )
            led1Off = self.led1OffAdd+"*"
            self.ser.write(led1Off.encode('utf-8'))

            usedClasses["led1"] = self.LED1
            #print (self.LED1)
        else:
            usedClasses["led1"] = 0
        ###LED2###
        if self.led2Flag == 1:
            import LED
            self.frameLed2 = tk.Frame(row1Frame, bd=3)
            self.frameLed2.grid(row=0, column=1, sticky="NW")
            self.LED2 = LED.LED(parent=self.frameLed2, label="LED 2",
                          onAdd=self.led2OnAdd, offAdd=self.led2OffAdd,
                          zapDurAdd=self.led2ZapDurAdd, ser=self.ser,
                          #prot=self.prot, protFrame=self.frameProt,
                          )
            led2Off = self.led2OffAdd+"*"
            self.ser.write(led2Off.encode('utf-8'))
            usedClasses["led2"] = self.LED2
        else:   
            usedClasses["led2"] = 0


        ###MATRIX###
        if self.matrixFlag == 1:
            import Matrix
            self.frameMatrix = tk.Frame(row1Frame, bd=3)
            self.frameMatrix.grid(row=0, column=2, sticky="W",)
            self.Matrix = Matrix.Matrix(parent=self.frameMatrix, label="MATRIX",
                               pat3Add=self.matPat3Add, offAdd=self.matOffAdd,
                               pat1Add=self.matPat1Add, pat2Add=self.matPat2Add,
                               brightAdd=self.matBrightAdd,
                               # prot=self.prot, protFrame=self.frameProt,
                               ser=self.ser)
            matOff = self.matOffAdd+"*"
            self.ser.write(matOff.encode('utf-8'))
            usedClasses["matrix"] = self.Matrix
        else:   
            usedClasses["matrix"] = 0

        ###RING###
        if self.ringFlag == 1:
            import Ring
            self.frameRing = tk.Frame(row1Frame, bd=3)
            self.frameRing.grid(row=1, column=0, sticky="NW",
                                columnspan=3, rowspan=1)

            self.Ring = Ring.Ring(parent=self.frameRing, label="RING",
                             ringOnAdd=self.ringOnAdd,
                             ringOffAdd=self.ringOffAdd,
                             ringZapAdd=self.ringZapAdd,
                             redAdd=self.ringRedAdd,
                             greenAdd=self.ringGreenAdd,
                             blueAdd=self.ringBlueAdd,
                             allAdd=self.ringAllAdd,
                             rotAdd=self.ringRotAdd,
                             ser=self.ser)

            ringOff=self.ringOffAdd+"*"
            self.ser.write(ringOff.encode('utf-8'))
            usedClasses["ring"] = self.Ring
        else:   
            usedClasses["ring"] = 0
            
        ###PELTIER###
        if self.peltierFlag == 1:
            import Peltier
            self.framePelt = tk.Frame(row4Frame, bd=3)
            self.framePelt.pack(side="left")
            self.Peltier = Peltier.Peltier(parent=self.framePelt,
                                           label="PELTIER",
                                           onAdd=self.peltOnAdd,
                                           offAdd=self.peltOffAdd,
                                           tempAdd=self.peltTempAdd,
                                           basePath=self.basePath,
                                           ser=self.ser)
            peltOff = self.peltOffAdd+"*"
            self.ser.write(peltOff.encode('utf-8'))
            usedClasses["peltier"] = self.Peltier
            
        else:   
            usedClasses["peltier"] = 0


        ###Auto Focus###
        if self.autofocusFlag == 1:
            import AutoFocus
            self.frameAuto = tk.Frame(row4Frame, bd=3)
            self.frameAuto.pack(side="left")
            self.AutoFocus = AutoFocus.AutoFocus(parent=self.frameAuto,
                                           label="Focus",
                                           velAdd=self.autoFocusAdd,
                                           ser=self.ser)
            servoOff=str(self.autoFocusAdd)+"*"+ str(0)+"*"
            self.ser.write(servoOff.encode('utf-8'))

        ###Protocol###
        if self.protocolFlag == 1:
            import Protocol
            
            self.frameProt = tk.Frame(master=row3Frame,
                                      bd=3,
                                      relief="ridge")
            self.frameProt.pack(side="top")
            self.Protocol = Protocol.Protocol(parent = self.frameProt,
                                              usedClasses=usedClasses,
                                              basePath = self.basePath+"/protocol/",
                                              label="Protocols",ser=self.ser)
            #self.prot = True
            #self.protocol = Protocol(parent=self.frameProt, ser=self.ser)

        else:
            self.frameProt = ""
            self.prot = False

        ###QUIT###
        if self.quitFlag == 1:
            self.frameQuit = tk.Frame(master=row4Frame)
            self.frameQuit.pack(side="right")
            #self.frameQuit.grid(row=5, column=2, sticky="NW")
            self.quitAPP(parent=self.frameQuit)

        #draw all frames on screen
        row4Frame.grid(row=5, column=0, sticky="NWE", columnspan=1)
        row1Frame.grid(row=1, column=0, sticky="NWE", columnspan=1)
        row3Frame.grid(row=1, column=2, sticky="NWE")
        row2Frame.grid(row=0, column=0, sticky="NWE", columnspan=1)

    ######################################## QUIT
    def quitAPP(self, parent="none"):
        ##callback to close the program and close serial port
        def quitNcloseSerial():
            if self.peltierFlag == 1 and self.Peltier.peltFlag1 == 1:
                print("close pelt file")
                self.Peltier.fh.close()
            if serialAvail == True:

                self.ser.flush()
                self.ser.close()

            self.quit.quit()
        self.qLabel=tk.Label(master=parent,text="exit program")
        self.qLabel.pack()
        self.quit = tk.Button(master=parent, text="QUIT",
                              fg="red", command=quitNcloseSerial)
        self.quit.pack(fill="x")
