    ######################################## LED
import tkinter as tk


class LED:

    def __init__(self, parent="none", label="LED",
                 onAdd="", offAdd="",
                 zapDurAdd="", prot=False, protFrame="",
                 ser="",lockwait=""):

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
    def ledOn(self):
        output = str(self.onAdress)
        self.ser.write(output.encode("utf-8"))
        self.lockwait()
        #print(self.label + " ON")

    def ledOff(self):
        output = str(self.offAdress)
        self.ser.write(output.encode("utf-8"))
        self.lockwait()
        #print(self.label + " OFF")

    def ledZap(self):
        address=str(self.zapDurAddress)
        time = self.ledZapTime.get()
        if time == "zap in ms":
            time = str(500)
            #print("you didn't set a value!")
        time = address+"<"+time+">>"

        output = str(self.onAdress)
        self.ser.write(output.encode("utf-8"))
        self.lockwait()
        self.ser.write(time.encode("utf-8"))
        self.lockwait()
        output = str(self.offAdress)
        self.ser.write(output.encode("utf-8"))
        self.lockwait()
        #print(self.label + " ZAP for " + time[0:])
