#this is the first working version of the flypi python GUI.
#it was written by T. Baden. Please remember that this is the 
#first working prototype of the software, so many things are
#not made in the most elegant way. Our plan is to improve this on the
#next iterations


# import libraries
import tkinter
import serial
import picamera
import time
import threading


# setup serial
#ser = serial.Serial("COM5", 9600) # for PC
#ser = serial.Serial('/dev/ttyACM0', 19200, timeout = 0.2) # for Arduino Uno from RPi
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.2) # for Arduino Nano from RPi
#ser = serial.Serial('/dev/ttyAMA0') # for Gertuino from RPi

# setup camera
camera = picamera.PiCamera()
camera.led = False
camera.exposure_mode = "fixedfps"
camera.exposure_compensation = 0
camera.brightness = 50

# window setup
main = tkinter.Tk()
main.title('FlyPi v0.09')
main.geometry('385x700')


####################################################
# variables 

zoom_factor = 1.0
Cam_X_offset = 0.0
Cam_Y_offset = 0.0

Cam_framerate = 15
Cam_pixels = 1944
Cam_binning = 1
Cam_size = 480

pic_counter = 0
vid_counter = 0
TL_counter = 0
TL_timing = 1.0
vid_duration = 5 # sec

Cam_mode = 0
Cam_WBmode = 0

temperature = 0.0

ColdSet = tkinter.StringVar()
ColdSet.set("19")
HotSet = tkinter.StringVar()
HotSet.set("32")

Speed_Str = tkinter.StringVar()
Bin_Str = tkinter.StringVar()
Pix_Str = tkinter.StringVar()
Zoom_Str = tkinter.StringVar()
Effect_Str = tkinter.StringVar()
WBM_Str = tkinter.StringVar()
Temp_Str = tkinter.StringVar()
Peltier_Str = tkinter.StringVar()

Speed_Str.set("15")

Bin_Str.set("1")
Pix_Str.set("1944")
Zoom_Str.set("1.0")
Effect_Str.set("0")
WBM_Str.set("0")
Peltier_Str.set("OFF")

##########################################################
# SERIAL COMMANDS TO ARDUINO #############################   
##########################################################

def LEDRing_Mode(): # COMMANDS 1,x
    ser.write(b"11,")
def LEDRing_Bright():
    ser.write(b"12,")
def LEDRing_Dim():
    ser.write(b"13,")
def LEDRing_Zap():
    ser.write(b"14,")
def LEDRing_ZapMode():
    ser.write(b"15,")
def LEDRing_LongZap():
    ser.write(b"16,")
def LEDRing_Baseline():
    ser.write(b"17,")
def LEDRing_Rotateleft():
    ser.write(b"18,")
def LEDRing_Rotateright():
    ser.write(b"19,")

def LED1_ON():  # COMMANDS 2,x
    ser.write(b"21,")
def LED1_OFF():
    ser.write(b"22,")
def LED1_ZAP():
    ser.write(b"23,")

def LED2_ON():  # COMMANDS 3,x
    ser.write(b"31,")
def LED2_OFF():
    ser.write(b"32,")
def LED2_ZAP():
    ser.write(b"33,")

def Peltier_OFF(): # COMMANDS 4,x
    ser.write(b"41,")
    Peltier_Str.set("OFF")
def Peltier_Low(): # COMMANDS 4,x
    ser.write(b"42,")
    var = int(Peltier_ColdSet.get())
    Serial_var = bytes(str(var)+",", 'utf-8')
    ser.write(Serial_var)
    Peltier_Str.set("Cold")
      
def Peltier_High(): # COMMANDS 4,x
    ser.write(b"43,")
    var = int(Peltier_HotSet.get())
    Serial_var = bytes(str(var)+",", 'utf-8')
    ser.write(Serial_var)
    Peltier_Str.set("Hot")

def LEDMatrix_Mode(): # COMMANDS 5,x
    ser.write(b"51,")
def LEDMatrix_Bright():
    ser.write(b"52,")
def LEDMatrix_Dim():
    ser.write(b"53,")

def Flash_RedLED():
    ser.write(b"91,")
def Flash_GreenLED():
    ser.write(b"92,")
def Flash_BlueLED():
    ser.write(b"93,")




##################################################
######  Timers                         ###########
##################################################

def updateTemp():
    ser.write(b"99,")
    temperature = ser.read(2)
    Temp_Str.set(temperature)
    t = threading.Timer(0.4, updateTemp)
    t.start()

updateTemp()

##################################################
######  ACTIONS                        ###########
##################################################
# actions

def Cam_ON():
    global Cam_framerate
    global Cam_pixels  
    global Cam_size  
    camera.framerate = (Cam_framerate)
    camera.resolution = (Cam_pixels,Cam_pixels)
    camera.start_preview()
    camera.preview_fullscreen = False
    camera.preview.window = (0,0,Cam_size,Cam_size)

def Cam_OFF():
    camera.stop_preview()

def Cam_ONplus():
    global Cam_size
    if Cam_size<2000:
       Cam_size+=100
    camera.preview.window = (0,0,Cam_size,Cam_size)

def Cam_ONminus():
    global Cam_size
    if Cam_size>180:
       Cam_size-=100
    camera.preview.window = (0,0,Cam_size,Cam_size)

def Cam_refresh():
    global Cam_binning
    global Cam_pixels
    global Cam_framerate
    camera.framerate = (Cam_framerate)
    camera.resolution = (Cam_pixels,Cam_pixels)
    Speed_Str.set(Cam_framerate)
    Bin_Str.set(Cam_binning)
    Pix_Str.set(Cam_pixels)

def Cam_Snap():
    #global Cam_framerate
    #global Cam_pixels    
    #global zoom_factor
    #global Cam_X_offset  
    #global Cam_Y_offset
    #zoom_win = 1/zoom_factor
    #zoom_pos = (1-zoom_win) / 2
    #camera.framerate = (Cam_framerate)
    #camera.resolution = (Cam_pixels,Cam_pixels)
    #camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)
    
    #camera.start_preview()
    #camera.preview_fullscreen = False
    #camera.preview.window = (0,0,1000,1000)
    #time.sleep(5) # wait 5 sec to adjust pic

    filePath = "/home/pi/Desktop/FlyPi_Snaps/"
    baseName = "snap"
    global pic_counter
    pic_counter+=1
    camera.capture(filePath+baseName+str(pic_counter)+".jpeg")
    print ("Snapped pic",pic_counter)

