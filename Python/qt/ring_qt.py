from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)



class Ring():

    def createRing(self):
        
        def remap(value, min1=0,max1=100,min2=0,max2=255):
            oldRange = (max1 - min1)  
            newRange = (max2 - min2)  
            newValue = (((value - min1) * newRange) / oldRange) + min2
            return newValue
            
        self.Ring = QGroupBox("Ring")

        onButton = QPushButton("Ring ON")
        onButton.setCheckable(True)
        onButton.setChecked(False)

        zapButton = QPushButton("ZAP NOW!")
        zapButton.setCheckable(False)
        zapButton.setChecked(False)

        redLabel = QLabel("RED:")
        redSlider = QSlider(Qt.Horizontal,self.Ring)
        redSlider.setMinimum(0)
        redSlider.setMaximum(100)
        redSlider.setValue(10)
        redSlider.setTickPosition(QSlider.TicksBelow)
        redSlider.setTickInterval(1)


        greenLabel = QLabel("GREEN:")
        greenSlider = QSlider(Qt.Horizontal,self.Ring)
        greenSlider.setMinimum(0)
        greenSlider.setMaximum(100)
        greenSlider.setValue(10)
        greenSlider.setTickPosition(QSlider.TicksBelow)
        greenSlider.setTickInterval(1)


        blueLabel = QLabel("BLUE:")
        blueSlider = QSlider(Qt.Horizontal,self.Ring)
        blueSlider.setMinimum(0)
        blueSlider.setMaximum(100)
        blueSlider.setValue(10)
        blueSlider.setTickPosition(QSlider.TicksBelow)
        blueSlider.setTickInterval(1)

        allLabel = QLabel("ALL:")
        allSlider = QSlider(Qt.Horizontal,self.Ring)
        allSlider.setMinimum(0)
        allSlider.setMaximum(100)
        allSlider.setValue(10)
        allSlider.setTickPosition(QSlider.TicksBelow)
        allSlider.setTickInterval(1)


        redZapLabel  = QLabel("RED ZAP:")
        redZapBox = QLineEdit(self)
        redZapBox.setText("0")

        greenZapLabel  = QLabel("GREEN ZAP:")
        greenZapBox = QLineEdit()
        greenZapBox.setText("0")

        blueZapLabel  = QLabel("BLUE ZAP:")
        blueZapBox = QLineEdit()
        blueZapBox.setText("0")
        
        durZapLabel  = QLabel("ZAP Duration (ms):")
        durZapBox = QLineEdit()
        durZapBox.setText("0")
        
        layout = QGridLayout()
        layout.addWidget(onButton, 1, 0)
        layout.addWidget(zapButton, 1, 1)

        layout.addWidget(redLabel, 2, 0)
        layout.addWidget(redSlider, 3, 0)

        layout.addWidget(greenLabel, 2, 1)
        layout.addWidget(greenSlider, 3, 1)

        layout.addWidget(blueLabel, 2, 2)
        layout.addWidget(blueSlider, 3, 2)

        layout.addWidget(allLabel, 2, 3)
        layout.addWidget(allSlider, 3, 3)

        layout.addWidget(redZapLabel, 4, 0)
        layout.addWidget(redZapBox, 5, 0)

        layout.addWidget(greenZapLabel, 4,1)
        layout.addWidget(greenZapBox, 5, 1)

        layout.addWidget(blueZapLabel, 4,2)
        layout.addWidget(blueZapBox, 5, 2)

        layout.addWidget(durZapLabel, 4,3)
        layout.addWidget(durZapBox, 5, 3)

        self.Ring.setLayout(layout)

        def redUpdate(self):
            print(redSlider.value())
            if loadSerial == 1:
                value = remap(redSlider.value())
                

                output = primer + "RR " + str(value) + ";"
                ser.write(output.encode("utf-8"))
            return
                

        def greenUpdate(self):
            print(greenSlider.value())
            if loadSerial == 1:
                value = remap(greenSlider.value())
                output = primer + "RG " + str(value) + ";"
                ser.write(output.encode("utf-8"))
                

        def blueUpdate(self):
            print(blueSlider.value())
            if loadSerial == 1:
                value = remap(blueSlider.value())
                output = primer + "RB " + str(value) + ";"
                ser.write(output.encode("utf-8"))
                
                
        def allUpdate(self):
            value = str(allSlider.value())
            
            redSlider.setValue(int(value))
            greenSlider.setValue(int(value))
            blueSlider.setValue(int(value))

            return
                
        def zapUpdate(self):
            print("zap")
            if onButton.isChecked():
                print(redZapBox.text())
                print(greenZapBox.text())
                print(blueZapBox.text())
                print(durZapBox.text())
                print(redSlider.value())
                print(greenSlider.value())
                print(blueSlider.value())
                if loadSerial == 1:
                    
                    output = primer + "RR " + redZapBox.text() + ";"
                    output = output + "RG " + greenZapBox.text() + ";"                    
                    output = output + "RB " + blueZapBox.text() + ";"                 
                    output = output + "TW " + durZapBox.text() + ";"
                    ser.write(output.encode("utf-8"))  
                    
                    
                    
                    output = primer + "RR " + str(redSlider.value()) + ";"
                    output = output + "RG " + str(greenSlider.value()) + ";"
                    output = output + "RB " + str(blueSlider.value()) + ";"
                    ser.write(output.encode("utf-8"))  
                    

        def onUpdate(self):
            if onButton.isChecked():
                #if loadSerial == 1:
                    
                output = "R1;"
                #   ser.write(output.encode("utf-8")) 
                print("ring ON")
            else:
                #if loadSerial == 1:
                output = "R0;"
                    #ser.write(output.encode("utf-8")) 
                print("ring OFF")
            
            return output

        
        onButton.clicked.connect(onUpdate)
        zapButton.clicked.connect(zapUpdate)
        redSlider.valueChanged.connect(redUpdate)
        greenSlider.valueChanged.connect(greenUpdate)
        blueSlider.valueChanged.connect(blueUpdate)
        allSlider.valueChanged.connect(allUpdate)
	
        return self.Ring
