    ######################################## LED RING
import tkinter as tk
import numpy as np

class Ring:
    


    def __init__(self, parent="none", label="none", ser="", #protFrame="",
                 ringOnAdd="", ringOffAdd="", ringZapAdd="",
                 greenAdd="RGR", redAdd="RRE", blueAdd="RBL",
                 allAdd="", rotAdd=""):

        self.ser = ser
        self.ringOnAdd = ringOnAdd
        self.ringOffAdd = ringOffAdd
        self.ringZapAdd = ringZapAdd
        self.greenAdd = greenAdd
        self.redAdd = redAdd
        self.blueAdd = blueAdd
        self.allAdd = allAdd
        self.rotAdd = rotAdd
        
        ###########variables for ring sliders
        ringGreenVar = tk.IntVar()
        self.rgv=ringGreenVar
        
        ringRedVar = tk.IntVar()
        self.rrv=ringRedVar
        
        ringBlueVar = tk.IntVar()
        self.rbv=ringBlueVar
        
        ringAllVar = tk.IntVar()
        self.rav=ringAllVar
        
        ringRotVar = tk.IntVar()
        self.rrotv=ringRotVar
        
        ###########variables for ring zap
        zapGreenVar = tk.IntVar()
        zapRedVar = tk.IntVar()
        zapBlueVar = tk.IntVar()
        
        def lockwait(waitString="waited"):
            flag = True
            endFlag="END<>"
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
        ############callbacks for ring sliders
        def greenUpdate(self, ser=self.ser, address1=self.greenAdd,rgv=self.rgv):
#            print ("here11")
            value = rgv.get()           
            output = str(greenAdd) + "<" + str(value) + ">>"
            ser.write(output.encode("utf-8"))
            lockwait()
#            output = str(redAdd) + "<" + str(ringRedVar.get()) + ">"
#            ser.write(output.encode("utf-8"))
#            output = str(blueAdd) + "<" + str(ringBlueVar.get()) + ">"
#            ser.write(output.encode("utf-8")) 

            
        
        self.greenUpdate=greenUpdate        
        
        def redUpdate(self, ser=self.ser, address1=self.redAdd,redvar=self.rrv):
            value = redvar.get()            
            output = str(address1) + "<" + str(value) + ">>"         
            ser.write(output.encode("utf-8"))
            lockwait()
            
        self.redUpdate=redUpdate

        def blueUpdate(self, ser=self.ser, address1=self.blueAdd,bluevar=self.rbv):
            value = bluevar.get()
            output = str(address1) + "<" + str(value) + ">>"
            
            ser.write(output.encode("utf-8"))
            lockwait()
            
        self.blueUpdate=blueUpdate

        def allUpdate(self, ser=self.ser, address1=self.allAdd,
                      rav=self.rav,rrv= self.rrv,rgv=self.rgv,rbv=self.rbv):
            value = rav.get()
            rbv.set(value)
            rgv.set(value)
            rrv.set(value)
            output = address1 + "<" + str(value) + ">>"
            ser.write(output.encode("utf-8"))
            lockwait()
            
        def rotUpdate(self, ser=self.ser, address1=self.rotAdd, rrotv=self.rrotv):
            output = str(address1) +"<"+ str(rrotv.get())+">>"
            ser.write(output.encode("utf-8"))
            
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
                          command=self.greenUpdate,
                          variable=self.rgv, orient="vertical")
        self.ringGreen.set(10)
        self.ringGreen.pack()
        frame_green.grid(row=0, column=0)


        #self.ringGreen = self.ringSlider(parent=frame2, text_="Green",
        #                                func=self.greenUpdate,
        #                                fill_="x", 
        #                                orient_="vertical",
        #                                var=self.rgv,
        #                                rowIndx=0, colIndx=0,
        #                                from__=255, to__=0, res=1, set_=10)

        frame_red = tk.Frame(master=frame2)
        Label = tk.Label(master=frame_red, text="red", fg="black")
        Label.pack(fill="x", side="right")
        self.ringRed = tk.Scale(master=frame_red, #repeatdelay=delay,
                          from_=255, to=0, resolution=1,
                          command=self.redUpdate,
                          variable=self.rrv, orient="vertical")

        self.ringRed.set(10)
        self.ringRed.pack()
        frame_red.grid(row=0, column=1)

        #self.ringRed = self.ringSlider(parent=frame2, text_="Red",
        #                               func=redUpdate,
        #                               fill_="x", 
        #                               var=self.rrv, orient_="vertical",
        #                               rowIndx=0, colIndx=1,
        #                               from__=255, to__=0, res=1, set_=10)

        frame_blue = tk.Frame(master=frame2)
        Label = tk.Label(master=frame_blue, text="blue", fg="black")
        Label.pack(fill="x", side="right")
        self.ringBlue = tk.Scale(master=frame_blue, #repeatdelay=delay,
                          from_=255, to=0, resolution=1,
                          command=self.blueUpdate,
                          variable=self.rbv, orient="vertical")

        self.ringBlue.set(10)
        self.ringBlue.pack()
        frame_blue.grid(row=0, column=2)

        #self.ringBlue = self.ringSlider(parent=frame2, text_="Blue",
        #                               func=blueUpdate, orient_="vertical",
        #                               var=self.rbv,
        #                               fill_="x", 
        #                               rowIndx=0, colIndx=2,
        #                               from__=255, to__=0, res=1, set_=10)

        frame_all = tk.Frame(master=frame2)
        Label = tk.Label(master=frame_all, text="all", fg="black")
        Label.pack(fill="x", side="right")
        self.ringAll = tk.Scale(master=frame_all, #repeatdelay=delay,
                          from_=255, to=0, resolution=1,
                          command=allUpdate,
                          variable=self.rav, orient="vertical")

        self.ringAll.set(10)
        self.ringAll.pack()
        frame_all.grid(row=0, column=3)


        #self.ringAll = self.ringSlider(parent=frame2, text_="All",
        #                               func=allUpdate,
        #                               fill_="x", 
        #                               var=self.rav, orient_="vertical",
        #                               colSpan=1,delay=300,
        #                               rowIndx=0, colIndx=3,
        #                               from__=255, to__=0, res=1, set_=10)