def Cam_TLapse():
    global TL_counter
    global TL_counter_current
    global TL_timing
    global TL_nFrames
    filePath = "/home/pi/Desktop/FlyPi_TimeLapse/"
    baseName = "TimeLapse"
    TL_counter_current+=1
    print ("TL",TL_counter_current,"/",TL_nFrames)
    camera.capture(filePath+baseName+str(TL_counter)+"_"+str(TL_counter_current)+".jpeg")
    if TL_counter_current<TL_nFrames:
      t2 = threading.Timer(TL_timing, Cam_TLapse)
      t2.start()
    else:
      print ("...done")

def Cam_TLapse_init():
    global TL_counter
    global TL_counter_current
    global vid_duration
    global TL_timing
    global TL_nFrames
    vid_duration = float(Cam_Vid_length.get())  
    TL_timing = float(Cam_TL_Interval.get())  
    if TL_timing<1.0:
       TL_timing = 1.0
       print ("Forced interval to 1.0 s...") 
    TL_nFrames = vid_duration / TL_timing
    TL_counter+=1
    TL_counter_current = 0
    print ("Starting TimeLapse", TL_counter,"...")
    Cam_TLapse()

def Cam_Vid():
    global Cam_framerate
    global Cam_pixels    
    global zoom_factor
    global Cam_X_offset  
    global Cam_Y_offset
    if Cam_pixels > 972: # ie if not x2 or higher binning
       BinX2();
    zoom_win = 1/zoom_factor
    zoom_pos = (1-zoom_win) / 2
    camera.framerate = (Cam_framerate)
    camera.resolution = (Cam_pixels,Cam_pixels)
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)

    filePath = "/home/pi/Desktop/FlyPi_Videos/"
    baseName = "Video"
    global vid_counter
    global vid_duration
    vid_duration = float(Cam_Vid_length.get())
    vid_counter+=1

    camera.start_preview()
    camera.preview_fullscreen = False
    camera.preview.window = (0,0,1000,1000)
    print ("waiting 2 s while camera settles...")
    time.sleep(2) # wait 2 sec to adjust pic
    print ("recording",vid_counter,"...")
    camera.start_recording( output = filePath+baseName+str(vid_counter)+".h264",
                            format = "h264",
                            #quality = 10, # (10 best, 40 worst)
                            bitrate = 17000000) 
    camera.wait_recording(vid_duration)
    print ("...done!")
    camera.stop_recording()

##########################################################

def BinX1():
    global Cam_binning
    global Cam_pixels
    global Cam_framerate
    Cam_binning = 1
    Cam_pixels = 1944
    Cam_framerate = 15
    Cam_refresh()   
def BinX2():
    global Cam_binning
    global Cam_pixels
    global Cam_framerate
    Cam_binning = 2
    Cam_pixels = 972
    Cam_framerate = 42
    Cam_refresh()

def BinX4():
    global Cam_binning
    global Cam_pixels
    global Cam_framerate
    Cam_binning = 4
    Cam_pixels = 480
    Cam_framerate = 90
    Cam_refresh()

##########################################################

def Zoom_plus():
    global zoom_factor
    global Cam_X_offset  
    global Cam_Y_offset
    zoom_factor*=1.1
    if zoom_factor>10:
       zoom_factor = 10
    zoom_win = 1/zoom_factor
    zoom_pos = (1-zoom_win) / 2
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)
    Zoom_Str.set(zoom_factor)

def Zoom_minus():
    global zoom_factor
    global Cam_X_offset  
    global Cam_Y_offset
    zoom_factor/=1.1
    if zoom_factor<1:
       zoom_factor = 1
    zoom_win = 1/zoom_factor
    zoom_pos = (1-zoom_win) / 2
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)
    Zoom_Str.set(zoom_factor)

def DigiZoomleft():
    global zoom_factor
    global Cam_X_offset  
    global Cam_Y_offset
    if Cam_X_offset>-100:
       Cam_X_offset-=2
    zoom_win = 1/zoom_factor
    zoom_pos = ((1-zoom_win) / 2)
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)

def DigiZoomright():
    global zoom_factor
    global Cam_X_offset
    global Cam_Y_offset    
    if Cam_X_offset<100:
       Cam_X_offset+=2
    zoom_win = 1/zoom_factor
    zoom_pos = ((1-zoom_win) / 2) 
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)

def DigiZoomup():
    global zoom_factor
    global Cam_X_offset  
    global Cam_Y_offset
    if Cam_Y_offset>-100:
       Cam_Y_offset-=2
    zoom_win = 1/zoom_factor
    zoom_pos = ((1-zoom_win) / 2)
    camera.zoom = Peltier_HotSet(zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)

def DigiZoomdown():
    global zoom_factor
    global Cam_X_offset
    global Cam_Y_offset    
    if Cam_Y_offset<100:
       Cam_Y_offset+=2
    zoom_win = 1/zoom_factor
    zoom_pos = ((1-zoom_win) / 2) 
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)

def DigiZoomCentre():
    global zoom_factor
    global Cam_X_offset  
    global Cam_Y_offset
    Cam_X_offset = 0.0
    Cam_Y_offset = 0.0
    zoom_win = 1/zoom_factor
    zoom_pos = ((1-zoom_win) / 2)
    camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)

##########################################################

# framerate and exposure
def fps_plus():
    global Cam_framerate
    if Cam_framerate<90:
       Cam_framerate+=1
    Cam_refresh()

def fps_minus():
    global Cam_framerate
    if Cam_framerate>1:
       Cam_framerate-=1
    Cam_refresh()

def Cam_AutoExpON():
    camera.exposure_mode = 'auto'
def Cam_AutoExpOff():
    camera.exposure_mode = 'off'

def Cam_BrightPlus():
    b = camera.brightness
    if b<95:
       b+=5
    camera.brightness = b
       
def Cam_BrightMinus():
    b = camera.brightness
    if b>5:
       b-=5
    camera.brightness = b

def Cam_ContrastPlus():
    c = camera.contrast
    if c<91:
       c+=10
    camera.contrast = c
       
def Cam_ContrastMinus():
    c = camera.contrast
    if c>-91:
       c-=10
    camera.contrast = c

