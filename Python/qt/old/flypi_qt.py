from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from camera_qt import Camera
#from ring_qt import Ring

try:
    import serial
    serialAvail = True

except ImportError:
    serialAvail = False
    print ("serial module not available!")
    print ("user interface will not control flypi!")


loadSerial = 1

if loadSerial == 1:
    if serialAvail == True:
        # for Arduino Uno from RPi
        #self.ser = serial.Serial('/dev/ttyACM0', 115200)
        # for Arduino Nano from RPi
        ser = serial.Serial('/dev/ttyUSB0', 115200)
        primer = "TW 1;"




class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("FlyPi User Interface:")
        

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createCamera = Camera.createCamera(self)
        self.createRing ()
        self.createLEDs()
        self.createPeltier()
        #self.createProtocol()
        
        disableWidgetsCheckBox.toggled.connect(self.Camera.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.Peltier.setDisabled)
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        
        topLayout.addStretch(1)
        
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        
        mainLayout.addWidget(self.createCamera, 1, 0)
        mainLayout.addWidget(self.Ring, 1, 1)
        mainLayout.addWidget(self.Leds, 3, 0)
        mainLayout.addWidget(self.Peltier, 4, 0)
        mainLayout.addWidget(self.Protocol,3, 1)
        
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("FlyPi app")

        
    def serwrite(self,msg):
        primer = "TW 1;"
        output = primer + msg
        return output
        
        
    def createProtocol(self):
        self.Protocol = QGroupBox("Protocol")
        return
    
    def createPeltier(self):
        self.Peltier = QGroupBox("Peltier")
        
        PeltieronButton = QPushButton("Peltier ON")
        PeltieronButton.setCheckable(True)
        PeltieronButton.setChecked(False)
        
        setTempLabel  = QLabel("Desired temperature:")
        setTempBox = QLineEdit(self)
        
        getTempLabel  = QLabel("current temperature:")
        tempLabel  = QLabel("35 " + "C")
        
        logTempCheckBox = QCheckBox("&log temperature:")
        
        layout = QGridLayout()
        layout.addWidget(PeltieronButton , 0, 0)
        layout.addWidget(setTempLabel,0,1)
        layout.addWidget(setTempBox,1,1)
        layout.addWidget(getTempLabel,0,2)
        layout.addWidget(tempLabel,1,2)
        
        layout.addWidget(logTempCheckBox,1,3 )
        
        self.Peltier.setLayout(layout)
        
        def peltOnUpdate(self):
            if PeltieronButton.isChecked():
                if loadSerial == 1:
                    output = primer+"P1;"
                    ser.write(output.encode("utf-8"))

                print("ON")
            else:
                if loadSerial == 1:
                    output=primer+"P0"
                    ser.write(output.encode("utf-8"))
                print("OFF")

        PeltieronButton.clicked.connect(peltOnUpdate)
        
    def createLEDs(self):
        self.Leds = QGroupBox("LEDs")

        L1onButton = QPushButton("LED1 ON")
        L1onButton.setCheckable(True)
        L1onButton.setChecked(False)

        zap1Button = QPushButton("ZAP Led1")
        zap1Button.setCheckable(False)
        zap1Button.setChecked(False)

        L1Label = QLabel("Brightness:")
        L1Slider = QSlider(Qt.Horizontal,self.Leds)
        L1Slider.setMinimum(0)
        L1Slider.setMaximum(100)
        L1Slider.setValue(10)
        L1Slider.setTickPosition(QSlider.TicksBelow)
        L1Slider.setTickInterval(1)

        L1ZapLabel = QLabel("L1 Zap Brightness:")
        L1ZapSlider = QSlider(Qt.Horizontal,self.Leds)
        L1ZapSlider.setMinimum(0)
        L1ZapSlider.setMaximum(100)
        L1ZapSlider.setValue(10)
        L1ZapSlider.setTickPosition(QSlider.TicksBelow)
        L1ZapSlider.setTickInterval(1)

        L2onButton = QPushButton("LED2 ON")
        L2onButton.setCheckable(True)
        L2onButton.setChecked(False)

        zap2Button = QPushButton("ZAP Led2")
        zap2Button.setCheckable(False)
        zap2Button.setChecked(False)

        L2Label = QLabel("Brightness:")
        L2Slider = QSlider(Qt.Horizontal,self.Leds)
        L2Slider.setMinimum(0)
        L2Slider.setMaximum(100)
        L2Slider.setValue(10)
        L2Slider.setTickPosition(QSlider.TicksBelow)
        L2Slider.setTickInterval(1)

        L2ZapLabel = QLabel("L2 Zap Brightness:")
        L2ZapSlider = QSlider(Qt.Horizontal,self.Leds)
        L2ZapSlider.setMinimum(0)
        L2ZapSlider.setMaximum(100)
        L2ZapSlider.setValue(10)
        L2ZapSlider.setTickPosition(QSlider.TicksBelow)
        L2ZapSlider.setTickInterval(1)

        layout = QGridLayout()
        layout.addWidget(L1onButton, 1, 0)
        layout.addWidget(L1Label, 2, 0)
        layout.addWidget(L1Slider, 3, 0)
        layout.addWidget(zap1Button, 4, 0)
        layout.addWidget(L1ZapLabel, 5, 0)
        layout.addWidget(L1ZapSlider, 6, 0)

        layout.addWidget(L2onButton, 1, 1)

        layout.addWidget(L2Label, 2, 1)
        layout.addWidget(L2Slider, 3, 1)
        layout.addWidget(zap2Button, 4, 1)
        layout.addWidget(L2ZapLabel, 5, 1)
        layout.addWidget(L2ZapSlider, 6, 1)
        #layout.addWidget(zapButton, 1, 1)
        self.Leds.setLayout(layout)


        def L1onUpdate(self):
            #if L1onButton.isChecked():
            if loadSerial == 1:
                output="L11;"
                ser.write(output.encode("utf-8"))

                print("ON")
            else:
                if loadSerial == 1:
                    output="L10;"
                    ser.write(output.encode("utf-8"))
                print("OFF")

        def L2onUpdate(self):
            if L2onButton.isChecked():
                if loadSerial == 1:
                    output="L21;"
                    ser.write(output.encode("utf-8"))

                print("ON")
            else:
                if loadSerial == 1:
                    output="L20 0;"
                    ser.write(output.encode("utf-8"))

                print("OFF")

        def L1SliUpdate(self):
            print(L1Slider.value())
            if loadSerial == 1:


                output="L10"
                ser.write(output.encode("utf-8"))

                output=str(L1Slider.value())
                ser.write(output.encode("utf-8"))

        def L2SliUpdate(self):
            print(L2Slider.value())
            if loadSerial == 1:
                output="L20" + str(L2Slider.value()) + ";"
                ser.write(output.encode("utf-8"))
                

        def zap1Update(self):
            if zap1Button.isChecked():
                #print("this")
                print(L1ZapSlider.value())
                if L1onButton.isChecked():
                    if loadSerial == 1:
                        output = "L11 " + str(L1ZapSlider.value()) + ";"
                        ser.write(output.encode("utf-8"))
                        
                        output = "TW 500;"
                        ser.write(output.encode("utf-8"))
                        
                        output = "L11 " + str(L1Slider.value()) + ";"
                        ser.write(output.encode("utf-8"))

                        #ser.println("zap1test")

        def zap2Update(self):
            #print(L2ZapSlider.value())
            if L2onButton.isChecked():
                if loadSerial == 1:
                    output = "L21"
                    ser.write(output.encode("utf-8"))
                    output = L2ZapSlider.value()
                    ser.write(output.encode("utf-8"))
                    output = "TW"
                    ser.write(output.encode("utf-8"))
                    output = "L21"
                    ser.write(output.encode("utf-8"))
                    output = L2Slider.value()
                    ser.write(output.encode("utf-8"))
                    #ser.println("zap2test")
                    
                    #print(L2ZapSlider.value())
                    #ser.println()
                    #ser.println(L2ZapSlider.value())


        L1onButton.clicked.connect(L1onUpdate)
        L1Slider.valueChanged.connect(L1SliUpdate)
        zap1Button.clicked.connect(zap1Update)

        L2onButton.clicked.connect(L2onUpdate)
        L2Slider.valueChanged.connect(L2SliUpdate)

        zap2Button.clicked.connect(zap2Update)




        return

    def createRing(self):
        
        def remap(value, min1=0,max1=100,min2=0,max2=255):
            oldRange = (max1 - min1)  
            newRange = (max2 - min2)  
            newValue = (((value - min1) * newRange) / oldRange) + min2
            return newValue
            
        self.Ring = QGroupBox("Ring")

        onButton = QPushButton("Ring ON")
        self.test = onButton
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
                if loadSerial == 1:
                    output = "R1;"
                    ser.write(output.encode("utf-8")) 
                    
                print("ring ON")
            else:
                if loadSerial == 1:
                    output = "R0;"
                    ser.write(output.encode("utf-8")) 
                    
                print("ring OFF")
            return

        
        onButton.clicked.connect(onUpdate)
        zapButton.clicked.connect(zapUpdate)
        redSlider.valueChanged.connect(redUpdate)
        greenSlider.valueChanged.connect(greenUpdate)
        blueSlider.valueChanged.connect(blueUpdate)
        allSlider.valueChanged.connect(allUpdate)
	
        return


    

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
