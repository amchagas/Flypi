from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

try:
    import serial
    serialAvail = True

except ImportError:
    serialAvail = False
    print ("serial module not available!")
    print ("user interface will not control flypi!")


loadSerial = 0

if loadSerial == 1:
    if serialAvail == True:
        # for Arduino Uno from RPi
        #self.ser = serial.Serial('/dev/ttyACM0', 115200)
        # for Arduino Nano from RPi
        ser = serial.Serial('/dev/ttyUSB0', 115200)



#from camera_qt import camera

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("FlyPi User Interface:")
        #styleLabel.setBuddy(styleComboBox)

        #self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        #self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createCamera()
        self.createRing()
        self.createLEDs()
        #self.createTopRightGroupBox()
        #self.createBottomLeftTabWidget()
        #self.createBottomRightGroupBox()
        #self.createProgressBar()

        #styleComboBox.activated[str].connect(self.changeStyle)

        #self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.midLeftGroupBox.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        #topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        #topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomLeftGroupBox, 3, 0)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("FlyPi app")
        #self.changeStyle('Fusion')

    #def changeStyle(self, styleName):
    #    QApplication.setStyle(QStyleFactory.create(styleName))
    #    self.changePalette()

    #def changePalette(self):
    #    if (self.useStylePaletteCheckBox.isChecked()):
    #        QApplication.setPalette(QApplication.style().standardPalette())
    #    else:
    #        QApplication.setPalette(self.originalPalette)

    #def advanceProgressBar(self):
    #    curVal = self.progressBar.value()
    #    maxVal = self.progressBar.maximum()
    #    self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createLEDs(self):
        self.bottomLeftGroupBox = QGroupBox("LEDs")

        L1onButton = QPushButton("LED1 ON")
        L1onButton.setCheckable(True)
        L1onButton.setChecked(False)

        zap1Button = QPushButton("ZAP Led1")
        zap1Button.setCheckable(False)
        zap1Button.setChecked(False)

        L1Label = QLabel("Brightness:")
        L1Slider = QSlider(Qt.Horizontal,self.bottomLeftGroupBox)
        L1Slider.setMinimum(0)
        L1Slider.setMaximum(100)
        L1Slider.setValue(10)
        L1Slider.setTickPosition(QSlider.TicksBelow)
        L1Slider.setTickInterval(1)

        L1ZapLabel = QLabel("L1 Zap Brightness:")
        L1ZapSlider = QSlider(Qt.Horizontal,self.bottomLeftGroupBox)
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
        L2Slider = QSlider(Qt.Horizontal,self.bottomLeftGroupBox)
        L2Slider.setMinimum(0)
        L2Slider.setMaximum(100)
        L2Slider.setValue(10)
        L2Slider.setTickPosition(QSlider.TicksBelow)
        L2Slider.setTickInterval(1)

        L2ZapLabel = QLabel("L2 Zap Brightness:")
        L2ZapSlider = QSlider(Qt.Horizontal,self.bottomLeftGroupBox)
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
        self.bottomLeftGroupBox.setLayout(layout)


        def L1onUpdate(self):
            if L1onButton.isChecked():
                if loadSerial == 1:
                    ser.println("L11")
                print("ON")
            else:
                if loadSerial == 1:
                    ser.println("L10")
                print("OFF")

        def L2onUpdate(self):
            if L2onButton.isChecked():
                if loadSerial == 1:
                    ser.println("L21")
                print("ON")
            else:
                if loadSerial == 1:
                    ser.println("L20")
                print("OFF")

        def L1SliUpdate(self):
            print(L1Slider.value())
            if loadSerial == 1:
                ser.println("L12")
                ser.println(L1Slider.value())

        def L2SliUpdate(self):
            print(L2Slider.value())
            if loadSerial == 1:
                ser.println("L22")
                ser.println(L2Slider.value())

        def zap1Update(self):
            if zap1Button.isChecked():
                if L1onButton.isChecked():
                    if loadSerial == 1:

                        ser.println("zap1test")

        def zap2Update(self):
            if zap2Button.isChecked():
                if L2onButton.isChecked():
                    if loadSerial == 1:
                        ser.println("zap2test")

        L1onButton.clicked.connect(L1onUpdate)
        L1Slider.valueChanged.connect(L1SliUpdate)
        zap1Button.clicked.connect(zap1Update)

        L2onButton.clicked.connect(L2onUpdate)
        L2Slider.valueChanged.connect(L2SliUpdate)

        zap2Button.clicked.connect(zap2Update)




        return

    def createRing(self):
        self.topRightGroupBox = QGroupBox("Ring")

        onButton = QPushButton("Ring ON")
        onButton.setCheckable(True)
        onButton.setChecked(False)

        zapButton = QPushButton("ZAP NOW!")
        zapButton.setCheckable(False)
        zapButton.setChecked(False)

        redLabel = QLabel("RED:")
        redSlider = QSlider(Qt.Horizontal,self.topRightGroupBox)
        redSlider.setMinimum(0)
        redSlider.setMaximum(100)
        redSlider.setValue(10)
        redSlider.setTickPosition(QSlider.TicksBelow)
        redSlider.setTickInterval(1)


        greenLabel = QLabel("GREEN:")
        greenSlider = QSlider(Qt.Horizontal,self.topRightGroupBox)
        greenSlider.setMinimum(0)
        greenSlider.setMaximum(100)
        greenSlider.setValue(10)
        greenSlider.setTickPosition(QSlider.TicksBelow)
        greenSlider.setTickInterval(1)


        blueLabel = QLabel("BLUE:")
        blueSlider = QSlider(Qt.Horizontal,self.topRightGroupBox)
        blueSlider.setMinimum(0)
        blueSlider.setMaximum(100)
        blueSlider.setValue(10)
        blueSlider.setTickPosition(QSlider.TicksBelow)
        blueSlider.setTickInterval(1)

        allLabel = QLabel("ALL:")
        allSlider = QSlider(Qt.Horizontal,self.topRightGroupBox)
        allSlider.setMinimum(0)
        allSlider.setMaximum(100)
        allSlider.setValue(10)
        allSlider.setTickPosition(QSlider.TicksBelow)
        allSlider.setTickInterval(1)


        redZapLabel  = QLabel("RED ZAP:")
        redZapBox = QLineEdit(self)

        greenZapLabel  = QLabel("GREEN ZAP:")
        greenZapBox = QLineEdit()

        blueZapLabel  = QLabel("BLUE ZAP:")
        blueZapBox = QLineEdit()

        durZapLabel  = QLabel("ZAP Duration (ms):")
        durZapBox = QLineEdit()

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

        self.topRightGroupBox.setLayout(layout)

        def redUpdate(self):
            print(redSlider.value())
            if loadSerial == 1:
                ser.println("RR")
                ser.println(redSlider.value())

        def greenUpdate(self):
            print(greenSlider.value())
            if loadSerial == 1:
                ser.println("RG")
                ser.println(greenSlider.value())

        def blueUpdate(self):
            print(blueSlider.value())
            if loadSerial == 1:
                ser.println("RB")
                ser.println(blueSlider.value())

        def allUpdate(self):
            print(allSlider.value())
            redSlider.setValue(allSlider.value())
            greenSlider.setValue(allSlider.value())
            blueSlider.setValue(allSlider.value())
            if loadSerial == 1:
                ser.println(redSlider.value())
                ser.println(greenSlider.value())
                ser.println(blueSlider.value())

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
                    ser.println(redZapBox.text())
                    ser.println(greenZapBox.text())
                    ser.println(blueZapBox.text())

                    ser.println(durZapBox.text())

                    ser.println(redSlider.value())
                    ser.println(greenSlider.value())
                    ser.println(blueSlider.value())

        def onUpdate(self):
            if onButton.isChecked():
                if loadSerial == 1:
                    ser.println("R1")
                print("ring ON")
            else:
                if loadSerial == 1:
                    ser.println("R0")
                print("ring OFF")

        #redZapBox.valueChanged.connect(redZapUpdate)
        onButton.clicked.connect(onUpdate)
        zapButton.clicked.connect(zapUpdate)
        redSlider.valueChanged.connect(redUpdate)
        greenSlider.valueChanged.connect(greenUpdate)
        blueSlider.valueChanged.connect(blueUpdate)
        allSlider.valueChanged.connect(allUpdate)


    def createCamera(self):

        self.topLeftGroupBox = QGroupBox("Camera")


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
        zoomSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        zoomSlider.setMinimum(0)
        zoomSlider.setMaximum(10)
        zoomSlider.setValue(0)
        zoomSlider.setTickPosition(QSlider.TicksBelow)
        zoomSlider.setTickInterval(1)

        binLabel = QLabel("Binning:")
        binSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        binSlider.setMinimum(0)
        binSlider.setMaximum(4)
        binSlider.setValue(0)
        binSlider.setTickPosition(QSlider.TicksBelow)
        binSlider.setTickInterval(1)

        windowLabel = QLabel("Window Size:")
        windowSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        windowSlider.setMinimum(10)
        windowSlider.setMaximum(800)
        windowSlider.setValue(240)
        windowSlider.setTickPosition(QSlider.TicksBelow)
        windowSlider.setTickInterval(5)

        fpsLabel = QLabel("Frames p/ second:")
        fpsSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        fpsSlider.setMinimum(15)
        fpsSlider.setMaximum(90)
        fpsSlider.setValue(15)
        fpsSlider.setTickPosition(QSlider.TicksBelow)
        fpsSlider.setTickInterval(5)

        exposureLabel = QLabel("Exposure:")
        exposureSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        exposureSlider.setValue(0)
        exposureSlider.setMinimum(-10)
        exposureSlider.setMaximum(10)
        exposureSlider.setTickPosition(QSlider.TicksBelow)
        exposureSlider.setTickInterval(1)

        horLabel = QLabel("Horizontal offset:")
        horSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        horSlider.setValue(0)
        horSlider.setMinimum(-10)
        horSlider.setMaximum(10)
        horSlider.setTickPosition(QSlider.TicksBelow)
        horSlider.setTickInterval(1)

        verLabel = QLabel("Vertical offset:")
        verSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        verSlider.setValue(0)
        verSlider.setMinimum(-10)
        verSlider.setMaximum(10)
        verSlider.setTickPosition(QSlider.TicksBelow)
        verSlider.setTickInterval(1)

        rotationLabel = QLabel("Rotation:")
        rotationSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        rotationSlider.setValue(0)
        rotationSlider.setMinimum(0)
        rotationSlider.setMaximum(3)
        rotationSlider.setTickPosition(QSlider.TicksBelow)
        rotationSlider.setTickInterval(1)

        brightnessLabel = QLabel("Brightness:")
        brightnessSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
        brightnessSlider.setValue(50)
        brightnessSlider.setMinimum(0)
        brightnessSlider.setMaximum(100)
        brightnessSlider.setTickPosition(QSlider.TicksBelow)
        brightnessSlider.setTickInterval(5)

        contrastLabel = QLabel("Contrast:")
        contrastSlider = QSlider(Qt.Horizontal,self.topLeftGroupBox)
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

        self.topLeftGroupBox.setLayout(layout)

        def onUpdate(self):
            if onButton.isChecked():
                print("ON")
            else:
                print("OFF")

        onButton.clicked.connect(onUpdate)

        def resUpdate(self):
            print("here")
            print(resolutionMenu.currentText())

        def wbUpdate(self):
            print("here")
            print(wbMenu.currentText())

        def modeUpdate(self):
            print("here")
            print(modeMenu.currentText())

        def colourUpdate(self):
            print("here")
            print(colourMenu.currentText())


        def rotationUpdate(self):
            print("here")
            print(rotationSlider.value())

        def zoomUpdate(self):
            print("here")
            print(zoomSlider.value())

        def verUpdate(self):
            print("here")
            print(verSlider.value())

        def horUpdate(self):
            print("here")
            print(horSlider.value())

        def windowUpdate(self):
            print("here")
            print(windowSlider.value())

        def binUpdate(self):
            print("here")
            print(binSlider.value())

        def exposureUpdate(self):
            print("here")
            print(exposureSlider.value())

        def brightnessUpdate(self):
            print("here")
            print(brightnessSlider.value())

        def contrastUpdate(self):
            print("here")
            print(contrastSlider.value())

        def fpsUpdate(self):
            print("here")
            print(fpsSlider.value())


        rotationSlider.valueChanged.connect(rotationUpdate)
        fpsSlider.valueChanged.connect(fpsUpdate)
        zoomSlider.valueChanged.connect(zoomUpdate)
        verSlider.valueChanged.connect(verUpdate)
        horSlider.valueChanged.connect(horUpdate)
        windowSlider.valueChanged.connect(windowUpdate)
        binSlider.valueChanged.connect(binUpdate)
        exposureSlider.valueChanged.connect(exposureUpdate)
        brightnessSlider.valueChanged.connect(brightnessUpdate)
        contrastSlider.valueChanged.connect(contrastUpdate)



        modeMenu.activated.connect(modeUpdate)
        wbMenu.activated.connect(wbUpdate)
        colourMenu.activated.connect(colourUpdate)
        resolutionMenu.activated.connect(resUpdate)

    # def createTopRightGroupBox(self):
    #     self.topRightGroupBox = QGroupBox("Group 2")
    #
    #     defaultPushButton = QPushButton("Default Push Button")
    #     defaultPushButton.setDefault(True)
    #
    #     togglePushButton = QPushButton("Toggle Push Button")
    #     togglePushButton.setCheckable(True)
    #     togglePushButton.setChecked(True)
    #
    #     flatPushButton = QPushButton("Flat Push Button")
    #     flatPushButton.setFlat(True)
    #
    #     layout = QVBoxLayout()
    #     layout.addWidget(defaultPushButton)
    #     layout.addWidget(togglePushButton)
    #     layout.addWidget(flatPushButton)
    #     layout.addStretch(1)
    #     self.topRightGroupBox.setLayout(layout)

    # def createBottomLeftTabWidget(self):
    #     self.bottomLeftTabWidget = QTabWidget()
    #     self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
    #             QSizePolicy.Ignored)
    #
    #     tab1 = QWidget()
    #     tableWidget = QTableWidget(10, 10)
    #
    #     tab1hbox = QHBoxLayout()
    #     tab1hbox.setContentsMargins(5, 5, 5, 5)
    #     tab1hbox.addWidget(tableWidget)
    #     tab1.setLayout(tab1hbox)
    #
    #     tab2 = QWidget()
    #     textEdit = QTextEdit()
    #
    #     textEdit.setPlainText("Twinkle, twinkle, little star,\n"
    #                           "How I wonder what you are.\n"
    #                           "Up above the world so high,\n"
    #                           "Like a diamond in the sky.\n"
    #                           "Twinkle, twinkle, little star,\n"
    #                           "How I wonder what you are!\n")
    #
    #     tab2hbox = QHBoxLayout()
    #     tab2hbox.setContentsMargins(5, 5, 5, 5)
    #     tab2hbox.addWidget(textEdit)
    #     tab2.setLayout(tab2hbox)
    #
    #     self.bottomLeftTabWidget.addTab(tab1, "&Table")
    #     self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    # def createBottomRightGroupBox(self):
    #     self.bottomRightGroupBox = QGroupBox("Group 3")
    #     self.bottomRightGroupBox.setCheckable(True)
    #     self.bottomRightGroupBox.setChecked(True)
    #
    #     lineEdit = QLineEdit('s3cRe7')
    #     lineEdit.setEchoMode(QLineEdit.Password)
    #
    #     spinBox = QSpinBox(self.bottomRightGroupBox)
    #     spinBox.setValue(50)
    #
    #     dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
    #     dateTimeEdit.setDateTime(QDateTime.currentDateTime())
    #
    #     slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
    #     slider.setValue(40)
    #
    #     scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
    #     scrollBar.setValue(60)
    #
    #     dial = QDial(self.bottomRightGroupBox)
    #     dial.setValue(30)
    #     dial.setNotchesVisible(True)
    #
    #     layout = QGridLayout()
    #     layout.addWidget(lineEdit, 0, 0, 1, 2)
    #     layout.addWidget(spinBox, 1, 0, 1, 2)
    #     layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
    #     layout.addWidget(slider, 3, 0)
    #     layout.addWidget(scrollBar, 4, 0)
    #     layout.addWidget(dial, 3, 1, 2, 1)
    #     layout.setRowStretch(5, 1)
    #     self.bottomRightGroupBox.setLayout(layout)
    #
    # def createProgressBar(self):
    #     self.progressBar = QProgressBar()
    #     self.progressBar.setRange(0, 10000)
    #     self.progressBar.setValue(0)
    #
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.advanceProgressBar)
    #     timer.start(1000)

    #callback functions


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
