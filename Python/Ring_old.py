    ######################################## LED RING
import tkinter as tk


class Ring2:

    def __init__(self, parent="none", label="none", ser="", protFrame="",
                 ringOnAdd="", ringOffAdd="", ringZapAdd="",
                 greenAdd="", redAdd="", blueAdd="",
                 allAdd="", rotAdd=""):

        #self.label=label
        #self.protFrame=protFrame
        self.ser = ser
        self.ringOnAdd = ringOnAdd
        self.ringOffAdd = ringOffAdd
        self.ringZapAdd = ringZapAdd
        self.greenAdd = greenAdd
        self.redAdd = redAdd
        self.blueAdd = blueAdd
        self.allAdd = allAdd
        self.rotAdd = rotAdd

#        ###########variables for ring sliders
        ringGreenVar = tk.IntVar()
        ringRedVar = tk.IntVar()
        ringBlueVar = tk.IntVar()
        ringAllVar = tk.IntVar()
        ringRotVar = tk.IntVar()

        ###########variables for ring z
        zapGreenVar = tk.IntVar()
        zapRedVar = tk.IntVar()
        zapBlueVar = tk.IntVar()

#    ############callbacks for ring sliders
        def greenUpdate(self, ser=self.ser, address1=self.greenAdd):
            address = int(address1)
            output = address + ringGreenVar.get()
            output = str(output) + "*"
            #print("green hue: "+ output[2:-1])
            ser.write(output.encode("utf-8"))

        def redUpdate(self, ser=self.ser, address1=self.redAdd):
            address = int(address1)
            output = address + ringRedVar.get()
            output = str(output) + "*"
            #print("red hue: " +output[2:-1])
            ser.write(output.encode("utf-8"))

        def blueUpdate(self, ser=self.ser, address1=self.blueAdd):
            address = int(address1)
            output = address + ringBlueVar.get()
            output = str(output) + "*"
            #print("blue hue: " +output[2:-1])
            ser.write(output.encode("utf-8"))

        def allUpdate(self, ser=self.ser, address1=self.allAdd):
            address = int(address1)
            output = ringAllVar.get()
            ringBlueVar.set(output)
            ringGreenVar.set(output)
            ringRedVar.set(output)
            output = address + ringAllVar.get()
            output = str(output) + "*"
            #print("ring all: "+ output[2:-1])
            ser.write(output.encode("utf-8"))

        def rotUpdate(self, ser=self.ser, address=self.rotAdd):
            address = int(address)
            output = address + ringRotVar.get()
            output = str(output) + "*"
            #print("rotation: " + output[2:-1])
            ser.write(output.encode("utf-8"))

        frame1 = tk.Frame(master=parent)
        frame1.grid(row=0, column=0)
        frame2 = tk.Frame(master=parent)
        frame2.grid(row=0, column=2)
        frame3 = tk.Frame(master=parent)
        frame3.grid(row=0, column=1)

        self.ringLabel = tk.Label(master=frame1, text=label)
        self.ringLabel.pack()
        #self.ringLabel.grid(row = 0, column = 0,sticky="W")

        self.ringOnButt = self.ringButton(parent=frame1,
                                          fill="x",
                                          buttText="ON",
                                          color="green", func=self.ringOn)

        self.ringOnffButt = self.ringButton(parent=frame1,
                                            fill="x",
                                            buttText="OFF",
                                            color="red", func=self.ringOff)

        self.ringZapTime = tk.Entry(frame1, width=10)
        self.ringZapTime.insert(0, "zap in ms")
        self.ringZapTime.pack(fill="x")

        self.GLabel = tk.Label(master=frame3, text="Green flash")
        self.GLabel.pack()
        self.ringGZap = tk.Entry(frame3, width=10)
        self.ringGZap.insert(0, "0")
        self.ringGZap.pack()

        self.RLabel = tk.Label(master=frame3, text="Red flash")
        self.RLabel.pack()
        self.ringRZap = tk.Entry(frame3, width=10)
        self.ringRZap.insert(0, "0")
        self.ringRZap.pack()

        self.BLabel = tk.Label(master=frame3, text="Blue flash")
        self.BLabel.pack()
        self.ringBZap = tk.Entry(frame3, width=10)
        self.ringBZap.insert(0, "0")
        self.ringBZap.pack()

        self.ringZapButt = self.ringButton(parent=frame1,
                                           fill="x",
                                           buttText="ZAP",
                                           color="black", func=self.ringZap)

        self.ringGreen = self.ringSlider(parent=frame2, text_="Green",
                                        func=greenUpdate,
                                        fill_="x", side="top",
                                        orient_="vertical",
                                        var=ringGreenVar,
                                        rowIndx=0, colIndx=0, sticky="WE",
                                        from__=255, to__=0, res=1, set_=10)

        self.ringRed = self.ringSlider(parent=frame2, text_="Red",
                                       func=redUpdate,
                                       fill_="x", side="top",
                                       var=ringRedVar, orient_="vertical",
                                       rowIndx=0, colIndx=1, sticky="WE",
                                       from__=255, to__=0, res=1, set_=10)

        self.ringBlue = self.ringSlider(parent=frame2, text_="Blue",
                                       func=blueUpdate, orient_="vertical",
                                       var=ringBlueVar,
                                       fill_="x", side="top",
                                       rowIndx=0, colIndx=2, sticky="WE",
                                       from__=255, to__=0, res=1, set_=10)

        self.ringAll = self.ringSlider(parent=frame2, text_="All",
                                       func=allUpdate,
                                       fill_="x", side="top",
                                       var=ringAllVar, orient_="vertical",
                                       colSpan=1,
                                       rowIndx=0, colIndx=3, sticky="WE",
                                       from__=255, to__=0, res=1, set_=10)

        self.ringRot = self.ringSlider(parent=frame2, text_="Rotate",
                                       func=rotUpdate, colSpan=2, delay=1000,
                                       var=ringRotVar, orient_="vertical",
                                       rowIndx=0, colIndx=4,
                                       fill_="x", side="top",
                                       from__=100, to__=-100, res=5, set_=0)

    def ringButton(self, parent="none", side="top", fill="x",
                   buttText="button", color="black", func="none"):

        button = tk.Button(parent, text=buttText, fg=color, command=func)
        button.pack(side=side, fill=fill)

    def ringSlider(self, parent="none", text_="empty", side="right",
                   func="", var="", color="black", fill_="x",
                   rowIndx=1, colIndx=0, sticky="", orient_="vertical",
                   colSpan=1, delay=300,
                   from__=100, to__=0, res=1, set_=0):

        frame_loc = tk.Frame(master=parent)
        Label = tk.Label(master=frame_loc, text=text_, fg=color)
        Label.pack(fill=fill_, side=side)
        #Label.grid(row=rowLabel,column=colIndx,columnspan=colSpan)
        Slider = tk.Scale(master=frame_loc, repeatdelay=delay,
                          from_=from__, to=to__, resolution=res,
                          command=func, variable=var, orient=orient_)
        Slider.set(set_)
        Slider.pack()
        frame_loc.grid(row=rowIndx, column=colIndx)
        #Slider.grid(row=rowIndx,column=colIndx,columnspan=colSpan)

    def ringOn(self):
        output = str(self.ringOnAdd) + "*"
        print("ring on " + output)
        self.ser.write(output.encode("utf-8"))

    def ringOff(self):
        output = str(self.ringOffAdd) + "*"
        print("ringOff" + output)
        self.ser.write(output.encode("utf-8"))

    def ringZap(self):
        #print ("works")
        green = self.ringGZap.get()
        if int(green) > 255:
            green = str(255)
        if int(green) < 0:
            green = str(0)
        green = int(green)

        red = self.ringRZap.get()
        if int(red) > 255:
            red = str(255)
        if int(red) < 0:
            red = str(0)
        red = int(red)

        blue = self.ringBZap.get()
        if int(blue) > 255:
            blue = str(255)
        if int(blue) < 0:
            blue = str(0)
        blue = int(blue)