def Cam_ExpSpeedPlus():
    c = camera.exposure_compensation
    if c<25:
       c+=1
    camera.exposure_compensation = c
       
def Cam_ExpSpeedMinus():
    c = camera.exposure_compensation
    if c>-25:
       c-=1
    camera.exposure_compensation = c  
    
    
# white balance
def Cam_AutoWBON():
    camera.awb_mode = 'auto'
def Cam_AutoWBOFF():
    r,b = camera.awb_gains    
    camera.awb_mode = 'off'
    camera.awb_gains = r,b

def Cam_WBRonly():
    camera.awb_mode = 'off'
    camera.awb_gains = 8.0, 1
    
def Cam_WBGonly():
    camera.awb_mode = 'off'
    camera.awb_gains = 1, 1
    
def Cam_WBBonly():
    camera.awb_mode = 'off'
    camera.awb_gains = 1, 8.0
    
def Cam_WBModePlus():
   global Cam_WBmode
   if Cam_WBmode<7:
      Cam_WBmode+=1
   else:
      Cam_WBmode=0
   Cam_WBMode_lookup()

def Cam_ColourR():
   camera.color_effects = 0,255
def Cam_ColourG():
   camera.color_effects = 0,0
def Cam_ColourB():
   camera.color_effects = 255,0
def Cam_ColourBW():
   camera.color_effects = 128,128
def Cam_ColourNone():
   camera.color_effects = None



def Cam_WBMode_lookup():
   global Cam_WBmode
   WBM_Str.set(Cam_WBmode)  
   if Cam_WBmode==0:
      camera.awb_mode = 'auto'
   if Cam_WBmode==1:
      camera.awb_mode = 'sunlight'
   if Cam_WBmode==2:
      camera.awb_mode = 'cloudy'
   if Cam_WBmode==3:
      camera.awb_mode = 'shade'
   if Cam_WBmode==4:
      camera.awb_mode = 'tungsten'
   if Cam_WBmode==5:
      camera.awb_mode = 'fluorescent'
   if Cam_WBmode==6:
      camera.awb_mode = 'incandescent'
   if Cam_WBmode==7:
      camera.awb_mode = 'flash'
   if Cam_WBmode==8:
      camera.awb_mode = 'horizon'   

# Rotate and stuff
def Cam_Rotate1():
    val = camera.rotation
    camera.rotation = val + 90

def Cam_Flip1():
    if camera.hflip:
       camera.hflip = False
    else: 
       camera.hflip = True

def Cam_Mode():
   global Cam_mode
   if Cam_mode>0:
      Cam_mode=0
   else:
      Cam_mode=1
   Cam_Mode_lookup()

def Cam_ModePlus():
   global Cam_mode
   if Cam_mode<20:
      Cam_mode+=1
   else:
      Cam_mode=0
   Cam_Mode_lookup()

def Cam_ModeMinus():
   global Cam_mode
   if Cam_mode>0:
      Cam_mode-=1
   else:
      Cam_mode=20
   Cam_Mode_lookup()

def Cam_Mode_lookup():
   global Cam_mode
   Effect_Str.set(Cam_mode)  
   if Cam_mode==0:
      camera.image_effect = 'none'
   if Cam_mode==1:
      camera.image_effect = 'negative'
   if Cam_mode==2:
      camera.image_effect = 'solarize'
   if Cam_mode==3:
      camera.image_effect = 'sketch'
   if Cam_mode==4:
      camera.image_effect = 'denoise'
   if Cam_mode==5:
      camera.image_effect = 'emboss'
   if Cam_mode==6:
      camera.image_effect = 'oilpaint'
   if Cam_mode==7:
      camera.image_effect = 'hatch'
   if Cam_mode==8:
      camera.image_effect = 'gpen'
   if Cam_mode==9:
      camera.image_effect = 'pastel'
   if Cam_mode==10:
      camera.image_effect = 'watercolor'
   if Cam_mode==11:
      camera.image_effect = 'film'
   if Cam_mode==12:
      camera.image_effect = 'blur'
   if Cam_mode==13:
      camera.image_effect = 'saturation'
   if Cam_mode==14:
      camera.image_effect = 'colorswap'
   if Cam_mode==15:
      camera.image_effect = 'washedout'
   if Cam_mode==16:
      camera.image_effect = 'posterise'
   if Cam_mode==17:
      camera.image_effect = 'colorpoint'
   if Cam_mode==18:
      camera.image_effect = 'colorbalance'
   if Cam_mode==19:
      camera.image_effect = 'cartoon'
   if Cam_mode==20:
      camera.image_effect = 'deinterlace1'
   if Cam_mode==21:
      camera.image_effect = 'deinterlace2'

##########################################################
#### GUI DEFINITIONS #####################################
##########################################################

# LED RING buttons
LED_label = tkinter.Label(master=main, text = "LED Ring")
LED_label.place(x=43,y=45-40)
Ring_mode = tkinter.Button(master=main, text = "Mode", command = LEDRing_Mode, repeatdelay = 1)
Ring_mode.place(x=20,y=70-40,width=50,height=40)
Ring_Rotate1 = tkinter.Button(master=main, text = "rot->", command = LEDRing_Rotateright, repeatdelay = 1)
Ring_Rotate1.place(x=70,y=70-40,width=50,height=20)
Ring_Rotate2 = tkinter.Button(master=main, text = "<-rot", command = LEDRing_Rotateleft, repeatdelay = 1)
Ring_Rotate2.place(x=70,y=90-40,width=50,height=20)
Dimmer = tkinter.Button(master=main, text = "--", command = LEDRing_Dim, repeatdelay = 1)
Dimmer.place(x=20,y=115-40,width=50,height=20)
Brighter = tkinter.Button(master=main, text = "++", command = LEDRing_Bright, repeatdelay = 1)
Brighter.place(x=70,y=115-40,width=50,height=20)
ZAP = tkinter.Button(master=main, text = "ZAP!", command = LEDRing_Zap, repeatdelay = 1 )
ZAP.place(x=20,y=140-40,width=50,height=40)
ZAPMode = tkinter.Button(master=main, text = "Colour", command = LEDRing_ZapMode, repeatdelay = 1 )
ZAPMode.place(x=70,y=140-40,width=50,height=40)

##########################################################

