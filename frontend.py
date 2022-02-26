from tkinter import ttk

from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
from numpy import size
import os
import signal
import subprocess
import threading



MSG_TITLE = "Collect Data"
MSG_CONTENT = """ 
To collect data: 
-> Go to Training Mode.
-> Practice before Recording.
-> To record press Record Button on top right corner.
-> Select the desired folder(Make sure to select folder in which .exe file is present).
-> Collect Images and train the model.
-> Enjoy !!.   
"""

def showImage():
    """
        Triggers the simulator for collecting images.
    """
    tk.messagebox.showinfo(MSG_TITLE, MSG_CONTENT)
    os.system("simulator.exe")

##################   All the code required for Training Data. ########################

def getFolderName():
    """
        Opens a dialog box for Image folder and csv file
    """
    global folder_selected
    if folder_selected := filedialog.askdirectory():
        lbl4.configure(text=f"..../{folder_selected[5:]}")


war_content = """
Training the model may take minimum 5 hours to train,
more depending on your system specifications.
It can hang up the exe until the process is completed.
Do you still want to continue training?.
If you wish to discontinue in middle of training close script manually running in the command line
"""
def trainData():
    """
        Script for traing data.
        Returns a model.h5 model
    """
    try:
        msg = 'Warning !!'
        cont = tk.messagebox.askquestion(msg, war_content)
        if cont == 'yes':
            os.system(f"model.py -d {folder_selected}")
    except Exception as e:
        msg = "Error: "
        content = "Please Select Folder First"
        tk.messagebox.showinfo(msg, content)
    



####################    All the code required for Testing Simulation. ########################


def runFast():
    title = 'Running Fast'
    content = """
    Make sure there is model file named 'model.h5' in the current working directory.
    Drive fast method triggered.
    This drives the car fast but not accurately.
    Click on Run Simulation and run in autonomous mode.
    """
    try:
        command = "netstat -ano | findstr 4567"
        c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = c.communicate()
        if 'TCP' in str(stdout):
            pid = int(stdout.decode().strip().split(' ')[-1])
            os.kill(pid, signal.SIGTERM)
    except OSError:
        title = "Error Occurred! :("
        content = "Error in closing connection. Close the Simulator and try again after some time !"

    tk.messagebox.showinfo(title, content)    
    os.system("drive.py model.h5")

    
def runSlow():
    title = 'Running SLOW'
    content = """
    Make sure there is model file named 'model.h5' in the current working directory.
    Drive Slow method triggered.
    This drives the car slowly but accurately.
    Click on Run Simulation and run in autonomous mode.
    """
    try:
        command = "netstat -ano | findstr 4567"
        c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = c.communicate()
        print(stdout)
        if 'TCP' in str(stdout):
            pid = int(stdout.decode().strip().split(' ')[-1])
            os.kill(pid, signal.SIGTERM)
    except OSError:
        title = "Error Occurred! :("
        content = "Error in closing connection. Close the Simulator and try again after some time !."

    tk.messagebox.showinfo(title, content)
    os.system("drive_slow.py")


def testModel():
    """
        Triggers the simulator.
    """
    title = 'Running Simulation'
    content = 'Click on autonomus mode to test the model'
    tk.messagebox.showinfo(title, content)
    os.system("simulator.exe")


def startFast():
    """
        Start a thread for running drive.py script
    """
    threading.Thread(target=runFast).start()

def startSlow():
    """
        Start a thread for running drive_slow.py script
    """
    threading.Thread(target=runSlow).start()


def closeSimulator():
    """
        Close the connection and exit the simulator.
    """
    try:
        command = "netstat -ano | findstr 4567"
        c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = c.communicate()
        print(stdout)
        if 'TCP' in str(stdout):
            pid = int(stdout.decode().strip().split(' ')[-1])
            os.kill(pid, signal.SIGTERM)
    except OSError:
        title = 'Error Occurred ! :('
        content = """
        Error in closing Connection.
        Click on X button on top right hand corner of simulator to close manually
        Close the Simulator and try again after some time !
        """
        tk.messagebox.showinfo(title, content)

    root.destroy()

