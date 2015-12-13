"""this script can be used to plot the data from the flypi temperature log
    it opens the txt file and extracts the data into two lists, a time one,
    with the time stamps (right now they are only down to seconds). The
    second list contains the temperature reads."""


#import necessary libraries
import os
import matplotlib.pyplot as pyplot

dataLocation = "/home/pi/Desktop/flypi_output/log_temp/"
dataFile = "temp_log_2015-12-13.txt"

fh = open(dataLocation + dataFile, "r")

times = list()
temps = list()

for line in fh.readlines():
    #print(line + "\n")
    indx1 = line.index(",")
    indx2 = line.index("\r\n")
    times.append(line[0:indx1])
    #print(line[0:indx1] + "\n")
    temps.append(line[indx1 + 1:indx2])

fh.close()
pyplot.plot(range(0, len(times)), temps)