# LED MATRIX buttons
LED_Matrix_label = tkinter.Label(master=main, text = "LED Matrix")
LED_Matrix_label.place(x=275,y=45-40)
Matrix_mode = tkinter.Button(master=main, text = "Mode", command = LEDMatrix_Mode, repeatdelay = 1)
Matrix_mode.place(x=260,y=70-40,width=50,height=40)
Matrix_Brighter = tkinter.Button(master=main, text = "++", command = LEDMatrix_Bright, repeatdelay = 1)
Matrix_Brighter.place(x=310,y=70-40,width=50,height=20)
Matrix_Dimmer = tkinter.Button(master=main, text = "--", command = LEDMatrix_Dim, repeatdelay = 1)
Matrix_Dimmer.place(x=310,y=90-40,width=50,height=20)

##########################################################

# Power LED buttons
PowerLED_label = tkinter.Label(master=main, text = "LED  LED   Pelt.")
PowerLED_label.place(x=140,y=45-40)
PowerLED1_ON = tkinter.Button(master=main, text = "ON", command = LED1_ON, repeatdelay = 1)
PowerLED1_ON.place(x=140,y=90-40,width=30,height=20)
PowerLED1_OFF = tkinter.Button(master=main, text = "OFF", command = LED1_OFF, repeatdelay = 1)
PowerLED1_OFF.place(x=140,y=70-40,width=30,height=20)
PowerLED1_ZAP = tkinter.Button(master=main, text = "ZAP", command = LED1_ZAP, repeatdelay = 1)
PowerLED1_ZAP.place(x=140,y=110-40,width=30,height=20)

PowerLED2_ON = tkinter.Button(master=main, text = "ON", command = LED2_ON, repeatdelay = 1)
PowerLED2_ON.place(x=170,y=90-40,width=30,height=20)
PowerLED2_OFF = tkinter.Button(master=main, text = "OFF", command = LED2_OFF, repeatdelay = 1)
PowerLED2_OFF.place(x=170,y=70-40,width=30,height=20)
PowerLED2_ZAP = tkinter.Button(master=main, text = "ZAP", command = LED2_ZAP, repeatdelay = 1)
PowerLED2_ZAP.place(x=170,y=110-40,width=30,height=20)

# Peltier
Peltier_OFFButton = tkinter.Button(master=main, text = "OFF", command = Peltier_OFF, repeatdelay = 1)
Peltier_OFFButton.place(x=200,y=70-40,width=40,height=20)
Peltier_Hot = tkinter.Button(master=main, text = "Hi", command = Peltier_High, repeatdelay = 1)
Peltier_Hot.place(x=200,y=90-40,width=40,height=20)
Peltier_Hot = tkinter.Button(master=main, text = "Lo", command = Peltier_Low, repeatdelay = 1)
Peltier_Hot.place(x=200,y=110-40,width=40,height=20)

PeltierHot_label = tkinter.Label(master=main, text = "High T:")
PeltierHot_label.place(x=140,y=138-40)
Peltier_HotSet = tkinter.Spinbox(master=main, from_=15, to=35, textvariable = HotSet)
Peltier_HotSet.place(x=200,y=138-40,width=40,height=20) 

PeltierCold_label = tkinter.Label(master=main, text = "Low T:")
PeltierCold_label.place(x=140,y=160-40)
Peltier_ColdSet = tkinter.Spinbox(master=main, from_=15, to=35, textvariable = ColdSet)
Peltier_ColdSet.place(x=200,y=160-40,width=40,height=20) 


##########################################################
# CAM buttons
Cam_label = tkinter.Label(master=main, text = "Camera")
Cam_label.place(x=44,y=225-70)
Cam_SwitchON = tkinter.Button(master=main, text = "ON", command = Cam_ON, repeatdelay = 1)
Cam_SwitchON.place(x=20,y=250-70,width=40,height=40)
Cam_SwitchOFF = tkinter.Button(master=main, text = "OFF", command = Cam_OFF, repeatdelay = 1)
Cam_SwitchOFF.place(x=60,y=250-70,width=40,height=40)
Cam_SwitchPlus = tkinter.Button(master=main, text = "+", command = Cam_ONplus, repeatdelay = 1)
Cam_SwitchPlus.place(x=100,y=250-70,width=20,height=20)
Cam_SwitchMinus = tkinter.Button(master=main, text = "-", command = Cam_ONminus, repeatdelay = 1)
Cam_SwitchMinus.place(x=100,y=270-70,width=20,height=20)

Cam_BinX1 = tkinter.Button(master=main, text = "x1", command = BinX1, repeatdelay = 1)
Cam_BinX1.place(x=20,y=300-70,width=30,height=30)
Cam_BinX2 = tkinter.Button(master=main, text = "x2", command = BinX2, repeatdelay = 1)
Cam_BinX2.place(x=55,y=300-70,width=30,height=30)
Cam_BinX4 = tkinter.Button(master=main, text = "x4", command = BinX4, repeatdelay = 1)
Cam_BinX4.place(x=90,y=300-70,width=30,height=30)

Cam_fpsPlus = tkinter.Button(master=main, text = "fps+", command = fps_plus, repeatdelay = 1)
Cam_fpsPlus.place(x=20,y=340-70,width=50,height=30)
Cam_fpsMinus = tkinter.Button(master=main, text = "fps-", command = fps_minus, repeatdelay = 1)
Cam_fpsMinus.place(x=70,y=340-70,width=50,height=30)

#######################################################
# DigiZoom panel
DigiZoom_label = tkinter.Label(master=main, text = "Digital Zoom")
DigiZoom_label.place(x=146,y=225-70)

Cam_ZoomPlus = tkinter.Button(master=main, text = "+", command = Zoom_plus, repeatdelay = 1)
Cam_ZoomPlus.place(x=220,y=250-70,width=20,height=20)
Cam_ZoomMinus = tkinter.Button(master=main, text = "-", command = Zoom_minus, repeatdelay = 1)
Cam_ZoomMinus.place(x=220,y=270-70,width=20,height=20)

