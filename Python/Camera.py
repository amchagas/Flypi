    ######################################## CAMERA
import tkinter as tk
import os
import time
import subprocess
from tkinter.filedialog import askopenfilename
#import warnings
#warnings.filterwarnings('default', category=DeprecationWarning)

class Camera:

    def __init__(self, parent="none",
                 label="CAMERA", basePath="~/Desktop/"):
        try:
            # picamera module
            import picamera
            #picameraAvail = True
            ##setup camera
            self.cam = picamera.PiCamera()
            self.cam.led = False
            self.cam.exposure_mode = "fixedfps"
            self.cam.exposure_compensation = 0
            self.cam.brightness = 50
            self.cam.awb_mode = "auto"

        except ImportError:
            #picameraAvail = False
            print ("picamera module not available!")

        self.camParent = parent
        self.basePath = basePath

        self.autoExpVar = tk.IntVar()

        self.flipVar = tk.IntVar()
        self.flipVal = 0

        self.zoomVar = tk.DoubleVar(value=1.0)
        self.zoomVal = 1.0
        self.FPSVar = tk.IntVar()
        self.FPSVal = 15
        self.bitRate = 17000000
        self.binVar = tk.IntVar()
        self.binVal = 0

        self.sizeVar = tk.IntVar()
        self.sizeVal = 180
        self.horVar = tk.DoubleVar()
        self.horVal = 1
        self.verVar = tk.DoubleVar()
        self.verVal = 1
        self.brightVar = tk.IntVar()
        self.brightVal = 50
        self.contVar = tk.IntVar()
        self.contVal = 50
        self.expVar = tk.IntVar()
        self.expVal = 0
        self.rotVar = tk.IntVar()
        self.rotVal = 0
        self.camallcalls = list()
        ###frames for all camera controls
        self.camFrame1 = tk.Frame(master=self.camParent, bd=2)
        self.camFrame1.grid(row=0, column=0,
                            columnspan=1, rowspan=2,
                            sticky="N")

        frame2 = tk.Frame(master=self.camParent, bd=2)
        frame2.grid(row=0, column=1, sticky="NW", columnspan=2)
        frame3 = tk.Frame(master=frame2, bd=2, relief="ridge")
        frame3.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="NW")
        ####
        ####variables for the dropdown menus
        self.camAWVar = tk.StringVar(master=self.camFrame1)
        self.camAWVal = "auto"
        self.camModVar = tk.StringVar(master=self.camFrame1)
        self.camColEffVar = tk.StringVar(master=self.camFrame1)
        self.camColEffVal = "NONE"
        self.resVar = tk.StringVar()
        self.resVal = "2592x1944"
        ####

        self.label = label
        #self.parent = parent
        self.camLabel = tk.Label(master=self.camFrame1, text=self.label)
        self.camLabel.pack()

        self.camOnButt = self.camButton(parent=self.camFrame1,
                            rowIndx=1, colIndx=0, fill="x",
                            buttText="ON", color="green", func=self.camOn)

        self.camOffButt = self.camButton(parent=self.camFrame1,
                            rowIndx=1, colIndx=1, fill="x",
                            buttText="OFF", color="red", func=self.camOff)
        self.camConvbutt = self.camButton(parent=self.camFrame1,
                            rowIndx=1, colIndx=2, fill="x",
                            buttText="to AVI", color="blue", func=self.camConv)

        self.camResLabel = tk.Label(master=self.camFrame1,
                                    text=" Resolution ")

        self.camResLabel.pack(fill="x")
        self.camResMenu = tk.OptionMenu(self.camFrame1,
                                       self.resVar,
                                       '2592x1944', '1920x1080',
                                       '1296x972', '1296x730', '640x480')
        self.resVar.set("2592x1944")
        self.camResMenu.pack(fill="x")
        self.camResMenu.pack_propagate(flag=False)
        self.camAWLabel = tk.Label(master=self.camFrame1,
                                   text=" White balance ")
        self.camAWLabel.pack(fill="x")
        self.camAWMenu = tk.OptionMenu(self.camFrame1,
                                       self.camAWVar,
                                       'off', 'auto', 'green',
                                       'red', 'blue', 'sunlight', 'cloudy',
                                       'shade', 'tungsten', 'fluorescent',
                                       'incandescent',
                                       'flash', 'horizon')
        self.camAWVar.set("auto")
        self.camAWval = "auto"
        self.camAWMenu.pack(fill="x")
        self.camAWMenu.pack_propagate(flag=False)
        self.camModLabel = tk.Label(master=self.camFrame1, text="Mode")
        self.camModLabel.pack(fill="x")
        self.camModes = tk.OptionMenu(self.camFrame1,
                                      self.camModVar,
                                      "none", "negative", "solarize", "sketch",
                                      "denoise", "emboss", "oilpaint", "hatch",
                                      "gpen", "pastel", "watercolor", "film",
                                      "blur", "saturation", "colorswap",
                                      "washedout",
                                      "posterise", "colorpoint",
                                      "colorbalance", "cartoon",
                                      "deinterlace1", "deinterlace2")
        self.camModVar.set("none")
        self.camModes.pack(fill="x")
        self.camColEffLabel = tk.Label(master=self.camFrame1,
                                       text="color effect")
        self.camColEffLabel.pack(fill="x")
        self.camColEff = tk.OptionMenu(self.camFrame1,
                                       self.camColEffVar,
                                      "NONE",
                                      "RED", "GREEN", "BLUE", "BW")
        self.camColEff.pack(fill="x")
        self.camColEffVar.set("none")
        self.camColEff.pack_propagate(flag=False)

        self.camFPS = self.camSlider(parent=frame2, label_="FPS",
                                   var=self.FPSVar, len=90,
                                   rowIndx=1, colIndx=2, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=15, to__=90,
                                   res=5, set_=15)

        #self.camBin = self.camSlider(parent=frame2, label_="Binning",
        #                           var=self.binVar, len=90,
        #                           rowIndx=0, colIndx=2, sticky="",
        #                           orient_="horizontal",
        #                           colSpan=1, from__=0, to__=4, res=2, set_=0)

        self.camSize = self.camSlider(parent=frame2, label_="Window size",
                                   var=self.sizeVar,
                                   rowIndx=0, colIndx=0, sticky="",
                                   orient_="horizontal", len=90,
                                   colSpan=1, from__=180, to__=2000,
                                   res=20, set_=240)

        self.camZoom = self.camSlider(parent=frame2, label_="Digi Zoom",
                                   var=self.zoomVar, len=90,
                                   rowIndx=0, colIndx=1, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=1,
                                   to__=10, res=1, set_=1.0)

        self.camHor = self.camSlider(parent=frame2, label_="Horiz. Offset",
                                   var=self.horVar, len=90,
                                   rowIndx=1, colIndx=0, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=1, to__=100,
                                   res=5, set_=1)

        self.camVer = self.camSlider(parent=frame2, label_="Verti. Offset",
                                   var=self.verVar, len=90,
                                   rowIndx=1, colIndx=1, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=1,
                                   to__=100, res=5, set_=1)

        self.camBright = self.camSlider(parent=frame2, label_="Brightness",
                                   var=self.brightVar, len=90,
                                   rowIndx=2, colIndx=0, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=0, to__=100,
                                   res=5, set_=50)

        self.camCont = self.camSlider(parent=frame2, label_="Contrast",
                                   var=self.contVar, len=90,
                                   rowIndx=2, colIndx=1, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=0, to__=100,
                                   res=5, set_=50)

        self.camExp = self.camSlider(parent=frame2, label_="Exposure",
                                   var=self.expVar, len=90,
                                   rowIndx=2, colIndx=2, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=-25, to__=25,
                                   res=5, set_=0)

        self.camRot = self.camSlider(parent=frame2, label_="Rotation",
                                   var=self.rotVar, len=90,
                                   rowIndx=3, colIndx=0, sticky="",
                                   orient_="horizontal",
                                   colSpan=1, from__=0, to__=270,
                                   res=90, set_=0)

        self.autoExposure = tk.Checkbutton(master=frame2,
                                           text="auto expos.",
                                           variable=self.autoExpVar,
                                           onvalue=1, offvalue=0)

        self.autoExpVar.set(1)
        self.autoExposure.grid(row=4, column=0, sticky="N")

        self.flip = tk.Checkbutton(master=frame2,
                                   text="Flip image",
                                   variable=self.flipVar,
                                   onvalue=1, offvalue=0)

        self.flipVar.set(0)
        self.flip.grid(row=4, column=0, sticky="S")

        #########Time lapse/video/photo####################

        self.TLLabel = tk.Label(master=frame3, text="TIME LAPSE")
        self.TLLabel.grid(row=2, column=0, sticky="N")

        self.TLdur = tk.Entry(master=frame3, width=8)
        self.TLdur.grid(row=3, column=1, sticky="WN")
        self.TLdur.insert(0, 0)

        self.TLdurLabel = tk.Label(master=frame3, text="DUR (sec)")
        self.TLdurLabel.grid(row=2, column=1, sticky="W")

        self.TLinter = tk.Entry(master=frame3, width=8)
        self.TLinter.insert(0, 0)
        self.TLinter.grid(row=5, column=1, sticky="NW")

        self.TLinterLabel = tk.Label(master=frame3, text="INTERVAL (sec)")
        self.TLinterLabel.grid(row=4, column=1, sticky="W")

        self.camRecButt = tk.Button(master=frame3,
                                  text="video", fg="black",
                                  command=self.camRec)
        self.camRecButt.grid(row=3, column=0, sticky="WEN")

        self.camTLButt = tk.Button(master=frame3,
                                 text="timelapse", fg="black",
                                 command=self.camTL)
        self.camTLButt.grid(row=4, column=0, sticky="WES")

        self.camSnapButt = tk.Button(master=frame3,
                                   text="photo", fg="black",
                                   command=self.camSnap)
        self.camSnapButt.grid(row=5, column=0, sticky="WEN")

        ####callback for menus
        self.camGetMenus()
        ####

    ########callback for menus
    def camGetMenus(self):
        #this is a recursive function that will call itself
        #with a minimum interval of 700ms.
        #upon calling it will get the value of three variables
        #white balance, mode and color effect
        self.camFrame1.after(400, self.camGetMenus)

        if self.cam.awb_mode != self.camAWVar.get():
            self.camAWVal = self.camAWVar.get()
            if self.camAWVal != "":
                if self.camAWVal == "green":
                    self.cam.awb_mode = "off"
                    self.cam.awb_gains = (1, 1)
                elif self.camAWVal == "red":
                    self.cam.awb_mode = "off"
                    self.cam.awb_gains = (8.0, 0.9)
                elif self.camAWVal == "blue":
                    self.cam.awb_mode = "off"
                    self.cam.awb_gains = (0.9, 8.0)
                elif self.camAWVal == "off":
                    self.cam.awb_mode = "off"
                else:
                    self.cam.awb_mode = self.camAWVal

        if self.cam.image_effect != self.camModVar.get():
            self.camModVal = self.camModVar.get()
            if self.camModVal != "":
                self.cam.image_effect = self.camModVal

        if self.camColEffVal != self.camColEffVar.get():
            self.camColEffVal = self.camColEffVar.get()
            if self.camColEffVal != "":
                if self.camColEffVal == "BW":
                    self.cam.color_effects = (128, 128)
                elif self.camColEffVal == "RED":
                    self.cam.color_effects = (0, 255)
                elif self.camColEffVal == "BLUE":
                    self.cam.color_effects = (255, 0)
                elif self.camColEffVal == "GREEN":
                    self.cam.color_effects = (0, 0)
                else:
                    self.cam.color_effects = None
        #ce = self.camColEffVar.get()

        autoExp = self.autoExpVar.get()
        if autoExp == 0:
            self.cam.exposure_mode = "off"
        else:
            self.cam.exposure_mode = "auto"

        #flip= self.flipVar.get()
        #print(type(flip1))
        if self.flipVal != self.flipVar.get():
            self.flipVal = self.flipVar.get()
            if self.flipVal == 1:
                self.cam.hflip = True
            else:
                self.cam.hflip = False

        if self.FPSVal != self.FPSVar.get():
            self.FPSVal = self.FPSVar.get()
            self.cam.framerate = (self.FPSVal)

        #if self.binVal != self.binVar.get():
        #    self.binVal = self.binVar.get()
        #    self.cam. = (self.binVal)

        #if self.binVal != self.binVar.get():
        #    self.binVal = self.binVar.get()
        #    self.cam. = (self.binVal)

        if self.brightVal != self.brightVar.get():
            self.brightVal = self.brightVar.get()
            self.cam.brightness = (self.brightVal)

        if self.contVal != self.contVar.get():
            self.contVal = self.contVar.get()
            self.cam.contrast = (self.contVal)

        if self.expVal != self.expVar.get():
            self.expVal = self.expVar.get()
            self.cam.exposure_compensation = (self.expVal)

        if self.sizeVal != self.sizeVar.get():
            self.sizeVal = self.sizeVar.get()
            self.cam.preview_window = (0, 0, self.sizeVal, self.sizeVal)

        if self.rotVal != self.rotVar.get():
            self.rotVal = self.rotVar.get()
            self.cam.rotation = self.rotVal

        if self.resVal != self.resVar.get():
            self.resVal = self.resVar.get()
            if self.resVal == "2592x1944":
                self.cam.resolution = (2592, 1944)
                self.cam.framerate = (15)
                self.FPSVar.set(15)
                self.binVar.set(0)
                #self.cam.zoom(0)
                self.zoomVar.set(1)
            if self.resVal == "1920x1080":
                self.cam.resolution = (1920, 1080)
                self.cam.framerate = (30)
                self.FPSVar.set(30)
                self.binVar.set(0)
                #self.zoomVar.set(3)
            if self.resVal == "1296x972":
                self.cam.resolution = (1296, 972)
                self.cam.framerate = (42)
                self.FPSVar.set(42)
                self.binVar.set(2)
            if self.resVal == "1296x730":
                self.cam.resolution = (1296, 730)
                self.cam.framerate = (49)
                self.FPSVar.set(49)
                self.binVar.set(2)
            if self.resVal == "640x480":
                self.cam.resolution = (640, 480)
                self.cam.framerate = (90)
                self.FPSVar.set(90)
                self.binVar.set(4)
                #self.zoomVar.set(5)

        if self.zoomVal != self.zoomVar.get() or \
           self.horVal != self.horVar.get() or \
           self.verVal != self.verVar.get() or \
           self.resVal != self.resVar.get():# or \
           #self.binVal != self.binVar.get():
            self.zoomVal = self.zoomVar.get()
            self.horVal = self.horVar.get()
            self.verVal = self.verVar.get()
            self.resVal = self.resVar.get()
            #self.binVal = self.binVar.get()
            if self.zoomVal == 1:
                self.cam.zoom = (0, 0, 1, 1)
                self.horVar.set(50)
                self.verVar.set(50)
            else:
                zoomSide = 1 / self.zoomVal
                edge = (1 - zoomSide)#*0.5
                self.cam.zoom = ((self.horVal / 100.0) * edge,
                               (self.verVal / 100.0) * edge,
                               1 / self.zoomVal,
                               1 / self.zoomVal)

    #general function to create buttons
    def camButton(self, parent="none", fill="", side="top",
                  rowIndx=1, colIndx=0, sticky="",
                  buttText="button", color="black",
                  func="none"):

        button = tk.Button(master=parent,
                           text=buttText,
                           fg=color, command=func)
        button.pack(fill=fill, side=side)
        return
    #general function for slider
    def camSlider(self, parent="none", label_="empty", len=90,
                   var="", rowIndx=1, colIndx=0,
                   sticky="", orient_="vertical",
                   colSpan=1, from__=100, to__=0,
                   res=1, set_=0):

        Slider = tk.Scale(master=parent, from_=from__, to=to__,
                          resolution=res, label=label_, length=90,
                          variable=var, orient=orient_)
        Slider.set(set_)
        Slider.grid(row=rowIndx, column=colIndx, columnspan=colSpan)
        return
    ##################callbacks for buttons
    def camOn(self):

        print ("cam on")
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
        return

    def camOff(self):
        print ("cam Off")
        self.cam.stop_preview()
        return

    def camConv(self):
        #tk().withdraw()
        opts = dict()
        opts["filetypes"] = [('h264 files','.h264'),('all files','.*')]
        opts["initialdir"] = [self.basePath]

        fileName = askopenfilename(**opts)
        if fileName == '':
            print ('no files selected')
            return
        fps = self.FPSVar.get()
        fps = "-r" + str(fps)
