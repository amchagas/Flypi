from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,QLCDNumber,QVBoxLayout)


from camera_qt import Camera
#from datetime import datetime
#from ring_qt import Ring
import time
import os

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
        while ser.in_waiting==0:
            print("init")
        print(ser.readline())
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

        #topLayout.addWidget(disableWidgetsCheckBox)

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
        
        return
    


    def serwrite(self,msg):
        #primer = "TW 1;"
        output = msg
        return output
    


    def createProtocol(self):
		
        def create_folder(folderPath="/home/pi/Desktop/flypi_output/",
                          folderName="output1"):
            absPath = folderPath+folderName+"/"
            if not os.path.exists(absPath):
                #if not, create it:
                os.makedirs(absPath)
                os.chown(absPath, 1000, 1000)
            return absPath
    
        def create_file(filePath="/home/pi/Desktop/flypi_output/output1/",
                        fileName="file1"+time.strftime('%Y-%m-%d') + ".txt"):
            #check if the file already exists
            if os.path.isfile(filePath + fileName) == False:
                #if it does not exist, create it
                fh = open(filePath + fileName, "w")
            else:
                #open file and append to it
                fh = open(filePath + fileName, "a")



            return fh
            
        
        #from stackoverflow - easy way to add item in between every item on the list
        def intersperse(lst, item):
            result = [item] * (len(lst) * 2 - 1)
            result[0::2] = lst
            return result
        
        #camera = self.createCamera
        
        self.Protocol = QGroupBox("Protocol")
        #self.Camera = QGroupBox("Camera")
        #camlayout = QGridLayout()
        layout = QGridLayout()
        #layout.setColumnStretch(0, 4)
        
        #self.Camera = Camera()
        
        #cam = Camera.createCamera(self)
        #print(self) 
        #cam1 = Camera()
        #cam = cam1.createCamera()
        
        #layout.addWidget(self.createCamera, row = 0, column = 0, rowSpan = 1, columnSpan=3,)
        #layout.addWidget(cam, 0, 0)        
        #row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0
        runButton = QPushButton("Run")
        runButton.setCheckable(True)
        runButton.setChecked(False)


        ringButton = QPushButton("ON")
        ringButton.setCheckable(True)
        ringButton.setChecked(False)
        layout.addWidget(ringButton, 1, 1)
        
        

        ringLabel = QLabel("Ring")
        layout.addWidget(ringLabel, 1, 0)

        redLabel  = QLabel("Red 0-100")
        layout.addWidget(redLabel, 2, 0)

        redBox1 = QLineEdit(self)
        redBox1.setText("0")
        layout.addWidget(redBox1, 2,1)
        redBox2 = QLineEdit(self)
        redBox2.setText("0")
        layout.addWidget(redBox2, 2,2)
        redBox3 = QLineEdit(self)
        redBox3.setText("0")
        layout.addWidget(redBox3, 2,3)
        redBox4 = QLineEdit(self)
        redBox4.setText("0")
        layout.addWidget(redBox4, 2,4)
        redBox5 = QLineEdit(self)
        redBox5.setText("0")
        layout.addWidget(redBox5, 2,5)

        greenLabel  = QLabel("green 0-100")
        layout.addWidget(greenLabel, 3, 0)

        greenBox1 = QLineEdit(self)
        greenBox1.setText("0")
        layout.addWidget(greenBox1, 3,1)

        greenBox2 = QLineEdit(self)
        greenBox2.setText("0")
        layout.addWidget(greenBox2, 3,2)

        greenBox3 = QLineEdit(self)
        greenBox3.setText("0")
        layout.addWidget(greenBox3, 3,3)
        greenBox4 = QLineEdit(self)
        greenBox4.setText("0")
        layout.addWidget(greenBox4, 3,4)
        greenBox5 = QLineEdit(self)
        greenBox5.setText("0")
        layout.addWidget(greenBox5, 3,5)

        blueLabel  = QLabel("blue 0-100")
        layout.addWidget(blueLabel, 4, 0)

        blueBox1 = QLineEdit(self)
        blueBox1.setText("0")
        layout.addWidget(blueBox1, 4,1)
        blueBox2 = QLineEdit(self)
        blueBox2.setText("0")
        layout.addWidget(blueBox2, 4,2)
        blueBox3 = QLineEdit(self)
        blueBox3.setText("0")
        layout.addWidget(blueBox3, 4,3)
        blueBox4 = QLineEdit(self)
        blueBox4.setText("0")
        layout.addWidget(blueBox4, 4,4)
        blueBox5 = QLineEdit(self)
        blueBox5.setText("0")
        layout.addWidget(blueBox5, 4,5)

        peltLabel = QLabel("Peltier")
        layout.addWidget(peltLabel, 5, 0)

        peltierButton = QPushButton("ON")
        peltierButton.setCheckable(True)
        peltierButton.setChecked(False)
        layout.addWidget(peltierButton, 5, 1)
        tempLabel = QLabel("Temp (15-40C)")
        layout.addWidget(tempLabel, 6, 0)

        peltBox1 = QLineEdit(self)

        peltBox1.setText("25")
        layout.addWidget(peltBox1, 6,1)

        peltBox2 = QLineEdit(self)
        peltBox2.setText("25")
        layout.addWidget(peltBox2, 6,2)

        peltBox3 = QLineEdit(self)
        peltBox3.setText("25")
        layout.addWidget(peltBox3, 6,3)

        peltBox4 = QLineEdit(self)
        peltBox4.setText("25")
        layout.addWidget(peltBox4, 6,4)


        peltBox5 = QLineEdit(self)
        peltBox5.setText("25")
        layout.addWidget(peltBox5, 6,5)

        durLabel  = QLabel("durat (ms)")
        layout.addWidget(durLabel, 7, 0)

        durBox1 = QLineEdit(self)
        durBox1.setText("500")
        layout.addWidget(durBox1, 7,1)

        durBox2 = QLineEdit(self)
        durBox2.setText("500")
        layout.addWidget(durBox2, 7,2)

        durBox3 = QLineEdit(self)
        durBox3.setText("500")
        layout.addWidget(durBox3, 7,3)

        durBox4 = QLineEdit(self)
        durBox4.setText("500")
        layout.addWidget(durBox4, 7,4)

        durBox5 = QLineEdit(self)
        durBox5.setText("500")
        layout.addWidget(durBox5, 7,5)

        itiLabel = QLabel("iti(ms)")
        layout.addWidget(itiLabel, 8, 0)
        itiBox1 = QLineEdit(self)
        itiBox1.setText("500")
        layout.addWidget(itiBox1, 8,1)

        repLabel = QLabel("repetitions")
        layout.addWidget(repLabel,8,2)
        rep1Box = QLineEdit(self)
        rep1Box.setText('2')
        layout.addWidget(rep1Box,8,3)

		
        layout.addWidget(runButton,9,0)
		
        lcd = QLCDNumber()
        lcd.setGeometry(30, 30, 800, 600)
        lcd.setWindowTitle('Time')
        lcd.setSegmentStyle(QLCDNumber.Flat)
     
        layout.addWidget(lcd,10,0)

        self.Protocol.setLayout(layout)



        def runUpdate(self):
            totalDur = 0
            basePath = '/home/pi/flypi_test/videos/'
            folderName = "protocols"
            timenow = time.strftime('%Y-%m-%d-%H-%M-%S')
            recFileName = 'video_'+ timenow + '.h264'
            #print(self.basePath)
            if not os.path.exists(basePath+folderName+'/'):
                #if not, create it:
                os.makedirs(basePath+folderName+'/')
                os.chown(basePath+folderName+'/', 1000, 1000)

            if runButton.isChecked():
                print("run")
                allcom = list()
                if ringButton.isChecked():
                    allcom.append('R1')
                    allcom.append(str('RR '+ str(redBox1.text())))
                    allcom.append(str('RG '+ str(greenBox1.text())))
                    allcom.append(str('RB '+ str(blueBox1.text())))

                if peltierButton.isChecked():
                    allcom.append('P1')
                    allcom.append(str('ST '+str(peltBox1.text())))
                    allcom.append(str('GT'))

                allcom.append(str('TW '+str(durBox1.text())))
                totalDur = totalDur + int(durBox1.text())

                if ringButton.isChecked():
                    allcom.append('R1')
                    allcom.append(str('RR '+ str(redBox2.text())))
                    allcom.append(str('RG '+ str(greenBox2.text())))
                    allcom.append(str('RB '+ str(blueBox2.text())))

                if peltierButton.isChecked():
                    allcom.append('P1')
                    allcom.append(str('ST '+str(peltBox2.text())))
                    #allcom.append(str('GT'))

                allcom.append(str('TW '+str(durBox2.text())))
                totalDur = totalDur + int(durBox2.text())

                if ringButton.isChecked():
                    allcom.append('R1')
                    allcom.append(str('RR '+ str(redBox3.text())))
                    allcom.append(str('RG '+ str(greenBox3.text())))
                    allcom.append(str('RB '+ str(blueBox3.text())))

                if peltierButton.isChecked():
                    allcom.append('P1')
                    allcom.append(str('ST '+str(peltBox3.text())))
                    #allcom.append(str('GT'))

                allcom.append(str('TW '+str(durBox3.text())))
                totalDur = totalDur + int(durBox3.text())

                if ringButton.isChecked():
                    allcom.append('R1')
                    allcom.append(str('RR '+ str(redBox4.text())))
                    allcom.append(str('RG '+ str(greenBox4.text())))
                    allcom.append(str('RB '+ str(blueBox4.text())))

                if peltierButton.isChecked():
                    allcom.append('P1')
                    allcom.append(str('ST '+str(peltBox4.text())))
                    #allcom.append(str('GT'))

                allcom.append(str('TW '+str(durBox4.text())))
                totalDur = totalDur + int(durBox4.text())



                if ringButton.isChecked():
                    allcom.append('R1')
                    allcom.append(str('RR '+ str(redBox5.text())))
                    allcom.append(str('RG '+ str(greenBox5.text())))
                    allcom.append(str('RB '+ str(blueBox5.text())))
                print(peltierButton.isChecked())
                if peltierButton.isChecked():
                    allcom.append('P1')
                    allcom.append(str('ST '+str(peltBox5.text())))
                    #allcom.append(str('GT'))

                allcom.append(str('TW '+str(durBox5.text())))
                totalDur = totalDur + int(durBox5.text())
                allcom.append(str('TW '+str(itiBox1.text())))
                totalDur = totalDur + int(itiBox1.text())

                reps = int(rep1Box.text())
                totalDur = totalDur*reps

                #add 1 sec buffer
                totalDur=totalDur+1000
                #convert milliseconds to seconds
                totalDur = totalDur/1000.0
                if totalDur<2.:
                    totalDur = 2

                if peltierButton.isChecked():
                    allcom = intersperse(allcom, "GT")
                    
                x=1
                print(allcom)
                
                temperature = -999.
                allTemps = list()
                allTimes = list()
                path = create_folder(folderPath="/home/pi/Desktop/flypi_output/",
							  folderName=time.strftime('%Y-%m-%d'))
				
                fh = create_file(filePath = path,
							fileName = "temp_log_"+time.strftime('%Y-%m-%d-%H-%M-%S')+".txt")

				# start camera rec
                #if cam. cameraFlag==1:
                #    print("hrere")
				
                for i in range(reps):
                    if i+1==reps:
                        allcom.append('R0')
                        allcom.append('P0')

                    for command in allcom:

                        haltFlag=1
                        ser.write(str(command+'\n').encode('utf-8'))
                        ser.flush()
                        
                        x=x+1
                        while ser.in_waiting==0:
                            x=x
                        while haltFlag==1:
							
                            test=ser.readline()
                            #lcd.display(x)
                            #print(test[0:-2])
                            if test[0:-2]=='d'.encode('utf-8') or test[0:-2]=='Ready'.encode('utf-8'):
                                haltFlag=0
                                lcd.display(temperature)
                            else:
								
                                temperature = float(test[0:-2]) 
                                fh.write(time.strftime('%Y-%m-%d-%H-%M-%S') + (','))
                                fh.write(str(temperature)+(',\r\n'))					
                                allTimes.append(time.strftime('%Y-%m-%d-%H-%M-%S'))
                                allTemps.append(temperature)
                                
                                
                                
                            
                print("done")
                fh.close()
                runButton.setChecked(False)
				
            return

        runButton.clicked.connect(runUpdate)
