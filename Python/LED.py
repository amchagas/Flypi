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
        address=str(self.zapDurAddress)
        time = self.ledZapTime.get()
        if time == "zap in ms":
            time = str(500)
            print("you didn't set a value!")
        time = address+"<"+time+">>"

        output = str(self.onAdress)+"*"
        self.ser.write(output.encode("utf-8"))

        self.ser.write(time.encode("utf-8"))
        
        output = str(self.offAdress)+"*"
        self.ser.write(output.encode("utf-8"))

        print(self.label + " ZAP for " + time[0:])
