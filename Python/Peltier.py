    ################PELTIER
import tkinter as tk
import os
import time


class Peltier:

    def __init__(self, parent="none", label="", ser="",
                 onAdd="", offAdd="", tempAdd="", basePath=""):

        self.onAdd = onAdd
        self.offAdd = offAdd
        self.tempAdd = tempAdd
        self.peltParent = parent
        self.ser = ser
        self.peltTempArd = tk.StringVar()
        
        peltTempVar = tk.IntVar()
        self.tempVar=peltTempVar
        self.logTemp = tk.IntVar()
        self.basePath = basePath
        self.peltFlag1 = 0

        def lockwait(waitString="waited"):
            flag = True
            #endFlag="END<>"
            #self.ser.flush()
            while flag== True:
                #if there is something to read on the serial port
                test=self.ser.inWaiting()
            
                #            print("test: "+str(test))
                if test>0:                
                    #read line
                    dummie=self.ser.readline()
                    #print (dummie[0:-2])
                    #if the line is "waited" get out of the waiting while loop
                    if dummie[0:-2].decode("utf-8")==waitString:
                    #                    self.ser.write(endFlag.encode("utf-8"))                    
                        flag = False 

            return
            
        def peltSetTemp(self):
            tempVal = peltTempVar.get()
            temp = tempAdd +"<"+str(tempVal) + ">>"
            ser.write(temp.encode("utf-8"))
            lockwait()
            
        frame1 = tk.Frame(master=self.peltParent)
        frame1.grid(row=0, column=0, sticky="NW")
        frame2 = tk.Frame(master=self.peltParent)
        frame2.grid(row=0, column=1, sticky="NW")

        self.peltLabel = tk.Label(master=frame1, text=label)
        self.peltLabel.pack(side="top")
        self.peltOnButt = tk.Button(master=frame1, text="ON ", fg="green",
                                    command=self.peltOn)
        self.peltOnButt.pack(side="top", fill="x")

        self.peltOffButt = tk.Button(master=frame1, text="OFF", fg="red",
                                     command=self.peltOff)
        self.peltOffButt.pack(side="top", fill="x")

        self.peltTempDisLabel = tk.Label(master=frame1, text="temp(C):")
        self.peltTempDisLabel.pack(side="top")

        self.peltTempDis = tk.Label(master=frame1,
                                    width=10,
                                    textvariable=self.peltTempArd)

        self.peltTempDis.pack(side="top")

        self.tempLabel = tk.Label(master=frame2, text="set temp(C)")
        self.tempLabel.pack(side="top")

        self.peltTemp = tk.Scale(master=frame2,
                                    from_=37, to=15, resolution=1,
                                    orient="vertical", repeatinterval=200,
                                    variable=peltTempVar,
                                    command=peltSetTemp)
        self.peltTemp.set(str(30.0))
        self.peltTemp.pack(side="top")
        self.peltLog = tk.Checkbutton(master=frame2,
                                   text="Log temp?",
                                   variable=self.logTemp,
                                   onvalue=1, offvalue=0)
        self.peltLog.pack(side="top")
        self.peltGetTempArd()

    def lockwait(self,waitString="waited"):
        flag = True
        #endFlag="END<>"
        #self.ser.flush()
        while flag== True:
            #if there is something to read on the serial port
            test=self.ser.inWaiting()
        
        #            print("test: "+str(test))
            if test>0:                
                #read line
                dummie=self.ser.readline()
                #print (dummie[0:-2])
                #if the line is "waited" get out of the waiting while loop
                if dummie[0:-2].decode("utf-8")==waitString:
                #                    self.ser.write(endFlag.encode("utf-8"))                    
                    flag = False 

        return
        
    def peltOn(self):
        print("peltier on")
        output = str(self.onAdd)        
        self.sendFlag = 1
        self.ser.write(output.encode("utf-8"))
        self.lockwait()

    def peltOff(self):
        print("peltier off")
        output = str(self.offAdd)
        self.ser.write(output.encode("utf-8"))
        self.lockwait()
        
    def peltGetTempArd(self):
        flag=True
        self.peltParent.after(200, self.peltGetTempArd)
        getTemp = self.tempAdd+"<99>>"
        self.ser.write(getTemp.encode("utf-8"))
#        self.lockwait()
        while flag == True:
            test=self.ser.inWaiting()
            if test>0:
                dummie=self.ser.readline()
                flag=False
        #print(test)
        #make a loop that waits untill data
        #from the arduino is available
        #while test == 0:
            #test = self.ser.inWaiting()
        #dummie = 0
#        if test > 0:
#            dummie = self.ser.readline()
            #dummie = self.ser.read(4)
                
        if str(dummie)[2:-5] != "waited":
            self.peltTempArd.set(dummie)
                #dummie = str(dummie)
            if self.logTemp.get() == 1:
                self.peltFlag1 = 1
                #create a folderpath name to store temperature logs
                logPath = self.basePath + '/log_temp/'
                #check if folder exists
                if not os.path.exists(logPath):
                    #if not, create it:
                    os.makedirs(logPath)
                    os.chown(logPath, 1000, 1000)
                fileName = "temp_log_" + time.strftime('%Y-%m-%d') + ".txt"
                #check if the file already exists
#                 os.chdir(basePath)
                if os.path.isfile(logPath + fileName) == False:
                    #if it does not exist, create it
                    #print("opening file")
                    self.fh = open(logPath + fileName, "w")
                else:
                    #open file and append to it
                    self.fh = open(logPath + fileName, "a")

                #print("writing to file")
                self.fh.write(time.strftime('%Y-%m-%d-%H-%M-%S') + (','))
                self.fh.write(dummie.decode("utf-8"))
