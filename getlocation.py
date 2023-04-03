import tkinter as tk
from tkinter import ttk
import mapview as tkmap
from typing import Union
from classes import *


class LocationPage:
    coordinates: tuple[float, float]

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("EAT EAT FORM")
        self.window.geometry("1200x800")

    def create_new_window(self, route: list[Node]):
        frame = tk.Frame(self.window)
        self.main_frame = frame
        frame.pack()

        final_map_frame = tk.LabelFrame(frame)
        final_map_frame.pack()

        map_widget = tkmap.create_map_widget(final_map_frame, [route], 800, 600)
        map_widget.pack()

    def run(self):
        self.window.mainloop()
