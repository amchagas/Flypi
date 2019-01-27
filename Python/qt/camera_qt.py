from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


class Camera():

    #def __init__(self):
    #    self.createCamera = createCamera()
    #    return


    def createCamera(self):
        try:
            # picamera module
            import picamera
            cam1=1
            self.cam = picamera.PiCamera()
            self.cam.led = False
            self.cam.exposure_mode = "fixedfps"
            self.cam.exposure_compensation = 0
            self.cam.brightness = 50
            self.cam.awb_mode = "auto"
            self.bitRate = 17000000

        except ImportError:
            cam1=0
            #picameraAvail = False
            print ("picamera module not available!")

        self.Camera = QGroupBox("Camera")


        onButton = QPushButton("ON")
        onButton.setCheckable(True)
        onButton.setChecked(False)



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
        colourMenu.addItems(["None", "Red", "Green", "Blue"])

        zoomLabel = QLabel("Zoom:")
        zoomSlider = QSlider(Qt.Horizontal,self.Camera)
        zoomSlider.setMinimum(0)
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

        self.Camera.setLayout(layout)

        def onUpdate(self):
            if onButton.isChecked():

                print ("cam on")
                if cam1==1:
                    res = self.resVar.get()
                    size = self.sizeVar.get()
                    self.cam.resolution = (2592, 1944)
                    self.cam.preview_window = (0, 0, size, size)
                    self.zoomVar.set(1)
                    self.horVar.set(0)
                    self.verVar.set(0)
                    self.cam.zoom = (self.horVar.get(),
                               self.verVar.get(),
                               self.zoomVar.get(),
                               self.zoomVar.get())
                    self.cam.start_preview()

                    self.cam.preview.fullscreen = False
                    #wait a second so the camera adjusts
                    time.sleep(1)
            else:
                print("OFF")
                if cam1==1:
                    self.cam.stop_preview()

        onButton.clicked.connect(onUpdate)

        def resUpdate(self):
            print(resolutionMenu.currentText())
            text = resolutionMenu.currentText()
            index = text.find('x')
            if cam1==1:
                self.cam.resolution = (int(text[0:index]),int(text[index+1:]))

        def wbUpdate(self):
            print(wbMenu.currentText())
            if cam1==1:
                if wbMenu.currentText() == "green":
                    self.cam.awb_mode = "off"
                    self.cam.awb_gains = (1, 1)
                elif wbMenu.currentText() == "red":
                    self.cam.awb_mode = "off"
                    self.cam.awb_gains = (8.0, 0.9)
                elif wbMenu.currentText() == "blue":
                    self.cam.awb_mode = "off"
                    self.cam.awb_gains = (0.9, 8.0)
                elif wbMenu.currentText() == "off":
                    self.cam.awb_mode = "off"
                else:
                    self.cam.awb_mode = wbMenu.currentText()


        def modeUpdate(self):
            print("here")
            print(modeMenu.currentText())

        def colourUpdate(self):
            print("here")
            print(colourMenu.currentText())


        def rotationUpdate(self):
            print(rotationSlider.value())
            if cam1==1:
                self.cam.rotation = (rotationSlider.value())


        def zoomUpdate(self):
            print(zoomSlider.value())
            if zoomSlider.value()==1:
                horSlider.setValue(5)
                verSlider.setValue(5)
            if cam1==1:
                if ZoomSlider.value()==1:
                    self.cam.zoom = (0, 0, 1, 1)
                    horSlider.setValue(0)
                    verSlider.setValue(0)
                else:
                    zoomSide = 1 / zoomSlider.Value()
                    edge = (1 - zoomSide)#*0.5
                    self.cam.zoom = ((horSlider.value() / 100.0) * edge,
                                   ( verSlider.value() / 100.0) * edge,
                                   1 / zoomSlider.Value(),
                                   1 / zoomSlider.Value())

        #def verUpdate(self):
        #    print(verSlider.value())

        #def horUpdate(self):
        #    print(horSlider.value())

        def windowUpdate(self):
            print(windowSlider.value())
            if cam1==1:
                self.cam.preview_window = (0, 0, windowSlider.value(), windowSlider.value())

        def binUpdate(self):
            print("here")
            print(binSlider.value())

        def exposureUpdate(self):
            print(exposureSlider.value())
            if cam1==1:
                self.cam.exposure_compensation = (exposureSlider.value())

        def brightnessUpdate(self):
            print(brightnessSlider.value())
            if cam1==1:
                self.cam.brightness = (brightnessSlider.value())

        def contrastUpdate(self):
            print(contrastSlider.value())
            if cam1==1:
                self.cam.contrast = (contrastSlider.value())

        def fpsUpdate(self):
            print(fpsSlider.value())
            if cam1==1:
                self.cam.framerate = (fpsSlider.value())



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



        modeMenu.activated.connect(modeUpdate)
        wbMenu.activated.connect(wbUpdate)
        colourMenu.activated.connect(colourUpdate)
        resolutionMenu.activated.connect(resUpdate)


        return self.Camera
    #callback functions
