import time
import tkinter as tk
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
        print('starting')

        pass

    def clean(self):
        os.remove('ggt.txt')
        pass

    def clean_strict(self):
        pass


if __name__ == '__main__':
    print(os.listdir())
    if is_admin():
        # Code of your program here
        cleaner = c_Cleaner()
        cleaner.clean()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
