

#import libraries
import Tkinter as tk


    
#import serial module   
try:
    import serial # picamera module
    serialAvail = True
    ## setup serial - create "ser" object that will be used to communicate with 
            ## the Arduino. Here the user can uncomment/comment lines according to the
            ## operational system running.
        
    #ser = serial.Serial("COM5", 9600) # for PC
    #ser = serial.Serial('/dev/ttyACM0', 115200) # for Arduino Uno from RPi
    #ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.2) # for Arduino Nano from RPi
except ImportError:
    serialAvail = False
    print ("serial module not available!")
    print ("user interface will not control flypi!")                 
    
   

    
    
        

class flypiApp:
    #use these flags to make whole pieces of the GUI disappear
    cameraFlag = 1       
    ringFlag = 1#1
    led1Flag = 1#1
    led2Flag = 1
    matrixFlag = 1#1  
    #protocolFlag=1    
    peltierFlag= 1   
    protocolFlag = 1
    quitFlag = 1
    
    #############adresses for all arduino components:
    ##LED1##
    led1OnAdd="31"
    led1OffAdd="32"
    led1ZapDurAdd="34000"
    
    ##LED2##
    led2OnAdd="35"
    led2OffAdd="36"
    led2ZapDurAdd="38000"

    ##MATRIX##
    matOnAdd="39"
    matOffAdd="40"
    matPat1Add="41"
    matPat2Add="42"
    matBrightAdd="43000"        
        
        
    ##RING##
    ringOnAdd="44"
    ringOffAdd="45"
    ringZapAdd="52000"
    ringRedAdd="49000"
    ringGreenAdd="50000"
    ringBlueAdd="51000"
    ringBrightAdd="46000"
    ringRotAdd="47500"
    
    ##PELTIER##
    peltOnAdd="53"
    peltOffAdd="54"
    peltTempAdd="55000"    
    
    
    #row4Frame = tk.Frame()
    def __init__(self,master,ser=""):

        
        
           
#        ##create the mainframe
#        self.frame = tk.Frame()
#        self.frame.grid(row=0,column=0,rowspan=1,columnspan=1)
        ##create the mainframe
        frame = tk.Frame()
        frame.grid(row=0,column=0,rowspan=1,columnspan=1)
        row4Frame=tk.Frame(master=frame,bd=2,relief="ridge")
        row1Frame = tk.Frame(master=frame,bd=2,relief="ridge")
        row2Frame = tk.Frame(master=frame,bd=2,relief="ridge")
        row3Frame = tk.Frame(master=frame,bd=2,relief="ridge")
        
        ##create variables for the scales
        #self.var=0
        if serialAvail==True:
            self.ser = serial.Serial('/dev/ttyACM0', 115200) # for Arduino Uno from RPi
                                     #bytesize=serial.EIGHTBITS,
                                     #parity=serial.PARITY_NONE,
                                     #stopbits=serial.STOPBITS_ONE,
                                     #timeout=1,
                                     #xonxoff=0,
                                     #rtscts=0
                                     #)

        ##show the pieces of the GUI 
        ##depending on which flags are on (see above): 
        if self.protocolFlag==1:
            self.frameProt = tk.Frame(master=row4Frame,
                                      bd=3,
                                      relief="ridge")            
            self.frameProt.pack(side="top")
            self.protocol=Protocol(parent=self.frameProt,ser=self.ser)
            
            
#            protLabel=tk.Label(master=self.frameProt,text="PROTOCOL: ")
#            protLabel.grid(row=0,column=0,columnspan=2,sticky="NW")

        else:
            self.frameProt=""
            
        if self.cameraFlag==1:
            self.frameCam = tk.Frame(master=row2Frame,bd=3)
            self.frameCam.pack(side="top")#.grid(row=2,column=0,columnspan=5,rowspan=1,sticky="NW")            
            self.Camera=Camera(parent=self.frameCam,label="CAMERA")

        
        if self.led1Flag==1:
            self.frameLed1 = tk.Frame(row1Frame,bd=3)
            self.frameLed1.grid(row=0,column=0,sticky="NW")
            
            self.LED1=LED(parent = self.frameLed1,label="LED 1",
                          onAdd=self.led1OnAdd,offAdd=self.led1OffAdd,
                          zapDurAdd=self.led1ZapDurAdd,ser = self.ser)            
            #self.LED1(self.frameLed1)
            #LED1 = self.basicFrame("LED1",self.led1On,self.led1Off,self.led1Zap)
            
        if self.led2Flag==1:
            self.frameLed2 = tk.Frame(row1Frame,bd=3)
            self.frameLed2.grid(row=0,column=1,sticky="NW")
            self.LED2=LED(parent=self.frameLed2, label = "LED 2",
                          onAdd=self.led2OnAdd,offAdd=self.led2OffAdd,
                          zapDurAdd=self.led2ZapDurAdd,ser=self.ser)
                          
        if self.ringFlag==1:
            self.frameRing = tk.Frame(row1Frame,bd=3)
            self.frameRing.grid(row=1,column=0,sticky="NW",columnspan=3,rowspan=1)
            self.RING = Ring(self.frameRing,label="RING",protFrame=self.frameProt,
                             ringOnAdd=self.ringOnAdd,ringOffAdd=self.ringOffAdd,
                             ringZapAdd=self.ringZapAdd,redAdd=self.ringRedAdd,
                             greenAdd=self.ringGreenAdd,blueAdd=self.ringBlueAdd,
                             brightAdd=self.ringBrightAdd,rotAdd=self.ringRotAdd,ser=self.ser) 


        if self.matrixFlag==1:
            self.frameMatrix = tk.Frame(row1Frame,bd=3)
            self.frameMatrix.grid(row=0, column=2,sticky="W",)
            self.Matrix=Matrix(parent=self.frameMatrix,label="MATRIX",
                               onAdd=self.matOnAdd,offAdd=self.matOffAdd,
                               pat1Add=self.matPat1Add,pat2Add=self.matPat2Add,
                               brightAdd=self.matBrightAdd,ser=self.ser)
                               
        
            
            
        
        
        if self.peltierFlag==1:
            self.framePelt = tk.Frame(row3Frame,bd=3)
            self.framePelt.pack(side="top")#.grid(row=0,column=3,sticky="WN")
            self.Peltier = Peltier(parent=self.framePelt,label="PELTIER",
                                   onAdd=self.peltOnAdd,offAdd=self.peltOffAdd,
                                   tempAdd=self.peltTempAdd,
                                   ser=self.ser)
            
            
        

#            self.Protocol=Protocols(parent=self.frameProt,
#                                    label="PROTOCOLS:")
        
        if self.quitFlag ==1:
            self.frameQuit = tk.Frame(master=frame)
            self.frameQuit.grid(row=5,column=0,sticky="NW")
            self.quitAPP(parent=self.frameQuit)
        
        #draw all frames on screen
        row4Frame.grid(row=5,column=0,sticky="NWE",columnspan=1)#pack(side="top",fill="x")
        row1Frame.grid(row=1,column=0,sticky="NWE",columnspan=1)#pack(side="top",fill="x")        
        row3Frame.grid(row=0,column=2,sticky="NWE")#pack(after=row1Frame,side="right",fill="x")        
        row2Frame.grid(row=0,column=0,sticky="NWE",columnspan=1)#pack(fill="x")        
        
    ######################################## QUIT
    def quitAPP(self,parent="none"):
        ##callback to close the program and close serial port
        def quitNcloseSerial():
            if serialAvail==True:
                self.ser.flush()
                self.ser.close()
            self.quit.quit()
            
        #self.rowCount=self.rowCount+1
        self.quit = tk.Button(parent,text="QUIT", fg="red", command=quitNcloseSerial)
        self.quit.pack(fill="x")#(row=self.rowCount,column=self.columnCount)

        

    ######################################## LED RING