Cam_DigiZoomleft = tkinter.Button(master=main, text = "<", command = DigiZoomleft, repeatdelay = 1)
Cam_DigiZoomleft.place(x=140,y=305-70,width=30,height=30)
Cam_DigiZoomright = tkinter.Button(master=main, text = ">", command = DigiZoomright, repeatdelay = 1)
Cam_DigiZoomright.place(x=210,y=305-70,width=30,height=30)
Cam_DigiZoomup = tkinter.Button(master=main, text = "^", command = DigiZoomup, repeatdelay = 1)
Cam_DigiZoomup.place(x=175,y=270-70,width=30,height=30)
Cam_DigiZoomdown = tkinter.Button(master=main, text = "V", command = DigiZoomdown, repeatdelay = 1)
Cam_DigiZoomdown.place(x=175,y=340-70,width=30,height=30)

Cam_DigiZoomZero = tkinter.Button(master=main, text = "0", command = DigiZoomCentre, repeatdelay = 1)
Cam_DigiZoomZero.place(x=175,y=305-70,width=30,height=30)

#########################################################
# Advanced Camera
Cam_AutoExplabel = tkinter.Label(master=main, text = "Exposure")
Cam_AutoExplabel.place(x=44,y=395-80)
Cam_AutoExpON = tkinter.Button(master=main, text = "ON", command = Cam_AutoExpON, repeatdelay = 1)
Cam_AutoExpON.place(x=20,y=420-80,width=40,height=20)
Cam_AutoExpOFF = tkinter.Button(master=main, text = "OFF", command = Cam_AutoExpOff, repeatdelay = 1)
Cam_AutoExpOFF.place(x=20,y=440-80,width=40,height=20)
Cam_BrightPlus = tkinter.Button(master=main, text = "+", command = Cam_BrightPlus, repeatdelay = 1)
Cam_BrightPlus.place(x=60,y=420-80,width=20,height=20)
Cam_Brightminus = tkinter.Button(master=main, text = "-", command = Cam_BrightMinus, repeatdelay = 1)
Cam_Brightminus.place(x=60,y=440-80,width=20,height=20)
Cam_ContrastPlus =tkinter.Button(master=main, text = "+", command = Cam_ContrastPlus, repeatdelay = 1)
Cam_ContrastPlus.place(x=80,y=420-80,width=20,height=20)
Cam_ContrastMinus = tkinter.Button(master=main, text = "-", command = Cam_ContrastMinus, repeatdelay = 1)
Cam_ContrastMinus.place(x=80,y=440-80,width=20,height=20)
Cam_ExpSpeedPlus = tkinter.Button(master=main, text = "+", command = Cam_ExpSpeedPlus, repeatdelay = 1)
Cam_ExpSpeedPlus.place(x=100,y=420-80,width=20,height=20)
Cam_ExpSpeedMinus = tkinter.Button(master=main, text = "-", command = Cam_ExpSpeedMinus, repeatdelay = 1)
Cam_ExpSpeedMinus.place(x=100,y=440-80,width=20,height=20)

Cam_AutoWBlabel = tkinter.Label(master=main, text = "White balance")
Cam_AutoWBlabel.place(x=144,y=395-80)
Cam_AutoWBON = tkinter.Button(master=main, text = "ON", command = Cam_AutoWBON, repeatdelay = 1)
Cam_AutoWBON.place(x=140,y=420-80,width=30,height=40)
Cam_AutoWBOFF = tkinter.Button(master=main, text = "OFF", command = Cam_AutoWBOFF, repeatdelay = 1)
Cam_AutoWBOFF.place(x=170,y=420-80,width=30,height=40)
Cam_WBR = tkinter.Button(master=main, text = "R", command = Cam_WBRonly, repeatdelay = 1)
Cam_WBR.place(x=200,y=420-80,width=20,height=20)
Cam_WBG = tkinter.Button(master=main, text = "G", command = Cam_WBGonly, repeatdelay = 1)
Cam_WBG.place(x=220,y=420-80,width=20,height=20)
Cam_WBB = tkinter.Button(master=main, text = "B", command = Cam_WBBonly, repeatdelay = 1)
Cam_WBB.place(x=200,y=440-80,width=20,height=20)
Cam_WBM = tkinter.Button(master=main, text = "M", command = Cam_WBModePlus, repeatdelay = 1)
Cam_WBM.place(x=220,y=440-80,width=20,height=20)

Cam_Rotate1 = tkinter.Button(master=main, text = "Rotate", command = Cam_Rotate1, repeatdelay = 1)
Cam_Rotate1.place(x=20,y=480-80,width=50,height=40)
Cam_Flip1 = tkinter.Button(master=main, text = "Flip", command = Cam_Flip1, repeatdelay = 1)
Cam_Flip1.place(x=70,y=480-80,width=50,height=40)

Cam_Effect = tkinter.Button(master=main, text = "Effect", command = Cam_Mode, repeatdelay = 1)
Cam_Effect.place(x=140,y=480-80,width=40,height=20)
Cam_Effectplus = tkinter.Button(master=main, text = "+", command = Cam_ModePlus, repeatdelay = 1)
Cam_Effectplus.place(x=140,y=500-80,width=20,height=20)
Cam_Effectminus = tkinter.Button(master=main, text = "-", command = Cam_ModeMinus, repeatdelay = 1)
Cam_Effectminus.place(x=160,y=500-80,width=20,height=20)

Cam_ColourNone = tkinter.Button(master=main, text = "RGB", command = Cam_ColourNone, repeatdelay = 1)
Cam_ColourNone.place(x=180,y=480-80,width=30,height=20)
Cam_ColourBW = tkinter.Button(master=main, text = "BW", command = Cam_ColourBW, repeatdelay = 1)
Cam_ColourBW.place(x=210,y=480-80,width=30,height=20)
Cam_ColourR = tkinter.Button(master=main, text = "R", command = Cam_ColourR, repeatdelay = 1)
Cam_ColourR.place(x=180,y=500-80,width=20,height=20)
Cam_ColourB = tkinter.Button(master=main, text = "B", command = Cam_ColourB, repeatdelay = 1)
Cam_ColourB.place(x=220,y=500-80,width=20,height=20)
Cam_ColourG = tkinter.Button(master=main, text = "G", command = Cam_ColourG, repeatdelay = 1)
Cam_ColourG.place(x=200,y=500-80,width=20,height=20)


#########################################################
# Snap/ record
Cam_Snap = tkinter.Button(master=main, text = "Photo", command = Cam_Snap, repeatdelay = 1)
Cam_Snap.place(x=20,y=540-90,width=50,height=40)
Cam_Snap = tkinter.Button(master=main, text = "T-lapse", command = Cam_TLapse_init, repeatdelay = 1)
Cam_Snap.place(x=70,y=560-90,width=50,height=20)
Cam_Vid = tkinter.Button(master=main, text = "Video", command = Cam_Vid, repeatdelay = 1)
Cam_Vid.place(x=70,y=540-90,width=50,height=20) 

