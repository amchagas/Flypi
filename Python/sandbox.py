from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

#from camera_qt import Camera
##from ring_qt import Ring
#import struct
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
        primer = 'TW 1;'


while ser.in_waiting==0:
    #print("wait1")
    x=1
print("setup done")
dummie = ser.readline()
#print('Ready'.encode('utf-8'))
#print(dummie[0:-2])
#print (dummie[0:-2]=='Ready'.encode('utf-8'))

#print(ser.readline())

runflag = 0
allcom = ['P1','TW 500','P0','TW 500',
          'P1','TW 500','P0','TW 1500',
          'P1','TW 500','P0','TW 1500',
          'P1','TW 500','P0','TW 500',
]
x=1
for command in allcom:

    haltFlag=1
    print(command)
    ser.write(str(command+'\n').encode('utf-8'))
    ser.flush()
    x=x+1


    while ser.in_waiting==0:
        x=x
    while haltFlag==1:
        test=ser.readline()
        if test[0:-2]=='d'.encode('utf-8'):
            haltFlag=0
