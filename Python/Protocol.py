##################protocols

import tkinter as tk
import os
import re
import time

#os.chdir ("/home/pi/Desktop/flypi/Flypi/Python/")
#import flypiApp as fp
class Protocol:


                    
############################################################################
                                
    def __init__(self, parent="none",ser="",
                 usedClasses = dict(),
                 timingAdd="",
                 label="Protocol", basePath="~/Desktop/"):


        self.ser = ser
        frame1 = tk.Frame(master=parent)
        frame1.grid(row=0, column=0)
        self.usedClasses = usedClasses
        self.basePath = basePath
        #create list to store all variables prefixes
        self.varNames = list()
        self.timingAdd = timingAdd 


        
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

                
        if self.usedClasses["ring"] != 0:
 
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
#                print(k) 
                protButt6 = tk.OptionMenu(frame1,
                                          temp[k],
                                          "OFF",
                                          "ON")
                temp[k].set("OFF")
                
                protButt6.grid(row=rows, column=x, sticky="NW")
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
        
        temp = [self.timeV1, 
                self.timeV2, 
                self.timeV3, 
                self.timeV4, 
                self.timeV5]
        k=1
        for item in temp:
            #print(item)
            timeEntry1 = tk.Entry(master = frame1, width=7,textvariable=item)
            timeEntry1.insert(0,"250")
            timeEntry1.grid(row=rows,column=k,sticky=("NW"))
            k=k+1
        rows=rows+1
        
        ##### number of repetitions
        timeLabel = tk.Label(master=frame1, text="Repetitions")
        timeLabel.grid(row=rows, column=0)

        self.timeR1 = tk.StringVar(master=frame1)
        
        timeEntry2 = tk.Entry(master = frame1, width=7,textvariable=self.timeR1)
        timeEntry2.insert(0,"2")
        timeEntry2.grid(row=rows,column=1,sticky=("NW"))
        rows=rows+1
        
        #### interval in between repetitions
        timeLabel = tk.Label(master=frame1, text="IRI(ms)")
        timeLabel.grid(row=rows, column=0)
        
        self.timeI = tk.StringVar(master=frame1)
        self.varNames.append("timeI")
        
        timeEntry3 = tk.Entry(master = frame1, width=7,textvariable=self.timeI)
        timeEntry3.insert(0,"125")
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


            temp = [self.camV1]
            
            #for k in range(len(temp)):
            protButt10 = tk.OptionMenu(frame1, temp[0], "ON", "OFF")
            temp[0].set("OFF") 
            protButt10.grid(row=rows, column=0+1, sticky="NW")
            
            rows = rows+1
        self.run_protocol()    
        runButt = tk.Button(master=frame1,text="RUN!",fg="green",
                            command=self.run_protocol,repeatdelay=10000)
        runButt.grid(row=rows+1,column=0)
        return
 
    

##############################################################################
    def run_protocol(self):
        def lockwait(waitString="waited"):
            flag = True

            while flag== True:
                #if there is something to read on the serial port
                test=self.ser.inWaiting()

                if test>0:                
                    #read line
                    dummie=self.ser.readline()
                    #if the line is "waited" get out of the waiting while loop
                    if dummie[0:-2].decode("utf-8")==waitString:                    
                        flag = False 
                        #print("done")

            return
            
        #get the number of repetitions of the 5 choice block
        numReps=self.timeR1.get()
        numReps=int(numReps)
        #print (numReps)
        commList = list()
        nullList = list()
        #loop the number of repetitions
        for i in range(1,numReps+1):
            commList.append("<>>")
            commList.append("<>>")
            #get all matrix steps
            for k in range(1,6):#hard coded because there are only 5 periods 
                                #per trial.
                

                #LED1
                if "led1V" in self.varNames:
                    com = eval("self.led1V"+str(k)+".get()")
                    nullList.append("LD1<0>>")
                    if com == "OFF":
                        commList.append("LD1<0>>")
                    else:
                        commList.append("LD1<1>>")
                        
                #LED2
                if "led2V" in self.varNames:
                    com = eval("self.led2V"+str(k)+".get()")
                    nullList.append("LD2<0>>")
                    if com == "OFF":
                        commList.append("LD2<0>>")
                    else:
                        commList.append("LD2<1>>")
                
                #peltier


                #matrix 
                if "matV" in self.varNames:
                    com = eval("self.matV"+str(k)+".get()")
                    nullList.append("MAT<0>>")
                    if com == "OFF":
#                        commList.append(self.usedClasses["matrix"].matrixOff()) 
                        commList.append("MAT<0>>")
                        #commList=[self.usedClasses["matrix"].matrixOff()]
                    elif com == "Patt1":
#                        commList.append(self.usedClasses["matrix"].matrixPattern1())
                        commList.append("MAT<1>>")                        
                    elif com == "Patt2":
#                        commList.append(self.usedClasses["matrix"].matrixPattern2())
                        commList.append("MAT<2>>")
                    elif com == "Patt3":
#                        commList.append(self.usedClasses["matrix"].matrixPattern3())
                        commList.append("MAT<3>>")

                #ring
                if "ringV" in self.varNames:
                    nullList.append("RIN<0>>")
                    
                    blue = "RBL<"+eval("self.ringB"+str(k)+".get()")+">>"
                    red = "RRE<"+eval("self.ringR"+str(k)+".get()")+">>"
                    green ="RGR<"+ eval("self.ringG"+str(k)+".get()")+">>"

                    commList.append(blue)
                    commList.append(red)                   
                    commList.append(green)                    
                        
                        

                    comR = eval("self.ringV"+str(k)+".get()")
                    if comR=="ON":
                        commList.append("RIN<1>>")

                    else:                    
                        commList.append("RIN<0>>")
                        
               
                #execute the time of the trial
                if "timeV"  in self.varNames:
                    nullList.append("TIM<100>>")
                    #self.ser.flush()
                    comT = eval("self.timeV"+str(k)+".get()")
                    
                    #print("comT: " + comT)
#                    output = self.timingAdd+"<"+str(comT)+">>"
                    output = "TIM<"+str(comT)+">>"

                    commList.append(output)

                if "timeI" in self.varNames and k==5:     
                    ITI = "TIM<"+self.timeI.get()+">>"
                    commList.append(ITI)
                    
#        for item in nullList:
#            self.ser.write(item.encode("utf-8"))      
        for item in commList:
            self.ser.write(item.encode("utf-8"))
            lockwait()                
#                time.sleep(0.02)
                #execute inter timing interval
            
            #        #self.ser.flush()
            #        
            #        #print(ITI)
            #        output = self.timingAdd+"<"+ITI+">"
            #        self.ser.write(output.encode("utf-8"))
            #        #self.lockwait()
            #        #self.ser.flush()
            #        print("trial end")
            
            

        return