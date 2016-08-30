##################protocols

import tkinter as tk
import os
import re

class Protocol:


    def lockwait():
        print("herre")
        leave=0
        while(leave==0):
            test=self.ser.inWaiting()
            if test>0:
                dummie=self.ser.readline()
                #print(dummie[0:7].decode("utf-8"))
                if dummie[0:7].decode("utf-8") == "waiting":
                    print("done waiting") 
                    leave=1
        
        return



##############################################################################
    def run_protocol(self):
  
        
        #print("here")
        coff=0        
        l1off=0
        l2off=0
        moff=0
        poff=0
        roff=0
        #get the number of repetitions of the 5 choice block
        numReps="self.timeR1.get()"
        numReps = eval(numReps)
        numReps=int(numReps)
        trialDur=0
        print (numReps)
        

        #loop through the repetitions
        for j in range(numReps):
            #loop 5 times (since it is 5 choice block)
            for i in range(5):
                #and get all the names in the varNames list
                for name in self.varNames:
                    print(name)
                    com="self."+name+str(i+1)+".get()"
                    #print(eval(com))
                    #get the duration in every block in the 5 choice block                        
                    for k in range(5):
                        timeTemp = int(eval("self.timeV"+str(k+1)+".get()"))
                        if isinstance(timeTemp,int):
                            trialDur = trialDur+timeTemp
                        else:
                            trialDur = trialDur + 0
                    ####camera
                    if name =="camV" and i==0:
                        
                        if eval(com) =="OFF":
                            self.usedClasses["camera"].camOff()
                            coff=0
                        else:#if the camera is set to ON
                            recTime = 0.0
                            #use the duration of the 5 choice block as recording time (plus a buffer)
                            recTime = float(trialDur) + 1000.0
                            print (recTime)
                            #convert it to secs
                            recTime=float(recTime)/1000.
                            print(recTime)
                            #change the TL dur variable in the camera GUI
                            self.usedClasses["camera"].TLdur.insert(0,str(recTime))
                            #turn it on and start preview using the callback from camera class
                            self.usedClasses["camera"].camOn()
                            #start recording using the callback from camera class
                            self.usedClasses["camera"].camRec()
                            coff=1
                            
                    ####led1
                    if name == "led1V":
                        if eval(com) == "OFF":
                            self.usedClasses["led1"].ledOff()
                            l1off=0
                        else:
                            self.usedClasses["led1"].ledOn()
                            l1off=1
                            
                    ####led2
                    if name == "led2V":
                        if eval(com) == "OFF":
                            self.usedClasses["led2"].ledOff()
                            l2off=0
                        else:
                            self.usedClasses["led2"].ledOn()
                            l2off=1
                    ####matrix
                    if name == "matV":
                        if eval(com) == "OFF":
                            self.usedClasses["matrix"].matrixOff()
                            moff=0
                        elif eval(com) == "Patt1":
                            self.usedClasses["matrix"].matrixPattern1()
                            moff=1
                        elif eval(com) == "Patt2":
                            self.usedClasses["matrix"].matrixPattern2()
                            moff=1
                        elif eval(com) == "Patt3":
                            self.usedClasses["matrix"].matrixPattern3()
                            moff=1
                    ####ring
                    if name == "ringV":
                        if eval(com) == "OFF":
                            self.usedClasses["ring"].ringOff()
                            roff=0
                        elif eval(com) == "ON":
                            red=eval ( "self.ringR"+str(i+1)+".get()")
                            if red >"255":
                                print ("setting red value to 255")
                                red=255
                            else:
                                red=int(red)
                            green=eval ( "self.ringG"+str(i+1)+".get()")
                            if green >"255":
                                print ("setting green value to 255")
                                green=255
                            else:
                                green=int(green)

                            blue=eval ( "self.ringB"+str(i+1)+".get()")
                            if blue =="255":
                                print ("setting blue value to 255")
                                blue=255
                            else:
                                blue=int(blue)
                            
                            self.usedClasses["ring"].rrv.set(str(red))
                            self.usedClasses["ring"].rgv.set(str(green))
                            self.usedClasses["ring"].rbv.set(str(blue))
                            
                            self.usedClasses["ring"].redUpdate(self)
                            self.usedClasses["ring"].greenUpdate(self)
                            self.usedClasses["ring"].blueUpdate(self)
                            self.usedClasses["ring"].ringOn()
                            roff=1
                            
                    if name == "peltV":
                        if eval(com) =="OFF":
                            self.usedClasses["peltier"].peltOff()
                            poff = 0
                        else:
                            temp = eval ( "self.peltT"+str(i+1)+".get()")
                            temp = int(temp)
                            self.usedClasses["peltier"].tempVar.set(temp)
                            self.usedClasses["peltier"].logTemp.set(1)
                            #self.usedClasses["peltier"].peltSetTemp()
                            self.usedClasses["peltier"].peltOn()
                            poff=1
                            #get the duration of one repetition of the 5 choice block
                    
                    if name == "timeV":
                        timeTemp = int(eval("self.timeV"+str(i+1)+".get()"))
                        if isinstance(timeTemp,int):
                            timeTemp = "TIM<"+str(timeTemp)+">>"
            
                        else:
                            timeTemp="TIM<0>>"
                            
                        self.ser.write(timeTemp.encode("utf-8"))
