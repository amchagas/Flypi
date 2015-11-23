    ######################################## MATRIX
import tkinter as tk


class Matrix:

    def __init__(self, parent="none", label="none",
                 pat3Add="39", offAdd="40", pat1Add="41",
                 pat2Add="42", brightAdd="43000", prot=False,
                 protFrame="", ser=""):

        self.label = label
        self.pat3Add = pat3Add
        self.offAdd = offAdd
        self.pat1Add = pat1Add
        self.pat2Add = pat2Add
        self.brightAdd = brightAdd
        self.ser = ser
        self.matParent = parent
        #####callback for brightness slider
        matBrightVar = tk.IntVar()

        def matrixUpdate(self, ser=self.ser, brightAdd=self.brightAdd):
            address = int(brightAdd)
            output = address + matBrightVar.get()
            output = str(output) + "*"
            print("mat bright " + output[2:-1])
            ser.write(output.encode("utf-8"))

        frame1 = tk.Frame(master=self.matParent, width=10)
        frame1.pack()
        self.matrixLabel = tk.Label(master=frame1, text=self.label)
        self.matrixLabel.pack(side="top")

        self.matrixOffButt = self.MatButton(parent=frame1, side="top",
                                            buttText="OFF", color="red",
                                            func=self.matrixOff, fill="x")

        self.matrixPat1Butt = self.MatButton(parent=frame1, side="top",
                                      buttText="PATTERN 1", color="black",
                                      func=self.matrixPattern1, fill="x")

        self.matrixPat2Butt = self.MatButton(parent=frame1, side="top",
                                      buttText="PATTERN 2", color="black",
                                      func=self.matrixPattern2, fill="x")

        self.matrixPat3Butt = self.MatButton(parent=frame1, side="top",
                                      buttText="PATTERN3", color="black",
                                      func=self.matrixPattern3, fill="x")

        frame4 = tk.Frame(master=frame1)

        self.matrixBrightLabel = tk.Label(master=frame4, text="Brightness")
        self.matrixBrightLabel.pack()
        self.matrixBright = tk.Scale(master=frame4, from_=16, to=0,
                                     orient="vertical",
                                     var=matBrightVar, command=matrixUpdate,
                                     width=15, length=90)
        matBrightVar.set(1)
        self.matrixBright.pack(after=self.matrixBrightLabel, side="left")
        frame4.pack(after=self.matrixLabel, side="right")

####################protocol##########################

        if prot == True:
            tempFrame = tk.Frame(master=protFrame)
            tempFrame.pack()
            matV1 = tk.StringVar(master=tempFrame)
#            matV1.set(self.offAdd)

            matV2 = tk.StringVar(master=tempFrame)
#            matV2.set(self.offAdd)

            matV3 = tk.StringVar(master=tempFrame)
#            matV3.set(self.offAdd)

            matV4 = tk.StringVar(master=tempFrame)
#            matV4.set(self.offAdd)

            matV5 = tk.StringVar(master=tempFrame)
#            matV5.set(self.offAdd)

            def matProtCB():
                dummie = list()
                dummie.append(matV1.get())
                dummie.append(matV2.get())
                dummie.append(matV3.get())
                dummie.append(matV4.get())
                dummie.append(matV5.get())
                return dummie

            protMatLabel = tk.Label(master=tempFrame, text="MATRIX:")
            protMatLabel.grid(row=0, column=0)
#            matMods = [("OFF", self.offAdd, matV1),
#                        ("PATT1", self.pat1Add, matV1),
#                        ("PATT2", self.pat2Add, matV1),
#                        ("PATT3", self.pat3Add, matV1),
#
#                        ("OFF", self.offAdd, matV2),
#                        ("PATT1", self.pat1Add, matV2),
#                        ("PATT2", self.pat2Add, matV2),
#                        ("PATT3", self.pat3Add, matV2),
#
#                        ("OFF", self.offAdd, matV3),
#                        ("PATT1", self.pat1Add, matV3),
#                        ("PATT2", self.pat2Add, matV3),
#                        ("PATT3", self.pat3Add, matV3),
#
#                        ("OFF", self.offAdd, matV4),
#                        ("PATT1", self.pat1Add, matV4),
#                        ("PATT2", self.pat2Add, matV4),
#                        ("PATT3", self.pat3Add, matV4),
#
#                        ("OFF", self.offAdd, matV5),
#                        ("PATT1", self.pat1Add, matV5),
#                        ("PATT2", self.pat2Add, matV5),
#                        ("PATT3", self.pat3Add, matV5)]

            buttonsFrame = tk.Frame(master=tempFrame, bd=3)
            buttonsFrame.grid(row=0, column=1)

            vars = [matV1, matV2, matV3, matV4, matV5]
            for k in range(0, 5):
                protButt1 = tk.OptionMenu(buttonsFrame,
                                          vars[k],
                                          "OFF",
                                          "Patt1",
                                          "Patt2",
                                          "Patt3")
                vars[k].set("OFF")
                protButt1.grid(row=1, column=k, sticky="NW")

#            row1 = 0
#            column1 = 1
#            for label, address, var in matMods:
#                protButt1 = tk.Radiobutton(master=buttonsFrame, text=label,
#                                             command=matProtCB, indicatoron=0,
#                                             value=address,
#                                             variable=var, width=5)
#                protButt1.grid(row=row1, column=column1, sticky="NW")
#                if row1 == 3:
#                    row1 = 0
#                    column1 = column1 + 1
#                else:
#                    row1 = row1 + 1

####################callbacks######################

    def MatButton(self, parent="none", fill="y",
                  side="top", buttText="button",
                  color="black", func="none"):

        button = tk.Button(parent, text=buttText, fg=color, command=func)
        button.pack(side=side, fill=fill)

    def matrixOff(self):
        output = str(self.offAdd) + "*"
        print("matrix off " + output)
        self.ser.write(output.encode("utf-8"))

    def matrixPattern1(self):
        output = str(self.pat1Add) + "*"
        print("matrix pattern1 " + output)
        self.ser.write(output.encode("utf-8"))

    def matrixPattern2(self):
        output = str(self.pat2Add) + "*"
        print("matrix pattern2 " + output)
        self.ser.write(output.encode("utf-8"))

    def matrixPattern3(self):
        output = str(self.pat3Add) + "*"
        print ("matrix pattern3 " + output)
        self.ser.write(output.encode("utf-8"))