Cam_TL_Int_label = tkinter.Label(master=main, text = "int.")
Cam_TL_Int_label.place(x=150,y=560-90) 

Cam_Vid_length_label = tkinter.Label(master=main, text = "dur.")
Cam_Vid_length_label.place(x=150,y=540-90)

Cam_Vid_length = tkinter.Entry(master=main)
Cam_Vid_length.place(x=120,y=540-90,width=30,height=20)
Cam_TL_Interval = tkinter.Entry(master=main)
Cam_TL_Interval.place(x=120,y=560-90,width=30,height=20) 
 

###########################################################



Peltier_label = tkinter.Label(master=main, text = "Peltier:")
Peltier_label.place(x=260,y=140-40)
Peltier_label = tkinter.Label(master=main, textvariable=Peltier_Str)
Peltier_label.place(x=335,y=140-40)

temperature_label = tkinter.Label(master=main, text = "Temp. (°C):")
temperature_label.place(x=260,y=160-40)
temperature_label = tkinter.Label(master=main, textvariable=Temp_Str)
temperature_label.place(x=335,y=160-40)


Cam_Speedlabel_Unit = tkinter.Label(master=main, text = "FRate (Hz):")
Cam_Speedlabel_Unit.place(x=260,y=250-70)
Cam_Speedlabel = tkinter.Label(master=main, textvariable=Speed_Str)
Cam_Speedlabel.place(x=335,y=250-70)

Cam_Pixlabel_Unit = tkinter.Label(master=main, text = "Res. (px): ")
Cam_Pixlabel_Unit.place(x=260,y=270-70)
Cam_Pixlabel = tkinter.Label(master=main, textvariable=Pix_Str)
Cam_Pixlabel.place(x=335,y=270-70)

Cam_Binlabel_Unit = tkinter.Label(master=main, text = "Binning (x):")
Cam_Binlabel_Unit.place(x=260,y=290-70)
Cam_Binlabel = tkinter.Label(master=main, textvariable=Bin_Str)
Cam_Binlabel.place(x=335,y=290-70)

Zoom_label_Unit = tkinter.Label(master=main, text = "Zoom (x):")
Zoom_label_Unit.place(x=260,y=310-70)
Zoom_label = tkinter.Label(master=main, textvariable=Zoom_Str)
Zoom_label.place(x=335,y=310-70)

WBM_label = tkinter.Label(master=main, text = "WB Mode:")
WBM_label.place(x=260,y=440-70)
WBM_label = tkinter.Label(master=main, textvariable=WBM_Str)
WBM_label.place(x=335,y=440-70)

Effect_label = tkinter.Label(master=main, text = "Effect:")
Effect_label.place(x=260,y=500-70)
Effect_label = tkinter.Label(master=main, textvariable=Effect_Str)
Effect_label.place(x=335,y=500-70)




##############################################################

## Protocol window

t1_Temp = tkinter.IntVar()
t2_Temp = tkinter.IntVar()
t3_Temp = tkinter.IntVar()
t4_Temp = tkinter.IntVar()
t5_Temp = tkinter.IntVar()
t1_LED = tkinter.IntVar()
t2_LED = tkinter.IntVar()
t3_LED = tkinter.IntVar()
t4_LED = tkinter.IntVar()
t5_LED = tkinter.IntVar()
t1_Ring = tkinter.IntVar()
t2_Ring = tkinter.IntVar()
t3_Ring = tkinter.IntVar()
t4_Ring = tkinter.IntVar()
t5_Ring = tkinter.IntVar()
t1_Time = tkinter.IntVar()
t2_Time = tkinter.IntVar()
t3_Time = tkinter.IntVar()
t4_Time = tkinter.IntVar()
t5_Time = tkinter.IntVar()

DontRecord = 1

def DryRun():
    global DontRecord
    DontRecord = 1
    TotalTime = int(Protocol_1_7.get())+int(Protocol_2_7.get())+int(Protocol_3_7.get())+int(Protocol_4_7.get())+int(Protocol_5_7.get())
    if TotalTime>0:
      Execute_protocol()
    else:
      print("Total Time is Zero! ... Protocol aborted")

def FullRun():
    global DontRecord
    DontRecord = 0
    TotalTime = int(Protocol_1_7.get())+int(Protocol_2_7.get())+int(Protocol_3_7.get())+int(Protocol_4_7.get())+int(Protocol_5_7.get())
    if TotalTime>0:
      Execute_protocol()
    else:
      print("Total Time is Zero! ... Protocol aborted")

def Execute_protocol():
    global DontRecord
    
    nLoops = int(Protocol_nLoops_entry.get())
    TotalTime = nLoops*(int(Protocol_1_7.get())+int(Protocol_2_7.get())+int(Protocol_3_7.get())+int(Protocol_4_7.get())+int(Protocol_5_7.get()))

 
    print("Start Protocol:", TotalTime, "s")

    if DontRecord==0:
      global Cam_framerate
      global Cam_pixels    
      global zoom_factor
      global Cam_X_offset  
      global Cam_Y_offset
      
      if Cam_pixels > 972: # ie if not x2 or higher binning
         BinX2();      

      zoom_win = 1/zoom_factor
      zoom_pos = (1-zoom_win) / 2
      camera.framerate = (Cam_framerate)
      camera.resolution = (Cam_pixels,Cam_pixels)
      camera.zoom = (zoom_pos+Cam_X_offset/200,zoom_pos+Cam_Y_offset/200,zoom_win,zoom_win)
      filePath = "/home/pi/Desktop/FlyPi_Videos/"
      baseName = "Protocol"
      global vid_counter
      global vid_duration
      vid_counter+=1
      camera.start_preview()
      camera.preview_fullscreen = False
      camera.preview.window = (0,0,1000,1000)
      print ("waiting 2 s while camera settles...")
      time.sleep(2) # wait 2 sec to adjust pic
      print ("recording...")
      camera.start_recording( output = filePath+baseName+str(vid_counter)+".h264",
                            format = "h264",
                            #quality = 10, # (10 best, 40 worst)
                            bitrate = 17000000) 
          
    
    for LoopCounter in range(0, nLoops):  
      print ("Loop ",LoopCounter+1,"/",nLoops)
      Flash_GreenLED() 

      # Execute 1
      if t1_LED.get() == 1:
         LED1_ON()
      else:
         LED1_OFF()
      if t1_Ring.get() == 1:
         LEDRing_LongZap()
      else:
         LEDRing_Baseline()
      if t1_Temp.get() == 1:
         Peltier_High()
      if t1_Temp.get() == 2:
         Peltier_Low()
      if t1_Temp.get() == 0:
         Peltier_OFF()
      current_wait = float(Protocol_1_7.get())
      time.sleep(current_wait)

