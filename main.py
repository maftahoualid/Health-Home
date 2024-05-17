import tkinter as tk
from tkinter import ttk
from utils import *

from model import Model
from controller import Controller
from view import View

if __name__ == '__main__':
    view = View()
    model = Model()
    controller = Controller(model, view)
    view.set_controller(controller)
    view.mainloop()