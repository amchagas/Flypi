    ######################################## LED RING
import tkinter as tk


class Ring:

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
        frame2.grid(row=0, column=1)

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

        self.ringZapButt = self.ringButton(parent=frame1,
                                           fill="x",
                                           buttText="ZAP",
                                           color="black", func=self.ringZap)

        self.ringGreen = self.ringSlider(parent=frame2, text_="Green",
                                        func=greenUpdate,
                                        fill_="x",
                                        var=ringGreenVar,
                                        rowIndx=0, colIndx=1, sticky="WE",
                                        from__=255, to__=0, res=1, set_=10)

        self.ringRed = self.ringSlider(parent=frame2, text_="Red",
                                       func=redUpdate, fill_="x",
                                       var=ringRedVar,
                                       rowIndx=0, colIndx=2, sticky="WE",
                                       from__=255, to__=0, res=1, set_=10)

        self.ringBlue = self.ringSlider(parent=frame2, text_="Blue",
                                        func=blueUpdate,
                                        var=ringBlueVar, fill_="x",
                                        rowIndx=0, colIndx=3, sticky="WE",
                                        from__=255, to__=0, res=1, set_=10)

        self.ringAll = self.ringSlider(parent=frame2, text_="All",
                                          func=allUpdate, fill_="x",
                                          var=ringAllVar, colSpan=1,
                                          rowIndx=0, colIndx=4, sticky="WE",
                                          from__=255, to__=0, res=1, set_=10)

        self.ringRot = self.ringSlider(parent=frame2, text_="Rotate",
                                       func=rotUpdate, colSpan=2, delay=1000,
                                       var=ringRotVar, orient_="vertical",
                                       rowIndx=0, colIndx=5, fill_="x",
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
        Label.pack(fill=fill_)
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
        time = int(self.ringZapTime.get())
        time = str(int(self.ringZapAdd) + time) + "*"
        self.ser.write(time.encode("utf-8"))
        print("ringZAP for " + time)