class Ring:
    
    
    def __init__(self,parent="none",label="none",ser="",protFrame="",
                 ringOnAdd="",ringOffAdd="",ringZapAdd="",
                 greenAdd="",redAdd="",blueAdd="",
                 brightAdd="",rotAdd=""):
        
       
        #self.label=label 
        self.protFrame=protFrame     
        self.ser=ser
        self.ringOnAdd=ringOnAdd
        self.ringOffAdd=ringOffAdd
        self.ringZapAdd=ringZapAdd
        self.greenAdd=greenAdd
        self.redAdd=redAdd
        self.blueAdd=blueAdd
        self.brightAdd=brightAdd
        self.rotAdd=rotAdd
        
        
        ###########variables for ring sliders
        ringGreenVar = tk.IntVar()                        
        ringRedVar = tk.IntVar()                    
        ringBlueVar = tk.IntVar()                    
        ringBrightVar = tk.IntVar()
        ringRotVar = tk.IntVar()
        
        
    ############callbacks for ring sliders
        def GreenUpdate(self,ser=self.ser,address=self.greenAdd):
            address=int(greenAdd)
            output = address+ringGreenVar.get()
            output=str(output)+"*"
            print("green hue: "+ output[2:-1])
            ser.write(output.encode("utf-8"))
        
        
        def RedUpdate(self,ser=self.ser,address=self.redAdd):
            address=int(redAdd)
            output = address+ringRedVar.get()
            output=str(output)+"*"
            print("red hue: " +output[2:-1])
            ser.write(output.encode("utf-8"))
        def BlueUpdate(self,ser=self.ser,address=self.blueAdd):
            address=int(address)
            output = address+ringBlueVar.get()
            output=str(output)+"*"
            print("blue hue: " + output[2:-1])
            ser.write(output.encode("utf-8"))
        def BrightUpdate(self,ser=self.ser,address=brightAdd):
            address=int(address)
            output = address+ringBrightVar.get()
            output=str(output)+"*"
            print("ring Bright: "+ output[2:-1])
            ser.write(output.encode("utf-8"))
        
        def RotUpdate(self,ser=self.ser,address=rotAdd):
            address=int(address)
            output = address+ringRotVar.get()
            output=str(output)+"*"
            print("rotation: " + output[2:-1])
            ser.write(output.encode("utf-8"))
            
            
        frame1=tk.Frame(master=parent)
        frame1.grid(row=0,column=0)#pack(side="left") 
        frame2=tk.Frame(master=parent)
        frame2.grid(row=0,column=1)
        
        self.ringLabel = tk.Label(master=frame1,text = label)
        self.ringLabel.pack()
        #self.ringLabel.grid(row = 0, column = 0,sticky="W")
       
        self.ringOnButt = self.ringButton(parent=frame1,
                                          fill="x",
                                          buttText="ON",color="green",func=self.ringOn)

        self.ringOnffButt = self.ringButton(parent=frame1,
                                            fill="x",
                                            buttText="OFF",color="red",func=self.ringOff)


        self.ringZapTime = tk.Entry(frame1,width=10)
        self.ringZapTime.insert(0,"zap in ms")        
        self.ringZapTime.pack(fill="x")#grid(row=1,column=3,sticky="W",columnspan=2)        
        
        self.ringZapButt = self.ringButton(parent=frame1,
                                           fill="x",
                                           buttText="ZAP",color="black",func=self.ringZap)
        

        



        
        
        self.ringGreen = self.ringSlider(parent=frame2,  text_="Green",                                 
                                        func=GreenUpdate,
                                        fill_="x",
                                        var=ringGreenVar,
                                        rowIndx=0,colIndx=1,sticky="WE",
                                        from__=100,to__=0,res=1,set_=0)
                   
        self.ringRed = self.ringSlider(parent=frame2,  text_="Red",            
                                       func=RedUpdate,fill_="x",
                                       var=ringRedVar,
                                       rowIndx=0,colIndx=2,sticky="WE",
                                       from__=100,to__=0,res=1,set_=0)
                                       
        self.ringBlue = self.ringSlider(parent=frame2,  text_="Blue",            
                                        func=BlueUpdate,
                                        var=ringBlueVar,fill_="x",
                                        rowIndx=0,colIndx=3,sticky="WE",
                                        from__=100,to__=0,res=1,set_=0)

        self.ringBright = self.ringSlider(parent=frame2,  text_="Brightness",            
                                          func=BrightUpdate,fill_="x", 
                                          var=ringBrightVar,colSpan=1,
                                          rowIndx=0,colIndx=4,sticky="WE",
                                          from__=255,to__=0,res=1,set_=0)

        self.ringRot = self.ringSlider(parent=frame2,  text_="Rotate",
                                       func=RotUpdate,colSpan=2,
                                       var=ringRotVar,orient_="vertical",
                                       rowIndx=0,colIndx=5,fill_="x",
                                       from__=100,to__=-100,res=5,set_=0)
        
        
        
        
#        ####create ring protocol part#######################################
#        if flypiApp.protocolFlag==1:
#            protLabel = tk.Label(master=self.protFrame,text="Ring:")
#            protLabel.grid(row=1,column=0,columnspan=1,sticky="NW")
#            
#            ringV1= tk.StringVar(master=self.protFrame)
#            ringV1.set(ringOffAdd)
#            ringV2= tk.StringVar(master=self.protFrame)
#            ringV2.set(ringOffAdd)
#            ringV3= tk.StringVar(master=self.protFrame)
#            ringV3.set(ringOffAdd)
#            ringV4= tk.StringVar(master=self.protFrame)
#            ringV4.set(ringOffAdd)
#            ringV5= tk.StringVar(master=self.protFrame)
#            ringV5.set(ringOffAdd)
#            
#            def ringProtCB1():
#                dummie=ringV1.get()
#                print(dummie)
#                return dummie
#                
#            def ringProtCB2():
#                dummie=ringV2.get()
#                print(dummie)
#            
#            def ringProtCB3():
#                dummie=ringV3.get()
#                print(dummie)
#                
#            def ringProtCB4():
#                dummie=ringV4.get()
#                print(dummie)
#                
#            def ringProtCB5():
#                dummie=ringV5.get()
#                print(dummie)
#
#            ringMods =[ ("ON", ringOnAdd,ringV1,ringProtCB1),("OFF", ringOffAdd,ringV1,ringProtCB1),
#                        ("ON", ringOnAdd,ringV2,ringProtCB2),("OFF", ringOffAdd,ringV2,ringProtCB2),
#                        ("ON", ringOnAdd,ringV3,ringProtCB3),("OFF", ringOffAdd,ringV3,ringProtCB3),
#                        ("ON", ringOnAdd,ringV4,ringProtCB4),("OFF", ringOffAdd,ringV4,ringProtCB4),
#                        ("ON", ringOnAdd,ringV5,ringProtCB5),("OFF", ringOffAdd,ringV5,ringProtCB5)]
##            row1=1
##            column1=1
#            buttonsFrame=tk.Frame(master=self.protFrame)
#            buttonsFrame.grid(row=2,column=1)
#            row1=0
#            column1=0
#            for label,address,var,call in ringMods:
#                protButt1=tk.Radiobutton(master=buttonsFrame,text=label, 
#                                             command=call,indicatoron=0,
#                                             value=address,variable=var,width=5)
#                protButt1.grid(row=row1,column=column1,sticky="NW")
#                if row1==1:
#                    row1=0
#                    column1=column1+1
#                else:
#                    row1=row1+1
                    
                
                    
                
            
            
        
        #var=tk.StringVar()        
        #ringMenu=tk.OptionMenu(parent,var,"ON","OFF")            
        #var.set("OFF")
        #return (var,ringMenu)#          
            
            
    
    def ringButton(self,parent="none",side="top",fill="x",
                   buttText="button",color="black",func="none"):

        button = tk.Button(parent,text = buttText, fg = color, command = func)
        button.pack(side=side,fill=fill)#,fill="x")#grid(row=rowIndx,column=colIndx,sticky=sticky)           
    
    def ringSlider(self,parent="none",  text_="empty",side="right",          
                   func="", var="",color="black",fill_="x",
                   rowIndx=1,colIndx=0,sticky="",orient_="vertical",
                   colSpan=1,
                   from__=100,to__=0,res=1,set_=0):
        
        frame_loc=tk.Frame(master=parent)
        Label = tk.Label(master=frame_loc,text=text_,fg=color)
        Label.pack(fill=fill_)       
        #Label.grid(row=rowLabel,column=colIndx,columnspan=colSpan)        
        Slider = tk.Scale(master=frame_loc,
                          from_=from__,to=to__,resolution=res,
                          command=func,variable=var,orient=orient_)
        Slider.set(set_)
        Slider.pack()
        frame_loc.grid(row=rowIndx,column=colIndx)
        #Slider.grid(row=rowIndx,column=colIndx,columnspan=colSpan)  
        
    def ringOn(self):
        output=str(self.ringOnAdd)
        print("ring on " + output)
        self.ser.write(output.encode("utf-8"))
        
    def ringOff(self):
        output=str(self.ringOffAdd)        
        print("ringOff" + output)
        self.ser.write(output.encode("utf-8"))
        
    def ringZap(self):
        time = int(self.ringZapTime.get())
        time = str(int(self.ringZapAdd)+time)
        self.ser.write(time.encode("utf-8")+"*")
        print("ringZAP for "+time)
    
    


    

    ######################################## LED