#        prevGreen = self.ringGreenVar.get()
#        prevGreen = str(int(self.greenAdd) + int(prevGreen)) + "*"
#        prevRed = ringRedVar.get()
#        prevRed = str(int(self.redAdd) + int(prevRed)) + "*"
#        prevBlue = ringBlueVar.get()
#        prevBlue = str(int(self.blueAdd) + int(prevBlue)) + "*"
#
        time = self.ringZapTime.get()
        if time == "zap in ms":
            time = 500
        time = str(time) + "*"

        greenAdd = str(int(self.greenAdd) + green) + "*"
        self.ser.write(greenAdd.encode("utf-8"))
        #self.ser.write(green.encode("utf-8"))

        redAdd = str(int(self.redAdd) + red) + "*"
        self.ser.write(redAdd.encode("utf-8"))
        #self.ser.write(red.encode("utf-8"))

        blueAdd = str(int(self.blueAdd) + blue) + "*"
        self.ser.write(blueAdd.encode("utf-8"))
        #self.ser.write(blue.encode("utf-8"))

        zapAdd = self.ringZapAdd + "*"
        self.ser.write(zapAdd.encode("utf-8"))
        self.ser.write(time.encode("utf-8"))
#        greenUpdate(self, ser=self.ser, address1=self.greenAdd)
        #greenUpdate
        print("ringZAP for " + time)
