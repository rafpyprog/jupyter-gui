from IPython.display import display
import ipywidgets as widgets
from tkinter import *
from tkinter import filedialog


class OpenFile():
    def __init__(self, label):
        self.button = widgets.Button(description=label)
        display(self.button)
        self.button.on_click(self.on_click)

    def on_click(self, b):
        f = FileLoader()
        self.path = f.file_path


class FileLoader():
    def __init__(self):
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        self.file_path = filedialog.askopenfilename()