class LED:
    def __init__(self,parent="none",label="LED",
                 onAdd="21",offAdd="22",
                 zapDurAdd="24000",
                 ser=""):
                    
        self.label=label
        self.onAdress=onAdd
        self.offAdress=offAdd

        self.zapDurAddress=zapDurAdd
        self.ledLabel = tk.Label(master=parent,text = self.label)
        self.ledLabel.pack()#grid(row = 0, column = 0)
        self.ser=ser
                        
        self.ledOnButt = tk.Button(master=parent,text = "ON", fg = "green", command = self.ledOn)
        self.ledOnButt.pack(fill="x")
        

        self.ledOffButt = tk.Button(master=parent,text = "OFF", fg = "RED", command = self.ledOff)
        self.ledOffButt.pack(fill="x")        

        
        self.ledZapTime = tk.Entry(master=parent,width=10)
        self.ledZapTime.insert(0,"zap in ms")
        self.ledZapTime.pack(fill="x")
        
        self.ledZapButt = tk.Button(master=parent,text = "ZAP!", command = self.ledZap)
        self.ledZapButt.pack(fill="x")        
 
    #callbacks for LED
    def ledOn(self):
        output=str(self.onAdress)
        self.ser.write(output.encode("utf-8"))
        #test = self.led1ZapTime.get()
        print (self.label+" ON")
    def ledOff(self):
        output=str(self.offAdress)        
        self.ser.write(output.encode("utf-8"))
        print(self.label +" OFF")
        #ser.write(b"22,")
    def ledZap(self):
        time = self.ledZapTime.get()
        if time=="zap in ms":
            time=0
            print "you didn't set a value!"
        time=int(time)
        time = str(int(self.zapDurAddress)+time)
        self.ser.write(time.encode("utf-8")+"*")
        print(self.label+" ZAP for "+time[1:])
        
