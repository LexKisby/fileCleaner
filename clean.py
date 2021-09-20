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
        self.local = os.path.dirname(os.path.abspath(__file__))
        self.downloads = os.path.join(
            'C:', os.sep, 'Users', 'Alexander Kisby', "Downloads")

    def clean(self, loc):
        path = self.local if loc == 1 else self.downloads
        self._clean(False, path)

    def clean_strict(self, loc):
        path = self.local if loc == 1 else self.downloads
        self._clean(True, path)

    def _clean(self, strict, path):
        print(f"{strict=}, {path=}")
        os.chdir(path)
        dir = os.listdir()
        print(dir)
        for file in dir:
            pass


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.cleaner = c_Cleaner()
        self.master = master
        self.loc = IntVar()
        self.loc.set(1)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.clean = ttk.Button(self)
        self.clean_strict = ttk.Button(self)
        self.clean["text"] = "Clean"
        self.clean["command"] = lambda: self.cleaner.clean(self.loc.get())
        self.clean_strict["text"] = "Clean Strictly"
        self.clean_strict["command"] = lambda: self.cleaner.clean_strict(
            self.loc.get())
        self.clean_strict.pack(side="bottom")
        self.clean.pack(side="bottom")
        Label(root,
              text="""Choose a folder location:""",
              justify=LEFT).pack()

        ttk.Radiobutton(root,
                        text="local",
                        variable=self.loc,
                        value=1).pack(anchor=W)

        ttk.Radiobutton(root,
                        text="Downloads",
                        variable=self.loc,
                        value=2).pack(anchor=W)


if __name__ == '__main__':

    if is_admin() or True:
        # Code of your program here
        print('starting')
        root = Tk(className='File Cleaner')
        root.geometry("280x150")
        app = Application(master=root)
        app.mainloop()

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
