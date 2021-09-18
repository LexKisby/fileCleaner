import time
from tkinter import *
from tkinter import ttk
import json
import os
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class c_Cleaner():
    def __init__(self):
        print('cleaner init')
        pass

    def clean(self):
        print('clean')
        pass

    def clean_strict(self):
        pass


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.cleaner = c_Cleaner()
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Clean"
        self.hi_there["command"] = self.cleaner.clean
        self.hi_there.pack(side="top")

        self.quit = ttk.Button(self, text="QUIT",
                               command=self.master.destroy)
        self.quit.pack(side="bottom")


if __name__ == '__main__':
    print(os.listdir())
    if is_admin() or True:
        # Code of your program here
        print('starting')
        root = Tk(className='File Cleaner')
        root.geometry("280x130")
        app = Application(master=root)
        app.mainloop()

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