################Protocol
class Protocol:
    
    
    def __init__(self,parent="",ser=""):
        protFrame=tk.Frame(master=parent)
        protFrame.grid(row=0,column=0)
        protLabel=tk.Label(master=protFrame,text="PROTOCOL:")
        protLabel.grid(row=0,column=0,columnspan=2)
        
        #####protocol led1####
        if flypiApp.led1Flag==1:
            
            led1V1= tk.StringVar(master=protFrame)
            led1V1.set(flypiApp.led1OffAdd)
            
            led1V2= tk.StringVar(master=protFrame)
            led1V2.set(flypiApp.led1OffAdd)
            
            led1V3= tk.StringVar(master=protFrame)
            led1V3.set(flypiApp.led1OffAdd)
            
            led1V4= tk.StringVar(master=protFrame)
            led1V4.set(flypiApp.led1OffAdd)
            
            led1V5= tk.StringVar(master=protFrame)
            led1V5.set(flypiApp.led1OffAdd)    
            
            def led1ProtCB():
                dummie=list()
                dummie.append(led1V1.get())
                dummie.append(led1V2.get())
                dummie.append(led1V3.get())
                dummie.append(led1V4.get())
                dummie.append(led1V5.get())
                return dummie
                
            
            protLed1Label=tk.Label(master=protFrame,text="LED1:")
            protLed1Label.grid(row=1,column=0)
            led1Mods =[ ("ON", flypiApp.led1OnAdd,led1V1),
                        ("OFF", flypiApp.led1OffAdd,led1V1),
                        ("ON", flypiApp.led1OnAdd,led1V2),
                        ("OFF", flypiApp.led1OffAdd,led1V2),
                        ("ON", flypiApp.led1OnAdd,led1V3),
                        ("OFF", flypiApp.led1OffAdd,led1V3),
                        ("ON", flypiApp.led1OnAdd,led1V4),
                        ("OFF", flypiApp.led1OffAdd,led1V4),
                        ("ON", flypiApp.led1OnAdd,led1V5),
                        ("OFF", flypiApp.led1OffAdd,led1V5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame,bd=3)
            buttonsFrame.grid(row=1,column=1)
            row1=0
            column1=0
            for label,address,var in led1Mods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label, 
                                             command=led1ProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==1:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1
        
        
        
        
        #####protocol led2#############
        if flypiApp.led2Flag==1:
            led2V1= tk.StringVar(master=protFrame)
            led2V1.set(flypiApp.led2OffAdd)
            
            led2V2= tk.StringVar(master=protFrame)
            led2V2.set(flypiApp.led2OffAdd)
            
            led2V3= tk.StringVar(master=protFrame)
            led2V3.set(flypiApp.led2OffAdd)
            
            led2V4= tk.StringVar(master=protFrame)
            led2V4.set(flypiApp.led2OffAdd)
            
            led2V5= tk.StringVar(master=protFrame)
            led2V5.set(flypiApp.led2OffAdd)    
            
            def led2ProtCB():
                dummie=list()
                dummie.append(led2V1.get())
                dummie.append(led2V2.get())
                dummie.append(led2V3.get())
                dummie.append(led2V4.get())
                dummie.append(led2V5.get())
                return dummie
                

            
            protled2Label=tk.Label(master=protFrame,text="LED 2:")
            protled2Label.grid(row=3,column=0)
            led2Mods =[ ("ON", flypiApp.led2OnAdd,led2V1),
                        ("OFF", flypiApp.led2OffAdd,led2V1),
                        ("ON", flypiApp.led2OnAdd,led2V2),
                        ("OFF", flypiApp.led2OffAdd,led2V2),
                        ("ON", flypiApp.led2OnAdd,led2V3),
                        ("OFF", flypiApp.led2OffAdd,led2V3),
                        ("ON", flypiApp.led2OnAdd,led2V4),
                        ("OFF", flypiApp.led2OffAdd,led2V4),
                        ("ON", flypiApp.led2OnAdd,led2V5),
                        ("OFF", flypiApp.led2OffAdd,led2V5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame,bd=3)
            buttonsFrame.grid(row=3,column=1)
            row1=0
            column1=0
            for label,address,var in led2Mods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label, 
                                             command=led2ProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==1:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1
        
        
        
        #######protocol matrix#########
        if flypiApp.matrixFlag==1:
            
            matV1= tk.StringVar(master=protFrame)
            matV1.set(flypiApp.matOffAdd)
            
            matV2= tk.StringVar(master=protFrame)
            matV2.set(flypiApp.matOffAdd)
            
            matV3= tk.StringVar(master=protFrame)
            matV3.set(flypiApp.matOffAdd)
            
            matV4= tk.StringVar(master=protFrame)
            matV4.set(flypiApp.matOffAdd)
            
            matV5= tk.StringVar(master=protFrame)
            matV5.set(flypiApp.matOffAdd)    
            
            def matProtCB():
                dummie=list()
                dummie.append(matV1.get())
                dummie.append(matV2.get())
                dummie.append(matV3.get())
                dummie.append(matV4.get())
                dummie.append(matV5.get())
                return dummie
                

            
            protMatLabel=tk.Label(master=protFrame,text="MATRIX:")
            protMatLabel.grid(row=4,column=0)
            matMods =[ ("ON", flypiApp.matOnAdd,matV1),
                        ("OFF", flypiApp.matOffAdd,matV1),
                        ("PATT1", flypiApp.matPat1Add,matV1),
                        ("PATT2", flypiApp.matPat2Add,matV1),
                        ("ON", flypiApp.matOnAdd,matV2),
                        ("OFF", flypiApp.matOffAdd,matV2),
                        ("PATT1", flypiApp.matPat1Add,matV2),
                        ("PATT2", flypiApp.matPat2Add,matV2),
                        ("ON", flypiApp.matOnAdd,matV3),
                        ("OFF", flypiApp.matOffAdd,matV3),
                        ("PATT1", flypiApp.matPat1Add,matV3),
                        ("PATT2", flypiApp.matPat2Add,matV3),
                        ("ON", flypiApp.matOnAdd,matV4),
                        ("OFF", flypiApp.matOffAdd,matV4),
                        ("PATT1", flypiApp.matPat1Add,matV4),
                        ("PATT2", flypiApp.matPat2Add,matV4),
                        ("ON", flypiApp.matOnAdd,matV5),
                        ("OFF", flypiApp.matOffAdd,matV5),
                        ("PATT1", flypiApp.matPat1Add,matV5),
                        ("PATT2", flypiApp.matPat2Add,matV5),]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame,bd=3)
            buttonsFrame.grid(row=4,column=1)
            row1=0
            column1=0
            for label,address,var in matMods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label, 
                                             command=matProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==3:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1
        
        
        #####protocol ring#########
        if flypiApp.ringFlag==1:
            protRingLabel = tk.Label(master=protFrame,text="RING:")
            protRingLabel.grid(row=5,column=0,columnspan=2,sticky="NW")
            
            ringV1= tk.StringVar(master=protFrame)
            ringV1.set(flypiApp.ringOffAdd)
            ringV2= tk.StringVar(master=protFrame)
            ringV2.set(flypiApp.ringOffAdd)
            ringV3= tk.StringVar(master=protFrame)
            ringV3.set(flypiApp.ringOffAdd)
            ringV4= tk.StringVar(master=protFrame)
            ringV4.set(flypiApp.ringOffAdd)
            ringV5= tk.StringVar(master=protFrame)
            ringV5.set(flypiApp.ringOffAdd)
            
            def ringProtCB():
                dummie=list()
                dummie.append(ringV1.get())
                dummie.append(ringV2.get())
                dummie.append(ringV3.get())
                dummie.append(ringV4.get())
                dummie.append(ringV5.get())
                return dummie
                
            

            ringMods =[ ("ON", flypiApp.ringOnAdd,ringV1),
                       ("OFF", flypiApp.ringOffAdd,ringV1),
                        ("ON", flypiApp.ringOnAdd,ringV2),
                        ("OFF", flypiApp.ringOffAdd,ringV2),
                        ("ON", flypiApp.ringOnAdd,ringV3),
                        ("OFF", flypiApp.ringOffAdd,ringV3),
                        ("ON", flypiApp.ringOnAdd,ringV4),
                        ("OFF", flypiApp.ringOffAdd,ringV4),
                        ("ON", flypiApp.ringOnAdd,ringV5),
                        ("OFF", flypiApp.ringOffAdd,ringV5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame)
            buttonsFrame.grid(row=5,column=1)
            row1=0
            column1=0
            for label,address,var in ringMods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label, 
                                             command=ringProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==1:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1
                    
                    
        if flypiApp.peltierFlag==1:
            
            protPeltLabel = tk.Label(master=protFrame,text="PELTIER:")
            protPeltLabel.grid(row=6,column=0,columnspan=2,sticky="NW")
            
            peltV1= tk.StringVar(master=protFrame)            
            peltV1.set(flypiApp.peltOffAdd)
            peltTV1=tk.StringVar(master=protFrame)            
            peltTV1.set("temp")
            
            peltV2= tk.StringVar(master=protFrame)            
            peltV2.set(flypiApp.peltOffAdd)
            peltTV2=tk.StringVar(master=protFrame)
            peltTV2.set("temp")
            
            peltV3= tk.StringVar(master=protFrame)
            peltV3.set(flypiApp.peltOffAdd)
            peltTV3=tk.StringVar(master=protFrame)
            peltTV3.set("temp")
            
            peltV4= tk.StringVar(master=protFrame)
            peltV4.set(flypiApp.peltOffAdd)
            peltTV4=tk.StringVar(master=protFrame)
            peltTV4.set("temp")            
            
            peltV5= tk.StringVar(master=protFrame)
            peltV5.set(flypiApp.peltOffAdd)
            peltTV5=tk.StringVar(master=protFrame)
            peltTV5.set("temp")            
            
            def peltProtCB():
                dummie=list()
                dummie.append(peltV1.get())
                dummie.append(peltV2.get())
                dummie.append(peltV3.get())
                dummie.append(peltV4.get())
                dummie.append(peltV5.get())
                temp=list()
                temp.append(peltTV1.get())
                temp.append(peltTV2.get())
                temp.append(peltTV3.get())
                temp.append(peltTV4.get())
                temp.append(peltTV5.get())
                return dummie, temp
                
           
                
            peltMods =[ ("ON", flypiApp.peltOnAdd,peltV1),
                       ("OFF", flypiApp.peltOffAdd,peltV1),
                        ("TEMP",flypiApp.peltTempAdd,peltTV1),
                        ("ON", flypiApp.peltOnAdd,peltV2),
                        ("OFF", flypiApp.peltOffAdd,peltV2),
                        ("TEMP",flypiApp.peltTempAdd,peltTV2),                        
                        ("ON", flypiApp.peltOnAdd,peltV3),
                        ("OFF", flypiApp.peltOffAdd,peltV3),
                        ("TEMP",flypiApp.peltTempAdd,peltTV3),
                        ("ON", flypiApp.peltOnAdd,peltV4),
                        ("OFF", flypiApp.peltOffAdd,peltV4),
                        ("TEMP",flypiApp.peltTempAdd,peltTV4),
                        ("ON", flypiApp.peltOnAdd,peltV5),
                        ("OFF", flypiApp.peltOffAdd,peltV5),
                        ("TEMP",flypiApp.peltTempAdd,peltTV5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame)
            buttonsFrame.grid(row=6,column=1)
            row1=0
            column1=0
            for label,address,var in peltMods:
                if label is "TEMP":
                    
                    proEntry=tk.Entry(master=buttonsFrame,
                                      width=5,text="temp",
                                      textvariable=var)
                    proEntry.grid(row=row1,column=column1,sticky="NW")
#                    if row1=0:
#                        tempLabel=tk.label()
                else:
                    protButt1=tk.Radiobutton(master=buttonsFrame,text=label, 
                                             command=peltProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                    protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==2:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1
                    
        ####### create the time for each round:
        protDurLabel = tk.Label(master=protFrame,text="DUR(S):")
        protDurLabel.grid(row=7,column=0,columnspan=2,sticky="NW")                    
        
        durV1=tk.StringVar(master=protFrame)            
        durV1.set("0.0")
        
        durV2= tk.StringVar(master=protFrame)            
        durV2.set("0.0")
        
        
        durV3= tk.StringVar(master=protFrame)
        durV3.set("0.0")
        
        
        durV4= tk.StringVar(master=protFrame)
        durV4.set("0.0")
        
        
        durV5= tk.StringVar(master=protFrame)
        durV5.set("0.0")
        
        def durProtCB():
            dummie=list()
            dummie.append(durV1.get())
            dummie.append(durV2.get())
            dummie.append(durV3.get())
            dummie.append(durV4.get())
            dummie.append(durV5.get())
            return dummie
                
       
        durMods =[     ("TEMP",durV1),
                        ("TEMP",durV2),                        
                        ("TEMP",durV3),
                        ("TEMP",durV4),
                        ("TEMP",durV5),]
        buttonsFrame=tk.Frame(master=protFrame)
        buttonsFrame.grid(row=7,column=1)
        row1=0
        column1=0
        for label,var in durMods:               
            durEntry=tk.Entry(master=buttonsFrame,
                                      width=5,text="temp",
                                      textvariable=var)
            durEntry.grid(row=row1,column=column1,sticky="NW")
#                    if row1=0:
#                        tempLabel=tk.label()
            column1=column1+1
        #######create the run and dry run buttons
        #create callbacks
        def dryRunCB():
            allVar=dict()
            if flypiApp.led1Flag==1:
                led1=led1ProtCB()
                allVar["led1"]=led1
                
            if flypiApp.led2Flag==1:
                led2=led2ProtCB()
                allVar["led2"]=led2
                
            if flypiApp.matrixFlag==1:
                matrix=matProtCB()
                allVar["matrix"]=matrix
                
            if flypiApp.ringFlag==1:
                ring=ringProtCB()
                allVar["ring"]=ring
                
            if flypiApp.peltierFlag==1:
                peltier,temp=peltProtCB()
                allVar["peltier"]=(peltier,temp)
                

            durations=durProtCB()
            allVar["durations"]=durations
            print (allVar)
            return allVar

        def runCB():
            allVars=dryRunCB()
            if flypiApp.cameraFlag==1:
                print "recording"
                ###wait a couple of seconds for the camera to settle
                ###start recording
            #send prot address to arduino and send code to be run
                
            
            
        protDryRun=tk.Button(master=protFrame, text="DRY RUN",command=dryRunCB,)
        protDryRun.grid(row=2,column=5,sticky="WN")
        
        protRun=tk.Button(master=protFrame, text="RUN",command=runCB,)
        protRun.grid(row=3,column=5,sticky="WN")
        
        #protrunRec=tk.Checkbutton
        
    ######################################## MATRIX
class Matrix:
        
    def __init__(self,parent="none",label="none",
                 onAdd="39",offAdd="40",pat1Add="41",
                 pat2Add="42",brightAdd="43000",ser=""):
        
        self.label=label
        self.onAdd=onAdd
        self.offAdd=offAdd      
        self.pat1Add=pat1Add
        self.pat2Add=pat2Add 
        self.brightAdd=brightAdd
        self.ser=ser
        self.matParent=parent
        #####callback for brightness slider
        matBrightVar = tk.IntVar()                    
        def matrixUpdate(self,ser=self.ser,brightAdd=self.brightAdd):
            address=int(brightAdd)
            output = address+matBrightVar.get()
            output=str(output)+"*"
            print("mat bright " + output[2:-1])
            ser.write(output.encode("utf-8"))
            
        frame1=tk.Frame(master=self.matParent,width=10) 
        frame1.pack()
        self.matrixLabel = tk.Label(master=frame1,text = self.label)
        self.matrixLabel.pack(side="top")#grid(row = 0, column = 0,sticky="NW")
        
        self.matrixOnButt = self.MatButton(parent=frame1,side="top",
                                      buttText="ON",color="green",
                                      func=self.matrixOn,fill="x")
                  
        self.matrixOffButt = self.MatButton(parent=frame1,side="top",
                                            buttText="OFF",color="red",
                                            func=self.matrixOff,fill="x")

        self.matrixPat1Butt = self.MatButton(parent=frame1,side="top",
                                      buttText="PATTERN 1",color="black",
                                      func=self.matrixPattern1,fill="x")

        self.matrixPat2Butt = self.MatButton(parent=frame1,side="top",
                                      buttText="PATTERN 2",color="black",
                                      func=self.matrixPattern2,fill="x")

        frame4=tk.Frame(master=frame1)
        
        self.matrixBrightLabel=tk.Label(master=frame4,text="Brightness")
        self.matrixBrightLabel.pack()
        self.matrixBright = tk.Scale(master=frame4,from_=0, to=255,
                                     orient="vertical",
                                     var=matBrightVar, command=matrixUpdate,
                                     width=15,length=90)
                                     
        self.matrixBright.pack(after=self.matrixBrightLabel,side="left")#grid(row=1,column=5,sticky="N")
        frame4.pack(after=self.matrixLabel,side="right")
#        self.matrixBrightLabel=tk.Label(master=frame1,text = "brightness")
#        self.matrixBrightLabel.pack(side="top")#grid(row=0,column=5,sticky="W")
        
        
    def MatButton(self,parent="none",fill="y",
                  side="top",buttText="button",
                  color="black",func="none"):
                   
        button = tk.Button(parent,text = buttText, fg = color, command = func)
        button.pack(side=side,fill=fill)#grid(row=rowIndx,column=colIndx,columnspan=colSpan);
        
        
    def matrixOn(self):
        output=str(self.onAdd)+"*"
        print ("matrix on " + output)
        self.ser.write(output.encode("utf-8"))
        
    def matrixOff(self):
        output=str(self.offAdd)+"*"
        print("matrix off " + output)
        self.ser.write(output.encode("utf-8"))
        
    def matrixPattern1(self):
        output=str(self.pat1Add)+"*"
        print("matrix pattern1 " + output)
        self.ser.write(output.encode("utf-8"))
    
    def matrixPattern2(self):
        output=str(self.pat2Add)+"*"
        print("matrix pattern2 "+ output )
        self.ser.write(output.encode("utf-8"))
    
    ################PELTIER
class Peltier:
    def __init__(self,parent="none",label="",ser="",
                 onAdd="",offAdd="",tempAdd=""):
        import Tkinter as tk 
        
        self.peltParent=parent
        self.ser=ser
        
        self.peltTempArd=tk.StringVar()    
        peltTempVar=tk.IntVar()
        
        self.peltGetTempArd()

        def peltSetTemp(self):
            tempVal=peltTempVar.get()
            tempVal=tempVal+int(tempAdd)
            print(tempVal)
            ser.write(str(tempVal)+"*")
        frame1=tk.Frame(master=self.peltParent)
        frame1.grid(row=0,column=0,sticky="NW")    
        frame2=tk.Frame(master=self.peltParent)
        frame2.grid(row=0,column=1,sticky="NW")  
        
        self.peltLabel=tk.Label(master=frame1,text=label)
        self.peltLabel.pack(side="top")
        self.peltOnButt = tk.Button(master =frame1,text="ON ",fg="green",
                                    command=self.peltOn)        
        self.peltOnButt.pack(side="top",fill="x")
        
        self.peltOffButt = tk.Button(master = frame1,text="OFF",fg="red",
                                     command=self.peltOff)        
        self.peltOffButt.pack(side="top",fill="x")
        
        self.peltTempDisLabel=tk.Label(master=frame1,text="temp(C):")
        self.peltTempDisLabel.pack(side="top")
        
        self.peltTempDis = tk.Label(master=frame1,
                                    width=10,
                                    textvariable=self.peltTempArd)
                                    
        self.peltTempDis.pack(side="top") 
        
        self.tempLabel=tk.Label(master = frame2,text = "set temp(C)")
        self.tempLabel.pack(side="top")
        
        self.peltTemp = tk.Scale(master=frame2,
                                    from_=37, to=15,resolution=1,
                                    orient="vertical",repeatinterval=300,
                                     variable=peltTempVar, command=peltSetTemp)
        self.peltTemp.set(str(25.0))
        self.peltTemp.pack(side="top")
    
   
   
                          
    def peltOn(self):
        print("peltier on")
        #print(peltTempVar)
        #ser
    def peltOff(self):
        print("peltier off")
        #print(peltSetTemp)
        #ser

    def peltGetTempArd(self):
        self.peltParent.after(900, self.peltGetTempArd)
        #print("func")
        
        if self.ser.inWaiting > 0:
            #print("working")
            dummie=self.ser.readline() 
            self.peltTempArd.set(dummie)
            print ("temperature: " + dummie)
#        else:
#            print("nothing to read")
        
    


        
    ######################################## CAMERA
class Camera:    
       
    def __init__(self,parent="none",label="CAMERA"):           
        import Tkinter as tk 
        self.camParent=parent
        self.autoExpVar=tk.IntVar() 
        self.flipVar = tk.IntVar()
        
        try:
            import picamera # picamera module
            #picameraAvail = True
            ##setup camera
            self.cam = picamera.PiCamera()
            self.cam.led = False
            self.cam.exposure_mode = "fixedfps"
            self.cam.exposure_compensation = 0
            self.cam.brightness = 50
            
        except ImportError:
            #picameraAvail = False
            print ("picamera module not available!")    
        
      
        zoomVar=tk.IntVar()
        def camGetZoom(self):
            zoom=zoomVar.get()
            print("cam zoom: "+str(zoom)) 
            
        FPSVar=tk.IntVar()
        def camGetFPS(self):
            FPSVal=FPSVar.get()
            print("cam frames per sec: "+str(FPSVal)) 
            
        binVar=tk.IntVar()
        def camGetBin(self):
            binVal=binVar.get()
            print("cam binning: "+str(binVal)) 
        
        resVar=tk.IntVar()
        def camGetRes(self):
            resVal=resVar.get()
            print("cam resolution: "+str(resVal)) 
        
        sizeVar=tk.IntVar()
        def camGetSize(self):
            sizeVal=sizeVar.get()
            print("image size: "+str(sizeVal))

        horVar=tk.IntVar()
        def camGetHor(self):
            horVal=horVar.get()
            print("cam horiz position: "+str(horVal))
        verVar=tk.IntVar()
        def camGetVer(self):
            verVal=verVar.get()
            print("cam vert position"+str(verVal))            
            
        brightVar=tk.IntVar()
        def camGetBright(self):
            brightVal=brightVar.get()
            print("cam brightness: " + str(brightVal))

        contVar=tk.IntVar()
        def camGetCont(self):
            contVal=contVar.get()
            print("cam contrast: "+str(contVal))
            
        expVar=tk.IntVar()
        def camGetExp(self):
            expVal=expVar.get()
            print("cam exposure: "+str(expVal))
        
        rotVar=tk.IntVar()
        def camGetRot(self):
            rotVal=rotVar.get()
            print("cam rotation: "+str(rotVal))

        ###frames for all camera controls
        self.camFrame1=tk.Frame(master=self.camParent,bd=2)
        self.camFrame1.grid(row=0,column=0,columnspan=1,rowspan=2,sticky="N")
        
                
        frame2=tk.Frame(master=self.camParent,bd=2)
        frame2.grid(row=0,column=1,sticky="NW",columnspan=2)

        frame3=tk.Frame(master=frame2,bd=2,relief="ridge")
        frame3.grid(row=3,column=1,columnspan=2,rowspan=2,sticky="NW")
        ####
        
        
        
        ####variables for the dropdown menus
        self.camAWVar=tk.StringVar(master=self.camFrame1)
        self.camModVar=tk.StringVar(master=self.camFrame1)
        self.camColEffVar=tk.StringVar(master=self.camFrame1)
        ####
        
        ####callback for menus        
        self.camGetMenus()
        ####


            
        self.label=label
        #self.parent = parent

        self.camLabel = tk.Label(master=self.camFrame1,text = self.label)
        self.camLabel.pack()#grid(row = 0, column = 0,sticky="W")        

        self.camOnButt=self.camButton(parent=self.camFrame1,
                            rowIndx=1,colIndx=0,fill="x",
                            buttText="ON",color="green",func=self.camOn)
       

        self.camOffButt=self.camButton(parent=self.camFrame1,
                            rowIndx=1,colIndx=1,fill="x",
                            buttText="OFF",color="red",func=self.camOff)
     


        
        self.camAWLabel = tk.Label(master=self.camFrame1,text = " White balance ")
        self.camAWLabel.pack(fill="x")#grid(row=3, column=0,sticky="WE")
        self.camAWMenu = tk.OptionMenu(self.camFrame1,
                                       self.camAWVar,
                                       "auto","manual","sunlight","cloudy",
                                       "shade","tungsten","fluorescent","incandescent",
                                       "flash","horizon")
        self.camAWVar.set("auto")
        self.camAWMenu.pack(fill="x")#grid(row=4,column=0,columnspan=2,sticky="WE")  
        self.camAWMenu.pack_propagate(flag=False)
        

        self.camModLabel = tk.Label(master=self.camFrame1,text = "Mode")
        self.camModLabel.pack(fill="x")#grid(row=5, column=0,sticky="W")       
        self.camModes = tk.OptionMenu(self.camFrame1,
                                      self.camModVar,
                                      "none","negative","solarize","sketch",
                                      "denoise","emboss","oilpaint","hatch",
                                      "gpen","pastel","watercolor","film",
                                      "blur","saturation","colorswap","washedout",
                                      "pasterise","colorpoint","colorbalace","cartoon",
                                      "deinterlace1","deinterlace2")                            
        #self.camModes.setvar("none")
        self.camModVar.set("none")
        #self.camModes.pack_propagate(flag=False)
        self.camModes.pack(fill="x")#grid(row=6,column=0,columnspan=2,sticky="WE")
        
        self.camColEffLabel = tk.Label(master=self.camFrame1,text = "color effect")
        self.camColEffLabel.pack(fill="x")#grid(row=3, column=2,sticky="W")       
        self.camColEff = tk.OptionMenu(self.camFrame1,
                                       self.camColEffVar,
                                      "none","RED","GREEN","BLUE","BW")
                                      

        self.camColEff.pack(fill="x")#grid(row=4,column=2,columnspan=1,sticky="WE")
        self.camColEffVar.set("none")
        self.camColEff.pack_propagate(flag=False)
        
#        self.camFPSLabel=tk.Label(master=frame2,text="FPS")
#        self.camFPSLabel.grid(row=0,column=0)              
        self.camFPS = tk.Scale(master=frame2,
                               from_=15, to=90,resolution=5,
                               orient="horizontal",
                               variable=FPSVar, command=camGetFPS,
                               label="FPS",length=90)
        self.camFPS.grid(row=0,column=0)


        
#        self.camBinLabel=tk.Label(master=frame2,text="Binning")
#        self.camBinLabel.grid(row=0,column=1)        
        self.camBin = tk.Scale(master=frame2,from_=1, to=4,
                               orient="horizontal",variable=binVar,
                               command=camGetBin,label="BINNING",
                               length=90)
        self.camBin.grid(row=0,column=1)
               
#        self.camResLabel=tk.Label(master=frame2,text="Resolution")
#        self.camResLabel.grid(row=0,column=2)        
        self.camRes = tk.Scale(master=frame2,from_=512, to=1024,
                               resolution=9,label="RESOLUTION",
                               orient="horizontal",variable=resVar,
                               command=camGetRes,length=90)
        self.camRes.grid(row=0,column=2)
      
#        
#        self.camSizeLabel=tk.Label(master=frame2,text="size")
#        self.camSizeLabel.grid(row=0,column=3)        
        self.camSize = tk.Scale(master=frame2,
                                from_=180, to=2000,resolution=20,
                               orient="horizontal",variable=sizeVar,
                               command=camGetSize,label="WIN SIZE",
                               length=90)
        self.camSize.grid(row=1,column=2)


#        
#        self.camZoomLabel=tk.Label(master=frame2,text="X Zoom")
#        self.camZoomLabel.grid(row=0,column=4)        
        
        self.camZoom = tk.Scale(master=frame2,from_=1, to=10,orient="horizontal",
                                variable=zoomVar, command=camGetZoom,
                                label="DIG ZOOM",length=90)
        self.camZoom.grid(row=1,column=1)

        
#        self.camHorLabel=tk.Label(master=frame2,text="Hor. location")
#        self.camHorLabel.grid(row=2,column=1)        
        self.camHor = tk.Scale(master=frame2,from_=-50, to=50,
                               orient="horizontal",variable=horVar,
                               command=camGetHor,length=90,
                               label="HOR OFFSET")
        self.camHor.set(0)
        self.camHor.grid(row=2,column=1)
        
#        self.camVerLabel=tk.Label(master=frame2,text="Ver. location")
#        self.camVerLabel.grid(row=2,column=2)        
        self.camVer = tk.Scale(master=frame2,from_=-50, to=50,
                               orient="horizontal",variable=verVar,
                               command=camGetVer,length=90,
                               label="VER OFFSET")
        self.camVer.set(0)
        self.camVer.grid(row=2,column=2)
        

#        self.camBrightLabel=tk.Label(master=frame2,text="brightness")
#        self.camBrightLabel.grid(row=2,column=3)        
        self.camBright = tk.Scale(master=frame2,from_=0, to=100,
                               orient="horizontal",variable=brightVar,
                               command=camGetBright,length=90,
                               label="BRIGHTNESS")
        self.camBright.set(50)
        self.camBright.grid(row=1,column=0)
        
#        self.camContLabel=tk.Label(master=frame2,text="contrast")
#        self.camContLabel.grid(row=2,column=4)        
        self.camCont = tk.Scale(master=frame2,
                                from_=0, to=100,resolution=5,
                               orient="horizontal",variable=contVar,
                               command=camGetCont,label="CONTRAST",
                               length=90)
        self.camCont.set(50)
        self.camCont.grid(row=2,column=0)  

             
#        self.camExpLabel=tk.Label(master=frame2,text="exposure")
#        self.camExpLabel.grid(row=2,column=0)        
        self.camExp = tk.Scale(master=frame2,from_=-25, to=25,
                               resolution=1,
                               orient="horizontal",variable=expVar,
                               command=camGetExp,length=90,label="EXPOSURE")
        self.camExp.set(0)
        self.camExp.grid(row=3,column=0)
        
        self.camRot = tk.Scale(master=frame2,from_=0, to=270,
                               resolution=90,
                               orient="horizontal",variable=rotVar,
                               command=camGetRot,length=90,label="ROTATION")
        self.camRot.set(0)
        self.camRot.grid(row=4,column=0)
        
        
        self.autoExposure = tk.Checkbutton(master=self.camFrame1,
                                           text="auto expos.",
                                           variable = self.autoExpVar,
                                           onvalue=1,offvalue=0,
                                           command=self.autoExpVar.get)
        self.autoExpVar.set(1)
        self.autoExposure.pack()#grid(row=2, column=3,sticky="N")
        
        
        self.flip = tk.Checkbutton(master=self.camFrame1,
                                   text="Flip image",
                                   variable = self.flipVar,
                                   onvalue=1,offvalue=0,
                                   command=self.flipVar.get)
        self.flipVar.set(0)
        self.flip.pack()#grid(row=2, column=3,sticky="W")
            
            
        #########Time lapse/video/photo####################            
        
        #self.frame4=tk.Frame(master=self.frame3)           
        self.TLLabel=tk.Label(master=frame3,text="TIME LAPSE")
        self.TLLabel.grid(row=2,column=0,sticky="N")
        

        self.TLdur = tk.Entry(master=frame3,width=8)
        self.TLdur.grid(row=3,column=1,sticky="WN")
        self.TLdur.insert(0,0)
        
        self.TLdurLabel=tk.Label(master=frame3,text="DUR (sec)")  
        self.TLdurLabel.grid(row=2,column=1,sticky="W")
        
        self.TLinter = tk.Entry(master=frame3,width=8)
        self.TLinter.insert(0,0)
        self.TLinter.grid(row=5,column=1,sticky="NW")
        
        self.TLinterLabel=tk.Label(master=frame3,text="INTERVAL (sec)")  
        self.TLinterLabel.grid(row=4,column=1,sticky="W")
        
        self.camRecButt=tk.Button(master=frame3,
                                  text="video",fg="black",
                                  command=self.camRec)
        self.camRecButt.grid(row=3,column=0,sticky="WEN")
                                          
        
        
        
        self.camTLButt=tk.Button(master=frame3,
                                 text="timelapse",fg="black",
                                 command=self.camTL)
        self.camTLButt.grid(row=4,column=0,sticky="WES")
        
                 
        self.camSnapButt=tk.Button(master=frame3,
                                   text="photo",fg="black",command=self.camSnap)
        self.camSnapButt.grid(row=5,column=0,sticky="WEN")
        
       
    
    ########callback for menus
    def camGetMenus(self):
        #this is a recursive function that will call itself 
        #with a minimum interval of 500ms.
        #upon calling it will get the value of three variables
        #white balance, mode and color effect
        self.camFrame1.after(500, self.camGetMenus)
        #print("works")
        aw = self.camAWVar.get()
        cm = self.camModVar.get()
        ce = self.camColEffVar.get()
        autoExp= self.autoExpVar.get()
        flip1= self.flipVar.get()
        print ("white bal: "+ aw)
        print("color effect: " +ce)
        print("cam mode: " +cm) 
        print("auto Exp: "+str(autoExp))
        print("flip: "+str(flip1))
    
    #general function to create buttons
    def camButton(self,parent="none",fill="",side="top",
                  rowIndx=1,colIndx=0,sticky="",
                  buttText="button",color="black",func="none"):
                   
        button = tk.Button(master=parent,text = buttText, fg = color, command = func)
        button.pack(fill=fill,side=side)#grid(row=rowIndx,column=colIndx,sticky=sticky)
        ##
        

                   

    #callbacks for buttons        
    def camOn(self):
        print ("cam on")
    def camOff(self):
        print ("cam Off")
            
            
    def camRec(self):
        dur=self.TLdur.get()
        print ("recording for: " +dur+ " secs" )
    def camTL(self):
        dur=self.TLdur.get()
        interval = self.TLinter.get()
        print("timeLapse:")
        print("duration " + dur)
        print("interval "+interval)
    def camSnap(self):
        print("Click!")
        




       
       
#################PROGRAM EXECUTION       
#create a root     
root = tk.Tk() 
root.title("Fly Pi 0.99")

dummie = flypiApp(root)


#dummie.title("test")
root.resizable(width=False, height=False)
root.mainloop()

root.destroy()



#    ######################################## PROTOCOLS
#class Protocols:
#    
#    def __init__(self,parent="none",label="PROTOCOL"):
#        
#        #create frame
#        self.frame1=tk.Frame(master=parent)
#        #display frame
#        self.frame1.grid(row=0,column=0)
#        #index for update the row where each item will be displayed        
#        self.rowIndx=0  
#        #list for knowing how many items will be displayed        
#        self.protSum=list()
#        
#        #label for the protocol part of the GUI
#        protLabel=tk.Label(master=self.frame1,text=label)
#        protLabel.grid(row=self.rowIndx,column=0)
#        #update row index
#        self.rowIndx=+1        
#        
#        #if the LED1 GUI is displayed
#        if flypiApp.led1Flag==1:
#            label="LED1: "
#            dummie,led1Menu=self.ledMenu(rowIndx=self.rowIndx,colIndx=0,
#                                         text_="LED1: ",parent=self.frame1)
#            led1Menu.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append(label)
#        #if the LED2 GUI is displayed
#        if flypiApp.led2Flag==1:
#            label="LED2: "
#            dummie,led2Menu=self.ledMenu(rowIndx=self.rowIndx,colIndx=0,
#                                         text_=label,parent=self.frame1)
#            led2Menu.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append("LED2: ")
#        #if the MATRIX GUI is displayed
#        if flypiApp.matrixFlag==1:
#            dummie,matMenu=self.matrixMenu(rowIndx=self.rowIndx,colIndx=0,
#                                           text_="MATRIX: ",parent=self.frame1)
#            matMenu.grid(row=self.rowIndx,column=1) 
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append("matrix")
#        #if the RING GUI is displayed
#        if flypiApp.ringFlag==1:
#            dummie,ringMenu=self.ringMenu(rowIndx=self.rowIndx,colIndx=0,
#                                          text_="RING: ",parent=self.frame1)
#            ringMenu.grid(row=self.rowIndx,column=1) 
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append("ring")
#            val = Protocols.runCallBack
#            print ("value"+str(val))
#        #if PELTIER GUI is displayed
#        if flypiApp.peltierFlag==1:
#            var,temp,peltierMenu1,tempEntry=self.peltierMenu(rowIndx=self.rowIndx,colIndx=0,
#                                                            text_="PELTIER: ",parent=self.frame1)
#            peltierMenu1.grid(row=self.rowIndx,column=1) 
#            tempEntry.grid(row=self.rowIndx+2,column=1)
#            self.rowIndx=self.rowIndx+2
#            self.protSum.append("peltier")
#        
#        #if any GUI are displayed create Duration entry
#        if len(self.protSum) != 0:
#            time,timeEntry =self.timeMenu(parent=self.frame1,rowIndx=self.rowIndx,
#                                          colIndx=0,text_="DUR (Sec)")
#                                        
#            timeEntry.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            
#            
#            
#    ##### functions to create the protocol panel        
#    def ledMenu(self,rowIndx=0,colIndx=0,text_="LED",parent="none"):
#
#        ledLabel = tk.Label(master=parent,text=text_)
#        ledLabel.grid(row=rowIndx,column=colIndx)
#        
#        var=tk.StringVar()        
#        ledMenu=tk.OptionMenu(parent,var,"ON","OFF")            
#        var.set("OFF")
#       
#        return(var,ledMenu)
#
#    def matrixMenu(self,rowIndx=0,colIndx=0,text_="MATRIX",parent="none"):
#
#        MatLabel = tk.Label(master=parent,text=text_)
#        MatLabel.grid(row=rowIndx,column=colIndx)
#        
#        var=tk.StringVar()        
#        matMenu=tk.OptionMenu(parent,var,"ON","OFF","PAT1","PAT2")            
#        var.set("OFF")
#        return (var,matMenu)
#    
#    def ringMenu(self,rowIndx=0,colIndx=0,text_="RING",parent="none"):
#
#        ringLabel = tk.Label(master=parent,text=text_)
#        ringLabel.grid(row=rowIndx,column=colIndx)
#        
#        var=tk.StringVar()        
#        ringMenu=tk.OptionMenu(parent,var,"ON","OFF")            
#        var.set("OFF")
#        return (var,ringMenu)#
#    
#    def peltierMenu(self,rowIndx=0,colIndx=0,text_="Peltier",parent="none"):
#
#        peltierLabel = tk.Label(master=parent,text=text_)
#        peltierLabel.grid(row=rowIndx,column=colIndx)
#        
#        var=tk.StringVar()        
#        peltierMenu=tk.OptionMenu(parent,var,"ON","OFF")            
#        var.set("OFF")
#        
#        tempLabel=tk.Label(master=parent,text="TEMP (C)")
#        tempLabel.grid(row=rowIndx+2,column=colIndx)
#        
#        temp=tk.StringVar()
#        tempEntry=tk.Entry(master=parent,width=8,
#                           textvariable=temp)
#        temp.set("25")
#        return (var,temp,peltierMenu,tempEntry)        
#    
#    def timeMenu(self,rowIndx=0,colIndx=0,text_="DUR (Sec)",parent="none"):
#        timeLabel=tk.Label(master=self.frame1,text=text_)
#        timeLabel.grid(row=rowIndx,column=colIndx)
#            
#        time=tk.StringVar()
#        timeEntry=tk.Entry(master=self.frame1,
#                           textvariable=time,
#                           width=8)
#        time.set("0")
#        
#        
#        return(time,timeEntry)
#        
##    def run(self):
##        runButt=tk.Button(master=self.frame1,text="RUN",command=self.run)
##        try:
##            self.protSum("LED1")
##            print "works"
##        except ValueError:
##            print "def works"
#    def runCallBack():
#        try:
#            val = flypiApp.RING.ringGreenVar.get()#flypiApp.RING.ringGreenVar.get()
#            
#            print(val)
#        except NameError:
#            print("no ring")
#        return val

#        self.camAWVar.set("incadescent")
#        self.camFrame1.grid_propagate(flag=False)
#        self.TLLabel.pack()
#        self.camRecButt.pack(fill="x") 
#        self.camTLButt.pack(fill="x")
#        self.camSnapButt.pack(fill="x")
#        self.TLdurLabel.pack()        
#        self.TLdur.pack()        
#        self.TLinterLabel.pack()        
#        self.TLinter.pack()
        