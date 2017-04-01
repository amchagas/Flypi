    ######################################## LED
import tkinter as tk


class Mock_up:

    def __init__(self, parent="none", label="mock_up",
                 prot=False, protFrame="",
                 ser=""):

        #bare minimum 
        self.label = label
       
        self.mockLabel = tk.Label(master=parent, text=self.label)
        self.mockLabel.pack()
        #include ability to interact with serial port
        self.ser = ser

        #create buttons or other tools for GUI
        self.OnButt = tk.Button(master=parent,
                                   text="ON", fg="green",
                                   command=self.on)

        self.onButt.pack(fill="x")

        self.offButt = tk.Button(master=parent,
                                    text="OFF",
                                    fg="RED",
                                    command=self.off)

        self.offButt.pack(fill="x")

        


    #callbacks for buttons

    def on(self):
        output = "on button pressed"
        print(output)
        return 
    
    def off(self):
        output = "off button pressed"
        print(output)
        return 

   
