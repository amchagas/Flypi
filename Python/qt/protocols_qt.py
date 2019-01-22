from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from camera_qt import Camera
#from ring_qt import Ring
import struct
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
        self.createProtocol()
		
		
        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        
        topLayout.addStretch(1)
        
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        
        mainLayout.addWidget(self.createCamera, 1, 0)
        #mainLayout.addWidget(self.Ring, 1, 1)
        #mainLayout.addWidget(self.Leds, 3, 0)
        #mainLayout.addWidget(self.Peltier, 4, 0)
        mainLayout.addWidget(self.Protocol,2, 0)
        
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Protocols app")
    
    def serwrite(self,msg):
        primer = "TW 1;"
        output = primer + msg
        return output
        
        
    def createProtocol(self):
        self.Protocol = QGroupBox("Protocol")
        layout = QGridLayout()
        
        runButton = QPushButton("Run")
        runButton.setCheckable(True)
        runButton.setChecked(False)
        
        ringLabel = QLabel("Ring")
        layout.addWidget(ringLabel, 0, 0)
        
        redLabel  = QLabel("Red 0-100")
        layout.addWidget(redLabel, 1, 0)
        
        redBox1 = QLineEdit(self)
        redBox1.setText("1")
        layout.addWidget(redBox1, 1,1)
        redBox2 = QLineEdit(self)
        redBox2.setText("2")
        layout.addWidget(redBox2, 1,2)
        redBox3 = QLineEdit(self)
        redBox3.setText("3")
        layout.addWidget(redBox3, 1,3)
        redBox4 = QLineEdit(self)
        redBox4.setText("4")
        layout.addWidget(redBox4, 1,4)
        redBox5 = QLineEdit(self)
        redBox5.setText("5")
        layout.addWidget(redBox5, 1,5)
        
        greenLabel  = QLabel("green 0-100")
        layout.addWidget(greenLabel, 2, 0)
        
        greenBox1 = QLineEdit(self)
        greenBox1.setText("6")
        layout.addWidget(greenBox1, 2,1)
        
        greenBox2 = QLineEdit(self)
        greenBox2.setText("7")
        layout.addWidget(greenBox2, 2,2)
        
        greenBox3 = QLineEdit(self)
        greenBox3.setText("8")
        layout.addWidget(greenBox3, 2,3)
        greenBox4 = QLineEdit(self)
        greenBox4.setText("9")
        layout.addWidget(greenBox4, 2,4)
        greenBox5 = QLineEdit(self)
        greenBox5.setText("10")
        layout.addWidget(greenBox5, 2,5)
        
        blueLabel  = QLabel("blue 0-100")
        layout.addWidget(blueLabel, 3, 0)
        
        blueBox1 = QLineEdit(self)
        blueBox1.setText("11")
        layout.addWidget(blueBox1, 3,1)
        blueBox2 = QLineEdit(self)
        blueBox2.setText("12")
        layout.addWidget(blueBox2, 3,2)
        blueBox3 = QLineEdit(self)
        blueBox3.setText("13")
        layout.addWidget(blueBox3, 3,3)
        blueBox4 = QLineEdit(self)
        blueBox4.setText("14")
        layout.addWidget(blueBox4, 3,4)
        blueBox5 = QLineEdit(self)
        blueBox5.setText("15")
        layout.addWidget(blueBox5, 3,5)
        
        peltLabel = QLabel("Peltier")
        layout.addWidget(peltLabel, 4, 0)
        #tempLabel = QLabel("15C to 45C")
        #layout.addWidget(tempLabel, 5, 0)
        
        peltBox1 = QLineEdit(self)
        peltBox1.setText("16")
        layout.addWidget(peltBox1, 5,1)
        
        peltBox2 = QLineEdit(self)
        peltBox2.setText("17")
        layout.addWidget(peltBox2, 5,2)
        
        peltBox3 = QLineEdit(self)
        peltBox3.setText("18")
        layout.addWidget(peltBox3, 5,3)
        
        peltBox4 = QLineEdit(self)
        peltBox4.setText("19")
        layout.addWidget(peltBox4, 5,4)
        
        
        peltBox5 = QLineEdit(self)
        peltBox5.setText("20")
        layout.addWidget(peltBox5, 5,5)
        
        durLabel  = QLabel("durat (ms)")
        layout.addWidget(durLabel, 6, 0)
        
        durBox1 = QLineEdit(self)
        durBox1.setText("21")
        layout.addWidget(durBox1, 6,1)
        
        durBox2 = QLineEdit(self)
        durBox2.setText("22")
        layout.addWidget(durBox2, 6,2)
        
        durBox3 = QLineEdit(self)
        durBox3.setText("23")
        layout.addWidget(durBox3, 6,3)
        
        durBox4 = QLineEdit(self)
        durBox4.setText("24")
        layout.addWidget(durBox4, 6,4)
        
        durBox5 = QLineEdit(self)
        durBox5.setText("25")
        layout.addWidget(durBox5, 6,5)
        
        itiLabel = QLabel("iti(ms)")
        layout.addWidget(itiLabel, 7, 0)
        itiBox1 = QLineEdit(self)
        itiBox1.setText("26")
        layout.addWidget(itiBox1, 7,1)
        
  
        
        layout.addWidget(runButton,8,0)
        
        
        
        self.Protocol.setLayout(layout)
        

        
        def runUpdate(self):
			#print("here")
			
            if runButton.isChecked():
                print("run")
				#trial1 = list()
                if ser.in_waiting != 0:
                    print(ser.readline())
                print(ser.in_waiting)
                primer = 'TW 1;'
                print(1)
                print(ser.in_waiting)
                ser.write(struct.pack('<p', primer))
                
                
                #ser.flush()
                print(2)
                print(ser.in_waiting)
                ser.write('R1;'.encode('utf-8')) 
                print(3)
                print(ser.in_waiting)
                ser.write(primer.encode('utf-8'))
                dummie = str('RR '+ str(redBox1.text())+';')
                print(4)
                print(ser.in_waiting)
                ser.write(dummie.encode('utf-8')) 
                ser.write(primer.encode('utf-8'))
                print(5)
                print(ser.in_waiting)
                dummie = 'RG ' + str(greenBox1.text())+ ';'
                ser.write(dummie.encode("utf-8")) 
                ser.write(primer.encode('utf-8'))
                print(6)
                print(ser.in_waiting)
                dummie = 'RB ' + str(blueBox1.text())+ ';'
                ser.write(dummie.encode("utf-8")) 
                ser.write(primer.encode('utf-8'))
                print(7)
                print(ser.in_waiting)
                dummie = 'TW ' + str(durBox1.text()) + ';'
                ser.write(dummie.encode('utf-8')) 
                
                dummie = 'R0;'
                
                ser.write(dummie.encode('utf-8')) 
                ser.write(primer.encode('utf-8'))
                ser.flush()
				#part2  
						  
                #ser.write('TW 1;'.encode('utf-8')) 
                #ser.write('R1;'.encode('utf-8')) 
                #ser.write('TW 1;'.encode('utf-8'))
                #dummie = str('RR '+ str(redBox2.text())+';')
                #ser.write(dummie.encode('utf-8')) 
                #dummie = 'RG " + greenBox1.text()+ ';'
                #ser.write(dummie.encode("utf-8")) 
                #dummie = 'RB " + blueBox1.text()+ ';'
                #ser.write(dummie.encode("utf-8")) 
                
                #dummie = 'TW ' + str(durBox2.text()) + ';'
                #ser.write(dummie.encode('utf-8')) 
                #dummie = 'R0;'
                #ser.write(dummie.encode('utf-8')) 						  
						  
                
                    
            return
                
        runButton.clicked.connect(runUpdate)