#    t2 = threading.Timer(current_wait, Execute2())
#    t2.start()

      # Execute 2
      if t2_LED.get() == 1:
         LED1_ON()
      else:
         LED1_OFF()
      if t2_Ring.get() == 1:
         LEDRing_LongZap()
      else:
         LEDRing_Baseline()
      if t2_Temp.get() == 1:
         Peltier_High()
      if t2_Temp.get() == 2:
         Peltier_Low()
      if t2_Temp.get() == 0:
         Peltier_OFF()
      current_wait = float(Protocol_2_7.get())
      time.sleep(current_wait)

      # Execute 3
      if t3_LED.get() == 1:
         LED1_ON()
      else:
       LED1_OFF()
      if t3_Ring.get() == 1:
       LEDRing_LongZap()
      else:
         LEDRing_Baseline()
      if t3_Temp.get() == 1:
         Peltier_High()
      if t3_Temp.get() == 2:
         Peltier_Low()
      if t3_Temp.get() == 0:
         Peltier_OFF()
      current_wait = float(Protocol_3_7.get())
      time.sleep(current_wait)
  
      # Execute 4
      if t4_LED.get() == 1:
         LED1_ON()
      else:
         LED1_OFF()
      if t4_Ring.get() == 1:
         LEDRing_LongZap()
      else:
         LEDRing_Baseline()
      if t4_Temp.get() == 1:
         Peltier_High()
      if t4_Temp.get() == 2:
         Peltier_Low()
      if t4_Temp.get() == 0:
         Peltier_OFF()
      current_wait = float(Protocol_4_7.get())
      time.sleep(current_wait)

      # Execute 5
      if t5_LED.get() == 1:
         LED1_ON()
      else:
         LED1_OFF()
      if t5_Ring.get() == 1:
         LEDRing_LongZap()
      else:
         LEDRing_Baseline()
      if t5_Temp.get() == 1:
        Peltier_High()
      if t5_Temp.get() == 2:
         Peltier_Low()
      if t5_Temp.get() == 0:
         Peltier_OFF()
      current_wait = float(Protocol_5_7.get())
      time.sleep(current_wait)

    


    # END of Execute
    if DontRecord==0:
      camera.stop_recording()

    Peltier_OFF()
    LED1_OFF()
    LEDRing_Baseline()
    print("...done")





Execute = tkinter.Button(master=main, text = "Dry Run", command = DryRun, repeatdelay = 1)
Execute.place(x=300,y=700-100,width=60,height=40)
Execute = tkinter.Button(master=main, text = "Execute", command = FullRun, repeatdelay = 1)
Execute.place(x=300,y=750-100,width=60,height=40)

Protocol_1_0 = tkinter.Radiobutton(master=main, text="OFF", variable = t1_Temp, value = 0, indicatoron = 0)
Protocol_1_1 = tkinter.Radiobutton(master=main, text="Hot", variable = t1_Temp, value = 1, indicatoron = 0)
Protocol_1_2 = tkinter.Radiobutton(master=main, text="Cold", variable = t1_Temp, value = 2, indicatoron = 0)
Protocol_1_3 = tkinter.Radiobutton(master=main, text="OFF", variable = t1_LED, value=0, indicatoron = 0)
Protocol_1_4 = tkinter.Radiobutton(master=main, text="ON", variable = t1_LED, value=1, indicatoron = 0)
Protocol_1_5 = tkinter.Radiobutton(master=main, text="OFF", variable = t1_Ring, value=0, indicatoron = 0)
Protocol_1_6 = tkinter.Radiobutton(master=main, text="ON", variable = t1_Ring, value=1, indicatoron = 0)
Protocol_1_7 = tkinter.Spinbox(master=main, from_=0, to=100)

Protocol_1_0.place(x=20,y=600-100,width=40,height=20)
Protocol_1_1.place(x=20,y=620-100,width=40,height=20)   
Protocol_1_2.place(x=20,y=640-100,width=40,height=20)
Protocol_1_3.place(x=20,y=670-100,width=40,height=20)
Protocol_1_4.place(x=20,y=690-100,width=40,height=20) 
Protocol_1_5.place(x=20,y=720-100,width=40,height=20) 
Protocol_1_6.place(x=20,y=740-100,width=40,height=20) 
Protocol_1_7.place(x=20,y=770-100,width=40,height=20) 

Protocol_2_0 = tkinter.Radiobutton(master=main, text="OFF", variable = t2_Temp, value = 0, indicatoron = 0)
Protocol_2_1 = tkinter.Radiobutton(master=main, text="Hot", variable = t2_Temp, value = 1, indicatoron = 0)
Protocol_2_2 = tkinter.Radiobutton(master=main, text="Cold", variable = t2_Temp, value = 2, indicatoron = 0)
Protocol_2_3 = tkinter.Radiobutton(master=main, text="OFF", variable = t2_LED, value=0, indicatoron = 0)
Protocol_2_4 = tkinter.Radiobutton(master=main, text="ON", variable = t2_LED, value=1, indicatoron = 0)
Protocol_2_5 = tkinter.Radiobutton(master=main, text="OFF", variable = t2_Ring, value=0, indicatoron = 0)
Protocol_2_6 = tkinter.Radiobutton(master=main, text="ON", variable = t2_Ring, value=1, indicatoron = 0)
Protocol_2_7 = tkinter.Spinbox(master=main, from_=0, to=100)
Protocol_2_0.place(x=65,y=600-100,width=40,height=20)
Protocol_2_1.place(x=65,y=620-100,width=40,height=20)   
Protocol_2_2.place(x=65,y=640-100,width=40,height=20)
Protocol_2_3.place(x=65,y=670-100,width=40,height=20)
Protocol_2_4.place(x=65,y=690-100,width=40,height=20) 
Protocol_2_5.place(x=65,y=720-100,width=40,height=20) 
Protocol_2_6.place(x=65,y=740-100,width=40,height=20) 
Protocol_2_7.place(x=65,y=770-100,width=40,height=20) 

