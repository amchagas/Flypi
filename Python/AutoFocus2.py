    ################Autofocus / servo
import tkinter as tk
import os
import time


class AutoFocus:
    
    def __init__(self, parent="none", label="", ser="",
                 velAdd=""):

        self.velAdd = velAdd
        self.ser = ser
        velVar = tk.IntVar()
        self.vel1=velVar
        self.autofocusparent = parent
        def lockwait(waitString="waited"):
            flag = True
            #endFlag="END<>"
            self.ser.flush()
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
        frame1 = tk.Frame(master=self.autofocusparent)
        frame1.grid(row=0, column=1, sticky="NW")
        
        def velSet(self):
            velVal = velVar.get()
            #convert the values to a range
            #between 0 and 180
            velVal = (velVal+10)*9 
            vel = velAdd +"<"+ str(velVal) + ">>"
            #print(vel)
            ser.write(vel.encode("utf-8"))
            lockwait()
            
        self.autoLabel = tk.Label(master=frame1, text="Auto Focus")
        self.autoLabel.pack(side="top")   
        self.autoscale = tk.Scale(master=frame1,
                                    from_=-10, to=10, resolution=1,
                                    orient="horizontal", repeatinterval=200,
                                    variable = velVar,
                                    command=velSet)

        velVar.set(str(0))
        self.autoscale.pack(side="top")

        self.autoOffButt = tk.Button(master=frame1, text="OFF", fg="red",
                                     command=self.autoOff)
        
        self.autoOffButt.pack(side="top", fill="x")
    
    def lockwait(self,waitString="waited"):
        flag = True
        #endFlag="END<>"
#        self.ser.flush()
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
    def autoOff(self):
        #print("motor off")
        output = str(self.velAdd) + "<90>>"
        self.ser.write(output.encode("utf-8"))
        self.lockwait()
        self.vel1.set(str(0))