#                        leave=0
#                        while(leave==0):
#                            test=self.ser.inWaiting()
#                            if test>0:
#                                dummie=self.ser.readline()
#                                #print(dummie[0:7].decode("utf-8"))
#                                if dummie[0:7].decode("utf-8") == "waiting":
#                                    print("done waiting") 
#                                    leave=1

                        print("end of period " + str(i+1) +" of trial " + str(j+1))
                
                    #if one reached the end of the trial, turn everything off
                    if i==4 and name =="timeI":
                        #print(i)
                        #print("here")
                        #if coff==1:
                        if self.usedClasses["camera"]:
                            self.usedClasses["camera"].camOff()
                        #if l1off==1:
                        if self.usedClasses["led1"]:
                            self.usedClasses["led1"].ledOff()
                        #if l2off==1:
                        if self.usedClasses["led2"]:
                            self.usedClasses["led2"].ledOff()
                        #if moff==1:
                        if self.usedClasses["matrix"]:
                            self.usedClasses["matrix"].matrixOff()
                        #if roff==1:
                       #print("ringOff!!!!!!!!!!!")
                        if self.usedClasses["ring"]:
                            self.usedClasses["ring"].rrv.set("0")
                            self.usedClasses["ring"].rgv.set("0")
                            self.usedClasses["ring"].rbv.set("0")
                            
                            self.usedClasses["ring"].redUpdate(self)
                            self.usedClasses["ring"].greenUpdate(self)
                            self.usedClasses["ring"].blueUpdate(self)
                            self.usedClasses["ring"].ringOff()
                        
                        #if poff==1:
                        if self.usedClasses["peltier"]:
                            self.usedClasses["peltier"].peltOff#()

                        time = eval("self."+name+str(1)+".get()")
                        
                        if time.isdigit():
                            
                            time="TIM<"+time+">>"
                            self.ser.write(time.encode("utf-8"))
                            #lockwait
#                            leave=0
#                            while(leave==0):
#                                test=self.ser.inWaiting()
#                                if test>0:
#                                    dummie=self.ser.readline()
#                                    #print(dummie[0:7].decode("utf-8"))
#                                    if dummie[0:7].decode("utf-8") == "waiting":
#                                        print("done waiting") 
#                                        leave=1

                    
############################################################################
                                
    def __init__(self, parent="none",ser="",
                 usedClasses = dict(),
                 led1C="",
                 label="Protocol", basePath="~/Desktop/"):

       # self, parent="none", label="none", ser="", #protFrame="",
       #          ringOnAdd="", ringOffAdd="", ringZapAdd="",
       #          greenAdd="", redAdd="", blueAdd="",
       #          allAdd="", rotAdd="")
        self.ser = ser
        frame1 = tk.Frame(master=parent)
        frame1.grid(row=0, column=0)
        self.usedClasses = usedClasses
        self.basePath = basePath
        #create list to store all variables prefixes
        self.varNames = list()
        #buttonsFrame = tk.Frame(master=frame1, bd=3)
        #buttonsFrame.grid(row=1, column=1)
