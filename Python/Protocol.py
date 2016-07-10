##################protocols

import tkinter as tk
import os


class Protocol:

    def __init__(self, parent="none",ser="",
                 usedClasses = dict(),
                 led1C="",
                 label="Protocol", basePath="~/Desktop/"):

       # self, parent="none", label="none", ser="", #protFrame="",
       #          ringOnAdd="", ringOffAdd="", ringZapAdd="",
       #          greenAdd="", redAdd="", blueAdd="",
       #          allAdd="", rotAdd="")

        frame1 = tk.Frame(master=parent)
        frame1.grid(row=0, column=0)

        #create dictionary to store all variables
        self.allVariables = dict()
        #buttonsFrame = tk.Frame(master=frame1, bd=3)
        #buttonsFrame.grid(row=1, column=1)



        rows=0
        protLabel = tk.Label(master=frame1, text=label)
        protLabel.grid(row=rows, column=0)
        rows=rows+1

        if usedClasses["camera"] != 0:
            camLabel = tk.Label(master=frame1, text="Camera")
            camLabel.grid(row=rows, column=0)

            camV1 = tk.StringVar(master=frame1)
            camV2 = tk.StringVar(master=frame1)
            camV3 = tk.StringVar(master=frame1)
            camV4 = tk.StringVar(master=frame1)
            camV5 = tk.StringVar(master=frame1)
            
            vars = [camV1, camV2, camV3, camV4, camV5]
            self.allVariables["camera"] = vars
            
            for k in range(len(vars)):
                protButt10 = tk.OptionMenu(frame1, vars[k], "ON", "OFF")
                vars[k].set("OFF")
                self.allVariables[eval(vars[k])] = vars[k]
                protButt10.grid(row=rows, column=k+1, sticky="NW")
            rows = rows+1

        ######### LED1 #################
        
        if usedClasses["led1"] != 0:
            ledLabel = tk.Label(master=frame1, text="LED1")
            ledLabel.grid(row=rows, column=0)
           
            
            led1V1 = tk.StringVar(master=frame1)
            led1V2 = tk.StringVar(master=frame1)
            led1V3 = tk.StringVar(master=frame1)
            led1V4 = tk.StringVar(master=frame1)
            led1V5 = tk.StringVar(master=frame1)

            
            vars = [led1V1, led1V2, led1V3, led1V4, led1V5]
            self.allVariables["led1"] = vars
            for k in range(len(vars)):
                protButt1 = tk.OptionMenu(frame1, vars[k], "ON", "OFF")
                vars[k].set("OFF")
                protButt1.grid(row=rows, column=k+1, sticky="NW")
            rows = rows+1

        ############ LED2 ###################

        if usedClasses["led2"] != 0:
            ledLabel = tk.Label(master=frame1, text="LED2")
            ledLabel.grid(row=rows, column=0)

            
            led2V1 = tk.StringVar(master=frame1)
            led2V2 = tk.StringVar(master=frame1)
            led2V3 = tk.StringVar(master=frame1)
            led2V4 = tk.StringVar(master=frame1)
            led2V5 = tk.StringVar(master=frame1)


            vars = [led2V1, led2V2, led2V3, led2V4, led2V5]
            for k in range(len(vars)):
                protButt2 = tk.OptionMenu(frame1, vars[k], "ON", "OFF")
                vars[k].set("OFF")
                protButt2.grid(row=rows, column=k+1, sticky="NW")
            rows = rows+1



        ##### Matrix ###########

                
        if usedClasses["matrix"] != 0:
 
            matLabel = tk.Label(master=frame1, text="Matrix")
            matLabel.grid(row=rows, column=0)
            

            matV1 = tk.StringVar(master=frame1)
            matV2 = tk.StringVar(master=frame1)
            matV3 = tk.StringVar(master=frame1)
            matV4 = tk.StringVar(master=frame1)
            matV5 = tk.StringVar(master=frame1)
            

