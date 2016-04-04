import tkinter as tk
import os

#import serial module
try:
    import serial
    serialAvail = True
    ## setup serial - create "ser" object that will be used to communicate with
    ## the Arduino. Here the user can uncomment/comment lines according to the
    ## operational system running.

    # for PC
    #ser = serial.Serial("COM5", 9600)
    # for Arduino Uno from RPi
    #ser = serial.Serial('/dev/ttyACM0', 115200)
    # for Arduino Nano from RPi
    #ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.2)
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
    protocolFlag = 0
    quitFlag = 1

    #############adresses for all arduino components:
    ##LED1##
    led1OnAdd = "31"
    led1OffAdd = "32"
    led1ZapDurAdd = "34000"

    ##LED2##
    led2OnAdd = "35"
    led2OffAdd = "36"
    led2ZapDurAdd = "38000"

    ##MATRIX##
    #matOnAdd = "39"
    matOffAdd = "40"
    matPat1Add = "41"
    matPat2Add = "42"
    matPat3Add = "39"
    matBrightAdd = "43000"

    ##RING##
    ringOnAdd = "44"
    ringOffAdd = "45"
    ringZapAdd = "52000"
    ringRedAdd = "49000"
    ringGreenAdd = "50000"
    ringBlueAdd = "46000"
    ringAllAdd = "51000"
    ringRotAdd = "47500"

    ##PELTIER##
    peltOnAdd = "53"
    peltOffAdd = "54"
    peltTempAdd = "55000"

    #row4Frame = tk.Frame()
    def __init__(self, master, ser=""):

        #create base path for storing files, temperature curves, etc:
        if not os.path.exists(self.basePath):
            #os.chdir('/home/pi/Desktop/')
            os.mkdir(self.basePath)
            os.chown(self.basePath, 1000, 1000)

        ##create the mainframe
        frame = tk.Frame()
        frame.grid(row=0, column=0, rowspan=1, columnspan=1)
        row4Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        row1Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        row2Frame = tk.Frame(master=frame, bd=2, relief="ridge")
        row3Frame = tk.Frame(master=frame, bd=2, relief="ridge")

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
            self.ser.write(self.led1OffAdd.encode('utf-8'))

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
            self.ser.write(self.led2OffAdd.encode('utf-8'))

        ###RING###
        if self.ringFlag == 1:
            import Ring
            self.frameRing = tk.Frame(row1Frame, bd=3)
            self.frameRing.grid(row=1, column=0, sticky="NW",
                                columnspan=3, rowspan=1)
            self.Ring = Ring.Ring(self.frameRing, label="RING",
                             #protFrame=self.frameProt,
                             ringOnAdd=self.ringOnAdd,
                             ringOffAdd=self.ringOffAdd,
                             ringZapAdd=self.ringZapAdd,
                             redAdd=self.ringRedAdd,
                             greenAdd=self.ringGreenAdd,
                             blueAdd=self.ringBlueAdd,
                             allAdd=self.ringAllAdd,
                             rotAdd=self.ringRotAdd, ser=self.ser)
            self.ser.write(self.ringOffAdd.encode('utf-8'))

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
            self.ser.write(self.matOffAdd.encode('utf-8'))

        ###PELTIER###
        if self.peltierFlag == 1:
            import Peltier
            self.framePelt = tk.Frame(row3Frame, bd=3)
            self.framePelt.pack(side="top")
            self.Peltier = Peltier.Peltier(parent=self.framePelt,
                                           label="PELTIER",
                                           onAdd=self.peltOnAdd,
                                           offAdd=self.peltOffAdd,
                                           tempAdd=self.peltTempAdd,
                                           basePath=self.basePath,
                                           ser=self.ser)
            self.ser.write(self.peltOffAdd.encode('utf-8'))

        ###Protocol###
        if self.protocolFlag == 1:
            self.frameProt = tk.Frame(master=row4Frame,
                                      bd=3,
                                      relief="ridge")
            self.frameProt.pack(side="top")
            self.prot = True
            #self.protocol = Protocol(parent=self.frameProt, ser=self.ser)

        else:
            self.frameProt = ""
            self.prot = False

        ###QUIT###
        if self.quitFlag == 1:
            self.frameQuit = tk.Frame(master=frame)
            self.frameQuit.grid(row=5, column=2, sticky="NW")
            self.quitAPP(parent=self.frameQuit)

        #draw all frames on screen
        row4Frame.grid(row=5, column=0, sticky="NWE", columnspan=1)
        row1Frame.grid(row=1, column=0, sticky="NWE", columnspan=1)
        row3Frame.grid(row=0, column=2, sticky="NWE")
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

        self.quit = tk.Button(parent, text="QUIT",
                              fg="red", command=quitNcloseSerial)
        self.quit.pack(fill="x")