Protocol_3_0 = tkinter.Radiobutton(master=main, text="OFF", variable = t3_Temp, value = 0, indicatoron = 0)
Protocol_3_1 = tkinter.Radiobutton(master=main, text="Hot", variable = t3_Temp, value = 1, indicatoron = 0)
Protocol_3_2 = tkinter.Radiobutton(master=main, text="Cold", variable = t3_Temp, value = 2, indicatoron = 0)
Protocol_3_3 = tkinter.Radiobutton(master=main, text="OFF", variable = t3_LED, value=0, indicatoron = 0)
Protocol_3_4 = tkinter.Radiobutton(master=main, text="ON", variable = t3_LED, value=1, indicatoron = 0)
Protocol_3_5 = tkinter.Radiobutton(master=main, text="OFF", variable = t3_Ring, value=0, indicatoron = 0)
Protocol_3_6 = tkinter.Radiobutton(master=main, text="ON", variable = t3_Ring, value=1, indicatoron = 0)
Protocol_3_7 = tkinter.Spinbox(master=main, from_=0, to=100)
Protocol_3_0.place(x=110,y=600-100,width=40,height=20)
Protocol_3_1.place(x=110,y=620-100,width=40,height=20)   
Protocol_3_2.place(x=110,y=640-100,width=40,height=20)
Protocol_3_3.place(x=110,y=670-100,width=40,height=20)
Protocol_3_4.place(x=110,y=690-100,width=40,height=20) 
Protocol_3_5.place(x=110,y=720-100,width=40,height=20) 
Protocol_3_6.place(x=110,y=740-100,width=40,height=20) 
Protocol_3_7.place(x=110,y=770-100,width=40,height=20) 

Protocol_4_0 = tkinter.Radiobutton(master=main, text="OFF", variable = t4_Temp, value = 0, indicatoron = 0)
Protocol_4_1 = tkinter.Radiobutton(master=main, text="Hot", variable = t4_Temp, value = 1, indicatoron = 0)
Protocol_4_2 = tkinter.Radiobutton(master=main, text="Cold", variable = t4_Temp, value = 2, indicatoron = 0)
Protocol_4_3 = tkinter.Radiobutton(master=main, text="OFF", variable = t4_LED, value=0, indicatoron = 0)
Protocol_4_4 = tkinter.Radiobutton(master=main, text="ON", variable = t4_LED, value=1, indicatoron = 0)
Protocol_4_5 = tkinter.Radiobutton(master=main, text="OFF", variable = t4_Ring, value=0, indicatoron = 0)
Protocol_4_6 = tkinter.Radiobutton(master=main, text="ON", variable = t4_Ring, value=1, indicatoron = 0)
Protocol_4_7 = tkinter.Spinbox(master=main, from_=0, to=100)
Protocol_4_0.place(x=155,y=600-100,width=40,height=20)
Protocol_4_1.place(x=155,y=620-100,width=40,height=20)   
Protocol_4_2.place(x=155,y=640-100,width=40,height=20)
Protocol_4_3.place(x=155,y=670-100,width=40,height=20)
Protocol_4_4.place(x=155,y=690-100,width=40,height=20) 
Protocol_4_5.place(x=155,y=720-100,width=40,height=20) 
Protocol_4_6.place(x=155,y=740-100,width=40,height=20) 
Protocol_4_7.place(x=155,y=770-100,width=40,height=20)  

Protocol_5_0 = tkinter.Radiobutton(master=main, text="OFF", variable = t5_Temp, value = 0, indicatoron = 0)
Protocol_5_1 = tkinter.Radiobutton(master=main, text="Hot", variable = t5_Temp, value = 1, indicatoron = 0)
Protocol_5_2 = tkinter.Radiobutton(master=main, text="Cold", variable = t5_Temp, value = 2, indicatoron = 0)
Protocol_5_3 = tkinter.Radiobutton(master=main, text="OFF", variable = t5_LED, value=0, indicatoron = 0)
Protocol_5_4 = tkinter.Radiobutton(master=main, text="ON", variable = t5_LED, value=1, indicatoron = 0)
Protocol_5_5 = tkinter.Radiobutton(master=main, text="OFF", variable = t5_Ring, value=0, indicatoron = 0)
Protocol_5_6 = tkinter.Radiobutton(master=main, text="ON", variable = t5_Ring, value=1, indicatoron = 0)
Protocol_5_7 = tkinter.Spinbox(master=main, from_=0, to=100)
Protocol_5_0.place(x=200,y=600-100,width=40,height=20)
Protocol_5_1.place(x=200,y=620-100,width=40,height=20)   
Protocol_5_2.place(x=200,y=640-100,width=40,height=20)
Protocol_5_3.place(x=200,y=670-100,width=40,height=20)
Protocol_5_4.place(x=200,y=690-100,width=40,height=20) 
Protocol_5_5.place(x=200,y=720-100,width=40,height=20) 
Protocol_5_6.place(x=200,y=740-100,width=40,height=20) 
Protocol_5_7.place(x=200,y=770-100,width=40,height=20) 

Protocol_nLoops_label = tkinter.Label(master=main, text = "Loops")
Protocol_nLoops_label.place(x=320,y=655-100)
Protocol_nLoops_entry = tkinter.Spinbox(master=main, from_=1, to=100)
Protocol_nLoops_entry.place(x=320,y=670-100,width=40,height=20) 

Protocol_Peltier_label = tkinter.Label(master=main, text = "Peltier")
Protocol_Peltier_label.place(x=240,y=620-100)
Protocol_LED1_label = tkinter.Label(master=main, text = "LED1")
Protocol_LED1_label.place(x=240,y=680-100)
Protocol_RingLED_label = tkinter.Label(master=main, text = "Ring")
Protocol_RingLED_label.place(x=240,y=730-100)
Protocol_Time_label = tkinter.Label(master=main, text = "Time (s)")
Protocol_Time_label.place(x=240,y=770-100)


# run
main.mainloop()