#            def matProtCB():
#                dummie = list()
#                dummie.append(matV1.get())
#                dummie.append(matV2.get())
#                dummie.append(matV3.get())
#                dummie.append(matV4.get())
#                dummie.append(matV5.get())
#                return dummie      

            vars = [matV1, matV2, matV3, matV4, matV5]
            for k in range(len(vars)):
                protButt3 = tk.OptionMenu(frame1,
                                          vars[k],
                                          "OFF",
                                          "Patt1",
                                          "Patt2",
                                          "Patt3")
                vars[k].set("OFF")
                protButt3.grid(row=rows, column=k+1, sticky="NW")

            rows = rows+1
                ##### Matrix ###########

                
        if usedClasses["ring"] != 0:
 
            ringLabel = tk.Label(master=frame1, text="Ring")
            ringLabel.grid(row=rows, column=0)

            ringLabel = tk.Label(master=frame1, text="Red")
            ringLabel.grid(row=rows+1, column=0)

            ringLabel = tk.Label(master=frame1, text="Green")
            ringLabel.grid(row=rows+2, column=0)

            ringLabel = tk.Label(master=frame1, text="Blue")
            ringLabel.grid(row=rows+3, column=0)

            ringV1 = tk.StringVar(master=frame1)
            ringV2 = tk.StringVar(master=frame1)
            ringV3 = tk.StringVar(master=frame1)
            ringV4 = tk.StringVar(master=frame1)
            ringV5 = tk.StringVar(master=frame1)

            ringR1 = tk.StringVar(master=frame1)
            ringR2 = tk.StringVar(master=frame1)
            ringR3 = tk.StringVar(master=frame1)
            ringR4 = tk.StringVar(master=frame1)
            ringR5 = tk.StringVar(master=frame1)

            ringG1 = tk.StringVar(master=frame1)
            ringG2 = tk.StringVar(master=frame1)
            ringG3 = tk.StringVar(master=frame1)
            ringG4 = tk.StringVar(master=frame1)
            ringG5 = tk.StringVar(master=frame1)

            ringB1 = tk.StringVar(master=frame1)
            ringB2 = tk.StringVar(master=frame1)
            ringB3 = tk.StringVar(master=frame1)
            ringB4 = tk.StringVar(master=frame1)
            ringB5 = tk.StringVar(master=frame1)

            
            vars = [ringV1,ringR1,ringG1,ringB1,
                    ringV2,ringR2,ringG2,ringB2,
                    ringV3,ringR3,ringG3,ringB3,
                    ringV4,ringR4,ringG4,ringB4,
                    ringV5,ringR5,ringG5,ringB5]
            x=1
            for k in range(0,len(vars),4):
                protButt3 = tk.OptionMenu(frame1,
                                          vars[k],
                                          "OFF",
                                          "ON")
                vars[k].set("OFF")
                protButt3.grid(row=rows, column=x, sticky="NW")
                protEntry2 = tk.Entry(master = frame1, width=7,textvariable=vars[k+1])
                protEntry2.insert(0,"0-255")
                protEntry2.grid(row=rows+1,column=x,sticky=("NW"))

                protEntry2 = tk.Entry(master = frame1, width=7,textvariable=vars[k+2])
                protEntry2.insert(0,"0-255")
                protEntry2.grid(row=rows+2,column=x,sticky=("NW"))

                protEntry2 = tk.Entry(master = frame1, width=7,textvariable=vars[k+3])
                protEntry2.insert(0,"0-255")
                protEntry2.grid(row=rows+3,column=x,sticky=("NW"))
                x=x+1
            rows = rows+4


        if usedClasses["peltier"] != 0:
 
            peltierLabel = tk.Label(master=frame1, text="Peltier")
            peltierLabel.grid(row=rows, column=0)
            
            tempLabel = tk.Label(master=frame1, text="Pelt temp(C)")
            tempLabel.grid(row=rows+1, column=0)
            peltV1 = tk.StringVar(master=frame1)
            peltV2 = tk.StringVar(master=frame1)
            peltV3 = tk.StringVar(master=frame1)
            peltV4 = tk.StringVar(master=frame1)
            peltV5 = tk.StringVar(master=frame1)
            peltT1 = tk.StringVar(master=frame1)
            peltT2 = tk.StringVar(master=frame1)
            peltT3 = tk.StringVar(master=frame1)
            peltT4 = tk.StringVar(master=frame1)
            peltT5 = tk.StringVar(master=frame1)
            
            #tempFrame =


            vars = [peltV1,peltT1,
                    peltV2,peltT2,
                    peltV3,peltT3,
                    peltV4,peltT4,
                    peltV5,peltT5]
            x=1
            for k in range(0,len(vars),2):
                protButt4 = tk.OptionMenu(frame1,
                                        vars[k],
                                          "OFF",
                                          "ON")
                vars[k].set("OFF")
                protButt4.grid(row=rows, column=x, sticky="NW")
                
                protEntry1 = tk.Entry(master = frame1, width=7,textvariable=vars[k+1])
                protEntry1.insert(0,"25")
                protEntry1.grid(row=rows+1,column=x,sticky=("NW"))
                x=x+1
            rows = rows+2

        #####TIME DURATIONS

        timeLabel = tk.Label(master=frame1, text="Dur(ms)")
        timeLabel.grid(row=rows, column=0)
        timeV1 = tk.StringVar(master=frame1)
        timeV2 = tk.StringVar(master=frame1)
        timeV3 = tk.StringVar(master=frame1)
        timeV4 = tk.StringVar(master=frame1)
        timeV5 = tk.StringVar(master=frame1)

        vars = [timeV1, timeV2, timeV3, timeV4, timeV5]
        for k in range(len(vars)):
            timeEntry1 = tk.Entry(master = frame1, width=7,textvariable=vars[k])
            timeEntry1.insert(0,"0")
            timeEntry1.grid(row=rows,column=k+1,sticky=("NW"))
            
        rows=rows+1
        
        ##### number of repetitions
        timeLabel = tk.Label(master=frame1, text="Repetitions")
        timeLabel.grid(row=rows, column=0)

        timeR1 = tk.StringVar(master=frame1)
        
        timeEntry2 = tk.Entry(master = frame1, width=7,textvariable=timeR1)
        timeEntry2.insert(0,"0")
        timeEntry2.grid(row=rows,column=1,sticky=("NW"))
        rows=rows+1
        
        #### interval in between repetitions
        timeLabel = tk.Label(master=frame1, text="IRI(ms)")
        timeLabel.grid(row=rows, column=0)
        
        timeI1 = tk.StringVar(master=frame1)
        
        timeEntry2 = tk.Entry(master = frame1, width=7,textvariable=timeI1)
        timeEntry2.insert(0,"0")
        timeEntry2.grid(row=rows,column=1,sticky=("NW"))
        rows = rows+1

        ###start protocols
        #runLabel = tk.Label(master=frame1,text="Start protocols:")
        #runLabel.grid(row=rows,column=0)
        #runV1 = tk.StringVar(master=frame1)
        
        runButt = tk.Button(master=frame1,text="RUN!",fg="green",command=self.run_protocol)
        runButt.grid(row=rows-1,column=3)


    def run_protocol(self):
        for key in self.allVariables.keys():
            for i in range(len(self.allVariables[key])):
                if key=="camera":
                    if self.allVariables[key][i].get() =="OFF":
                        print(self.allVariables[key][i].trace_vinfo())
        
        
        
        
        