#        fps = int(fps)
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
        command = ['avconv', '-i', fileName,"-b",str(self.bitRate) ,"-c:v","copy", outname]
        subprocess.call(command,shell=False)
        print("done.")
        return


    def camRec(self,dur=None):
        if dur == None:
            dur = self.TLdur.get()


        videoPath = self.basePath + '/videos/'
        if not os.path.exists(videoPath):
            #if not, create it:
            os.makedirs(videoPath)
            os.chown(videoPath, 1000, 1000)
        #it seems that the raspi-cam doesn't like shooting videos at full res.
        #so the softw. will automatically use a lower resolution for videos
        if self.resVal == "2592x1944":
            self.resVar.set ("1920x1080")
            self.cam.resolution = (1920, 1080)
            if self.FPSVar.get()<30:
                self.FPSVar.set(30)
            print ("impossible to record at 2592X1944,")
            print ("due to camera limitations.")
            print("dropping to next possible resolution")


        print("recording for: " + str(dur) + " secs")
        self.cam.start_recording(output = videoPath +
                                'video_' +
                                time.strftime('%Y-%m-%d-%H-%M-%S') + '.h264',
                                format = "h264",)
                                #resize = (1920,1080))
        self.cam.wait_recording(float(dur))
        self.cam.stop_recording()
        print("done.")
        #here we restore the preview resolution if it was the maximal one.
        if self.resVal == "2592x1944":
            self.cam.resolution = (2592, 1944)
        return



    def camTL(self):
        dur = self.TLdur.get()
        interval = self.TLinter.get()
        tlPath = self.basePath + '/time_lapse/'

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
