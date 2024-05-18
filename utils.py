import tkinter as tk
from tkinter import ttk

# Configurazione finestra
#min_width = 425     # larghezza minima
#min_height = 200    # altezza minima
#max_width = 700     # larghezza massima
#max_height = 500    # altezza massima 

## LOGGER COLORS
RED = '\033[31m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
BOLD = '\033[1m'
END = '\033[0m'
GREEN = '\033[32m'

def Log(log_type="view",text=""):
    types = { "view": f"{RED}",
              "ctrl": f"{YELLOW}",
              "model": f"{MAGENTA}",
              "conn": f"{GREEN}" }
    print(f"{BOLD}{types.get(log_type,{RED})}[{log_type}]: {text}{END}")

def get_center_coordinates(screen_width:int, screen_height:int, window_width:int, window_height:int) -> tuple[int,int] :
    """Calcola le coordinate del centro dello schermo"""
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    return center_x, center_y

def set_window_default_settings(app:tk.Tk, title:str="Titolo", window_width:int=600, window_height:int=400) -> None :
    """Setta le impostazioni di default di una finestra"""
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    center_x, center_y = get_center_coordinates(screen_width, screen_height, window_width, window_height)
    app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') # Imposto dimensione e posizione della finestra
    app.resizable(True, True) # Si può allargare in larghezza e altezza
    #app.minsize(min_width, min_height) # Ha una larghezza minima e massima
    #app.maxsize(max_width, max_height) # Ha una altezza minima e massima
    app.attributes('-topmost', 1) # È posizionata sopra tutte le altre finestre
    app.title(f"{title}") # Imposto il titolo