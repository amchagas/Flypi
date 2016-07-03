    ######################################## LED
import tkinter as tk


class LED:

    def __init__(self, parent="none", label="LED",
                 onAdd="", offAdd="",
                 zapDurAdd="", prot=False, protFrame="",
                 ser=""):

        self.label = label
        self.onAdress = onAdd
        self.offAdress = offAdd
        self.zapDurAddress = zapDurAdd
        self.ledLabel = tk.Label(master=parent, text=self.label)
        self.ledLabel.pack()
        self.ser = ser

        self.ledOnButt = tk.Button(master=parent,
                                   text="ON", fg="green",
                                   command=self.ledOn)

        self.ledOnButt.pack(fill="x")

        self.ledOffButt = tk.Button(master=parent,
                                    text="OFF",
                                    fg="RED",
                                    command=self.ledOff)

        self.ledOffButt.pack(fill="x")

        self.ledZapTime = tk.Entry(master=parent, width=10)

        self.ledZapTime.insert(0, "zap in ms")

        self.ledZapTime.pack(fill="x")

        self.ledZapButt = tk.Button(master=parent,
                                    text="ZAP!",
                                    command=self.ledZap)

        self.ledZapButt.pack(fill="x")

#        if prot == True:
#
#            tempFrame = tk.Frame(master=protFrame)
#            tempFrame.pack()
#            #ledLabel = tk.Label(master=protFrame, text=self.label)
#            #ledLabel.grid(row=0, column=0)

#            led1V1 = tk.StringVar(master=tempFrame)
#            led1V2 = tk.StringVar(master=tempFrame)
#            led1V3 = tk.StringVar(master=tempFrame)
#            led1V4 = tk.StringVar(master=tempFrame)
#            led1V5 = tk.StringVar(master=tempFrame)

##            led1V1.set(self.offAdress)
##            led1V2.set(self.offAdress)
##            led1V3.set(self.offAdress)
##            led1V4.set(self.offAdress)
##            led1V5.set(self.offAdress)

#            def led1ProtCB():
#                dummie = list()
#                dummie.append(led1V1.get())
#                dummie.append(led1V2.get())
#                dummie.append(led1V3.get())
#                dummie.append(led1V4.get())
#                dummie.append(led1V5.get())
#                return dummie

#           protLed1Label = tk.Label(master=tempFrame, text=self.label)
#            protLed1Label.grid(row=1, column=0)

#            buttonsFrame = tk.Frame(master=tempFrame, bd=3)
#            buttonsFrame.grid(row=1, column=1)

#            vars = [led1V1, led1V2, led1V3, led1V4, led1V5]
#            for k in range(0, 5):
#                protButt1 = tk.OptionMenu(buttonsFrame, vars[k], "ON", "OFF")
#                vars[k].set("OFF")
#                protButt1.grid(row=1, column=k, sticky="NW")

    #callbacks for LED

    def ledOn(self):
        output = str(self.onAdress)
        self.ser.write(output.encode("utf-8"))
        print(self.label + " ON")

    def ledOff(self):
        output = str(self.offAdress)
        self.ser.write(output.encode("utf-8"))
        print(self.label + " OFF")

    def ledZap(self):
        address=str(self.zapDurAddress)+"*"
        time = self.ledZapTime.get()
        if time == "zap in ms":
            time = str(500)
            print("you didn't set a value!")
        time = time+"*"
        self.ser.write(address.encode("utf-8"))
        self.ser.write(time.encode("utf-8"))
        print(self.label + " ZAP for " + time[0:])
