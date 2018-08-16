    ################PELTIER
import tkinter as tk
import os
import time


class Peltier:

    def __init__(self, parent="none", label="", #ser="",
                 onAdd="", offAdd="", tempAdd="", basePath=""):

        self.onAdd = onAdd
        self.offAdd = offAdd
        self.tempAdd = tempAdd
        self.peltParent = parent
        #self.ser = ser
        self.peltTempArd = tk.StringVar()

        peltTempVar = tk.IntVar()
        self.tempVar=peltTempVar
        self.logTemp = tk.IntVar()
        self.basePath = basePath
        self.peltFlag1 = 0
        self.peltierallcalls = list()

        #def peltSetTemp(self):
        #    tempVal = peltTempVar.get()
        #    temp = tempAdd +"<"+str(tempVal) + ">>"
        #    return


        frame1 = tk.Frame(master=self.peltParent)
        frame1.grid(row=0, column=0, sticky="NW")
        #frame2 = tk.Frame(master=self.peltParent)
        #frame2.grid(row=0, column=1, sticky="NW")
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

        self.peltTime = tk.Entry(master=frame1, width=10)

        self.peltTime.insert(0, "no func yet")

        self.peltTime.pack(fill="x")

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
                                    #command=peltSetTemp
                                    )
        self.peltTemp.set(str(30.0))
        self.peltTemp.pack(side="top")
        self.peltLog = tk.Checkbutton(master=frame2,
                                   text="Log temp?",
                                   variable=self.logTemp,
                                   onvalue=1, offvalue=0)
        self.peltLog.pack(side="top")
        #self.peltGetTempArd()


    def peltOn(self):
        print("peltier on")
        output = str(self.onAdd)
        #self.sendFlag = 1
        self.peltierallcalls.append(output)
        return

    def peltOff(self):
        print("peltier off")
        output = str(self.offAdd)
        self.peltierallcalls.append(output)
        return

    def peltGetTempArd(self):

        output = self.tempAdd+"<99>>"

        return output
    def peltSetTemp(self):
        output = self.tempAdd +"<"+str(self.peltTemp.get())+ ">>"
        return output
