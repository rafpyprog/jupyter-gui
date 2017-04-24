from IPython.display import display
import ipywidgets as widgets
from tkinter import *
from tkinter import filedialog


class FileLoader():
    def __init__(self, action="getpath", mode="r"):
        self.mode = mode
        self.action = action

        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        if self.action == "getpath":
            self.file = filedialog.askopenfilename()
        elif self.action == "getfile":
            self.file = filedialog.askopenfile(mode=self.mode)
        else:
            raise ValueError("{} is not a valid action.".format(self.action))


class Button():
    def __init__(self, label="", callback=None, callback_args=None):
        self.label = label
        self.callback = callback
        self.callback_args = callback_args
        self.show_button()
        self.value = None

    def show_button(self):
        self.button = widgets.Button(description=self.label)
        display(self.button)
        self.button.on_click(self.on_click)

    def on_click(self, b):
        if self.callback_args is not None:
            f = self.callback(**self.callback_args)
        else:
            f = self.callback()
        self.value = f.file


class Open(Button):
    def __init__(self, label="Open...", action="getpath", mode="r"):
        self.label = label
        self.show_button()
        self.callback = FileLoader
        self.callback_args = {"action": action, "mode": mode}
