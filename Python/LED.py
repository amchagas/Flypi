    ######################################## LED
import tkinter as tk


class LED:

    def __init__(self, parent="none", label="LED",
                 onAdd="", offAdd="",
                 zapDurAdd="", prot=False, protFrame="",
                 #ser="",lockwait=""
                 ):

        self.label = label
        self.onAdress = onAdd
        self.offAdress = offAdd
        self.zapDurAddress = zapDurAdd
        self.ledLabel = tk.Label(master=parent, text=self.label)
        self.ledLabel.pack()
        #self.ser = ser

        self.ledallcalls = list()#ringallcalls


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

    def ledOn(self):
        output = str(self.onAdress)
        self.ledallcalls.append(output)
        #self.ser.write(output.encode("utf-8"))
        #self.lockwait()
        #print(self.label + " ON")

    def ledOff(self):
        output = str(self.offAdress)
        self.ledallcalls.append(output)
        #self.ser.write(output.encode("utf-8"))
        #self.lockwait()
        #print(self.label + " OFF")

    def ledZap(self):
        address=str(self.zapDurAddress)
        self.ledallcalls.append(address)
        time = self.ledZapTime.get()
        if time == "zap in ms":
            time = str(500)
            #print("you didn't set a value!")
        output = address+"<"+time+">>"
        self.ledallcalls.append(output)
