#!/usr/bin/python

# Tkinter interface to the McMillan installer / PyInstaller
# (c) 2003 Alan James Salmoni - yes, all this bad code is all mine!!!
# (c) 2011 Hartmut Goebel: adopted to PyInstaller 1.6, use subprocess
# released under the MIT license

import os
import sys
import subprocess
from Tkinter import *
import tkFileDialog
import FileDialog

class PyInstallerGUI:

    def make_checkbutton(self, frame, text):
        var = IntVar()
        widget = Checkbutton(frame, text=text, variable=var)
        widget.grid(sticky="NW")
        return var

    def __init__(self):
        root = Tk()
        root.title("PyInstaller GUI")
        fr1 = Frame(root)
        fr1["width"] = 200
        fr1["height"] = 100
        fr1.pack(side="top")
        fr2 = Frame(root)
        fr2["width"] = 200
        fr2["height"] = 300
        fr2["borderwidth"] = 2
        fr2["relief"] = "ridge"
        fr2.pack()
        fr4 = Frame(root)
        fr4["width"] = 200
        fr4["height"] = 100
        fr4.pack(side="bottom")

        getFileButton = Button(fr1, text="Script to bundle ...")
        getFileButton.bind("<Button>", self.GetFile)
        getFileButton.pack(side="left")
        self.filein = Entry(fr1)
        self.filein.pack(side="right")
        self.filetype = self.make_checkbutton(fr2, "One File Package")
        self.ascii = self.make_checkbutton(fr2, "Do NOT include decodings")
        self.debug = self.make_checkbutton(fr2, "Use debug versions")
        self.noconsole = self.make_checkbutton(fr2, "No console (Windows only)")

        okaybutton = Button(fr4, text="Okay   ")
        okaybutton.bind("<Button>", self.makePackage)
        okaybutton.pack(side="left")

        cancelbutton = Button(fr4, text="Cancel")
        cancelbutton.bind("<Button>", self.killapp)
        cancelbutton.pack(side="right")
        self.fin = ''
        self.fout = ''
        root.mainloop()

    def killapp(self, event):
        sys.exit(0)

    def makePackage(self, event):
        commands = ['python', 'pyinstaller.py']
        if self.filetype.get():
            commands.append('--onefile')
        if self.ascii.get():
            commands.append('--ascii')
        if self.debug.get():
            commands.append('--debug')
        if self.noconsole.get():
            commands.append('--noconsole')
        commands.append(self.fin)
        retcode = subprocess.call(commands)
        sys.exit(retcode)

    def GetFile(self, event):
        self.fin = tkFileDialog.askopenfilename()
        self.filein.insert(0, self.fin)

if __name__ == "__main__":
    try:
        app = PyInstallerGUI()
    except KeyboardInterrupt:
        raise SystemExit("Aborted by user request.")
