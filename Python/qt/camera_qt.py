from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog)

import time
import os
import subprocess

class Camera():

    #def __init__(self):
    #    self.createCamera = createCamera()
    #    return


    def createCamera(self):
        try:
            # picamera module
            import picamera
            cam1=1
            cam = picamera.PiCamera()
            cam.led = False
            cam.exposure_mode = "fixedfps"
            cam.exposure_compensation = 0
            cam.brightness = 50
            cam.awb_mode = "auto"
            bitRate = 17000000
            basePath = '/home/pi/Desktop/flypi_output/'

        except ImportError:
            cam1=0
            #picameraAvail = False
            print ("picamera module not available!")

        self.Camera = QGroupBox("Camera")


        onButton = QPushButton("ON")
        onButton.setCheckable(True)
        onButton.setChecked(False)
        
        convButton = QPushButton("to AVI")
        convButton.setCheckable(False)
        convButton.setChecked(False)
        
        tlButton = QPushButton("Time Lapse")
        tlButton.setCheckable(False)
        tlButton.setChecked(False)

        snapButton = QPushButton("Photo")
        snapButton.setCheckable(False)
        snapButton.setChecked(False)
        
        recButton = QPushButton("REC video")
        recButton.setCheckable(False)
        recButton.setChecked(False)
        
        resolutionLabel = QLabel("Resolution:")

        resolutionMenu = QComboBox()
        resolutionMenu.addItems(['2592x1944', '1920x1080',
                                '1296x972', '1296x730', '640x480'])

        wbLabel = QLabel("White balance:")
        wbMenu = QComboBox()
        wbMenu.addItems(['off', 'auto', 'green',
                           'red', 'blue', 'sunlight', 'cloudy',
                           'shade', 'tungsten', 'fluorescent',
                           'incandescent','flash', 'horizon'])


        modeLabel = QLabel("Mode:")
        modeMenu = QComboBox()
        modeMenu.addItems(["none", "negative", "solarize", "sketch",
                            "denoise", "emboss", "oilpaint", "hatch",
                            "gpen", "pastel", "watercolor", "film",
                            "blur", "saturation", "colorswap",
                            "washedout","posterise", "colorpoint",
                            "colorbalance", "cartoon",
                            "deinterlace1", "deinterlace2"])

        colourLabel = QLabel("Colour Effect:")
        colourMenu = QComboBox()
        colourMenu.addItems(["None","BW", "Red", "Green", "Blue"])

        zoomLabel = QLabel("Zoom:")
        zoomSlider = QSlider(Qt.Horizontal,self.Camera)
        zoomSlider.setMinimum(1)
        zoomSlider.setMaximum(10)
        zoomSlider.setValue(0)
        zoomSlider.setTickPosition(QSlider.TicksBelow)
        zoomSlider.setTickInterval(1)

        binLabel = QLabel("Binning:")
        binSlider = QSlider(Qt.Horizontal,self.Camera)
        binSlider.setMinimum(0)
        binSlider.setMaximum(4)
        binSlider.setValue(0)
        binSlider.setTickPosition(QSlider.TicksBelow)
        binSlider.setTickInterval(1)

        windowLabel = QLabel("Window Size:")
        windowSlider = QSlider(Qt.Horizontal,self.Camera)
        windowSlider.setMinimum(10)
        windowSlider.setMaximum(800)
        windowSlider.setValue(240)
        windowSlider.setTickPosition(QSlider.TicksBelow)
        windowSlider.setTickInterval(5)

        fpsLabel = QLabel("Frames p/ second:")
        fpsSlider = QSlider(Qt.Horizontal,self.Camera)
        fpsSlider.setMinimum(15)
        fpsSlider.setMaximum(90)
        fpsSlider.setValue(15)
        fpsSlider.setTickPosition(QSlider.TicksBelow)
        fpsSlider.setTickInterval(5)

        exposureLabel = QLabel("Exposure:")
        exposureSlider = QSlider(Qt.Horizontal,self.Camera)
        exposureSlider.setValue(0)
        exposureSlider.setMinimum(-10)
        exposureSlider.setMaximum(10)
        exposureSlider.setTickPosition(QSlider.TicksBelow)
        exposureSlider.setTickInterval(1)

        horLabel = QLabel("Horizontal offset:")
        horSlider = QSlider(Qt.Horizontal,self.Camera)
        horSlider.setValue(0)
        horSlider.setMinimum(-10)
        horSlider.setMaximum(10)
        horSlider.setTickPosition(QSlider.TicksBelow)
        horSlider.setTickInterval(1)

        verLabel = QLabel("Vertical offset:")
        verSlider = QSlider(Qt.Horizontal,self.Camera)
        verSlider.setValue(0)
        verSlider.setMinimum(-10)
        verSlider.setMaximum(10)
        verSlider.setTickPosition(QSlider.TicksBelow)
        verSlider.setTickInterval(1)

        rotationLabel = QLabel("Rotation:")
        rotationSlider = QSlider(Qt.Horizontal,self.Camera)
        rotationSlider.setValue(0)
        rotationSlider.setMinimum(0)
        rotationSlider.setMaximum(3)
        rotationSlider.setTickPosition(QSlider.TicksBelow)
        rotationSlider.setTickInterval(1)

        brightnessLabel = QLabel("Brightness:")
        brightnessSlider = QSlider(Qt.Horizontal,self.Camera)
        brightnessSlider.setValue(50)
        brightnessSlider.setMinimum(0)
        brightnessSlider.setMaximum(100)
        brightnessSlider.setTickPosition(QSlider.TicksBelow)
        brightnessSlider.setTickInterval(5)

        contrastLabel = QLabel("Contrast:")
        contrastSlider = QSlider(Qt.Horizontal,self.Camera)
        contrastSlider.setValue(50)
        contrastSlider.setMinimum(0)
        contrastSlider.setMaximum(100)
        contrastSlider.setTickPosition(QSlider.TicksBelow)
        contrastSlider.setTickInterval(5)

        recDurLabel  = QLabel("record Duration (sec)")
        recDurBox = QLineEdit(self)
        recDurBox.setText("1")

        tlDurLabel  = QLabel("TL Duration (sec)")
        tlDurBox = QLineEdit(self)
        tlDurBox.setText("1")
        
        tlIntLabel  = QLabel("interval between images (sec)")
        tlIntBox = QLineEdit(self)
        tlIntBox.setText("1")
        
        
        
        # add all widgets to a grid
        layout = QGridLayout()
        layout.addWidget(onButton, 1, 0)


        layout.addWidget(resolutionLabel,0,1)
        layout.addWidget(resolutionMenu,1,1)

        layout.addWidget(wbLabel,0, 2)
        layout.addWidget(wbMenu,1, 2)

        layout.addWidget(modeLabel,0, 3)
        layout.addWidget(modeMenu,1, 3)

        layout.addWidget(colourLabel,0, 4)
        layout.addWidget(colourMenu,1, 4)

        layout.addWidget(zoomLabel,2, 1)
        layout.addWidget(zoomSlider,3, 1)

        layout.addWidget(binLabel,4, 0)
        layout.addWidget(binSlider,5, 0)

        layout.addWidget(windowLabel,2, 3)
        layout.addWidget(windowSlider,3, 3)

        layout.addWidget(fpsLabel,2, 4)
        layout.addWidget(fpsSlider,3, 4)

        layout.addWidget(exposureLabel,4, 1)
        layout.addWidget(exposureSlider,5, 1)

        layout.addWidget(rotationLabel,2,0 )
        layout.addWidget(rotationSlider,3, 0)

        layout.addWidget(verLabel,2, 2)
        layout.addWidget(verSlider,3, 2)

        layout.addWidget(horLabel,4, 2)
        layout.addWidget(horSlider,5, 2)

        layout.addWidget(brightnessLabel,4, 3)
        layout.addWidget(brightnessSlider,5, 3)

        layout.addWidget(contrastLabel,4, 4)
        layout.addWidget(contrastSlider,5, 4)
        layout.addWidget(convButton,6,0)
        layout.addWidget(tlButton,6,1)
        layout.addWidget(snapButton,7,1)
        layout.addWidget(recButton,8,1)
        
        layout.addWidget(recDurBox, 8,2)
        layout.addWidget(recDurLabel, 8, 3)
        layout.addWidget(tlDurBox, 6,2)
        layout.addWidget(tlDurLabel, 6, 3)
        layout.addWidget(tlIntBox, 7,2)
        layout.addWidget(tlIntLabel, 7, 3)
        
        self.Camera.setLayout(layout)
        

        def onUpdate():
            if onButton.isChecked():

                print ("cam on")
                if cam1==1:
                    res = resUpdate()
                    size = windowSlider.value()
                    cam.resolution = (res[0],res[1])
                    cam.preview_window = (0, 0, size, size)
                    zoomSlider.setValue(1)
                    horSlider.setValue(0)
                    verSlider.setValue(0)
                    cam.zoom = (horSlider.value(),
                                verSlider.value(),
                                zoomSlider.value(),
                                zoomSlider.value())
                    cam.start_preview()

                    cam.preview.fullscreen = False
                    #wait a second so the camera adjusts
                    time.sleep(1)
            else:
                print("OFF")
                if cam1==1:
                    cam.stop_preview()

        

        def resUpdate():
            
            text = resolutionMenu.currentText()
            index = text.find('x')
            values = [int(text[0:index]),int(text[index+1:])]
            if cam1==1:
                cam.resolution = (int(text[0:index]),int(text[index+1:]))
            
            print(values)
            return values

        def wbUpdate():
            print(wbMenu.currentText())
            if cam1==1:
                if wbMenu.currentText() == "green":
                    cam.awb_mode = "off"
                    cam.awb_gains = (1, 1)
                elif wbMenu.currentText() == "red":
                    cam.awb_mode = "off"
                    cam.awb_gains = (8.0, 0.9)
                elif wbMenu.currentText() == "blue":
                    cam.awb_mode = "off"
                    cam.awb_gains = (0.9, 8.0)
                elif wbMenu.currentText() == "off":
                    cam.awb_mode = "off"
                else:
                    cam.awb_mode = wbMenu.currentText()


        def modeUpdate(self):
            print("here")
            print(modeMenu.currentText())
            if cam1==1:
                if self.cam.image_effect != modeMenu.currentText():
                    self.cam.image_effect = modeMenu.currentText()

        def colourUpdate(self):
            if cam1==1:
                if self.camColEffVal != "":
                    if self.colourMenu.currentText() == "BW":
                        self.cam.color_effects = (128, 128)
                    elif self.colourMenu.currentText() == "RED":
                        self.cam.color_effects = (0, 255)
                    elif self.colourMenu.currentText() == "BLUE":
                        self.cam.color_effects = (255, 0)
                    elif self.colourMenu.currentText() == "GREEN":
                        self.cam.color_effects = (0, 0)
                    else:
                        self.cam.color_effects = None
            #print("here")
            print(colourMenu.currentText())


        def rotationUpdate(self):
            print(rotationSlider.value())
            if cam1==1:
                cam.rotation = (rotationSlider.value())


        def zoomUpdate(self):
            print(zoomSlider.value())
            if zoomSlider.value()==1:
                horSlider.setValue(5)
                verSlider.setValue(5)
            if cam1==1:
                if zoomSlider.value()==1:
                    cam.zoom = (0, 0, 1, 1)
                    horSlider.setValue(0)
                    verSlider.setValue(0)
                elif zoomSlider.value()!=0:                        
                    zoomSide = 1 / zoomSlider.value()
                    edge = (1 - zoomSide)#*0.5
                    cam.zoom = ((horSlider.value() / 100.0) * edge,
                                   ( verSlider.value() / 100.0) * edge,
                                   1 / zoomSlider.value(),
                                   1 / zoomSlider.value())

        def verUpdate(self):
            print(verSlider.value())

        def horUpdate(self):
            print(horSlider.value())

        def windowUpdate(self):
            print(windowSlider.value())
            if cam1==1:
                cam.preview_window = (0, 0, windowSlider.value(), windowSlider.value())

        def binUpdate(self):
            print("here")
            print(binSlider.value())

        def exposureUpdate(self):
            print(exposureSlider.value())
            if cam1==1:
                cam.exposure_compensation = (exposureSlider.value())

        def brightnessUpdate(self):
            print(brightnessSlider.value())
            if cam1==1:
                cam.brightness = (brightnessSlider.value())

        def contrastUpdate(self):
            print(contrastSlider.value())
            if cam1==1:
                cam.contrast = (contrastSlider.value())

        def fpsUpdate(self):
            print(fpsSlider.value())
            if cam1==1:
                cam.framerate = (fpsSlider.value())



        rotationSlider.valueChanged.connect(rotationUpdate)
        fpsSlider.valueChanged.connect(fpsUpdate)
        zoomSlider.valueChanged.connect(zoomUpdate)
        #verSlider.valueChanged.connect(verUpdate)
        #horSlider.valueChanged.connect(horUpdate)
        windowSlider.valueChanged.connect(windowUpdate)
        binSlider.valueChanged.connect(binUpdate)
        exposureSlider.valueChanged.connect(exposureUpdate)
        brightnessSlider.valueChanged.connect(brightnessUpdate)
        contrastSlider.valueChanged.connect(contrastUpdate)



        
        
        def camConv2():

            #opts = dict()
            #opts["filetypes"] = [('h264 files','*.h264'),('all files','.*')]
            #opts["initialdir"] = [self.basePath]

            #fileName = QFileDialog.getOpenFileName()
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","h264 Files (.h264);;Python Files (*.py)", options=options)
            
            if fileName == '':
                print ('no files selected')
                return
            fps = fpsSlider.value()
            fps = "-r" + str(fps)

            print (fileName)
            print ("converting video to avi")
            outname = os.path.splitext(fileName)[0]+".avi"
            lastInd=fileName.rindex("/")
            files = os.listdir(fileName[0:lastInd])
            outCore = outname.rindex("/")
            print ("out:" + outname[outCore:])
            if outname[outCore+1:] in files:
                print ("file is already converted! Skipping...")
                print("done.")
                return
            command = ['MP4Box', '-add', fileName, outname]
            #command = ['ffmpeg', '-i', fileName,"-b",str(self.bitRate) ,"-pix_fmt","nv12","-f:v","-vcodec rawvideo", outname]
            subprocess.call(command,shell=False)
            print("done.")
            return
        
        
        
        
        def camRec(self,dur=None):
            if dur == None:
                dur = self.recDurBox.text()


            videoPath = self.basePath + '/videos/'
            if not os.path.exists(videoPath):
                #if not, create it:
                os.makedirs(videoPath)
                os.chown(videoPath, 1000, 1000)
            #it seems that the raspi-cam doesn't like shooting videos at full res.
            #so the softw. will automatically use a lower resolution for videos
            if resVal == "2592x1944":
                resVar.set ("1920x1080")
                cam.resolution = (1920, 1080)
                if FPSVar.get()<30:
                    FPSVar.set(30)
                print ("impossible to record at 2592X1944,")
                print ("due to camera limitations.")
                print("dropping to next possible resolution")


            print("recording for: " + str(dur) + " secs")
            cam.start_recording(output = videoPath +
                                'video_' +
                                time.strftime('%Y-%m-%d-%H-%M-%S') + '.h264',
                                format = "h264",)
                                #resize = (1920,1080))
            cam.wait_recording(float(dur))
            cam.stop_recording()
            print("done.")
            #here we restore the preview resolution if it was the maximal one.
            if resVal == "2592x1944":
                cam.resolution = (2592, 1944)
            return



        def camTL(self):
                
            dur = tlDurBox.text()
            interval = tlIntBox.text()
            tlPath = basePath + '/time_lapse/'

            #check to see if the time lapse output folder is present:
            if not os.path.exists(tlPath):
                #if not, create it:
                os.makedirs(tlPath)
                os.chown(tlPath, 1000, 1000)

            #get the present time, down to seconds
            tlFold = time.strftime("%Y-%m-%d-%H-%M-%S")

            #make a new folder to store all time lapse photos
            os.makedirs(tlPath + tlFold)
            os.chown(tlPath + tlFold, 1000, 1000)
            #os.chdir(tlPath+tlFold)

            shots = int(int(dur) / int(interval))
            if shots <= 0:
                print("something wrong with time specifications!")
            else:
                print('time lapse:')
                print('number of shots: ' + str(shots))
                for i in range(0, shots):
                    print("TL " + str(i + 1) + "/" + str(shots))
                    self.cam.capture(tlPath + tlFold + "/TL_" + str(i + 1) + ".jpg")
                    time.sleep(float(interval))
                print("done.")
            return
    
        def camSnap(self):
            photoPath = self.basePath + '/snaps/'
            #check to see if the snap output folder is present:
            if not os.path.exists(photoPath):
                #if not, create it:
                os.makedirs(photoPath)
                os.chown(photoPath, 1000, 1000)



            # Camera warm-up time
            time.sleep(1)
            self.cam.capture(photoPath + 'snap_' +
                        time.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg')
            return        
        
        onButton.clicked.connect(onUpdate)
        convButton.clicked.connect(camConv2)
        tlButton.clicked.connect(camTL)
        modeMenu.activated.connect(modeUpdate)
        wbMenu.activated.connect(wbUpdate)
        colourMenu.activated.connect(colourUpdate)
        resolutionMenu.activated.connect(resUpdate)
        

        return self.Camera
    
