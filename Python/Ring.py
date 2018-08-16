    ######################################## LED RING
import tkinter as tk
import numpy as np

class Ring:
    


    def __init__(self, parent="none", label="none", #ser="", #protFrame="",
                 #ringallcalls = list(),
                 ringOnAdd="", ringOffAdd="", ringZapAdd="",
                 greenAdd="RGR", redAdd="RRE", blueAdd="RBL",
                 allAdd="", rotAdd=""):

        #self.ser = ser
        self.ringOnAdd = ringOnAdd
        self.ringOffAdd = ringOffAdd
        self.ringZapAdd = ringZapAdd
        self.greenAdd = greenAdd
        self.redAdd = redAdd
        self.blueAdd = blueAdd
        
        self.ringallcalls = list()#ringallcalls
       
        ###########variables for ring sliders
        ringGreenVar = tk.IntVar()
        #self.rgv=ringGreenVar
        
        ringRedVar = tk.IntVar()
        #self.rrv=ringRedVar
        
        ringBlueVar = tk.IntVar()
        #self.rbv=ringBlueVar
        
        ###########variables for ring zap
        #zapGreenVar = tk.IntVar()
        #zapRedVar = tk.IntVar()
        #zapBlueVar = tk.IntVar()
        
       
        frame1 = tk.Frame(master=parent)
        frame1.grid(row=0, column=0)
        frame2 = tk.Frame(master=parent)
        frame2.grid(row=0, column=2)
        frame3 = tk.Frame(master=parent)
        frame3.grid(row=0, column=1)

        self.ringLabel = tk.Label(master=frame1, text=label)
        self.ringLabel.pack()
 

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


        frame_green = tk.Frame(master=frame2)
        Label = tk.Label(master=frame_green, text="green", fg="black")
        Label.pack(fill="x", side="right")
        self.ringGreen = tk.Scale(master=frame_green, #repeatdelay=delay,
                          from_=255, to=0, resolution=1,
                          #command=self.greenUpdate,
                          variable=ringGreenVar,#self.rgv,
                           orient="vertical")
        self.ringGreen.set(10)
        self.ringGreen.pack()
        frame_green.grid(row=0, column=0)



        frame_red = tk.Frame(master=frame2)
        Label = tk.Label(master=frame_red, text="red", fg="black")
        Label.pack(fill="x", side="right")
        self.ringRed = tk.Scale(master=frame_red, #repeatdelay=delay,
                          from_=255, to=0, resolution=1,
                          #command=self.redUpdate,
                          variable=ringRedVar, orient="vertical")

        self.ringRed.set(10)
        self.ringRed.pack()
        frame_red.grid(row=0, column=1)


        frame_blue = tk.Frame(master=frame2)
        Label = tk.Label(master=frame_blue, text="blue", fg="black")
        Label.pack(fill="x", side="right")
        self.ringBlue = tk.Scale(master=frame_blue, #repeatdelay=delay,
                          from_=255, to=0, resolution=1,
                          #command=self.blueUpdate,
                          variable=ringBlueVar, orient="vertical")

        self.ringBlue.set(10)
        self.ringBlue.pack()
        frame_blue.grid(row=0, column=2)





    def ringButton(self, parent="none", side="top", fill="x",
                   buttText="button", color="black", func="none"):

        button = tk.Button(parent, text=buttText, fg=color, command=func)
        button.pack(side=side, fill=fill)
        return
    #def ringSlider(self, parent="none", text_="empty", side="right",
    #               func="", var="",  fill_="x",color="black",
    #               rowIndx=1, colIndx=0, orient_="vertical",delay=100,
    #               colSpan=1, from__=100, to__=0, res=1, set_=45):#

    #    frame_loc = tk.Frame(master=parent)
    #    Label = tk.Label(master=frame_loc, text=text_, fg=color)
    #    Label.pack(fill=fill_, side=side)
    #    Slider = tk.Scale(master=frame_loc, repeatdelay=delay,
    #                      from_=from__, to=to__, resolution=res,
    #                      command=func, variable=var, orient=orient_)
    #    Slider.set(set_)
    #    Slider.pack()
    #    frame_loc.grid(row=rowIndx, column=colIndx)
    #    return

    def ringOn(self):
        output = str(self.ringOnAdd)
        self.ringallcalls.append(output)
        return
        
    def ringOff(self):
        output = str(self.ringOffAdd)
        self.ringallcalls.append(output)
        return
    def ringZap(self):
        zapAdd = self.ringZapAdd
        green = self.ringGZap.get()
        
        if int(green) > 255:
            green = str(255)
        
        if int(green) < 0:
            green = str(0)
        green = int(green)
        output = zapAdd+"G<"+str(green)+">>"
        
        self.ringallcalls.append(output)
        
        red = self.ringRZap.get()
        if int(red) > 255:
            red = str(255)
        if int(red) < 0:
            red = str(0)
        red = int(red)
        output = zapAdd+"R<"+str(red)+">>"
        self.ringallcalls.append(output)
        
        blue = self.ringBZap.get()
        if int(blue) > 255:
            blue = str(255)
        if int(blue) < 0:
            blue = str(0)
        blue = int(blue)
        output = zapAdd+"B<"+str(blue)+">>"
        self.ringallcalls.append(output)
        
        time = self.ringZapTime.get()
        if time == "zap in ms":
            time = 500
        time = str(time)
        
        output = zapAdd+"T<"+time+">>"
        print(output)

        self.ringallcalls.append(output)
        return
        
    def update(self):
        dummie1=list()
        value = self.ringGreen.get()

                  
        dummie1.append(str(self.greenAdd) + "<" + str(value) + ">>")
        
        value = self.ringRed.get()           
        dummie1.append(str(self.redAdd) + "<" + str(value) + ">>")
        value = self.ringBlue.get()           
        dummie1.append(str(self.blueAdd) + "<" + str(value) + ">>")
        
        return dummie1
