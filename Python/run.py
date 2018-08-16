

#import "global" libraries
import tkinter as tk
#import os
#import time


#################PROGRAM EXECUTION
from flypiApp import *

#create a root
root = tk.Tk()
root.title("Fly Pi 0.99")

flypiApp(root)


#dummie.title("test")
root.resizable(width=False, height=False)
root.mainloop()

root.destroy()
