from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class camera():

    def createCamera(self):

        self.topLeftGroupBox = QGroupBox("Camera")


        onButton = QPushButton("ON")
        onButton.setCheckable(True)
        onButton.setChecked(False)
        onButton.clicked.connect(self.btnstate)


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
        rotationSlider.setMaximum(270)
        rotationSlider.setTickPosition(QSlider.TicksBelow)
        rotationSlider.setTickInterval(90)

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
    #callback functions

    def btnstate(self):
        print("HERE")
        print(self.onButton.isChecked())