########################################### UI Area ###########################################
root = Tk()
style = ttk.Style(root)
style.theme_use('winnative')


root.config(
            padx = 5 , 
            bg = "#eaf2fa"
        )
root.title('Welcome')


frm = LabelFrame(
                root,
                relief=SUNKEN,
                borderwidth=4,
                text = "Welcome",
                font=("Inter", 10)
            )
frm.pack(
        side = TOP, 
        padx = 15,
        pady = 15,
        ipadx = 5, 
        ipady = 5
    )


lbl = Label(frm)
fln = "image1.png"
img = Image.open(fln)
img.thumbnail((350, 450))
img = ImageTk.PhotoImage(img)
lbl.configure(image = img)
lbl.image = img
lbl.pack(side = TOP, pady=5)


""" 
    Collect Data Section
"""
frm3 = LabelFrame(
                root, 
                relief=GROOVE, 
                borderwidth=4, 
                text = "Collect Data",
                font=("Inter", 9)
            )
frm3.pack(
        side = TOP, 
        ipadx = 5, 
        ipady = 5
    )

lbl2 = Label(
            frm3, 
            text="Welcome to Self-Driving Car Simulator", 
            fg = 'red', 
            font=("Inter", 15)
        )
lbl2.pack(side = TOP)


btn = Button(
            frm3, 
            text = 'Collect Data',
            font=("Inter", 10), 
            command = showImage
        )
btn.pack(
        side=TOP, 
        pady = 5
    )


"""
    Train Data Section
"""
frm1 = LabelFrame(root, 
                relief=GROOVE, 
                borderwidth=4, 
                text = "Training",
                font=("Inter", 9))
frm1.pack(
            side = TOP, 
            padx = 5, 
            pady = 5, 
            ipadx = 5, 
            ipady = 5
        )

lbl3 = Label(frm1, 
            text="Train Images", 
            font=("Inter", 15), 
            fg = 'red')
lbl3.pack(side = TOP)

btn = Button(frm1, 
            text = 'Select Folder',
            font=("Inter", 10), 
            command = getFolderName)
btn.pack(side=TOP, 
        pady = 5)

lbl4 = Label(frm1, 
            fg = 'green')
lbl4.pack(side = TOP)

btn1 = Button(
            frm1, 
            text = 'Train Model',
            font=("Inter", 10), 
            command = trainData)
btn1.pack(side=TOP)


"""
    Test Simulation Section.
"""

frm2 = LabelFrame(
                root, 
                relief=GROOVE, 
                borderwidth=4, 
                text = "Testing",
                font=("Inter", 9))
frm2.pack(
            side = BOTTOM, 
            ipadx = 5, 
            ipady = 5, 
            padx = 5, 
            pady = 15
        )

lbl5 = Label(
        frm2, 
        text="Run Simulation", 
        font=("Inter", 15), 
        fg = 'red')
lbl5.pack(side = TOP)


btn2 = Button(
                frm2, 
                text = 'Run Fast', 
                font=("Inter", 10),
                command = startFast)
btn2.pack(side=LEFT,
            padx = 10, 
            pady = 5
        )

btn3 = Button(
            frm2, 
            text = 'Run Slow',
            font=("Inter", 10), 
            command = startSlow)
btn3.pack(
            side=LEFT,
            padx = 10, 
            pady = 5
        )



btn4 = Button(
            frm2, 
            text = 'Run Simulator',
            font=("Inter", 10), 
            command = testModel
        )
btn4.pack(side=LEFT,
            padx = 10, 
            pady = 5
        )

btn5 = Button(
            frm2, 
            text = 'CLOSE',
            font=("Inter", 10), 
            command = closeSimulator)
btn5.pack(
        side=LEFT,
        padx = 10, 
        pady = 5
    )



root.title("Self Driving Car Simulator")
root.geometry('550x690')

root.mainloop()