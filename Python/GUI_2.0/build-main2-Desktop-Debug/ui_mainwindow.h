/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.9.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QScrollBar>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QTabWidget *tabs;
    QWidget *camera;
    QWidget *gridLayoutWidget;
    QGridLayout *cameragrid;
    QVBoxLayout *photolayout;
    QVBoxLayout *contrastlayout;
    QLabel *contrastlabel;
    QLCDNumber *contrastlcd;
    QScrollBar *contrastbar;
    QVBoxLayout *binlayout;
    QLabel *binlabel;
    QLCDNumber *binlcd;
    QScrollBar *binbar;
    QVBoxLayout *cameralabellayout;
    QLabel *cameralabel;
    QVBoxLayout *flipexposurelayout;
    QPushButton *camonbutton;
    QPushButton *to_avibutton;
    QVBoxLayout *resolutionlayout;
    QLabel *resolutionlabel;
    QComboBox *resolutionbox;
    QLabel *whitebalancelabel;
    QComboBox *whitebalancebox;
    QVBoxLayout *exposurelayout;
    QLabel *exposurelabel;
    QLCDNumber *exposurelcd;
    QScrollBar *exposurebar;
    QVBoxLayout *verticallayout;
    QLabel *verticallabel;
    QLCDNumber *verticallcd;
    QScrollBar *verticalbar;
    QVBoxLayout *windowsizelayout;
    QLabel *windowlabel;
    QLCDNumber *windowlcd;
    QScrollBar *windowbar;
    QVBoxLayout *colourlayout;
    QLabel *intervallabel;
    QSpinBox *intervalbox;
    QLabel *durationlabel;
    QSpinBox *durationbox;
    QVBoxLayout *rotationlayout;
    QLabel *rotationlabel;
    QLCDNumber *rotationlcd;
    QScrollBar *rotationbar;
    QVBoxLayout *zoomverticallayout;
    QLabel *zoomlabel;
    QLCDNumber *zoomlcd;
    QScrollBar *zoombar;
    QVBoxLayout *whitebalancelayout;
    QLabel *modelabel;
    QComboBox *modebox;
    QLabel *colourlabel;
    QComboBox *colourbox;
    QVBoxLayout *modelayout;
    QPushButton *photobutton;
    QPushButton *timelapsebutton;
    QPushButton *videobutton;
    QVBoxLayout *fpslayout;
    QLabel *fpslabel;
    QLCDNumber *fpslcd;
    QScrollBar *fpsbar;
    QVBoxLayout *horizontallayout;
    QLabel *horizontallabel;
    QLCDNumber *horizontallcd;
    QScrollBar *horizontalbar;
    QVBoxLayout *intervallayout;
    QCheckBox *autoexposurebox;
    QCheckBox *flipimagebox;
    QVBoxLayout *brightnesslayout;
    QLabel *brightnesslabel;
    QLCDNumber *brightnesslcd;
    QScrollBar *brightnessbar;
    QWidget *lightdevices;
    QFrame *ringframe;
    QWidget *gridLayoutWidget_2;
    QGridLayout *ringgrid_2;
    QVBoxLayout *verticalLayout_9;
    QLabel *led1label;
    QPushButton *led1onbutton;
    QLabel *led1brightlabel;
    QSlider *led1slider;
    QProgressBar *led1brightindicator;
    QLabel *pulsedurationlabel_2;
    QLineEdit *led1pulsebrightness;
    QLabel *pulsedurationlabel;
    QLineEdit *led1pulseduration;
    QPushButton *led1pulsebutton;
    QVBoxLayout *verticalLayout_8;
    QLabel *matrixlabel;
    QPushButton *matrixonbutton;
    QLabel *matbrightlabel;
    QSlider *matrixslider;
    QProgressBar *matbrightindicator;
    QPushButton *matrixpat1;
    QPushButton *matrixpat2;
    QPushButton *matrixpat3;
    QSpacerItem *verticalSpacer_2;
    QVBoxLayout *verticalLayout_10;
    QLabel *led2label;
    QPushButton *led2onbutton;
    QLabel *led2brightlabel_2;
    QSlider *led2slider;
    QProgressBar *led2brightindicator;
    QLabel *led2pulsebrightlabel;
    QLineEdit *led2pulsebrightness;
    QLabel *led2pulsedurlabel;
    QLineEdit *led2pulseduration;
    QPushButton *led2pulsebutton;
    QVBoxLayout *verticalLayout_2;
    QLabel *label;
    QPushButton *ringonbutton;
    QLabel *redlabel;
    QSlider *redslider;
    QProgressBar *redindicator;
    QLabel *greenlabel;
    QSlider *greenslider;
    QProgressBar *greenindicator;
    QLabel *bluelabel;
    QSlider *blueslider;
    QProgressBar *blueindicator;
    QLabel *bluelabel_2;
    QSlider *allslider;
    QProgressBar *allindicator;
    QVBoxLayout *verticalLayout_7;
    QVBoxLayout *verticalLayout_4;
    QSpacerItem *verticalSpacer;
    QLabel *greenpulselable_2;
    QLineEdit *redpulse;
    QLabel *greenpulselabel;
    QLineEdit *greenpulse;
    QLabel *bluepulselabel;
    QLineEdit *bluepulse;
    QLabel *ringpulsedurlabel_2;
    QLineEdit *ringpulsedurinput;
    QPushButton *ringpulsebutton;
    QWidget *peltier;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout_2;
    QVBoxLayout *verticalLayout_12;
    QPushButton *peltonbutton;
    QHBoxLayout *horizontalLayout_4;
    QCheckBox *logtempcheck;
    QRadioButton *tempclosedloop;
    QHBoxLayout *horizontalLayout_3;
    QSlider *tempslider;
    QVBoxLayout *verticalLayout_15;
    QLabel *desiredtemplabel;
    QProgressBar *desiredtempbar;
    QLabel *actualtemplabel;
    QProgressBar *actualtempbar;
    QGraphicsView *tempgraph;
    QVBoxLayout *verticalLayout_11;
    QWidget *servo;
    QWidget *verticalLayoutWidget_3;
    QVBoxLayout *verticalLayout_13;
    QPushButton *servobutton;
    QLabel *servolabel;
    QSlider *servoslider;
    QProgressBar *servobar;
    QWidget *protocol;
    QFrame *frame;
    QWidget *verticalLayoutWidget_2;
    QVBoxLayout *verticalLayout_6;
    QGroupBox *Ringgroup;
    QVBoxLayout *verticalLayout_5;
    QGridLayout *ringgrid;
    QSpinBox *redinput2;
    QSpinBox *greeninput3;
    QLabel *period_2;
    QPushButton *protringbutton;
    QSpinBox *greeninput1;
    QSpinBox *greeninput5;
    QSpinBox *blueinput2;
    QSpinBox *blueinput1;
    QSpinBox *redinput3;
    QLabel *blue;
    QSpinBox *blueinput5;
    QSpinBox *redinput4;
    QLabel *period_1;
    QSpinBox *greeninput4;
    QLabel *period_3;
    QLabel *red;
    QLabel *period_5;
    QSpinBox *blueinput4;
    QLabel *period_4;
    QSpinBox *greeninput2;
    QLabel *green;
    QSpinBox *blueinput3;
    QSpinBox *redinput5;
    QSpinBox *redinput1;
    QGroupBox *led1group;
    QFrame *frame_2;
    QWidget *gridLayoutWidget_3;
    QGridLayout *gridLayout_2;
    QLabel *brightness_7;
    QLabel *brightness_8;
    QLabel *brightness_9;
    QSpinBox *led1box1;
    QSpinBox *led1box2;
    QSpinBox *led1box4;
    QSpinBox *led1box5;
    QSpinBox *led1box3;
    QLabel *brightness_6;
    QPushButton *protled1button;
    QLabel *Brightness1_2;
    QLabel *Brightness1_3;
    QGroupBox *led2group;
    QFrame *led2frame;
    QWidget *gridLayoutWidget_4;
    QGridLayout *gridLayout_3;
    QLabel *brightness_10;
    QLabel *brightness_11;
    QLabel *brightness_12;
    QSpinBox *led2box1;
    QSpinBox *led2box2;
    QSpinBox *led2box3;
    QSpinBox *led2box4;
    QSpinBox *led2box5;
    QLabel *led2per4label;
    QPushButton *protled2button;
    QLabel *Brightness1_4;
    QLabel *led2brightlabel;
    QGroupBox *Peltiergroup;
    QHBoxLayout *horizontalLayout;
    QGridLayout *peltier_grid;
    QSpinBox *peltinput1;
    QLabel *peltlabel1;
    QSpinBox *peltinput3;
    QLabel *templabel;
    QSpinBox *peltinput4;
    QLabel *peltlabel3;
    QPushButton *protpeltierbutton;
    QSpinBox *peltinput2;
    QLabel *peltlabel2;
    QLabel *peltlabel4;
    QLabel *peltlabel5;
    QSpinBox *peltinput5;
    QGroupBox *matrixgroup;
    QFrame *matrixframe;
    QWidget *gridLayoutWidget_5;
    QGridLayout *gridLayout_4;
    QLabel *brightness_15;
    QPushButton *protmatrixbutton;
    QLabel *Brightness1_6;
    QLabel *brightness_17;
    QLabel *brightness_16;
    QSpinBox *led2box2_2;
    QSpinBox *led2box1_2;
    QLabel *Brightness1_7;
    QLabel *brightness_14;
    QSpinBox *led2box3_2;
    QSpinBox *led2box4_2;
    QSpinBox *led2box5_2;
    QLabel *Brightness1_8;
    QSpinBox *matrixpattern1;
    QSpinBox *matrixpattern1_2;
    QSpinBox *matrixpattern1_3;
    QSpinBox *matrixpattern1_4;
    QSpinBox *matrixpattern1_5;
    QGroupBox *timegroup;
    QVBoxLayout *verticalLayout_3;
    QGridLayout *timegrid;
    QPushButton *runbutton;
    QSpinBox *itiinput;
    QLabel *replabel;
    QSpinBox *timeinput3;
    QLabel *period1;
    QSpinBox *repinput;
    QSpinBox *timeinput1;
    QLabel *durationlabel_2;
    QSpinBox *timeinput4;
    QLabel *period3;
    QSpinBox *timeinput2;
    QLabel *period2;
    QLabel *period4;
    QLabel *period5;
    QSpinBox *timeinput5;
    QLabel *itilabel;
    QCheckBox *checkBox;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1023, 898);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setBaseSize(QSize(0, 20));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        scrollArea = new QScrollArea(centralWidget);
        scrollArea->setObjectName(QStringLiteral("scrollArea"));
        scrollArea->setGeometry(QRect(0, 0, 961, 821));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QStringLiteral("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 959, 819));
        tabs = new QTabWidget(scrollAreaWidgetContents);
        tabs->setObjectName(QStringLiteral("tabs"));
        tabs->setGeometry(QRect(0, 0, 929, 1011));
        tabs->setTabPosition(QTabWidget::North);
        tabs->setTabShape(QTabWidget::Rounded);
        tabs->setElideMode(Qt::ElideLeft);
        camera = new QWidget();
        camera->setObjectName(QStringLiteral("camera"));
        gridLayoutWidget = new QWidget(camera);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(10, 10, 911, 471));
        cameragrid = new QGridLayout(gridLayoutWidget);
        cameragrid->setSpacing(6);
        cameragrid->setContentsMargins(11, 11, 11, 11);
        cameragrid->setObjectName(QStringLiteral("cameragrid"));
        cameragrid->setContentsMargins(0, 0, 0, 0);
        photolayout = new QVBoxLayout();
        photolayout->setSpacing(6);
        photolayout->setObjectName(QStringLiteral("photolayout"));
        photolayout->setContentsMargins(-1, -1, -1, 2);

        cameragrid->addLayout(photolayout, 3, 0, 1, 1);

        contrastlayout = new QVBoxLayout();
        contrastlayout->setSpacing(6);
        contrastlayout->setObjectName(QStringLiteral("contrastlayout"));
        contrastlayout->setContentsMargins(-1, -1, -1, 2);
        contrastlabel = new QLabel(gridLayoutWidget);
        contrastlabel->setObjectName(QStringLiteral("contrastlabel"));

        contrastlayout->addWidget(contrastlabel);

        contrastlcd = new QLCDNumber(gridLayoutWidget);
        contrastlcd->setObjectName(QStringLiteral("contrastlcd"));
        contrastlcd->setDigitCount(3);
        contrastlcd->setSegmentStyle(QLCDNumber::Flat);
        contrastlcd->setProperty("value", QVariant(50));
        contrastlcd->setProperty("intValue", QVariant(50));

        contrastlayout->addWidget(contrastlcd);

        contrastbar = new QScrollBar(gridLayoutWidget);
        contrastbar->setObjectName(QStringLiteral("contrastbar"));
        contrastbar->setAcceptDrops(false);
        contrastbar->setMinimum(0);
        contrastbar->setMaximum(100);
        contrastbar->setSingleStep(1);
        contrastbar->setPageStep(1);
        contrastbar->setValue(50);
        contrastbar->setOrientation(Qt::Horizontal);

        contrastlayout->addWidget(contrastbar);


        cameragrid->addLayout(contrastlayout, 2, 4, 1, 1);

        binlayout = new QVBoxLayout();
        binlayout->setSpacing(6);
        binlayout->setObjectName(QStringLiteral("binlayout"));
        binlayout->setContentsMargins(-1, -1, -1, 2);
        binlabel = new QLabel(gridLayoutWidget);
        binlabel->setObjectName(QStringLiteral("binlabel"));

        binlayout->addWidget(binlabel);

        binlcd = new QLCDNumber(gridLayoutWidget);
        binlcd->setObjectName(QStringLiteral("binlcd"));
        binlcd->setDigitCount(2);
        binlcd->setSegmentStyle(QLCDNumber::Flat);
        binlcd->setProperty("value", QVariant(1));
        binlcd->setProperty("intValue", QVariant(1));

        binlayout->addWidget(binlcd);

        binbar = new QScrollBar(gridLayoutWidget);
        binbar->setObjectName(QStringLiteral("binbar"));
        binbar->setAcceptDrops(false);
        binbar->setMinimum(1);
        binbar->setMaximum(4);
        binbar->setSingleStep(1);
        binbar->setValue(1);
        binbar->setOrientation(Qt::Horizontal);

        binlayout->addWidget(binbar);


        cameragrid->addLayout(binlayout, 2, 7, 1, 1);

        cameralabellayout = new QVBoxLayout();
        cameralabellayout->setSpacing(6);
        cameralabellayout->setObjectName(QStringLiteral("cameralabellayout"));
        cameralabellayout->setContentsMargins(-1, -1, -1, 2);
        cameralabel = new QLabel(gridLayoutWidget);
        cameralabel->setObjectName(QStringLiteral("cameralabel"));
        cameralabel->setMaximumSize(QSize(16777215, 20));
        cameralabel->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);

        cameralabellayout->addWidget(cameralabel);


        cameragrid->addLayout(cameralabellayout, 0, 0, 1, 1);

        flipexposurelayout = new QVBoxLayout();
        flipexposurelayout->setSpacing(6);
        flipexposurelayout->setObjectName(QStringLiteral("flipexposurelayout"));
        flipexposurelayout->setContentsMargins(-1, -1, -1, 2);
        camonbutton = new QPushButton(gridLayoutWidget);
        camonbutton->setObjectName(QStringLiteral("camonbutton"));
        camonbutton->setCheckable(true);

        flipexposurelayout->addWidget(camonbutton);

        to_avibutton = new QPushButton(gridLayoutWidget);
        to_avibutton->setObjectName(QStringLiteral("to_avibutton"));

        flipexposurelayout->addWidget(to_avibutton);


        cameragrid->addLayout(flipexposurelayout, 2, 0, 1, 1);

        resolutionlayout = new QVBoxLayout();
        resolutionlayout->setSpacing(6);
        resolutionlayout->setObjectName(QStringLiteral("resolutionlayout"));
        resolutionlayout->setContentsMargins(-1, -1, -1, 2);
        resolutionlabel = new QLabel(gridLayoutWidget);
        resolutionlabel->setObjectName(QStringLiteral("resolutionlabel"));
        resolutionlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        resolutionlayout->addWidget(resolutionlabel);

        resolutionbox = new QComboBox(gridLayoutWidget);
        resolutionbox->setObjectName(QStringLiteral("resolutionbox"));

        resolutionlayout->addWidget(resolutionbox);

        whitebalancelabel = new QLabel(gridLayoutWidget);
        whitebalancelabel->setObjectName(QStringLiteral("whitebalancelabel"));
        whitebalancelabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        resolutionlayout->addWidget(whitebalancelabel);

        whitebalancebox = new QComboBox(gridLayoutWidget);
        whitebalancebox->setObjectName(QStringLiteral("whitebalancebox"));

        resolutionlayout->addWidget(whitebalancebox);


        cameragrid->addLayout(resolutionlayout, 3, 4, 1, 1);

        exposurelayout = new QVBoxLayout();
        exposurelayout->setSpacing(6);
        exposurelayout->setObjectName(QStringLiteral("exposurelayout"));
        exposurelayout->setContentsMargins(-1, -1, -1, 2);
        exposurelabel = new QLabel(gridLayoutWidget);
        exposurelabel->setObjectName(QStringLiteral("exposurelabel"));

        exposurelayout->addWidget(exposurelabel);

        exposurelcd = new QLCDNumber(gridLayoutWidget);
        exposurelcd->setObjectName(QStringLiteral("exposurelcd"));
        exposurelcd->setBaseSize(QSize(20, 20));
        exposurelcd->setDigitCount(3);
        exposurelcd->setSegmentStyle(QLCDNumber::Flat);
        exposurelcd->setProperty("value", QVariant(0));
        exposurelcd->setProperty("intValue", QVariant(0));

        exposurelayout->addWidget(exposurelcd);

        exposurebar = new QScrollBar(gridLayoutWidget);
        exposurebar->setObjectName(QStringLiteral("exposurebar"));
        exposurebar->setAcceptDrops(false);
        exposurebar->setMinimum(-25);
        exposurebar->setMaximum(25);
        exposurebar->setSingleStep(1);
        exposurebar->setPageStep(1);
        exposurebar->setValue(0);
        exposurebar->setSliderPosition(0);
        exposurebar->setOrientation(Qt::Horizontal);

        exposurelayout->addWidget(exposurebar);


        cameragrid->addLayout(exposurelayout, 2, 5, 1, 1);

        verticallayout = new QVBoxLayout();
        verticallayout->setSpacing(6);
        verticallayout->setObjectName(QStringLiteral("verticallayout"));
        verticallayout->setContentsMargins(-1, -1, -1, 2);
        verticallabel = new QLabel(gridLayoutWidget);
        verticallabel->setObjectName(QStringLiteral("verticallabel"));

        verticallayout->addWidget(verticallabel);

        verticallcd = new QLCDNumber(gridLayoutWidget);
        verticallcd->setObjectName(QStringLiteral("verticallcd"));
        verticallcd->setDigitCount(3);
        verticallcd->setSegmentStyle(QLCDNumber::Flat);
        verticallcd->setProperty("value", QVariant(0));
        verticallcd->setProperty("intValue", QVariant(0));

        verticallayout->addWidget(verticallcd);

        verticalbar = new QScrollBar(gridLayoutWidget);
        verticalbar->setObjectName(QStringLiteral("verticalbar"));
        verticalbar->setAcceptDrops(false);
        verticalbar->setMinimum(-100);
        verticalbar->setMaximum(100);
        verticalbar->setSingleStep(0);
        verticalbar->setValue(0);
        verticalbar->setOrientation(Qt::Horizontal);

        verticallayout->addWidget(verticalbar);


        cameragrid->addLayout(verticallayout, 0, 6, 1, 1);

        windowsizelayout = new QVBoxLayout();
        windowsizelayout->setSpacing(6);
        windowsizelayout->setObjectName(QStringLiteral("windowsizelayout"));
        windowsizelayout->setContentsMargins(-1, -1, -1, 2);
        windowlabel = new QLabel(gridLayoutWidget);
        windowlabel->setObjectName(QStringLiteral("windowlabel"));

        windowsizelayout->addWidget(windowlabel);

        windowlcd = new QLCDNumber(gridLayoutWidget);
        windowlcd->setObjectName(QStringLiteral("windowlcd"));
        windowlcd->setDigitCount(3);
        windowlcd->setSegmentStyle(QLCDNumber::Flat);
        windowlcd->setProperty("intValue", QVariant(240));

        windowsizelayout->addWidget(windowlcd);

        windowbar = new QScrollBar(gridLayoutWidget);
        windowbar->setObjectName(QStringLiteral("windowbar"));
        windowbar->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(windowbar->sizePolicy().hasHeightForWidth());
        windowbar->setSizePolicy(sizePolicy1);
        windowbar->setAcceptDrops(false);
        windowbar->setMinimum(240);
        windowbar->setMaximum(800);
        windowbar->setSingleStep(5);
        windowbar->setOrientation(Qt::Horizontal);

        windowsizelayout->addWidget(windowbar);


        cameragrid->addLayout(windowsizelayout, 0, 3, 1, 1);

        colourlayout = new QVBoxLayout();
        colourlayout->setSpacing(6);
        colourlayout->setObjectName(QStringLiteral("colourlayout"));
        colourlayout->setContentsMargins(-1, -1, -1, 2);
        intervallabel = new QLabel(gridLayoutWidget);
        intervallabel->setObjectName(QStringLiteral("intervallabel"));
        intervallabel->setMaximumSize(QSize(250, 16777215));

        colourlayout->addWidget(intervallabel);

        intervalbox = new QSpinBox(gridLayoutWidget);
        intervalbox->setObjectName(QStringLiteral("intervalbox"));
        intervalbox->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        intervalbox->setMaximum(1000000);
        intervalbox->setValue(5);

        colourlayout->addWidget(intervalbox);

        durationlabel = new QLabel(gridLayoutWidget);
        durationlabel->setObjectName(QStringLiteral("durationlabel"));
        durationlabel->setMaximumSize(QSize(250, 16777215));

        colourlayout->addWidget(durationlabel);

        durationbox = new QSpinBox(gridLayoutWidget);
        durationbox->setObjectName(QStringLiteral("durationbox"));
        durationbox->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        durationbox->setMaximum(1000000);
        durationbox->setValue(5);

        colourlayout->addWidget(durationbox);


        cameragrid->addLayout(colourlayout, 3, 7, 1, 1);

        rotationlayout = new QVBoxLayout();
        rotationlayout->setSpacing(6);
        rotationlayout->setObjectName(QStringLiteral("rotationlayout"));
        rotationlayout->setContentsMargins(-1, -1, -1, 2);
        rotationlabel = new QLabel(gridLayoutWidget);
        rotationlabel->setObjectName(QStringLiteral("rotationlabel"));

        rotationlayout->addWidget(rotationlabel);

        rotationlcd = new QLCDNumber(gridLayoutWidget);
        rotationlcd->setObjectName(QStringLiteral("rotationlcd"));
        rotationlcd->setDigitCount(3);
        rotationlcd->setSegmentStyle(QLCDNumber::Flat);
        rotationlcd->setProperty("value", QVariant(0));
        rotationlcd->setProperty("intValue", QVariant(0));

        rotationlayout->addWidget(rotationlcd);

        rotationbar = new QScrollBar(gridLayoutWidget);
        rotationbar->setObjectName(QStringLiteral("rotationbar"));
        rotationbar->setAcceptDrops(false);
        rotationbar->setMinimum(0);
        rotationbar->setMaximum(270);
        rotationbar->setSingleStep(90);
        rotationbar->setPageStep(90);
        rotationbar->setValue(0);
        rotationbar->setOrientation(Qt::Horizontal);

        rotationlayout->addWidget(rotationbar);


        cameragrid->addLayout(rotationlayout, 0, 7, 1, 1);

        zoomverticallayout = new QVBoxLayout();
        zoomverticallayout->setSpacing(6);
        zoomverticallayout->setObjectName(QStringLiteral("zoomverticallayout"));
        zoomverticallayout->setContentsMargins(-1, -1, -1, 2);
        zoomlabel = new QLabel(gridLayoutWidget);
        zoomlabel->setObjectName(QStringLiteral("zoomlabel"));

        zoomverticallayout->addWidget(zoomlabel);

        zoomlcd = new QLCDNumber(gridLayoutWidget);
        zoomlcd->setObjectName(QStringLiteral("zoomlcd"));
        zoomlcd->setDigitCount(2);
        zoomlcd->setSegmentStyle(QLCDNumber::Flat);
        zoomlcd->setProperty("intValue", QVariant(0));

        zoomverticallayout->addWidget(zoomlcd);

        zoombar = new QScrollBar(gridLayoutWidget);
        zoombar->setObjectName(QStringLiteral("zoombar"));
        zoombar->setAcceptDrops(false);
        zoombar->setMinimum(0);
        zoombar->setMaximum(10);
        zoombar->setSingleStep(1);
        zoombar->setPageStep(1);
        zoombar->setSliderPosition(0);
        zoombar->setOrientation(Qt::Horizontal);

        zoomverticallayout->addWidget(zoombar);


        cameragrid->addLayout(zoomverticallayout, 0, 4, 1, 1);

        whitebalancelayout = new QVBoxLayout();
        whitebalancelayout->setSpacing(6);
        whitebalancelayout->setObjectName(QStringLiteral("whitebalancelayout"));
        whitebalancelayout->setContentsMargins(-1, -1, -1, 2);
        modelabel = new QLabel(gridLayoutWidget);
        modelabel->setObjectName(QStringLiteral("modelabel"));
        modelabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        whitebalancelayout->addWidget(modelabel);

        modebox = new QComboBox(gridLayoutWidget);
        modebox->setObjectName(QStringLiteral("modebox"));
        modebox->setMaxVisibleItems(25);

        whitebalancelayout->addWidget(modebox);

        colourlabel = new QLabel(gridLayoutWidget);
        colourlabel->setObjectName(QStringLiteral("colourlabel"));
        colourlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        whitebalancelayout->addWidget(colourlabel);

        colourbox = new QComboBox(gridLayoutWidget);
        colourbox->setObjectName(QStringLiteral("colourbox"));
        colourbox->setEditable(false);

        whitebalancelayout->addWidget(colourbox);


        cameragrid->addLayout(whitebalancelayout, 3, 5, 1, 1);

        modelayout = new QVBoxLayout();
        modelayout->setSpacing(6);
        modelayout->setObjectName(QStringLiteral("modelayout"));
        modelayout->setContentsMargins(-1, -1, -1, 2);
        photobutton = new QPushButton(gridLayoutWidget);
        photobutton->setObjectName(QStringLiteral("photobutton"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(photobutton->sizePolicy().hasHeightForWidth());
        photobutton->setSizePolicy(sizePolicy2);
        photobutton->setMinimumSize(QSize(100, 0));

        modelayout->addWidget(photobutton);

        timelapsebutton = new QPushButton(gridLayoutWidget);
        timelapsebutton->setObjectName(QStringLiteral("timelapsebutton"));

        modelayout->addWidget(timelapsebutton);

        videobutton = new QPushButton(gridLayoutWidget);
        videobutton->setObjectName(QStringLiteral("videobutton"));

        modelayout->addWidget(videobutton);


        cameragrid->addLayout(modelayout, 3, 6, 1, 1);

        fpslayout = new QVBoxLayout();
        fpslayout->setSpacing(6);
        fpslayout->setObjectName(QStringLiteral("fpslayout"));
        fpslayout->setContentsMargins(-1, -1, -1, 2);
        fpslabel = new QLabel(gridLayoutWidget);
        fpslabel->setObjectName(QStringLiteral("fpslabel"));

        fpslayout->addWidget(fpslabel);

        fpslcd = new QLCDNumber(gridLayoutWidget);
        fpslcd->setObjectName(QStringLiteral("fpslcd"));
        fpslcd->setDigitCount(2);
        fpslcd->setSegmentStyle(QLCDNumber::Flat);
        fpslcd->setProperty("intValue", QVariant(5));

        fpslayout->addWidget(fpslcd);

        fpsbar = new QScrollBar(gridLayoutWidget);
        fpsbar->setObjectName(QStringLiteral("fpsbar"));
        fpsbar->setAcceptDrops(false);
        fpsbar->setMinimum(5);
        fpsbar->setMaximum(90);
        fpsbar->setSingleStep(5);
        fpsbar->setPageStep(5);
        fpsbar->setValue(5);
        fpsbar->setOrientation(Qt::Horizontal);

        fpslayout->addWidget(fpsbar);


        cameragrid->addLayout(fpslayout, 2, 6, 1, 1);

        horizontallayout = new QVBoxLayout();
        horizontallayout->setSpacing(6);
        horizontallayout->setObjectName(QStringLiteral("horizontallayout"));
        horizontallayout->setContentsMargins(-1, -1, -1, 2);
        horizontallabel = new QLabel(gridLayoutWidget);
        horizontallabel->setObjectName(QStringLiteral("horizontallabel"));

        horizontallayout->addWidget(horizontallabel);

        horizontallcd = new QLCDNumber(gridLayoutWidget);
        horizontallcd->setObjectName(QStringLiteral("horizontallcd"));
        horizontallcd->setDigitCount(3);
        horizontallcd->setSegmentStyle(QLCDNumber::Flat);
        horizontallcd->setProperty("intValue", QVariant(0));

        horizontallayout->addWidget(horizontallcd);

        horizontalbar = new QScrollBar(gridLayoutWidget);
        horizontalbar->setObjectName(QStringLiteral("horizontalbar"));
        horizontalbar->setAcceptDrops(false);
        horizontalbar->setMinimum(-100);
        horizontalbar->setMaximum(100);
        horizontalbar->setSingleStep(0);
        horizontalbar->setValue(0);
        horizontalbar->setOrientation(Qt::Horizontal);

        horizontallayout->addWidget(horizontalbar);


        cameragrid->addLayout(horizontallayout, 0, 5, 1, 1);

        intervallayout = new QVBoxLayout();
        intervallayout->setSpacing(6);
        intervallayout->setObjectName(QStringLiteral("intervallayout"));
        intervallayout->setContentsMargins(-1, -1, -1, 2);
        autoexposurebox = new QCheckBox(gridLayoutWidget);
        autoexposurebox->setObjectName(QStringLiteral("autoexposurebox"));

        intervallayout->addWidget(autoexposurebox);

        flipimagebox = new QCheckBox(gridLayoutWidget);
        flipimagebox->setObjectName(QStringLiteral("flipimagebox"));

        intervallayout->addWidget(flipimagebox);


        cameragrid->addLayout(intervallayout, 3, 3, 1, 1);

        brightnesslayout = new QVBoxLayout();
        brightnesslayout->setSpacing(6);
        brightnesslayout->setObjectName(QStringLiteral("brightnesslayout"));
        brightnesslayout->setContentsMargins(-1, -1, -1, 2);
        brightnesslabel = new QLabel(gridLayoutWidget);
        brightnesslabel->setObjectName(QStringLiteral("brightnesslabel"));

        brightnesslayout->addWidget(brightnesslabel);

        brightnesslcd = new QLCDNumber(gridLayoutWidget);
        brightnesslcd->setObjectName(QStringLiteral("brightnesslcd"));
        brightnesslcd->setDigitCount(3);
        brightnesslcd->setSegmentStyle(QLCDNumber::Flat);
        brightnesslcd->setProperty("value", QVariant(50));
        brightnesslcd->setProperty("intValue", QVariant(50));

        brightnesslayout->addWidget(brightnesslcd);

        brightnessbar = new QScrollBar(gridLayoutWidget);
        brightnessbar->setObjectName(QStringLiteral("brightnessbar"));
        brightnessbar->setAcceptDrops(false);
        brightnessbar->setMinimum(0);
        brightnessbar->setMaximum(100);
        brightnessbar->setSingleStep(1);
        brightnessbar->setPageStep(1);
        brightnessbar->setValue(50);
        brightnessbar->setOrientation(Qt::Horizontal);

        brightnesslayout->addWidget(brightnessbar);


        cameragrid->addLayout(brightnesslayout, 2, 3, 1, 1);

        tabs->addTab(camera, QString());
        lightdevices = new QWidget();
        lightdevices->setObjectName(QStringLiteral("lightdevices"));
        ringframe = new QFrame(lightdevices);
        ringframe->setObjectName(QStringLiteral("ringframe"));
        ringframe->setGeometry(QRect(10, 10, 901, 771));
        ringframe->setFrameShape(QFrame::StyledPanel);
        ringframe->setFrameShadow(QFrame::Sunken);
        gridLayoutWidget_2 = new QWidget(ringframe);
        gridLayoutWidget_2->setObjectName(QStringLiteral("gridLayoutWidget_2"));
        gridLayoutWidget_2->setGeometry(QRect(0, 0, 701, 741));
        ringgrid_2 = new QGridLayout(gridLayoutWidget_2);
        ringgrid_2->setSpacing(6);
        ringgrid_2->setContentsMargins(11, 11, 11, 11);
        ringgrid_2->setObjectName(QStringLiteral("ringgrid_2"));
        ringgrid_2->setContentsMargins(0, 0, 0, 0);
        verticalLayout_9 = new QVBoxLayout();
        verticalLayout_9->setSpacing(6);
        verticalLayout_9->setObjectName(QStringLiteral("verticalLayout_9"));
        led1label = new QLabel(gridLayoutWidget_2);
        led1label->setObjectName(QStringLiteral("led1label"));
        QSizePolicy sizePolicy3(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(led1label->sizePolicy().hasHeightForWidth());
        led1label->setSizePolicy(sizePolicy3);

        verticalLayout_9->addWidget(led1label);

        led1onbutton = new QPushButton(gridLayoutWidget_2);
        led1onbutton->setObjectName(QStringLiteral("led1onbutton"));
        led1onbutton->setCheckable(true);

        verticalLayout_9->addWidget(led1onbutton);

        led1brightlabel = new QLabel(gridLayoutWidget_2);
        led1brightlabel->setObjectName(QStringLiteral("led1brightlabel"));
        sizePolicy1.setHeightForWidth(led1brightlabel->sizePolicy().hasHeightForWidth());
        led1brightlabel->setSizePolicy(sizePolicy1);
        led1brightlabel->setMinimumSize(QSize(0, 20));
        led1brightlabel->setFrameShape(QFrame::NoFrame);
        led1brightlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_9->addWidget(led1brightlabel);

        led1slider = new QSlider(gridLayoutWidget_2);
        led1slider->setObjectName(QStringLiteral("led1slider"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Maximum);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(led1slider->sizePolicy().hasHeightForWidth());
        led1slider->setSizePolicy(sizePolicy4);
        led1slider->setLayoutDirection(Qt::LeftToRight);
        led1slider->setMaximum(100);
        led1slider->setOrientation(Qt::Horizontal);
        led1slider->setTickPosition(QSlider::TicksBothSides);
        led1slider->setTickInterval(5);

        verticalLayout_9->addWidget(led1slider);

        led1brightindicator = new QProgressBar(gridLayoutWidget_2);
        led1brightindicator->setObjectName(QStringLiteral("led1brightindicator"));
        QSizePolicy sizePolicy5(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(led1brightindicator->sizePolicy().hasHeightForWidth());
        led1brightindicator->setSizePolicy(sizePolicy5);
        led1brightindicator->setMinimumSize(QSize(150, 0));
        led1brightindicator->setValue(10);
        led1brightindicator->setInvertedAppearance(false);

        verticalLayout_9->addWidget(led1brightindicator);

        pulsedurationlabel_2 = new QLabel(gridLayoutWidget_2);
        pulsedurationlabel_2->setObjectName(QStringLiteral("pulsedurationlabel_2"));
        QSizePolicy sizePolicy6(QSizePolicy::Maximum, QSizePolicy::Preferred);
        sizePolicy6.setHorizontalStretch(0);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(pulsedurationlabel_2->sizePolicy().hasHeightForWidth());
        pulsedurationlabel_2->setSizePolicy(sizePolicy6);
        pulsedurationlabel_2->setMinimumSize(QSize(100, 0));
        pulsedurationlabel_2->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_9->addWidget(pulsedurationlabel_2);

        led1pulsebrightness = new QLineEdit(gridLayoutWidget_2);
        led1pulsebrightness->setObjectName(QStringLiteral("led1pulsebrightness"));
        sizePolicy5.setHeightForWidth(led1pulsebrightness->sizePolicy().hasHeightForWidth());
        led1pulsebrightness->setSizePolicy(sizePolicy5);
        led1pulsebrightness->setMinimumSize(QSize(100, 0));

        verticalLayout_9->addWidget(led1pulsebrightness);

        pulsedurationlabel = new QLabel(gridLayoutWidget_2);
        pulsedurationlabel->setObjectName(QStringLiteral("pulsedurationlabel"));
        sizePolicy6.setHeightForWidth(pulsedurationlabel->sizePolicy().hasHeightForWidth());
        pulsedurationlabel->setSizePolicy(sizePolicy6);
        pulsedurationlabel->setMinimumSize(QSize(100, 0));
        pulsedurationlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_9->addWidget(pulsedurationlabel);

        led1pulseduration = new QLineEdit(gridLayoutWidget_2);
        led1pulseduration->setObjectName(QStringLiteral("led1pulseduration"));
        sizePolicy5.setHeightForWidth(led1pulseduration->sizePolicy().hasHeightForWidth());
        led1pulseduration->setSizePolicy(sizePolicy5);
        led1pulseduration->setMinimumSize(QSize(100, 0));

        verticalLayout_9->addWidget(led1pulseduration);

        led1pulsebutton = new QPushButton(gridLayoutWidget_2);
        led1pulsebutton->setObjectName(QStringLiteral("led1pulsebutton"));
        QSizePolicy sizePolicy7(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy7.setHorizontalStretch(0);
        sizePolicy7.setVerticalStretch(0);
        sizePolicy7.setHeightForWidth(led1pulsebutton->sizePolicy().hasHeightForWidth());
        led1pulsebutton->setSizePolicy(sizePolicy7);
        led1pulsebutton->setMinimumSize(QSize(125, 0));

        verticalLayout_9->addWidget(led1pulsebutton);


        ringgrid_2->addLayout(verticalLayout_9, 1, 1, 1, 1);

        verticalLayout_8 = new QVBoxLayout();
        verticalLayout_8->setSpacing(6);
        verticalLayout_8->setObjectName(QStringLiteral("verticalLayout_8"));
        matrixlabel = new QLabel(gridLayoutWidget_2);
        matrixlabel->setObjectName(QStringLiteral("matrixlabel"));
        sizePolicy3.setHeightForWidth(matrixlabel->sizePolicy().hasHeightForWidth());
        matrixlabel->setSizePolicy(sizePolicy3);
        matrixlabel->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);

        verticalLayout_8->addWidget(matrixlabel);

        matrixonbutton = new QPushButton(gridLayoutWidget_2);
        matrixonbutton->setObjectName(QStringLiteral("matrixonbutton"));
        matrixonbutton->setCheckable(true);

        verticalLayout_8->addWidget(matrixonbutton);

        matbrightlabel = new QLabel(gridLayoutWidget_2);
        matbrightlabel->setObjectName(QStringLiteral("matbrightlabel"));
        sizePolicy1.setHeightForWidth(matbrightlabel->sizePolicy().hasHeightForWidth());
        matbrightlabel->setSizePolicy(sizePolicy1);
        matbrightlabel->setMinimumSize(QSize(0, 20));
        matbrightlabel->setFrameShape(QFrame::NoFrame);
        matbrightlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_8->addWidget(matbrightlabel);

        matrixslider = new QSlider(gridLayoutWidget_2);
        matrixslider->setObjectName(QStringLiteral("matrixslider"));
        sizePolicy4.setHeightForWidth(matrixslider->sizePolicy().hasHeightForWidth());
        matrixslider->setSizePolicy(sizePolicy4);
        matrixslider->setLayoutDirection(Qt::LeftToRight);
        matrixslider->setMaximum(10);
        matrixslider->setOrientation(Qt::Horizontal);
        matrixslider->setTickPosition(QSlider::TicksBothSides);
        matrixslider->setTickInterval(5);

        verticalLayout_8->addWidget(matrixslider);

        matbrightindicator = new QProgressBar(gridLayoutWidget_2);
        matbrightindicator->setObjectName(QStringLiteral("matbrightindicator"));
        sizePolicy5.setHeightForWidth(matbrightindicator->sizePolicy().hasHeightForWidth());
        matbrightindicator->setSizePolicy(sizePolicy5);
        matbrightindicator->setMinimumSize(QSize(150, 0));
        matbrightindicator->setMaximum(10);
        matbrightindicator->setValue(0);
        matbrightindicator->setInvertedAppearance(false);

        verticalLayout_8->addWidget(matbrightindicator);

        matrixpat1 = new QPushButton(gridLayoutWidget_2);
        matrixpat1->setObjectName(QStringLiteral("matrixpat1"));

        verticalLayout_8->addWidget(matrixpat1);

        matrixpat2 = new QPushButton(gridLayoutWidget_2);
        matrixpat2->setObjectName(QStringLiteral("matrixpat2"));

        verticalLayout_8->addWidget(matrixpat2);

        matrixpat3 = new QPushButton(gridLayoutWidget_2);
        matrixpat3->setObjectName(QStringLiteral("matrixpat3"));

        verticalLayout_8->addWidget(matrixpat3);

        verticalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_8->addItem(verticalSpacer_2);


        ringgrid_2->addLayout(verticalLayout_8, 1, 3, 1, 1);

        verticalLayout_10 = new QVBoxLayout();
        verticalLayout_10->setSpacing(6);
        verticalLayout_10->setObjectName(QStringLiteral("verticalLayout_10"));
        led2label = new QLabel(gridLayoutWidget_2);
        led2label->setObjectName(QStringLiteral("led2label"));
        sizePolicy3.setHeightForWidth(led2label->sizePolicy().hasHeightForWidth());
        led2label->setSizePolicy(sizePolicy3);

        verticalLayout_10->addWidget(led2label);

        led2onbutton = new QPushButton(gridLayoutWidget_2);
        led2onbutton->setObjectName(QStringLiteral("led2onbutton"));
        led2onbutton->setCheckable(true);

        verticalLayout_10->addWidget(led2onbutton);

        led2brightlabel_2 = new QLabel(gridLayoutWidget_2);
        led2brightlabel_2->setObjectName(QStringLiteral("led2brightlabel_2"));
        sizePolicy1.setHeightForWidth(led2brightlabel_2->sizePolicy().hasHeightForWidth());
        led2brightlabel_2->setSizePolicy(sizePolicy1);
        led2brightlabel_2->setMinimumSize(QSize(0, 20));
        led2brightlabel_2->setFrameShape(QFrame::NoFrame);
        led2brightlabel_2->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_10->addWidget(led2brightlabel_2);

        led2slider = new QSlider(gridLayoutWidget_2);
        led2slider->setObjectName(QStringLiteral("led2slider"));
        sizePolicy4.setHeightForWidth(led2slider->sizePolicy().hasHeightForWidth());
        led2slider->setSizePolicy(sizePolicy4);
        led2slider->setLayoutDirection(Qt::LeftToRight);
        led2slider->setMaximum(100);
        led2slider->setOrientation(Qt::Horizontal);
        led2slider->setTickPosition(QSlider::TicksBothSides);
        led2slider->setTickInterval(5);

        verticalLayout_10->addWidget(led2slider);

        led2brightindicator = new QProgressBar(gridLayoutWidget_2);
        led2brightindicator->setObjectName(QStringLiteral("led2brightindicator"));
        sizePolicy5.setHeightForWidth(led2brightindicator->sizePolicy().hasHeightForWidth());
        led2brightindicator->setSizePolicy(sizePolicy5);
        led2brightindicator->setMinimumSize(QSize(150, 0));
        led2brightindicator->setValue(10);
        led2brightindicator->setInvertedAppearance(false);

        verticalLayout_10->addWidget(led2brightindicator);

        led2pulsebrightlabel = new QLabel(gridLayoutWidget_2);
        led2pulsebrightlabel->setObjectName(QStringLiteral("led2pulsebrightlabel"));
        sizePolicy6.setHeightForWidth(led2pulsebrightlabel->sizePolicy().hasHeightForWidth());
        led2pulsebrightlabel->setSizePolicy(sizePolicy6);
        led2pulsebrightlabel->setMinimumSize(QSize(100, 0));
        led2pulsebrightlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_10->addWidget(led2pulsebrightlabel);

        led2pulsebrightness = new QLineEdit(gridLayoutWidget_2);
        led2pulsebrightness->setObjectName(QStringLiteral("led2pulsebrightness"));
        sizePolicy5.setHeightForWidth(led2pulsebrightness->sizePolicy().hasHeightForWidth());
        led2pulsebrightness->setSizePolicy(sizePolicy5);
        led2pulsebrightness->setMinimumSize(QSize(100, 0));

        verticalLayout_10->addWidget(led2pulsebrightness);

        led2pulsedurlabel = new QLabel(gridLayoutWidget_2);
        led2pulsedurlabel->setObjectName(QStringLiteral("led2pulsedurlabel"));
        sizePolicy6.setHeightForWidth(led2pulsedurlabel->sizePolicy().hasHeightForWidth());
        led2pulsedurlabel->setSizePolicy(sizePolicy6);
        led2pulsedurlabel->setMinimumSize(QSize(100, 0));
        led2pulsedurlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_10->addWidget(led2pulsedurlabel);

        led2pulseduration = new QLineEdit(gridLayoutWidget_2);
        led2pulseduration->setObjectName(QStringLiteral("led2pulseduration"));
        sizePolicy5.setHeightForWidth(led2pulseduration->sizePolicy().hasHeightForWidth());
        led2pulseduration->setSizePolicy(sizePolicy5);
        led2pulseduration->setMinimumSize(QSize(100, 0));

        verticalLayout_10->addWidget(led2pulseduration);

        led2pulsebutton = new QPushButton(gridLayoutWidget_2);
        led2pulsebutton->setObjectName(QStringLiteral("led2pulsebutton"));
        sizePolicy7.setHeightForWidth(led2pulsebutton->sizePolicy().hasHeightForWidth());
        led2pulsebutton->setSizePolicy(sizePolicy7);
        led2pulsebutton->setMinimumSize(QSize(125, 0));

        verticalLayout_10->addWidget(led2pulsebutton);


        ringgrid_2->addLayout(verticalLayout_10, 1, 2, 1, 1);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        label = new QLabel(gridLayoutWidget_2);
        label->setObjectName(QStringLiteral("label"));

        verticalLayout_2->addWidget(label);

        ringonbutton = new QPushButton(gridLayoutWidget_2);
        ringonbutton->setObjectName(QStringLiteral("ringonbutton"));
        sizePolicy1.setHeightForWidth(ringonbutton->sizePolicy().hasHeightForWidth());
        ringonbutton->setSizePolicy(sizePolicy1);
        ringonbutton->setMinimumSize(QSize(100, 0));
        ringonbutton->setCheckable(true);

        verticalLayout_2->addWidget(ringonbutton);

        redlabel = new QLabel(gridLayoutWidget_2);
        redlabel->setObjectName(QStringLiteral("redlabel"));
        sizePolicy1.setHeightForWidth(redlabel->sizePolicy().hasHeightForWidth());
        redlabel->setSizePolicy(sizePolicy1);
        redlabel->setMinimumSize(QSize(0, 20));
        redlabel->setFrameShape(QFrame::NoFrame);
        redlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_2->addWidget(redlabel);

        redslider = new QSlider(gridLayoutWidget_2);
        redslider->setObjectName(QStringLiteral("redslider"));
        sizePolicy4.setHeightForWidth(redslider->sizePolicy().hasHeightForWidth());
        redslider->setSizePolicy(sizePolicy4);
        redslider->setLayoutDirection(Qt::LeftToRight);
        redslider->setMaximum(100);
        redslider->setValue(10);
        redslider->setOrientation(Qt::Horizontal);
        redslider->setInvertedControls(false);
        redslider->setTickPosition(QSlider::TicksBothSides);
        redslider->setTickInterval(5);

        verticalLayout_2->addWidget(redslider);

        redindicator = new QProgressBar(gridLayoutWidget_2);
        redindicator->setObjectName(QStringLiteral("redindicator"));
        sizePolicy5.setHeightForWidth(redindicator->sizePolicy().hasHeightForWidth());
        redindicator->setSizePolicy(sizePolicy5);
        redindicator->setMinimumSize(QSize(150, 0));
        redindicator->setValue(10);
        redindicator->setInvertedAppearance(false);

        verticalLayout_2->addWidget(redindicator);

        greenlabel = new QLabel(gridLayoutWidget_2);
        greenlabel->setObjectName(QStringLiteral("greenlabel"));
        QSizePolicy sizePolicy8(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy8.setHorizontalStretch(0);
        sizePolicy8.setVerticalStretch(0);
        sizePolicy8.setHeightForWidth(greenlabel->sizePolicy().hasHeightForWidth());
        greenlabel->setSizePolicy(sizePolicy8);
        greenlabel->setMaximumSize(QSize(16777215, 20));
        greenlabel->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_2->addWidget(greenlabel);

        greenslider = new QSlider(gridLayoutWidget_2);
        greenslider->setObjectName(QStringLiteral("greenslider"));
        sizePolicy4.setHeightForWidth(greenslider->sizePolicy().hasHeightForWidth());
        greenslider->setSizePolicy(sizePolicy4);
        greenslider->setBaseSize(QSize(0, 0));
        greenslider->setMaximum(100);
        greenslider->setValue(10);
        greenslider->setOrientation(Qt::Horizontal);
        greenslider->setTickPosition(QSlider::TicksBothSides);
        greenslider->setTickInterval(5);

        verticalLayout_2->addWidget(greenslider);

        greenindicator = new QProgressBar(gridLayoutWidget_2);
        greenindicator->setObjectName(QStringLiteral("greenindicator"));
        sizePolicy5.setHeightForWidth(greenindicator->sizePolicy().hasHeightForWidth());
        greenindicator->setSizePolicy(sizePolicy5);
        greenindicator->setMinimumSize(QSize(150, 0));
        greenindicator->setValue(10);

        verticalLayout_2->addWidget(greenindicator);

        bluelabel = new QLabel(gridLayoutWidget_2);
        bluelabel->setObjectName(QStringLiteral("bluelabel"));
        sizePolicy1.setHeightForWidth(bluelabel->sizePolicy().hasHeightForWidth());
        bluelabel->setSizePolicy(sizePolicy1);
        bluelabel->setMinimumSize(QSize(0, 20));
        bluelabel->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout_2->addWidget(bluelabel);

        blueslider = new QSlider(gridLayoutWidget_2);
        blueslider->setObjectName(QStringLiteral("blueslider"));
        sizePolicy4.setHeightForWidth(blueslider->sizePolicy().hasHeightForWidth());
        blueslider->setSizePolicy(sizePolicy4);
        blueslider->setMaximum(100);
        blueslider->setValue(10);
        blueslider->setOrientation(Qt::Horizontal);
        blueslider->setTickPosition(QSlider::TicksBothSides);
        blueslider->setTickInterval(5);

        verticalLayout_2->addWidget(blueslider);

        blueindicator = new QProgressBar(gridLayoutWidget_2);
        blueindicator->setObjectName(QStringLiteral("blueindicator"));
        sizePolicy5.setHeightForWidth(blueindicator->sizePolicy().hasHeightForWidth());
        blueindicator->setSizePolicy(sizePolicy5);
        blueindicator->setMinimumSize(QSize(150, 0));
        blueindicator->setValue(10);
        blueindicator->setInvertedAppearance(false);

        verticalLayout_2->addWidget(blueindicator);

        bluelabel_2 = new QLabel(gridLayoutWidget_2);
        bluelabel_2->setObjectName(QStringLiteral("bluelabel_2"));
        sizePolicy1.setHeightForWidth(bluelabel_2->sizePolicy().hasHeightForWidth());
        bluelabel_2->setSizePolicy(sizePolicy1);
        bluelabel_2->setMinimumSize(QSize(0, 20));
        bluelabel_2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout_2->addWidget(bluelabel_2);

        allslider = new QSlider(gridLayoutWidget_2);
        allslider->setObjectName(QStringLiteral("allslider"));
        sizePolicy3.setHeightForWidth(allslider->sizePolicy().hasHeightForWidth());
        allslider->setSizePolicy(sizePolicy3);
        allslider->setInputMethodHints(Qt::ImhDigitsOnly);
        allslider->setMaximum(100);
        allslider->setValue(10);
        allslider->setOrientation(Qt::Horizontal);
        allslider->setTickPosition(QSlider::TicksBothSides);
        allslider->setTickInterval(5);

        verticalLayout_2->addWidget(allslider);

        allindicator = new QProgressBar(gridLayoutWidget_2);
        allindicator->setObjectName(QStringLiteral("allindicator"));
        sizePolicy5.setHeightForWidth(allindicator->sizePolicy().hasHeightForWidth());
        allindicator->setSizePolicy(sizePolicy5);
        allindicator->setMinimumSize(QSize(150, 0));
        allindicator->setValue(10);

        verticalLayout_2->addWidget(allindicator);


        ringgrid_2->addLayout(verticalLayout_2, 2, 1, 1, 1);

        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setSpacing(6);
        verticalLayout_7->setObjectName(QStringLiteral("verticalLayout_7"));
        verticalLayout_7->setSizeConstraint(QLayout::SetDefaultConstraint);
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer);

        greenpulselable_2 = new QLabel(gridLayoutWidget_2);
        greenpulselable_2->setObjectName(QStringLiteral("greenpulselable_2"));
        QSizePolicy sizePolicy9(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy9.setHorizontalStretch(0);
        sizePolicy9.setVerticalStretch(0);
        sizePolicy9.setHeightForWidth(greenpulselable_2->sizePolicy().hasHeightForWidth());
        greenpulselable_2->setSizePolicy(sizePolicy9);
        greenpulselable_2->setMinimumSize(QSize(100, 0));

        verticalLayout_4->addWidget(greenpulselable_2);

        redpulse = new QLineEdit(gridLayoutWidget_2);
        redpulse->setObjectName(QStringLiteral("redpulse"));
        sizePolicy7.setHeightForWidth(redpulse->sizePolicy().hasHeightForWidth());
        redpulse->setSizePolicy(sizePolicy7);
        redpulse->setMinimumSize(QSize(20, 0));

        verticalLayout_4->addWidget(redpulse);

        greenpulselabel = new QLabel(gridLayoutWidget_2);
        greenpulselabel->setObjectName(QStringLiteral("greenpulselabel"));

        verticalLayout_4->addWidget(greenpulselabel);

        greenpulse = new QLineEdit(gridLayoutWidget_2);
        greenpulse->setObjectName(QStringLiteral("greenpulse"));
        sizePolicy5.setHeightForWidth(greenpulse->sizePolicy().hasHeightForWidth());
        greenpulse->setSizePolicy(sizePolicy5);
        greenpulse->setMinimumSize(QSize(20, 0));

        verticalLayout_4->addWidget(greenpulse);

        bluepulselabel = new QLabel(gridLayoutWidget_2);
        bluepulselabel->setObjectName(QStringLiteral("bluepulselabel"));

        verticalLayout_4->addWidget(bluepulselabel);

        bluepulse = new QLineEdit(gridLayoutWidget_2);
        bluepulse->setObjectName(QStringLiteral("bluepulse"));
        sizePolicy5.setHeightForWidth(bluepulse->sizePolicy().hasHeightForWidth());
        bluepulse->setSizePolicy(sizePolicy5);
        bluepulse->setMinimumSize(QSize(20, 0));

        verticalLayout_4->addWidget(bluepulse);


        verticalLayout_7->addLayout(verticalLayout_4);

        ringpulsedurlabel_2 = new QLabel(gridLayoutWidget_2);
        ringpulsedurlabel_2->setObjectName(QStringLiteral("ringpulsedurlabel_2"));
        sizePolicy6.setHeightForWidth(ringpulsedurlabel_2->sizePolicy().hasHeightForWidth());
        ringpulsedurlabel_2->setSizePolicy(sizePolicy6);
        ringpulsedurlabel_2->setMinimumSize(QSize(100, 0));
        ringpulsedurlabel_2->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

        verticalLayout_7->addWidget(ringpulsedurlabel_2);

        ringpulsedurinput = new QLineEdit(gridLayoutWidget_2);
        ringpulsedurinput->setObjectName(QStringLiteral("ringpulsedurinput"));
        sizePolicy5.setHeightForWidth(ringpulsedurinput->sizePolicy().hasHeightForWidth());
        ringpulsedurinput->setSizePolicy(sizePolicy5);
        ringpulsedurinput->setMinimumSize(QSize(100, 0));

        verticalLayout_7->addWidget(ringpulsedurinput);

        ringpulsebutton = new QPushButton(gridLayoutWidget_2);
        ringpulsebutton->setObjectName(QStringLiteral("ringpulsebutton"));
        sizePolicy7.setHeightForWidth(ringpulsebutton->sizePolicy().hasHeightForWidth());
        ringpulsebutton->setSizePolicy(sizePolicy7);
        ringpulsebutton->setMinimumSize(QSize(125, 0));

        verticalLayout_7->addWidget(ringpulsebutton);


        ringgrid_2->addLayout(verticalLayout_7, 2, 2, 1, 1);

        tabs->addTab(lightdevices, QString());
        peltier = new QWidget();
        peltier->setObjectName(QStringLiteral("peltier"));
        horizontalLayoutWidget = new QWidget(peltier);
        horizontalLayoutWidget->setObjectName(QStringLiteral("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(110, 70, 651, 381));
        horizontalLayout_2 = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        verticalLayout_12 = new QVBoxLayout();
        verticalLayout_12->setSpacing(6);
        verticalLayout_12->setObjectName(QStringLiteral("verticalLayout_12"));
        peltonbutton = new QPushButton(horizontalLayoutWidget);
        peltonbutton->setObjectName(QStringLiteral("peltonbutton"));
        peltonbutton->setCheckable(true);

        verticalLayout_12->addWidget(peltonbutton);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        logtempcheck = new QCheckBox(horizontalLayoutWidget);
        logtempcheck->setObjectName(QStringLiteral("logtempcheck"));
        logtempcheck->setAutoRepeat(false);
        logtempcheck->setAutoRepeatDelay(1000);
        logtempcheck->setAutoRepeatInterval(1000);

        horizontalLayout_4->addWidget(logtempcheck);

        tempclosedloop = new QRadioButton(horizontalLayoutWidget);
        tempclosedloop->setObjectName(QStringLiteral("tempclosedloop"));
        tempclosedloop->setEnabled(true);
        tempclosedloop->setCheckable(true);
        tempclosedloop->setChecked(true);
        tempclosedloop->setAutoRepeat(true);
        tempclosedloop->setAutoRepeatDelay(500);
        tempclosedloop->setAutoRepeatInterval(500);

        horizontalLayout_4->addWidget(tempclosedloop);


        verticalLayout_12->addLayout(horizontalLayout_4);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        tempslider = new QSlider(horizontalLayoutWidget);
        tempslider->setObjectName(QStringLiteral("tempslider"));
        tempslider->setMinimum(15);
        tempslider->setMaximum(40);
        tempslider->setSingleStep(1);
        tempslider->setPageStep(1);
        tempslider->setValue(20);
        tempslider->setOrientation(Qt::Vertical);
        tempslider->setTickPosition(QSlider::TicksBothSides);
        tempslider->setTickInterval(2);

        horizontalLayout_3->addWidget(tempslider);

        verticalLayout_15 = new QVBoxLayout();
        verticalLayout_15->setSpacing(6);
        verticalLayout_15->setObjectName(QStringLiteral("verticalLayout_15"));
        desiredtemplabel = new QLabel(horizontalLayoutWidget);
        desiredtemplabel->setObjectName(QStringLiteral("desiredtemplabel"));

        verticalLayout_15->addWidget(desiredtemplabel);

        desiredtempbar = new QProgressBar(horizontalLayoutWidget);
        desiredtempbar->setObjectName(QStringLiteral("desiredtempbar"));
        desiredtempbar->setMinimum(15);
        desiredtempbar->setMaximum(40);
        desiredtempbar->setValue(20);
        desiredtempbar->setAlignment(Qt::AlignCenter);
        desiredtempbar->setTextVisible(true);
        desiredtempbar->setOrientation(Qt::Horizontal);
        desiredtempbar->setTextDirection(QProgressBar::BottomToTop);

        verticalLayout_15->addWidget(desiredtempbar);

        actualtemplabel = new QLabel(horizontalLayoutWidget);
        actualtemplabel->setObjectName(QStringLiteral("actualtemplabel"));

        verticalLayout_15->addWidget(actualtemplabel);

        actualtempbar = new QProgressBar(horizontalLayoutWidget);
        actualtempbar->setObjectName(QStringLiteral("actualtempbar"));
        actualtempbar->setMinimum(15);
        actualtempbar->setMaximum(40);
        actualtempbar->setValue(20);
        actualtempbar->setAlignment(Qt::AlignCenter);
        actualtempbar->setTextVisible(true);
        actualtempbar->setOrientation(Qt::Horizontal);
        actualtempbar->setTextDirection(QProgressBar::BottomToTop);

        verticalLayout_15->addWidget(actualtempbar);

        tempgraph = new QGraphicsView(horizontalLayoutWidget);
        tempgraph->setObjectName(QStringLiteral("tempgraph"));
        QBrush brush(QColor(0, 0, 0, 255));
        brush.setStyle(Qt::NoBrush);
        tempgraph->setForegroundBrush(brush);

        verticalLayout_15->addWidget(tempgraph);


        horizontalLayout_3->addLayout(verticalLayout_15);


        verticalLayout_12->addLayout(horizontalLayout_3);


        horizontalLayout_2->addLayout(verticalLayout_12);

        verticalLayout_11 = new QVBoxLayout();
        verticalLayout_11->setSpacing(6);
        verticalLayout_11->setObjectName(QStringLiteral("verticalLayout_11"));

        horizontalLayout_2->addLayout(verticalLayout_11);

        tabs->addTab(peltier, QString());
        servo = new QWidget();
        servo->setObjectName(QStringLiteral("servo"));
        servo->setCursor(QCursor(Qt::ArrowCursor));
        verticalLayoutWidget_3 = new QWidget(servo);
        verticalLayoutWidget_3->setObjectName(QStringLiteral("verticalLayoutWidget_3"));
        verticalLayoutWidget_3->setGeometry(QRect(180, 160, 160, 112));
        verticalLayout_13 = new QVBoxLayout(verticalLayoutWidget_3);
        verticalLayout_13->setSpacing(6);
        verticalLayout_13->setContentsMargins(11, 11, 11, 11);
        verticalLayout_13->setObjectName(QStringLiteral("verticalLayout_13"));
        verticalLayout_13->setContentsMargins(0, 0, 0, 0);
        servobutton = new QPushButton(verticalLayoutWidget_3);
        servobutton->setObjectName(QStringLiteral("servobutton"));

        verticalLayout_13->addWidget(servobutton);

        servolabel = new QLabel(verticalLayoutWidget_3);
        servolabel->setObjectName(QStringLiteral("servolabel"));

        verticalLayout_13->addWidget(servolabel);

        servoslider = new QSlider(verticalLayoutWidget_3);
        servoslider->setObjectName(QStringLiteral("servoslider"));
        servoslider->setMinimum(-10);
        servoslider->setMaximum(10);
        servoslider->setOrientation(Qt::Horizontal);
        servoslider->setTickPosition(QSlider::TicksBothSides);

        verticalLayout_13->addWidget(servoslider);

        servobar = new QProgressBar(verticalLayoutWidget_3);
        servobar->setObjectName(QStringLiteral("servobar"));
        servobar->setMinimum(-10);
        servobar->setMaximum(10);
        servobar->setValue(0);
        servobar->setInvertedAppearance(false);

        verticalLayout_13->addWidget(servobar);

        tabs->addTab(servo, QString());
        protocol = new QWidget();
        protocol->setObjectName(QStringLiteral("protocol"));
        frame = new QFrame(protocol);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setGeometry(QRect(0, 0, 921, 801));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayoutWidget_2 = new QWidget(frame);
        verticalLayoutWidget_2->setObjectName(QStringLiteral("verticalLayoutWidget_2"));
        verticalLayoutWidget_2->setGeometry(QRect(10, 10, 901, 781));
        verticalLayout_6 = new QVBoxLayout(verticalLayoutWidget_2);
        verticalLayout_6->setSpacing(6);
        verticalLayout_6->setContentsMargins(11, 11, 11, 11);
        verticalLayout_6->setObjectName(QStringLiteral("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(0, 0, 0, 0);
        Ringgroup = new QGroupBox(verticalLayoutWidget_2);
        Ringgroup->setObjectName(QStringLiteral("Ringgroup"));
        verticalLayout_5 = new QVBoxLayout(Ringgroup);
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setContentsMargins(11, 11, 11, 11);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        ringgrid = new QGridLayout();
        ringgrid->setSpacing(6);
        ringgrid->setObjectName(QStringLiteral("ringgrid"));
        redinput2 = new QSpinBox(Ringgroup);
        redinput2->setObjectName(QStringLiteral("redinput2"));
        redinput2->setMaximum(100);

        ringgrid->addWidget(redinput2, 3, 2, 1, 1);

        greeninput3 = new QSpinBox(Ringgroup);
        greeninput3->setObjectName(QStringLiteral("greeninput3"));
        greeninput3->setMaximum(100);

        ringgrid->addWidget(greeninput3, 4, 3, 1, 1);

        period_2 = new QLabel(Ringgroup);
        period_2->setObjectName(QStringLiteral("period_2"));

        ringgrid->addWidget(period_2, 0, 2, 1, 1);

        protringbutton = new QPushButton(Ringgroup);
        protringbutton->setObjectName(QStringLiteral("protringbutton"));
        protringbutton->setCheckable(true);

        ringgrid->addWidget(protringbutton, 0, 0, 1, 1);

        greeninput1 = new QSpinBox(Ringgroup);
        greeninput1->setObjectName(QStringLiteral("greeninput1"));
        greeninput1->setMaximum(100);

        ringgrid->addWidget(greeninput1, 4, 1, 1, 1);

        greeninput5 = new QSpinBox(Ringgroup);
        greeninput5->setObjectName(QStringLiteral("greeninput5"));
        greeninput5->setMaximum(100);

        ringgrid->addWidget(greeninput5, 4, 5, 1, 1);

        blueinput2 = new QSpinBox(Ringgroup);
        blueinput2->setObjectName(QStringLiteral("blueinput2"));
        blueinput2->setMaximum(100);

        ringgrid->addWidget(blueinput2, 5, 2, 1, 1);

        blueinput1 = new QSpinBox(Ringgroup);
        blueinput1->setObjectName(QStringLiteral("blueinput1"));
        blueinput1->setMaximum(100);

        ringgrid->addWidget(blueinput1, 5, 1, 1, 1);

        redinput3 = new QSpinBox(Ringgroup);
        redinput3->setObjectName(QStringLiteral("redinput3"));
        redinput3->setMaximum(100);

        ringgrid->addWidget(redinput3, 3, 3, 1, 1);

        blue = new QLabel(Ringgroup);
        blue->setObjectName(QStringLiteral("blue"));

        ringgrid->addWidget(blue, 5, 0, 1, 1);

        blueinput5 = new QSpinBox(Ringgroup);
        blueinput5->setObjectName(QStringLiteral("blueinput5"));
        blueinput5->setMaximum(100);

        ringgrid->addWidget(blueinput5, 5, 5, 1, 1);

        redinput4 = new QSpinBox(Ringgroup);
        redinput4->setObjectName(QStringLiteral("redinput4"));
        redinput4->setMaximum(100);

        ringgrid->addWidget(redinput4, 3, 4, 1, 1);

        period_1 = new QLabel(Ringgroup);
        period_1->setObjectName(QStringLiteral("period_1"));

        ringgrid->addWidget(period_1, 0, 1, 1, 1);

        greeninput4 = new QSpinBox(Ringgroup);
        greeninput4->setObjectName(QStringLiteral("greeninput4"));
        greeninput4->setMaximum(100);

        ringgrid->addWidget(greeninput4, 4, 4, 1, 1);

        period_3 = new QLabel(Ringgroup);
        period_3->setObjectName(QStringLiteral("period_3"));

        ringgrid->addWidget(period_3, 0, 3, 1, 1);

        red = new QLabel(Ringgroup);
        red->setObjectName(QStringLiteral("red"));

        ringgrid->addWidget(red, 3, 0, 1, 1);

        period_5 = new QLabel(Ringgroup);
        period_5->setObjectName(QStringLiteral("period_5"));

        ringgrid->addWidget(period_5, 0, 5, 1, 1);

        blueinput4 = new QSpinBox(Ringgroup);
        blueinput4->setObjectName(QStringLiteral("blueinput4"));
        blueinput4->setMaximum(100);

        ringgrid->addWidget(blueinput4, 5, 4, 1, 1);

        period_4 = new QLabel(Ringgroup);
        period_4->setObjectName(QStringLiteral("period_4"));

        ringgrid->addWidget(period_4, 0, 4, 1, 1);

        greeninput2 = new QSpinBox(Ringgroup);
        greeninput2->setObjectName(QStringLiteral("greeninput2"));
        greeninput2->setMaximum(100);

        ringgrid->addWidget(greeninput2, 4, 2, 1, 1);

        green = new QLabel(Ringgroup);
        green->setObjectName(QStringLiteral("green"));

        ringgrid->addWidget(green, 4, 0, 1, 1);

        blueinput3 = new QSpinBox(Ringgroup);
        blueinput3->setObjectName(QStringLiteral("blueinput3"));
        blueinput3->setMaximum(100);

        ringgrid->addWidget(blueinput3, 5, 3, 1, 1);

        redinput5 = new QSpinBox(Ringgroup);
        redinput5->setObjectName(QStringLiteral("redinput5"));
        redinput5->setMaximum(100);

        ringgrid->addWidget(redinput5, 3, 5, 1, 1);

        redinput1 = new QSpinBox(Ringgroup);
        redinput1->setObjectName(QStringLiteral("redinput1"));
        redinput1->setMaximum(100);

        ringgrid->addWidget(redinput1, 3, 1, 1, 1);


        verticalLayout_5->addLayout(ringgrid);


        verticalLayout_6->addWidget(Ringgroup);

        led1group = new QGroupBox(verticalLayoutWidget_2);
        led1group->setObjectName(QStringLiteral("led1group"));
        frame_2 = new QFrame(led1group);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setGeometry(QRect(0, 20, 991, 91));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        gridLayoutWidget_3 = new QWidget(frame_2);
        gridLayoutWidget_3->setObjectName(QStringLiteral("gridLayoutWidget_3"));
        gridLayoutWidget_3->setGeometry(QRect(10, 0, 881, 85));
        gridLayout_2 = new QGridLayout(gridLayoutWidget_3);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        brightness_7 = new QLabel(gridLayoutWidget_3);
        brightness_7->setObjectName(QStringLiteral("brightness_7"));
        brightness_7->setFrameShape(QFrame::NoFrame);

        gridLayout_2->addWidget(brightness_7, 1, 4, 1, 1);

        brightness_8 = new QLabel(gridLayoutWidget_3);
        brightness_8->setObjectName(QStringLiteral("brightness_8"));
        brightness_8->setFrameShape(QFrame::NoFrame);

        gridLayout_2->addWidget(brightness_8, 1, 3, 1, 1);

        brightness_9 = new QLabel(gridLayoutWidget_3);
        brightness_9->setObjectName(QStringLiteral("brightness_9"));
        brightness_9->setFrameShape(QFrame::NoFrame);

        gridLayout_2->addWidget(brightness_9, 1, 6, 1, 1);

        led1box1 = new QSpinBox(gridLayoutWidget_3);
        led1box1->setObjectName(QStringLiteral("led1box1"));
        led1box1->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led1box1->setMaximum(100);

        gridLayout_2->addWidget(led1box1, 5, 2, 1, 1);

        led1box2 = new QSpinBox(gridLayoutWidget_3);
        led1box2->setObjectName(QStringLiteral("led1box2"));
        led1box2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led1box2->setMaximum(100);

        gridLayout_2->addWidget(led1box2, 5, 3, 1, 1);

        led1box4 = new QSpinBox(gridLayoutWidget_3);
        led1box4->setObjectName(QStringLiteral("led1box4"));
        led1box4->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led1box4->setMaximum(100);

        gridLayout_2->addWidget(led1box4, 5, 5, 1, 1);

        led1box5 = new QSpinBox(gridLayoutWidget_3);
        led1box5->setObjectName(QStringLiteral("led1box5"));
        led1box5->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led1box5->setMaximum(100);

        gridLayout_2->addWidget(led1box5, 5, 6, 1, 1);

        led1box3 = new QSpinBox(gridLayoutWidget_3);
        led1box3->setObjectName(QStringLiteral("led1box3"));
        led1box3->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led1box3->setMaximum(100);

        gridLayout_2->addWidget(led1box3, 5, 4, 1, 1);

        brightness_6 = new QLabel(gridLayoutWidget_3);
        brightness_6->setObjectName(QStringLiteral("brightness_6"));
        brightness_6->setFrameShape(QFrame::NoFrame);

        gridLayout_2->addWidget(brightness_6, 1, 5, 1, 1);

        protled1button = new QPushButton(gridLayoutWidget_3);
        protled1button->setObjectName(QStringLiteral("protled1button"));
        protled1button->setCheckable(true);
        protled1button->setChecked(false);
        protled1button->setAutoDefault(true);

        gridLayout_2->addWidget(protled1button, 1, 0, 1, 1);

        Brightness1_2 = new QLabel(gridLayoutWidget_3);
        Brightness1_2->setObjectName(QStringLiteral("Brightness1_2"));
        Brightness1_2->setFrameShape(QFrame::NoFrame);

        gridLayout_2->addWidget(Brightness1_2, 1, 2, 1, 1);

        Brightness1_3 = new QLabel(gridLayoutWidget_3);
        Brightness1_3->setObjectName(QStringLiteral("Brightness1_3"));
        Brightness1_3->setFrameShape(QFrame::NoFrame);

        gridLayout_2->addWidget(Brightness1_3, 5, 0, 1, 1);


        verticalLayout_6->addWidget(led1group);

        led2group = new QGroupBox(verticalLayoutWidget_2);
        led2group->setObjectName(QStringLiteral("led2group"));
        led2frame = new QFrame(led2group);
        led2frame->setObjectName(QStringLiteral("led2frame"));
        led2frame->setGeometry(QRect(0, 20, 991, 91));
        led2frame->setFrameShape(QFrame::StyledPanel);
        led2frame->setFrameShadow(QFrame::Raised);
        gridLayoutWidget_4 = new QWidget(led2frame);
        gridLayoutWidget_4->setObjectName(QStringLiteral("gridLayoutWidget_4"));
        gridLayoutWidget_4->setGeometry(QRect(10, 0, 881, 85));
        gridLayout_3 = new QGridLayout(gridLayoutWidget_4);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        brightness_10 = new QLabel(gridLayoutWidget_4);
        brightness_10->setObjectName(QStringLiteral("brightness_10"));
        brightness_10->setFrameShape(QFrame::NoFrame);

        gridLayout_3->addWidget(brightness_10, 1, 4, 1, 1);

        brightness_11 = new QLabel(gridLayoutWidget_4);
        brightness_11->setObjectName(QStringLiteral("brightness_11"));
        brightness_11->setFrameShape(QFrame::NoFrame);

        gridLayout_3->addWidget(brightness_11, 1, 3, 1, 1);

        brightness_12 = new QLabel(gridLayoutWidget_4);
        brightness_12->setObjectName(QStringLiteral("brightness_12"));
        brightness_12->setFrameShape(QFrame::NoFrame);

        gridLayout_3->addWidget(brightness_12, 1, 6, 1, 1);

        led2box1 = new QSpinBox(gridLayoutWidget_4);
        led2box1->setObjectName(QStringLiteral("led2box1"));
        led2box1->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box1->setMaximum(100);

        gridLayout_3->addWidget(led2box1, 5, 2, 1, 1);

        led2box2 = new QSpinBox(gridLayoutWidget_4);
        led2box2->setObjectName(QStringLiteral("led2box2"));
        led2box2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box2->setMaximum(100);

        gridLayout_3->addWidget(led2box2, 5, 3, 1, 1);

        led2box3 = new QSpinBox(gridLayoutWidget_4);
        led2box3->setObjectName(QStringLiteral("led2box3"));
        led2box3->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box3->setMaximum(100);

        gridLayout_3->addWidget(led2box3, 5, 5, 1, 1);

        led2box4 = new QSpinBox(gridLayoutWidget_4);
        led2box4->setObjectName(QStringLiteral("led2box4"));
        led2box4->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box4->setMaximum(100);

        gridLayout_3->addWidget(led2box4, 5, 6, 1, 1);

        led2box5 = new QSpinBox(gridLayoutWidget_4);
        led2box5->setObjectName(QStringLiteral("led2box5"));
        led2box5->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box5->setMaximum(100);

        gridLayout_3->addWidget(led2box5, 5, 4, 1, 1);

        led2per4label = new QLabel(gridLayoutWidget_4);
        led2per4label->setObjectName(QStringLiteral("led2per4label"));
        led2per4label->setFrameShape(QFrame::NoFrame);

        gridLayout_3->addWidget(led2per4label, 1, 5, 1, 1);

        protled2button = new QPushButton(gridLayoutWidget_4);
        protled2button->setObjectName(QStringLiteral("protled2button"));
        protled2button->setCheckable(true);
        protled2button->setChecked(false);
        protled2button->setAutoDefault(true);

        gridLayout_3->addWidget(protled2button, 1, 0, 1, 1);

        Brightness1_4 = new QLabel(gridLayoutWidget_4);
        Brightness1_4->setObjectName(QStringLiteral("Brightness1_4"));
        Brightness1_4->setFrameShape(QFrame::NoFrame);

        gridLayout_3->addWidget(Brightness1_4, 1, 2, 1, 1);

        led2brightlabel = new QLabel(gridLayoutWidget_4);
        led2brightlabel->setObjectName(QStringLiteral("led2brightlabel"));
        led2brightlabel->setFrameShape(QFrame::NoFrame);

        gridLayout_3->addWidget(led2brightlabel, 5, 0, 1, 1);


        verticalLayout_6->addWidget(led2group);

        Peltiergroup = new QGroupBox(verticalLayoutWidget_2);
        Peltiergroup->setObjectName(QStringLiteral("Peltiergroup"));
        horizontalLayout = new QHBoxLayout(Peltiergroup);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        peltier_grid = new QGridLayout();
        peltier_grid->setSpacing(6);
        peltier_grid->setObjectName(QStringLiteral("peltier_grid"));
        peltinput1 = new QSpinBox(Peltiergroup);
        peltinput1->setObjectName(QStringLiteral("peltinput1"));
        peltinput1->setMinimum(15);
        peltinput1->setMaximum(40);

        peltier_grid->addWidget(peltinput1, 3, 1, 1, 1);

        peltlabel1 = new QLabel(Peltiergroup);
        peltlabel1->setObjectName(QStringLiteral("peltlabel1"));

        peltier_grid->addWidget(peltlabel1, 0, 1, 1, 1);

        peltinput3 = new QSpinBox(Peltiergroup);
        peltinput3->setObjectName(QStringLiteral("peltinput3"));
        peltinput3->setMinimum(15);
        peltinput3->setMaximum(40);

        peltier_grid->addWidget(peltinput3, 3, 3, 1, 1);

        templabel = new QLabel(Peltiergroup);
        templabel->setObjectName(QStringLiteral("templabel"));

        peltier_grid->addWidget(templabel, 3, 0, 1, 1);

        peltinput4 = new QSpinBox(Peltiergroup);
        peltinput4->setObjectName(QStringLiteral("peltinput4"));
        peltinput4->setMinimum(15);
        peltinput4->setMaximum(40);

        peltier_grid->addWidget(peltinput4, 3, 4, 1, 1);

        peltlabel3 = new QLabel(Peltiergroup);
        peltlabel3->setObjectName(QStringLiteral("peltlabel3"));

        peltier_grid->addWidget(peltlabel3, 0, 3, 1, 1);

        protpeltierbutton = new QPushButton(Peltiergroup);
        protpeltierbutton->setObjectName(QStringLiteral("protpeltierbutton"));
        protpeltierbutton->setCheckable(true);

        peltier_grid->addWidget(protpeltierbutton, 0, 0, 1, 1);

        peltinput2 = new QSpinBox(Peltiergroup);
        peltinput2->setObjectName(QStringLiteral("peltinput2"));
        peltinput2->setMinimum(15);
        peltinput2->setMaximum(40);

        peltier_grid->addWidget(peltinput2, 3, 2, 1, 1);

        peltlabel2 = new QLabel(Peltiergroup);
        peltlabel2->setObjectName(QStringLiteral("peltlabel2"));

        peltier_grid->addWidget(peltlabel2, 0, 2, 1, 1);

        peltlabel4 = new QLabel(Peltiergroup);
        peltlabel4->setObjectName(QStringLiteral("peltlabel4"));

        peltier_grid->addWidget(peltlabel4, 0, 4, 1, 1);

        peltlabel5 = new QLabel(Peltiergroup);
        peltlabel5->setObjectName(QStringLiteral("peltlabel5"));

        peltier_grid->addWidget(peltlabel5, 0, 5, 1, 1);

        peltinput5 = new QSpinBox(Peltiergroup);
        peltinput5->setObjectName(QStringLiteral("peltinput5"));
        peltinput5->setMinimum(15);
        peltinput5->setMaximum(40);

        peltier_grid->addWidget(peltinput5, 3, 5, 1, 1);


        horizontalLayout->addLayout(peltier_grid);


        verticalLayout_6->addWidget(Peltiergroup);

        matrixgroup = new QGroupBox(verticalLayoutWidget_2);
        matrixgroup->setObjectName(QStringLiteral("matrixgroup"));
        matrixframe = new QFrame(matrixgroup);
        matrixframe->setObjectName(QStringLiteral("matrixframe"));
        matrixframe->setGeometry(QRect(0, 20, 991, 91));
        matrixframe->setFrameShape(QFrame::StyledPanel);
        matrixframe->setFrameShadow(QFrame::Raised);
        gridLayoutWidget_5 = new QWidget(matrixframe);
        gridLayoutWidget_5->setObjectName(QStringLiteral("gridLayoutWidget_5"));
        gridLayoutWidget_5->setGeometry(QRect(10, 0, 881, 91));
        gridLayout_4 = new QGridLayout(gridLayoutWidget_5);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        brightness_15 = new QLabel(gridLayoutWidget_5);
        brightness_15->setObjectName(QStringLiteral("brightness_15"));
        brightness_15->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(brightness_15, 1, 3, 1, 1);

        protmatrixbutton = new QPushButton(gridLayoutWidget_5);
        protmatrixbutton->setObjectName(QStringLiteral("protmatrixbutton"));
        protmatrixbutton->setCheckable(true);
        protmatrixbutton->setChecked(false);
        protmatrixbutton->setAutoDefault(true);

        gridLayout_4->addWidget(protmatrixbutton, 1, 0, 1, 1);

        Brightness1_6 = new QLabel(gridLayoutWidget_5);
        Brightness1_6->setObjectName(QStringLiteral("Brightness1_6"));
        Brightness1_6->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(Brightness1_6, 1, 2, 1, 1);

        brightness_17 = new QLabel(gridLayoutWidget_5);
        brightness_17->setObjectName(QStringLiteral("brightness_17"));
        brightness_17->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(brightness_17, 1, 5, 1, 1);

        brightness_16 = new QLabel(gridLayoutWidget_5);
        brightness_16->setObjectName(QStringLiteral("brightness_16"));
        brightness_16->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(brightness_16, 1, 6, 1, 1);

        led2box2_2 = new QSpinBox(gridLayoutWidget_5);
        led2box2_2->setObjectName(QStringLiteral("led2box2_2"));
        led2box2_2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box2_2->setMaximum(100);

        gridLayout_4->addWidget(led2box2_2, 5, 3, 1, 1);

        led2box1_2 = new QSpinBox(gridLayoutWidget_5);
        led2box1_2->setObjectName(QStringLiteral("led2box1_2"));
        led2box1_2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box1_2->setMaximum(100);

        gridLayout_4->addWidget(led2box1_2, 5, 2, 1, 1);

        Brightness1_7 = new QLabel(gridLayoutWidget_5);
        Brightness1_7->setObjectName(QStringLiteral("Brightness1_7"));
        Brightness1_7->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(Brightness1_7, 5, 0, 1, 1);

        brightness_14 = new QLabel(gridLayoutWidget_5);
        brightness_14->setObjectName(QStringLiteral("brightness_14"));
        brightness_14->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(brightness_14, 1, 4, 1, 1);

        led2box3_2 = new QSpinBox(gridLayoutWidget_5);
        led2box3_2->setObjectName(QStringLiteral("led2box3_2"));
        led2box3_2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box3_2->setMaximum(100);

        gridLayout_4->addWidget(led2box3_2, 5, 5, 1, 1);

        led2box4_2 = new QSpinBox(gridLayoutWidget_5);
        led2box4_2->setObjectName(QStringLiteral("led2box4_2"));
        led2box4_2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box4_2->setMaximum(100);

        gridLayout_4->addWidget(led2box4_2, 5, 6, 1, 1);

        led2box5_2 = new QSpinBox(gridLayoutWidget_5);
        led2box5_2->setObjectName(QStringLiteral("led2box5_2"));
        led2box5_2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        led2box5_2->setMaximum(100);

        gridLayout_4->addWidget(led2box5_2, 5, 4, 1, 1);

        Brightness1_8 = new QLabel(gridLayoutWidget_5);
        Brightness1_8->setObjectName(QStringLiteral("Brightness1_8"));
        Brightness1_8->setFrameShape(QFrame::NoFrame);

        gridLayout_4->addWidget(Brightness1_8, 6, 0, 1, 1);

        matrixpattern1 = new QSpinBox(gridLayoutWidget_5);
        matrixpattern1->setObjectName(QStringLiteral("matrixpattern1"));
        matrixpattern1->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        matrixpattern1->setMinimum(1);
        matrixpattern1->setMaximum(3);

        gridLayout_4->addWidget(matrixpattern1, 6, 2, 1, 1);

        matrixpattern1_2 = new QSpinBox(gridLayoutWidget_5);
        matrixpattern1_2->setObjectName(QStringLiteral("matrixpattern1_2"));
        matrixpattern1_2->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        matrixpattern1_2->setMinimum(1);
        matrixpattern1_2->setMaximum(3);

        gridLayout_4->addWidget(matrixpattern1_2, 6, 3, 1, 1);

        matrixpattern1_3 = new QSpinBox(gridLayoutWidget_5);
        matrixpattern1_3->setObjectName(QStringLiteral("matrixpattern1_3"));
        matrixpattern1_3->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        matrixpattern1_3->setMinimum(1);
        matrixpattern1_3->setMaximum(3);

        gridLayout_4->addWidget(matrixpattern1_3, 6, 4, 1, 1);

        matrixpattern1_4 = new QSpinBox(gridLayoutWidget_5);
        matrixpattern1_4->setObjectName(QStringLiteral("matrixpattern1_4"));
        matrixpattern1_4->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        matrixpattern1_4->setMinimum(1);
        matrixpattern1_4->setMaximum(3);

        gridLayout_4->addWidget(matrixpattern1_4, 6, 5, 1, 1);

        matrixpattern1_5 = new QSpinBox(gridLayoutWidget_5);
        matrixpattern1_5->setObjectName(QStringLiteral("matrixpattern1_5"));
        matrixpattern1_5->setButtonSymbols(QAbstractSpinBox::PlusMinus);
        matrixpattern1_5->setMinimum(1);
        matrixpattern1_5->setMaximum(3);

        gridLayout_4->addWidget(matrixpattern1_5, 6, 6, 1, 1);


        verticalLayout_6->addWidget(matrixgroup);

        timegroup = new QGroupBox(verticalLayoutWidget_2);
        timegroup->setObjectName(QStringLiteral("timegroup"));
        verticalLayout_3 = new QVBoxLayout(timegroup);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        timegrid = new QGridLayout();
        timegrid->setSpacing(6);
        timegrid->setObjectName(QStringLiteral("timegrid"));
        runbutton = new QPushButton(timegroup);
        runbutton->setObjectName(QStringLiteral("runbutton"));
        runbutton->setCheckable(true);

        timegrid->addWidget(runbutton, 4, 5, 1, 1);

        itiinput = new QSpinBox(timegroup);
        itiinput->setObjectName(QStringLiteral("itiinput"));
        itiinput->setMaximum(100000);
        itiinput->setValue(100);

        timegrid->addWidget(itiinput, 4, 1, 1, 1);

        replabel = new QLabel(timegroup);
        replabel->setObjectName(QStringLiteral("replabel"));

        timegrid->addWidget(replabel, 4, 2, 1, 1);

        timeinput3 = new QSpinBox(timegroup);
        timeinput3->setObjectName(QStringLiteral("timeinput3"));
        timeinput3->setMaximum(100);

        timegrid->addWidget(timeinput3, 3, 3, 1, 1);

        period1 = new QLabel(timegroup);
        period1->setObjectName(QStringLiteral("period1"));

        timegrid->addWidget(period1, 0, 1, 1, 1);

        repinput = new QSpinBox(timegroup);
        repinput->setObjectName(QStringLiteral("repinput"));
        repinput->setMinimum(1);
        repinput->setMaximum(100);

        timegrid->addWidget(repinput, 4, 3, 1, 1);

        timeinput1 = new QSpinBox(timegroup);
        timeinput1->setObjectName(QStringLiteral("timeinput1"));
        timeinput1->setMaximum(600000);
        timeinput1->setValue(100);

        timegrid->addWidget(timeinput1, 3, 1, 1, 1);

        durationlabel_2 = new QLabel(timegroup);
        durationlabel_2->setObjectName(QStringLiteral("durationlabel_2"));

        timegrid->addWidget(durationlabel_2, 3, 0, 1, 1);

        timeinput4 = new QSpinBox(timegroup);
        timeinput4->setObjectName(QStringLiteral("timeinput4"));
        timeinput4->setMaximum(100);

        timegrid->addWidget(timeinput4, 3, 4, 1, 1);

        period3 = new QLabel(timegroup);
        period3->setObjectName(QStringLiteral("period3"));

        timegrid->addWidget(period3, 0, 3, 1, 1);

        timeinput2 = new QSpinBox(timegroup);
        timeinput2->setObjectName(QStringLiteral("timeinput2"));
        timeinput2->setMaximum(100);

        timegrid->addWidget(timeinput2, 3, 2, 1, 1);

        period2 = new QLabel(timegroup);
        period2->setObjectName(QStringLiteral("period2"));

        timegrid->addWidget(period2, 0, 2, 1, 1);

        period4 = new QLabel(timegroup);
        period4->setObjectName(QStringLiteral("period4"));

        timegrid->addWidget(period4, 0, 4, 1, 1);

        period5 = new QLabel(timegroup);
        period5->setObjectName(QStringLiteral("period5"));

        timegrid->addWidget(period5, 0, 5, 1, 1);

        timeinput5 = new QSpinBox(timegroup);
        timeinput5->setObjectName(QStringLiteral("timeinput5"));
        timeinput5->setMaximum(100);

        timegrid->addWidget(timeinput5, 3, 5, 1, 1);

        itilabel = new QLabel(timegroup);
        itilabel->setObjectName(QStringLiteral("itilabel"));

        timegrid->addWidget(itilabel, 4, 0, 1, 1);

        checkBox = new QCheckBox(timegroup);
        checkBox->setObjectName(QStringLiteral("checkBox"));

        timegrid->addWidget(checkBox, 4, 4, 1, 1);


        verticalLayout_3->addLayout(timegrid);


        verticalLayout_6->addWidget(timegroup);

        tabs->addTab(protocol, QString());
        scrollArea->setWidget(scrollAreaWidgetContents);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1023, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabs->setCurrentIndex(1);
        colourbox->setCurrentIndex(0);
        protled1button->setDefault(false);
        protled2button->setDefault(false);
        protmatrixbutton->setDefault(false);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        contrastlabel->setText(QApplication::translate("MainWindow", "Contrast", Q_NULLPTR));
        binlabel->setText(QApplication::translate("MainWindow", "Binning", Q_NULLPTR));
        cameralabel->setText(QApplication::translate("MainWindow", "Camera", Q_NULLPTR));
        camonbutton->setText(QApplication::translate("MainWindow", "ON", Q_NULLPTR));
        to_avibutton->setText(QApplication::translate("MainWindow", "To AVI", Q_NULLPTR));
        resolutionlabel->setText(QApplication::translate("MainWindow", "Resolution", Q_NULLPTR));
        resolutionbox->clear();
        resolutionbox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "2592x1944", Q_NULLPTR)
         << QApplication::translate("MainWindow", "1920x1080", Q_NULLPTR)
         << QApplication::translate("MainWindow", "1296x972", Q_NULLPTR)
         << QApplication::translate("MainWindow", "1296x730", Q_NULLPTR)
         << QApplication::translate("MainWindow", "640x480", Q_NULLPTR)
        );
        whitebalancelabel->setText(QApplication::translate("MainWindow", "White balance", Q_NULLPTR));
        whitebalancebox->clear();
        whitebalancebox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "off", Q_NULLPTR)
         << QApplication::translate("MainWindow", "auto", Q_NULLPTR)
         << QApplication::translate("MainWindow", "green", Q_NULLPTR)
         << QApplication::translate("MainWindow", "red", Q_NULLPTR)
         << QApplication::translate("MainWindow", "blue", Q_NULLPTR)
         << QApplication::translate("MainWindow", "sunlight", Q_NULLPTR)
         << QApplication::translate("MainWindow", "cloudy", Q_NULLPTR)
         << QApplication::translate("MainWindow", "shade", Q_NULLPTR)
         << QApplication::translate("MainWindow", "tungsten", Q_NULLPTR)
         << QApplication::translate("MainWindow", "fluorescent", Q_NULLPTR)
         << QApplication::translate("MainWindow", "incandescent", Q_NULLPTR)
         << QApplication::translate("MainWindow", "flash", Q_NULLPTR)
         << QApplication::translate("MainWindow", "horizon", Q_NULLPTR)
        );
        exposurelabel->setText(QApplication::translate("MainWindow", "Exposure", Q_NULLPTR));
        verticallabel->setText(QApplication::translate("MainWindow", "vertical offset", Q_NULLPTR));
        windowlabel->setText(QApplication::translate("MainWindow", "Window size", Q_NULLPTR));
        intervallabel->setText(QApplication::translate("MainWindow", "interval between images (sec)", Q_NULLPTR));
        durationlabel->setText(QApplication::translate("MainWindow", "Total duration (sec)", Q_NULLPTR));
        rotationlabel->setText(QApplication::translate("MainWindow", "Rotation", Q_NULLPTR));
        zoomlabel->setText(QApplication::translate("MainWindow", "Digital zoom", Q_NULLPTR));
        modelabel->setText(QApplication::translate("MainWindow", "Mode", Q_NULLPTR));
        modebox->clear();
        modebox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "none", Q_NULLPTR)
         << QApplication::translate("MainWindow", "negative", Q_NULLPTR)
         << QApplication::translate("MainWindow", "solarize", Q_NULLPTR)
         << QApplication::translate("MainWindow", "sketch", Q_NULLPTR)
         << QApplication::translate("MainWindow", "denoise", Q_NULLPTR)
         << QApplication::translate("MainWindow", "emboss", Q_NULLPTR)
         << QApplication::translate("MainWindow", "oilpaint", Q_NULLPTR)
         << QApplication::translate("MainWindow", "hatch", Q_NULLPTR)
         << QApplication::translate("MainWindow", "gpen", Q_NULLPTR)
         << QApplication::translate("MainWindow", "pastel", Q_NULLPTR)
         << QApplication::translate("MainWindow", "watercolor", Q_NULLPTR)
         << QApplication::translate("MainWindow", "film", Q_NULLPTR)
         << QApplication::translate("MainWindow", "blur", Q_NULLPTR)
         << QApplication::translate("MainWindow", "saturation", Q_NULLPTR)
         << QApplication::translate("MainWindow", "colorswap", Q_NULLPTR)
         << QApplication::translate("MainWindow", "washedout", Q_NULLPTR)
         << QApplication::translate("MainWindow", "posterise", Q_NULLPTR)
         << QApplication::translate("MainWindow", "colorpoint", Q_NULLPTR)
         << QApplication::translate("MainWindow", "colorbalance", Q_NULLPTR)
         << QApplication::translate("MainWindow", "cartoon", Q_NULLPTR)
         << QApplication::translate("MainWindow", "deinterlace1", Q_NULLPTR)
         << QApplication::translate("MainWindow", "deinterlace2", Q_NULLPTR)
        );
        colourlabel->setText(QApplication::translate("MainWindow", "Colour effect", Q_NULLPTR));
        colourbox->clear();
        colourbox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "NONE", Q_NULLPTR)
         << QApplication::translate("MainWindow", "BW", Q_NULLPTR)
         << QApplication::translate("MainWindow", "RED", Q_NULLPTR)
         << QApplication::translate("MainWindow", "GREEN", Q_NULLPTR)
         << QApplication::translate("MainWindow", "BLUE", Q_NULLPTR)
        );
        colourbox->setCurrentText(QApplication::translate("MainWindow", "NONE", Q_NULLPTR));
        photobutton->setText(QApplication::translate("MainWindow", "Photo", Q_NULLPTR));
        timelapsebutton->setText(QApplication::translate("MainWindow", "Time lapse", Q_NULLPTR));
        videobutton->setText(QApplication::translate("MainWindow", "Record video", Q_NULLPTR));
        fpslabel->setText(QApplication::translate("MainWindow", "FPS", Q_NULLPTR));
        horizontallabel->setText(QApplication::translate("MainWindow", "Horiz offset", Q_NULLPTR));
        autoexposurebox->setText(QApplication::translate("MainWindow", "Auto exposure", Q_NULLPTR));
        flipimagebox->setText(QApplication::translate("MainWindow", "Flip image", Q_NULLPTR));
        brightnesslabel->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        tabs->setTabText(tabs->indexOf(camera), QApplication::translate("MainWindow", "Camera", Q_NULLPTR));
        led1label->setText(QApplication::translate("MainWindow", "LED 1", Q_NULLPTR));
        led1onbutton->setText(QApplication::translate("MainWindow", "On", Q_NULLPTR));
        led1brightlabel->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        led1brightindicator->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        pulsedurationlabel_2->setText(QApplication::translate("MainWindow", "Pulse brightness (0-100)", Q_NULLPTR));
        pulsedurationlabel->setText(QApplication::translate("MainWindow", "Pulse duration (ms)", Q_NULLPTR));
        led1pulsebutton->setText(QApplication::translate("MainWindow", "Pulse", Q_NULLPTR));
        matrixlabel->setText(QApplication::translate("MainWindow", "Matrix", Q_NULLPTR));
        matrixonbutton->setText(QApplication::translate("MainWindow", "On", Q_NULLPTR));
        matbrightlabel->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        matbrightindicator->setFormat(QApplication::translate("MainWindow", "%p", Q_NULLPTR));
        matrixpat1->setText(QApplication::translate("MainWindow", "Pattern1", Q_NULLPTR));
        matrixpat2->setText(QApplication::translate("MainWindow", "Pattern2", Q_NULLPTR));
        matrixpat3->setText(QApplication::translate("MainWindow", "Pattern3", Q_NULLPTR));
        led2label->setText(QApplication::translate("MainWindow", "LED 2", Q_NULLPTR));
        led2onbutton->setText(QApplication::translate("MainWindow", "On", Q_NULLPTR));
        led2brightlabel_2->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        led2brightindicator->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        led2pulsebrightlabel->setText(QApplication::translate("MainWindow", "Pulse brightness (0-100)", Q_NULLPTR));
        led2pulsedurlabel->setText(QApplication::translate("MainWindow", "Pulse duration (ms)", Q_NULLPTR));
        led2pulsebutton->setText(QApplication::translate("MainWindow", "Pulse", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "Ring", Q_NULLPTR));
        ringonbutton->setText(QApplication::translate("MainWindow", "On", Q_NULLPTR));
        redlabel->setText(QApplication::translate("MainWindow", "Red", Q_NULLPTR));
        redindicator->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        greenlabel->setText(QApplication::translate("MainWindow", "Green", Q_NULLPTR));
        greenindicator->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        bluelabel->setText(QApplication::translate("MainWindow", "Blue", Q_NULLPTR));
        blueindicator->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        bluelabel_2->setText(QApplication::translate("MainWindow", "All", Q_NULLPTR));
        allindicator->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        greenpulselable_2->setText(QApplication::translate("MainWindow", "Red pulse brightness (0-100)", Q_NULLPTR));
        greenpulselabel->setText(QApplication::translate("MainWindow", "Green pulse brightness (0-100)", Q_NULLPTR));
        bluepulselabel->setText(QApplication::translate("MainWindow", "Blue pulse brightness (0-100)", Q_NULLPTR));
        ringpulsedurlabel_2->setText(QApplication::translate("MainWindow", "Pulse duration (ms)", Q_NULLPTR));
        ringpulsebutton->setText(QApplication::translate("MainWindow", "Pulse", Q_NULLPTR));
        tabs->setTabText(tabs->indexOf(lightdevices), QApplication::translate("MainWindow", "Light devices", Q_NULLPTR));
        peltonbutton->setText(QApplication::translate("MainWindow", "On", Q_NULLPTR));
        logtempcheck->setText(QApplication::translate("MainWindow", "Log temperature?", Q_NULLPTR));
        tempclosedloop->setText(QApplication::translate("MainWindow", "closed loop temp control", Q_NULLPTR));
        desiredtemplabel->setText(QApplication::translate("MainWindow", "desired temp", Q_NULLPTR));
        desiredtempbar->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        actualtemplabel->setText(QApplication::translate("MainWindow", "actual temp", Q_NULLPTR));
        actualtempbar->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        tabs->setTabText(tabs->indexOf(peltier), QApplication::translate("MainWindow", "Peltier", Q_NULLPTR));
        servobutton->setText(QApplication::translate("MainWindow", "turn servo", Q_NULLPTR));
        servolabel->setText(QApplication::translate("MainWindow", "servo velocity", Q_NULLPTR));
        servobar->setFormat(QApplication::translate("MainWindow", "%v", Q_NULLPTR));
        tabs->setTabText(tabs->indexOf(servo), QApplication::translate("MainWindow", "servo", Q_NULLPTR));
        Ringgroup->setTitle(QApplication::translate("MainWindow", "Ring", Q_NULLPTR));
        period_2->setText(QApplication::translate("MainWindow", "period 2", Q_NULLPTR));
        protringbutton->setText(QApplication::translate("MainWindow", "ON", Q_NULLPTR));
        blue->setText(QApplication::translate("MainWindow", "Blue brightness", Q_NULLPTR));
        period_1->setText(QApplication::translate("MainWindow", "period 1", Q_NULLPTR));
        period_3->setText(QApplication::translate("MainWindow", "period 3", Q_NULLPTR));
        red->setText(QApplication::translate("MainWindow", "Red brightness", Q_NULLPTR));
        period_5->setText(QApplication::translate("MainWindow", "period 5", Q_NULLPTR));
        period_4->setText(QApplication::translate("MainWindow", "period 4", Q_NULLPTR));
        green->setText(QApplication::translate("MainWindow", "Green brightness", Q_NULLPTR));
        led1group->setTitle(QApplication::translate("MainWindow", "LED 1", Q_NULLPTR));
        brightness_7->setText(QApplication::translate("MainWindow", "period 3", Q_NULLPTR));
        brightness_8->setText(QApplication::translate("MainWindow", "period 2", Q_NULLPTR));
        brightness_9->setText(QApplication::translate("MainWindow", "period 5", Q_NULLPTR));
        brightness_6->setText(QApplication::translate("MainWindow", "period 4", Q_NULLPTR));
        protled1button->setText(QApplication::translate("MainWindow", "ON", Q_NULLPTR));
        Brightness1_2->setText(QApplication::translate("MainWindow", "period 1", Q_NULLPTR));
        Brightness1_3->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        led2group->setTitle(QApplication::translate("MainWindow", "LED 2", Q_NULLPTR));
        brightness_10->setText(QApplication::translate("MainWindow", "period 3", Q_NULLPTR));
        brightness_11->setText(QApplication::translate("MainWindow", "period 2", Q_NULLPTR));
        brightness_12->setText(QApplication::translate("MainWindow", "period 5", Q_NULLPTR));
        led2per4label->setText(QApplication::translate("MainWindow", "period 4", Q_NULLPTR));
        protled2button->setText(QApplication::translate("MainWindow", "ON", Q_NULLPTR));
        Brightness1_4->setText(QApplication::translate("MainWindow", "period 1", Q_NULLPTR));
        led2brightlabel->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        Peltiergroup->setTitle(QApplication::translate("MainWindow", "Peltier", Q_NULLPTR));
        peltlabel1->setText(QApplication::translate("MainWindow", "period 1", Q_NULLPTR));
        templabel->setText(QApplication::translate("MainWindow", "temp", Q_NULLPTR));
        peltlabel3->setText(QApplication::translate("MainWindow", "period 3", Q_NULLPTR));
        protpeltierbutton->setText(QApplication::translate("MainWindow", "ON", Q_NULLPTR));
        peltlabel2->setText(QApplication::translate("MainWindow", "period 2", Q_NULLPTR));
        peltlabel4->setText(QApplication::translate("MainWindow", "period 4", Q_NULLPTR));
        peltlabel5->setText(QApplication::translate("MainWindow", "period 5", Q_NULLPTR));
        matrixgroup->setTitle(QApplication::translate("MainWindow", "Matrix", Q_NULLPTR));
        brightness_15->setText(QApplication::translate("MainWindow", "period 2", Q_NULLPTR));
        protmatrixbutton->setText(QApplication::translate("MainWindow", "ON", Q_NULLPTR));
        Brightness1_6->setText(QApplication::translate("MainWindow", "period 1", Q_NULLPTR));
        brightness_17->setText(QApplication::translate("MainWindow", "period 4", Q_NULLPTR));
        brightness_16->setText(QApplication::translate("MainWindow", "period 5", Q_NULLPTR));
        Brightness1_7->setText(QApplication::translate("MainWindow", "Brightness", Q_NULLPTR));
        brightness_14->setText(QApplication::translate("MainWindow", "period 3", Q_NULLPTR));
        Brightness1_8->setText(QApplication::translate("MainWindow", "Pattern", Q_NULLPTR));
        timegroup->setTitle(QApplication::translate("MainWindow", "Time", Q_NULLPTR));
        runbutton->setText(QApplication::translate("MainWindow", "Run Protocol", Q_NULLPTR));
        replabel->setText(QApplication::translate("MainWindow", "Repetitions", Q_NULLPTR));
        period1->setText(QApplication::translate("MainWindow", "period 1", Q_NULLPTR));
        durationlabel_2->setText(QApplication::translate("MainWindow", "Durat(ms)   ", Q_NULLPTR));
        period3->setText(QApplication::translate("MainWindow", "period 3", Q_NULLPTR));
        period2->setText(QApplication::translate("MainWindow", "period 2", Q_NULLPTR));
        period4->setText(QApplication::translate("MainWindow", "period 4", Q_NULLPTR));
        period5->setText(QApplication::translate("MainWindow", "period 5", Q_NULLPTR));
        itilabel->setText(QApplication::translate("MainWindow", "ITI", Q_NULLPTR));
        checkBox->setText(QApplication::translate("MainWindow", "Record video?", Q_NULLPTR));
        tabs->setTabText(tabs->indexOf(protocol), QApplication::translate("MainWindow", "Protocol", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
