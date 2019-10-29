The flypi python code is deveped in Python3 and
is now divided in the following manner:

--flypiApp.py is the code that brings different classes together into the GUI

--Run.py takes care of "executing" the flypiApp. It creates a tkinter 
root object, throws it in flypiApp, and takes care of destroying it when the 
program is terminated.

--the other files are responsible for each peripheric device used. So if the 
user wants to create code for a new peripheric device, he/she should start by 
creating a new ".py" file and with a class that contains all code to control 
that device.

---To run this new code, the user should, should call the run.py file, either 
by calling "python3 /complete/path/to/run.py" or by moving into the folder
 where the file is and then calling it from there.