#        self.lockwait=lockwait
        

        rows=0
        protLabel = tk.Label(master=frame1, text=label)
        protLabel.grid(row=rows, column=0)
        rows=rows+1

        
        ######### LED1 #################
        
        if usedClasses["led1"] != 0:
            ledLabel = tk.Label(master=frame1, text="LED1")
            ledLabel.grid(row=rows, column=0)
           

            self.led1V1 = tk.StringVar(master=frame1)
            self.led1V2 = tk.StringVar(master=frame1)
            self.led1V3 = tk.StringVar(master=frame1)
            self.led1V4 = tk.StringVar(master=frame1)
            self.led1V5 = tk.StringVar(master=frame1)
            self.varNames.append("led1V")
            
            temp = [self.led1V1, self.led1V2, self.led1V3, self.led1V4, self.led1V5]

            for k in range(len(temp)):
                protButt1 = tk.OptionMenu(frame1,temp[k], "ON", "OFF")

                temp[k].set("OFF")
                protButt1.grid(row=rows, column=k+1, sticky="NW")
            rows = rows+1

        ############ LED2 ###################

        if usedClasses["led2"] != 0:
            ledLabel = tk.Label(master=frame1, text="LED2")
            ledLabel.grid(row=rows, column=0)

            
            self.led2V1 = tk.StringVar(master=frame1)
            self.led2V2 = tk.StringVar(master=frame1)
            self.led2V3 = tk.StringVar(master=frame1)
            self.led2V4 = tk.StringVar(master=frame1)
            self.led2V5 = tk.StringVar(master=frame1)

            
            temp = [self.led2V1, self.led2V2, self.led2V3, self.led2V4, self.led2V5]
            tempName = ["led2V1", "led2V2", "led2V3", "led2V4", "led2V5"]
            for k in range(len(temp)):
                protButt2 = tk.OptionMenu(frame1, temp[k], "ON", "OFF")

                temp[k].set("OFF")

                
                protButt2.grid(row=rows, column=k+1, sticky="NW")
            rows = rows+1



        ##### Matrix ###########

                
        if usedClasses["matrix"] != 0:
 
            matLabel = tk.Label(master=frame1, text="Matrix")
            matLabel.grid(row=rows, column=0)
            

            self.matV1 = tk.StringVar(master=frame1)
            self.matV2 = tk.StringVar(master=frame1)
            self.matV3 = tk.StringVar(master=frame1)
            self.matV4 = tk.StringVar(master=frame1)
            self.matV5 = tk.StringVar(master=frame1)
            self.varNames.append("matV")  

            temp = [self.matV1, self.matV2, self.matV3, self.matV4, self.matV5]

            
            for k in range(len(temp)):
                protButt3 = tk.OptionMenu(frame1,
                                          temp[k],
                                          "OFF",
                                          "Patt1",
                                          "Patt2",
                                          "Patt3")

                temp[k].set("OFF")
                protButt3.grid(row=rows, column=k+1, sticky="NW")

            rows = rows+1
                ##### ring ###########

                
        if usedClasses["ring"] != 0:
 
            ringLabel = tk.Label(master=frame1, text="Ring")
            ringLabel.grid(row=rows, column=0)

            ringLabel = tk.Label(master=frame1, text="Red")
            ringLabel.grid(row=rows+1, column=0)

            ringLabel = tk.Label(master=frame1, text="Green")
            ringLabel.grid(row=rows+2, column=0)

            ringLabel = tk.Label(master=frame1, text="Blue")
            ringLabel.grid(row=rows+3, column=0)

            self.ringV1 = tk.StringVar(master=frame1)
            self.ringV2 = tk.StringVar(master=frame1)
            self.ringV3 = tk.StringVar(master=frame1)
            self.ringV4 = tk.StringVar(master=frame1)
            self.ringV5 = tk.StringVar(master=frame1)

            self.ringR1 = tk.StringVar(master=frame1)
            self.ringR2 = tk.StringVar(master=frame1)
            self.ringR3 = tk.StringVar(master=frame1)
            self.ringR4 = tk.StringVar(master=frame1)
            self.ringR5 = tk.StringVar(master=frame1)

            self.ringG1 = tk.StringVar(master=frame1)
            self.ringG2 = tk.StringVar(master=frame1)
            self.ringG3 = tk.StringVar(master=frame1)
            self.ringG4 = tk.StringVar(master=frame1)
            self.ringG5 = tk.StringVar(master=frame1)

            self.ringB1 = tk.StringVar(master=frame1)
            self.ringB2 = tk.StringVar(master=frame1)
            self.ringB3 = tk.StringVar(master=frame1)
            self.ringB4 = tk.StringVar(master=frame1)
            self.ringB5 = tk.StringVar(master=frame1)
            self.varNames.append("ringV")
            self.varNames.append("ringR")
            self.varNames.append("ringG")
            self.varNames.append("ringB")
            
            temp = [self.ringV1,self.ringR1,self.ringG1,self.ringB1,
                    self.ringV2,self.ringR2,self.ringG2,self.ringB2,
                    self.ringV3,self.ringR3,self.ringG3,self.ringB3,
                    self.ringV4,self.ringR4,self.ringG4,self.ringB4,
                    self.ringV5,self.ringR5,self.ringG5,self.ringB5]


            x=1
            for k in range(0,len(temp),4):
                 
                protButt3 = tk.OptionMenu(frame1,
                                          temp[k],
                                          "OFF",
                                          "ON")
                temp[k].set("OFF")
                
                protButt3.grid(row=rows, column=x, sticky="NW")
                protEntry2 = tk.Entry(master = frame1, width=7,textvariable=temp[k+1])
                protEntry2.insert(0,"0")
                protEntry2.grid(row=rows+1,column=x,sticky=("NW"))

                protEntry2 = tk.Entry(master = frame1, width=7,textvariable=temp[k+2])
                protEntry2.insert(0,"0")
                protEntry2.grid(row=rows+2,column=x,sticky=("NW"))

                protEntry2 = tk.Entry(master = frame1, width=7,textvariable=temp[k+3])
                protEntry2.insert(0,"0")
                protEntry2.grid(row=rows+3,column=x,sticky=("NW"))
                

                
                x=x+1
                
            rows = rows+4


        if usedClasses["peltier"] != 0:
 
            peltierLabel = tk.Label(master=frame1, text="Peltier")
            peltierLabel.grid(row=rows, column=0)
            
            tempLabel = tk.Label(master=frame1, text="Pelt temp(C)")
            tempLabel.grid(row=rows+1, column=0)
            self.peltV1 = tk.StringVar(master=frame1)
            self.peltV2 = tk.StringVar(master=frame1)
            self.peltV3 = tk.StringVar(master=frame1)
            self.peltV4 = tk.StringVar(master=frame1)
            self.peltV5 = tk.StringVar(master=frame1)
            self.peltT1 = tk.StringVar(master=frame1)
            self.peltT2 = tk.StringVar(master=frame1)
            self.peltT3 = tk.StringVar(master=frame1)
            self.peltT4 = tk.StringVar(master=frame1)
            self.peltT5 = tk.StringVar(master=frame1)

            self.varNames.append("peltV")
            self.varNames.append("peltT")
            
            


            temp = [self.peltV1,self.peltT1,
                    self.peltV2,self.peltT2,
                    self.peltV3,self.peltT3,
                    self.peltV4,self.peltT4,
                    self.peltV5,self.peltT5]

            x=1
            for k in range(0,len(temp),2):
                protButt4 = tk.OptionMenu(frame1,
                                        temp[k],
                                          "OFF",
                                          "ON")
                temp[k].set("OFF")
                protButt4.grid(row=rows, column=x, sticky="NW")
                
                protEntry1 = tk.Entry(master = frame1, width=7,textvariable=temp[k+1])
                protEntry1.insert(0,"25")
                protEntry1.grid(row=rows+1,column=x,sticky=("NW"))
                x=x+1
                #self.allVariables.append(tempName[k])
                #self.allVariables.append(tempName[k+1])
            rows = rows+2

        #####TIME DURATIONS

        timeLabel = tk.Label(master=frame1, text="Dur(ms)")
        timeLabel.grid(row=rows, column=0)
        self.timeV1 = tk.StringVar(master=frame1)
        self.timeV2 = tk.StringVar(master=frame1)
        self.timeV3 = tk.StringVar(master=frame1)
        self.timeV4 = tk.StringVar(master=frame1)
        self.timeV5 = tk.StringVar(master=frame1)
        self.varNames.append("timeV")
        
        temp = [self.timeV1, self.timeV2, self.timeV3, self.timeV4, self.timeV5]
        for k in range(len(temp)):
            timeEntry1 = tk.Entry(master = frame1, width=7,textvariable=temp[k])
            timeEntry1.insert(0,"0")
            timeEntry1.grid(row=rows,column=k+1,sticky=("NW"))
            
        rows=rows+1
        
        ##### number of repetitions
        timeLabel = tk.Label(master=frame1, text="Repetitions")
        timeLabel.grid(row=rows, column=0)

        self.timeR1 = tk.StringVar(master=frame1)
        
        timeEntry2 = tk.Entry(master = frame1, width=7,textvariable=self.timeR1)
        timeEntry2.insert(0,"1")
        timeEntry2.grid(row=rows,column=1,sticky=("NW"))
        rows=rows+1
        
        #### interval in between repetitions
        timeLabel = tk.Label(master=frame1, text="IRI(ms)")
        timeLabel.grid(row=rows, column=0)
        
        self.timeI1 = tk.StringVar(master=frame1)
        self.varNames.append("timeI")
        
        timeEntry3 = tk.Entry(master = frame1, width=7,textvariable=self.timeI1)
        timeEntry3.insert(0,"0")
        timeEntry3.grid(row=rows,column=1,sticky=("NW"))
        rows = rows+1

        ###start protocols
        #runLabel = tk.Label(master=frame1,text="Start protocols:")
        #runLabel.grid(row=rows,column=0)
        #runV1 = tk.StringVar(master=frame1)
        

        
        
        #######CAMERA##############
        if usedClasses["camera"] != 0:
            camLabel = tk.Label(master=frame1, text="Camera")
            camLabel.grid(row=rows, column=0)
            #insert camera in the first position of the list,
            #since it has to be on when the other devices start
            self.varNames.insert(0,"camV")
            self.camV1 = tk.StringVar(master=frame1)
            #self.camV2 = tk.StringVar(master=frame1)
            #self.camV3 = tk.StringVar(master=frame1)
            #self.camV4 = tk.StringVar(master=frame1)
            #self.camV5 = tk.StringVar(master=frame1)

            temp = [self.camV1,] #self.camV2, self.camV3, self.camV4, self.camV5]
            
            #for k in range(len(temp)):
            protButt10 = tk.OptionMenu(frame1, temp[0], "ON", "OFF")
            temp[0].set("OFF") 
            protButt10.grid(row=rows, column=0+1, sticky="NW")
            
            rows = rows+1
            
        runButt = tk.Button(master=frame1,text="RUN!",fg="green",command=self.run_protocol)
        runButt.grid(row=rows-1,column=3)

 