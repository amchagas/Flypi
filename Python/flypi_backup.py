################Protocol
class Protocol:


    def __init__(self,parent="",ser=""):
        protFrame=tk.Frame(master=parent)
        protFrame.grid(row=0,column=0)
        protLabel=tk.Label(master=protFrame,text="PROTOCOL:")
        protLabel.grid(row=0,column=0,columnspan=2)

        #####protocol led1####
        if flypiApp.led1Flag==1:

            led1V1= tk.StringVar(master=protFrame)
            led1V1.set(flypiApp.led1OffAdd)

            led1V2= tk.StringVar(master=protFrame)
            led1V2.set(flypiApp.led1OffAdd)

            led1V3= tk.StringVar(master=protFrame)
            led1V3.set(flypiApp.led1OffAdd)

            led1V4= tk.StringVar(master=protFrame)
            led1V4.set(flypiApp.led1OffAdd)

            led1V5= tk.StringVar(master=protFrame)
            led1V5.set(flypiApp.led1OffAdd)

            def led1ProtCB():
                dummie=list()
                dummie.append(led1V1.get())
                dummie.append(led1V2.get())
                dummie.append(led1V3.get())
                dummie.append(led1V4.get())
                dummie.append(led1V5.get())
                return dummie


            protLed1Label=tk.Label(master=protFrame,text="LED1:")
            protLed1Label.grid(row=1,column=0)
            led1Mods =[ ("ON", flypiApp.led1OnAdd,led1V1),
                        ("OFF", flypiApp.led1OffAdd,led1V1),
                        ("ON", flypiApp.led1OnAdd,led1V2),
                        ("OFF", flypiApp.led1OffAdd,led1V2),
                        ("ON", flypiApp.led1OnAdd,led1V3),
                        ("OFF", flypiApp.led1OffAdd,led1V3),
                        ("ON", flypiApp.led1OnAdd,led1V4),
                        ("OFF", flypiApp.led1OffAdd,led1V4),
                        ("ON", flypiApp.led1OnAdd,led1V5),
                        ("OFF", flypiApp.led1OffAdd,led1V5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame,bd=3)
            buttonsFrame.grid(row=1,column=1)
            row1=0
            column1=0
            for label,address,var in led1Mods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label,
                                             command=led1ProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==1:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1




        #####protocol led2#############
        if flypiApp.led2Flag==1:
            led2V1= tk.StringVar(master=protFrame)
            led2V1.set(flypiApp.led2OffAdd)

            led2V2= tk.StringVar(master=protFrame)
            led2V2.set(flypiApp.led2OffAdd)

            led2V3= tk.StringVar(master=protFrame)
            led2V3.set(flypiApp.led2OffAdd)

            led2V4= tk.StringVar(master=protFrame)
            led2V4.set(flypiApp.led2OffAdd)

            led2V5= tk.StringVar(master=protFrame)
            led2V5.set(flypiApp.led2OffAdd)

            def led2ProtCB():
                dummie=list()
                dummie.append(led2V1.get())
                dummie.append(led2V2.get())
                dummie.append(led2V3.get())
                dummie.append(led2V4.get())
                dummie.append(led2V5.get())
                return dummie



            protled2Label=tk.Label(master=protFrame,text="LED 2:")
            protled2Label.grid(row=3,column=0)
            led2Mods =[ ("ON", flypiApp.led2OnAdd,led2V1),
                        ("OFF", flypiApp.led2OffAdd,led2V1),
                        ("ON", flypiApp.led2OnAdd,led2V2),
                        ("OFF", flypiApp.led2OffAdd,led2V2),
                        ("ON", flypiApp.led2OnAdd,led2V3),
                        ("OFF", flypiApp.led2OffAdd,led2V3),
                        ("ON", flypiApp.led2OnAdd,led2V4),
                        ("OFF", flypiApp.led2OffAdd,led2V4),
                        ("ON", flypiApp.led2OnAdd,led2V5),
                        ("OFF", flypiApp.led2OffAdd,led2V5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame,bd=3)
            buttonsFrame.grid(row=3,column=1)
            row1=0
            column1=0
            for label,address,var in led2Mods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label,
                                             command=led2ProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==1:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1



        #######protocol matrix#########
        if flypiApp.matrixFlag==1:

            matV1= tk.StringVar(master=protFrame)
            matV1.set(flypiApp.matOffAdd)

            matV2= tk.StringVar(master=protFrame)
            matV2.set(flypiApp.matOffAdd)

            matV3= tk.StringVar(master=protFrame)
            matV3.set(flypiApp.matOffAdd)

            matV4= tk.StringVar(master=protFrame)
            matV4.set(flypiApp.matOffAdd)

            matV5= tk.StringVar(master=protFrame)
            matV5.set(flypiApp.matOffAdd)

            def matProtCB():
                dummie = list()
                dummie.append(matV1.get())
                dummie.append(matV2.get())
                dummie.append(matV3.get())
                dummie.append(matV4.get())
                dummie.append(matV5.get())
                return dummie

            protMatLabel = tk.Label(master=protFrame, text="MATRIX:")
            protMatLabel.grid(row=4,column=0)
            matMods =[ ("OFF", flypiApp.matOffAdd,matV1),
                        ("PATT1", flypiApp.matPat1Add,matV1),
                        ("PATT2", flypiApp.matPat2Add,matV1),
                        ("PATT3", flypiApp.matOnAdd,matV1),

                        ("OFF", flypiApp.matOffAdd,matV2),
                        ("PATT1", flypiApp.matPat1Add,matV2),
                        ("PATT2", flypiApp.matPat2Add,matV2),
                        ("PATT3", flypiApp.matOnAdd,matV2),

                        ("OFF", flypiApp.matOffAdd,matV3),
                        ("PATT1", flypiApp.matPat1Add,matV3),
                        ("PATT2", flypiApp.matPat2Add,matV3),
                        ("PATT3", flypiApp.matOnAdd,matV3),

                        ("OFF", flypiApp.matOffAdd,matV4),
                        ("PATT1", flypiApp.matPat1Add,matV4),
                        ("PATT2", flypiApp.matPat2Add,matV4),
                        ("PATT3", flypiApp.matOnAdd,matV4),

                        ("OFF", flypiApp.matOffAdd,matV5),
                        ("PATT1", flypiApp.matPat1Add,matV5),
                        ("PATT2", flypiApp.matPat2Add,matV5),
                        ("PATT3", flypiApp.matOnAdd,matV5),]

#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame,bd=3)
            buttonsFrame.grid(row=4,column=1)
            row1=0
            column1=0
            for label,address,var in matMods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label,
                                             command=matProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==3:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1


        #####protocol ring#########
        if flypiApp.ringFlag==1:
            protRingLabel = tk.Label(master=protFrame,text="RING:")
            protRingLabel.grid(row=5,column=0,columnspan=2,sticky="NW")

            ringV1= tk.StringVar(master=protFrame)
            ringV1.set(flypiApp.ringOffAdd)
            ringV2= tk.StringVar(master=protFrame)
            ringV2.set(flypiApp.ringOffAdd)
            ringV3= tk.StringVar(master=protFrame)
            ringV3.set(flypiApp.ringOffAdd)
            ringV4= tk.StringVar(master=protFrame)
            ringV4.set(flypiApp.ringOffAdd)
            ringV5= tk.StringVar(master=protFrame)
            ringV5.set(flypiApp.ringOffAdd)

            def ringProtCB():
                dummie=list()
                dummie.append(ringV1.get())
                dummie.append(ringV2.get())
                dummie.append(ringV3.get())
                dummie.append(ringV4.get())
                dummie.append(ringV5.get())
                return dummie



            ringMods =[ ("ON", flypiApp.ringOnAdd,ringV1),
                       ("OFF", flypiApp.ringOffAdd,ringV1),
                        ("ON", flypiApp.ringOnAdd,ringV2),
                        ("OFF", flypiApp.ringOffAdd,ringV2),
                        ("ON", flypiApp.ringOnAdd,ringV3),
                        ("OFF", flypiApp.ringOffAdd,ringV3),
                        ("ON", flypiApp.ringOnAdd,ringV4),
                        ("OFF", flypiApp.ringOffAdd,ringV4),
                        ("ON", flypiApp.ringOnAdd,ringV5),
                        ("OFF", flypiApp.ringOffAdd,ringV5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame)
            buttonsFrame.grid(row=5,column=1)
            row1=0
            column1=0
            for label,address,var in ringMods:
                protButt1=tk.Radiobutton(master=buttonsFrame,text=label,
                                             command=ringProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==1:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1


        if flypiApp.peltierFlag==1:

            protPeltLabel = tk.Label(master=protFrame,text="PELTIER:")
            protPeltLabel.grid(row=6,column=0,columnspan=2,sticky="NW")

            peltV1= tk.StringVar(master=protFrame)
            peltV1.set(flypiApp.peltOffAdd)
            peltTV1=tk.StringVar(master=protFrame)
            peltTV1.set("temp")

            peltV2= tk.StringVar(master=protFrame)
            peltV2.set(flypiApp.peltOffAdd)
            peltTV2=tk.StringVar(master=protFrame)
            peltTV2.set("temp")

            peltV3= tk.StringVar(master=protFrame)
            peltV3.set(flypiApp.peltOffAdd)
            peltTV3=tk.StringVar(master=protFrame)
            peltTV3.set("temp")

            peltV4= tk.StringVar(master=protFrame)
            peltV4.set(flypiApp.peltOffAdd)
            peltTV4=tk.StringVar(master=protFrame)
            peltTV4.set("temp")

            peltV5= tk.StringVar(master=protFrame)
            peltV5.set(flypiApp.peltOffAdd)
            peltTV5=tk.StringVar(master=protFrame)
            peltTV5.set("temp")

            def peltProtCB():
                dummie=list()
                dummie.append(peltV1.get())
                dummie.append(peltV2.get())
                dummie.append(peltV3.get())
                dummie.append(peltV4.get())
                dummie.append(peltV5.get())
                temp=list()
                temp.append(peltTV1.get())
                temp.append(peltTV2.get())
                temp.append(peltTV3.get())
                temp.append(peltTV4.get())
                temp.append(peltTV5.get())
                return dummie, temp



            peltMods =[ ("ON", flypiApp.peltOnAdd,peltV1),
                       ("OFF", flypiApp.peltOffAdd,peltV1),
                        ("TEMP",flypiApp.peltTempAdd,peltTV1),
                        ("ON", flypiApp.peltOnAdd,peltV2),
                        ("OFF", flypiApp.peltOffAdd,peltV2),
                        ("TEMP",flypiApp.peltTempAdd,peltTV2),
                        ("ON", flypiApp.peltOnAdd,peltV3),
                        ("OFF", flypiApp.peltOffAdd,peltV3),
                        ("TEMP",flypiApp.peltTempAdd,peltTV3),
                        ("ON", flypiApp.peltOnAdd,peltV4),
                        ("OFF", flypiApp.peltOffAdd,peltV4),
                        ("TEMP",flypiApp.peltTempAdd,peltTV4),
                        ("ON", flypiApp.peltOnAdd,peltV5),
                        ("OFF", flypiApp.peltOffAdd,peltV5),
                        ("TEMP",flypiApp.peltTempAdd,peltTV5)]
#            row1=1
#            column1=1
            buttonsFrame=tk.Frame(master=protFrame)
            buttonsFrame.grid(row=6,column=1)
            row1=0
            column1=0
            for label,address,var in peltMods:
                if label is "TEMP":

                    proEntry=tk.Entry(master=buttonsFrame,
                                      width=5,text="temp",
                                      textvariable=var)
                    proEntry.grid(row=row1,column=column1,sticky="NW")
#                    if row1=0:
#                        tempLabel=tk.label()
                else:
                    protButt1=tk.Radiobutton(master=buttonsFrame,text=label,
                                             command=peltProtCB,indicatoron=0,
                                             value=address,variable=var,width=5)
                    protButt1.grid(row=row1,column=column1,sticky="NW")
                if row1==2:
                    row1=0
                    column1=column1+1
                else:
                    row1=row1+1

        ####### create the time for each round:
        protDurLabel = tk.Label(master=protFrame,text="DUR(S):")
        protDurLabel.grid(row=7,column=0,columnspan=2,sticky="NW")

        durV1=tk.StringVar(master=protFrame)
        durV1.set("0.0")

        durV2= tk.StringVar(master=protFrame)
        durV2.set("0.0")


        durV3= tk.StringVar(master=protFrame)
        durV3.set("0.0")


        durV4= tk.StringVar(master=protFrame)
        durV4.set("0.0")


        durV5= tk.StringVar(master=protFrame)
        durV5.set("0.0")

        def durProtCB():
            dummie=list()
            dummie.append(durV1.get())
            dummie.append(durV2.get())
            dummie.append(durV3.get())
            dummie.append(durV4.get())
            dummie.append(durV5.get())
            return dummie


        durMods =[     ("TEMP",durV1),
                        ("TEMP",durV2),
                        ("TEMP",durV3),
                        ("TEMP",durV4),
                        ("TEMP",durV5),]
        buttonsFrame=tk.Frame(master=protFrame)
        buttonsFrame.grid(row=7,column=1)
        row1=0
        column1=0
        for label,var in durMods:
            durEntry=tk.Entry(master=buttonsFrame,
                                      width=5,text="temp",
                                      textvariable=var)
            durEntry.grid(row=row1,column=column1,sticky="NW")
#                    if row1=0:
#                        tempLabel=tk.label()
            column1=column1+1
        #######create the run and dry run buttons
        #create callbacks
        def dryRunCB():
            allVar=dict()
            if flypiApp.led1Flag==1:
                led1=led1ProtCB()
                allVar["led1"]=led1

            if flypiApp.led2Flag==1:
                led2=led2ProtCB()
                allVar["led2"]=led2

            if flypiApp.matrixFlag==1:
                matrix=matProtCB()
                allVar["matrix"]=matrix

            if flypiApp.ringFlag==1:
                ring=ringProtCB()
                allVar["ring"]=ring

            if flypiApp.peltierFlag==1:
                peltier,temp=peltProtCB()
                allVar["peltier"]=(peltier,temp)


            durations=durProtCB()
            allVar["durations"]=durations
            print (allVar)
            return allVar

        def runCB():
            allVars=dryRunCB()
            if flypiApp.cameraFlag==1:
                print ("recording")
                ###wait a couple of seconds for the camera to settle
                Camera.start_recording('my_video.h264')
                Camera.cam.wait_recording(5)
                Camera.cam.stop_recording()
                ###start recording
            #send prot address to arduino and send code to be run



        protDryRun=tk.Button(master=protFrame, text="DRY RUN",command=dryRunCB,)
        protDryRun.grid(row=2,column=5,sticky="WN")

        protRun=tk.Button(master=protFrame, text="RUN",command=runCB,)
        protRun.grid(row=3,column=5,sticky="WN")

        #protrunRec=tk.Checkbutton












#    ######################################## PROTOCOLS
#class Protocols:
#
#    def __init__(self,parent="none",label="PROTOCOL"):
#
#        #create frame
#        self.frame1=tk.Frame(master=parent)
#        #display frame
#        self.frame1.grid(row=0,column=0)
#        #index for update the row where each item will be displayed
#        self.rowIndx=0
#        #list for knowing how many items will be displayed
#        self.protSum=list()
#
#        #label for the protocol part of the GUI
#        protLabel=tk.Label(master=self.frame1,text=label)
#        protLabel.grid(row=self.rowIndx,column=0)
#        #update row index
#        self.rowIndx=+1
#
#        #if the LED1 GUI is displayed
#        if flypiApp.led1Flag==1:
#            label="LED1: "
#            dummie,led1Menu=self.ledMenu(rowIndx=self.rowIndx,colIndx=0,
#                                         text_="LED1: ",parent=self.frame1)
#            led1Menu.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append(label)
#        #if the LED2 GUI is displayed
#        if flypiApp.led2Flag==1:
#            label="LED2: "
#            dummie,led2Menu=self.ledMenu(rowIndx=self.rowIndx,colIndx=0,
#                                         text_=label,parent=self.frame1)
#            led2Menu.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append("LED2: ")
#        #if the MATRIX GUI is displayed
#        if flypiApp.matrixFlag==1:
#            dummie,matMenu=self.matrixMenu(rowIndx=self.rowIndx,colIndx=0,
#                                           text_="MATRIX: ",parent=self.frame1)
#            matMenu.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append("matrix")
#        #if the RING GUI is displayed
#        if flypiApp.ringFlag==1:
#            dummie,ringMenu=self.ringMenu(rowIndx=self.rowIndx,colIndx=0,
#                                          text_="RING: ",parent=self.frame1)
#            ringMenu.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#            self.protSum.append("ring")
#            val = Protocols.runCallBack
#            print ("value"+str(val))
#        #if PELTIER GUI is displayed
#        if flypiApp.peltierFlag==1:
#            var,temp,peltierMenu1,tempEntry=self.peltierMenu(rowIndx=self.rowIndx,colIndx=0,
#                                                            text_="PELTIER: ",parent=self.frame1)
#            peltierMenu1.grid(row=self.rowIndx,column=1)
#            tempEntry.grid(row=self.rowIndx+2,column=1)
#            self.rowIndx=self.rowIndx+2
#            self.protSum.append("peltier")
#
#        #if any GUI are displayed create Duration entry
#        if len(self.protSum) != 0:
#            time,timeEntry =self.timeMenu(parent=self.frame1,rowIndx=self.rowIndx,
#                                          colIndx=0,text_="DUR (Sec)")
#
#            timeEntry.grid(row=self.rowIndx,column=1)
#            self.rowIndx=self.rowIndx+1
#
#
#
#    ##### functions to create the protocol panel
#    def ledMenu(self,rowIndx=0,colIndx=0,text_="LED",parent="none"):
#
#        ledLabel = tk.Label(master=parent,text=text_)
#        ledLabel.grid(row=rowIndx,column=colIndx)
#
#        var=tk.StringVar()
#        ledMenu=tk.OptionMenu(parent,var,"ON","OFF")
#        var.set("OFF")
#
#        return(var,ledMenu)
#
#    def matrixMenu(self,rowIndx=0,colIndx=0,text_="MATRIX",parent="none"):
#
#        MatLabel = tk.Label(master=parent,text=text_)
#        MatLabel.grid(row=rowIndx,column=colIndx)
#
#        var=tk.StringVar()
#        matMenu=tk.OptionMenu(parent,var,"ON","OFF","PAT1","PAT2")
#        var.set("OFF")
#        return (var,matMenu)
#
#    def ringMenu(self,rowIndx=0,colIndx=0,text_="RING",parent="none"):
#
#        ringLabel = tk.Label(master=parent,text=text_)
#        ringLabel.grid(row=rowIndx,column=colIndx)
#
#        var=tk.StringVar()
#        ringMenu=tk.OptionMenu(parent,var,"ON","OFF")
#        var.set("OFF")
#        return (var,ringMenu)#
#
#    def peltierMenu(self,rowIndx=0,colIndx=0,text_="Peltier",parent="none"):
#
#        peltierLabel = tk.Label(master=parent,text=text_)
#        peltierLabel.grid(row=rowIndx,column=colIndx)
#
#        var=tk.StringVar()
#        peltierMenu=tk.OptionMenu(parent,var,"ON","OFF")
#        var.set("OFF")
#
#        tempLabel=tk.Label(master=parent,text="TEMP (C)")
#        tempLabel.grid(row=rowIndx+2,column=colIndx)
#
#        temp=tk.StringVar()
#        tempEntry=tk.Entry(master=parent,width=8,
#                           textvariable=temp)
#        temp.set("25")
#        return (var,temp,peltierMenu,tempEntry)
#
#    def timeMenu(self,rowIndx=0,colIndx=0,text_="DUR (Sec)",parent="none"):
#        timeLabel=tk.Label(master=self.frame1,text=text_)
#        timeLabel.grid(row=rowIndx,column=colIndx)
#
#        time=tk.StringVar()
#        timeEntry=tk.Entry(master=self.frame1,
#                           textvariable=time,
#                           width=8)
#        time.set("0")
#
#
#        return(time,timeEntry)
#
##    def run(self):
##        runButt=tk.Button(master=self.frame1,text="RUN",command=self.run)
##        try:
##            self.protSum("LED1")
##            print "works"
##        except ValueError:
##            print "def works"
#    def runCallBack():
#        try:
#            val = flypiApp.RING.ringGreenVar.get()#flypiApp.RING.ringGreenVar.get()
#
#            print(val)
#        except NameError:
#            print("no ring")
#        return val

#        self.camAWVar.set("incadescent")
#        self.camFrame1.grid_propagate(flag=False)
#        self.TLLabel.pack()
#        self.camRecButt.pack(fill="x")
#        self.camTLButt.pack(fill="x")
#        self.camSnapButt.pack(fill="x")
#        self.TLdurLabel.pack()
#        self.TLdur.pack()
#        self.TLinterLabel.pack()
#        self.TLinter.pack()
