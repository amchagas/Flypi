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
        
        frame1 = tk.Frame(master=self.autofocusparent)
        frame1.grid(row=0, column=1, sticky="NW")
        
        def velSet(self):
            velVal = velVar.get()
            #convert the values to a range
            #between 0 and 180
            velVal = (velVal+10)*9 
            vel = velAdd +"*"+ str(velVal) + "*"
            #print(vel)
            ser.write(vel.encode("utf-8"))
            
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
        
    def autoOff(self):
        print("motor off")
        output = str(self.velAdd) + "*90*"
        self.ser.write(output.encode("utf-8"))
        self.vel1.set(str(0))