#        self.ringRot = self.ringSlider(parent=frame2, text_="Rotate", 
#                                       func=rotUpdate,var=self.rrotv,fill_="x", 
#                                       rowIndx=0,  colIndx=4,orient_="vertical",
#                                       colSpan=1, delay=300,color="black",
#                                       from__=100, to__=-100, res=10, set_=0)

    def ringButton(self, parent="none", side="top", fill="x",
                   buttText="button", color="black", func="none"):

        button = tk.Button(parent, text=buttText, fg=color, command=func)
        button.pack(side=side, fill=fill)

    def ringSlider(self, parent="none", text_="empty", side="right",
                   func="", var="",  fill_="x",color="black",
                   rowIndx=1, colIndx=0, orient_="vertical",delay=100,
                   colSpan=1, from__=100, to__=0, res=1, set_=45):

        frame_loc = tk.Frame(master=parent)
        Label = tk.Label(master=frame_loc, text=text_, fg=color)
        Label.pack(fill=fill_, side=side)
        Slider = tk.Scale(master=frame_loc, repeatdelay=delay,
                          from_=from__, to=to__, resolution=res,
                          command=func, variable=var, orient=orient_)
        Slider.set(set_)
        Slider.pack()
        frame_loc.grid(row=rowIndx, column=colIndx)


    def ringOn(self):
        output = str(self.ringOnAdd)
        print("ring on " + output)
        self.ser.write(output.encode("utf-8"))
#        lockwait()

    def ringOff(self):
        output = str(self.ringOffAdd)
        print("ringOff" + output)
        self.ser.write(output.encode("utf-8"))

        
    def ringZap(self):
        
        zapAdd = self.ringZapAdd

        green = self.ringGZap.get()
        if int(green) > 255:
            green = str(255)
        if int(green) < 0:
            green = str(0)
        green = int(green)
        output = zapAdd+"G<"+str(green)+">>"
        self.ser.write(output.encode("utf-8"))

        
        red = self.ringRZap.get()
        if int(red) > 255:
            red = str(255)
        if int(red) < 0:
            red = str(0)
        red = int(red)
        output = zapAdd+"R<"+str(red)+">>"
        self.ser.write(output.encode("utf-8"))

        
        blue = self.ringBZap.get()
        if int(blue) > 255:
            blue = str(255)
        if int(blue) < 0:
            blue = str(0)
        blue = int(blue)
        output = zapAdd+"B<"+str(blue)+">>"
        self.ser.write(output.encode("utf-8"))

        time = self.ringZapTime.get()
        if time == "zap in ms":
            time = 500
        time = str(time)
        
        output = zapAdd+"T<"+time+">>"
        print(output)
        self.ser.write(output.encode("utf-8"))


