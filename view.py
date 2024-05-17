import tkinter as tk
from tkinter import ttk
from utils import *
from PIL import Image, ImageTk

class View(tk.Tk):

    # LABEL ###################################################################
    def Xlabel(self, name, row, col):
        self.label = tk.Label(self, text=f"{name}:", **self.label_style)
        self.label.grid(row=row, column=col, **self.label_layout)
        return self.label
    ###########################################################################

    # ENTRY ###################################################################
    def Xinput(self, row, col, var=None):
        self.entry = tk.Entry(self, textvariable=var, **self.entry_style)
        self.entry.grid(row=row, column=col, **self.entry_layout)
        return self.entry
    ###########################################################################

    # RADIO BUTTON ############################################################
    def Xradio(self,txt,var,cmd,riga,colonna):
        self.r = tk.Radiobutton(self, text=txt, value=txt, variable=var, command=cmd, **self.radio_style)
        self.r.grid(row=riga,column=colonna, **self.radio_layout)
        return self.r
    ###########################################################################

    # BUTTON ##################################################################
    def Xbutton(self, str1, cmd, riga, col):
        btn = tk.Button(self, text=str1, command=cmd, **self.button_style)
        btn.grid(row=riga, column=col, **self.button_layout)
        return btn
    ###########################################################################

    # SET CONTROLLER ##########################################################
    def set_controller(self, controller):
        """ imposta il controller """
        self.controller = controller
    ###########################################################################

    # TOGGLE FIELDS ###########################################################
    def toggle_fields(self):
        """ mostra Email e nasconde CodSan e viceversa """
        if(self.user_type.get() == "Personale"):
            self.XEmail.grid(); self.YEmail.grid()
            self.XCodSan.grid_remove(); self.YCodSan.grid_remove(); self.YCodSan.delete(0, tk.END)
        elif(self.user_type.get() == "Paziente"):
            self.XCodSan.grid(); self.YCodSan.grid()
            self.XEmail.grid_remove(); self.YEmail.grid_remove(); self.YEmail.delete(0, tk.END)
    ###########################################################################

    # LOGIN CLICKED ###########################################################
    def login_clicked(self, event):
        email = self.email.get()
        codsan = self.codsan.get()
        password = self.password.get()
        user_type = self.user_type.get()

        self.controller.login(email,codsan,password,user_type)

    ###########################################################################

    # FOCUS PASSWORD ##########################################################
    def focus_password(self, event):
        self.YPassword.focus_set()
    ###########################################################################

    # INIT ####################################################################
    def __init__(self):
        super().__init__()

        # SET WINDOW DEFAULT SETTINGS #########################################
        set_window_default_settings(self, "Login", 425, 200)
        #######################################################################

        
        # Imposta lo stile ####################################################
        self.ttkstyle = ttk.Style()
        self.ttkstyle.theme_use('clam')

        # styles ################################
        # label style
        self.label_style = { "background" :"#0b6063", "foreground" :"#ffffff", "font":("Helvetica", 13), "width":15 }
        # entry style
        self.entry_style = { "background" :"#ffffff", "foreground" :"#000000", "font":("Helvetica", 13), "width":30 }
        # radio style
        self.radio_style = { "background" :"#ffffff", "foreground" :"#000000", "font":("Helvetica", 13), "width":13 }
        # button style
        self.button_style = { "background" :"#ffffff", "foreground" :"#000000", "font":("Helvetica", 10, "bold"), "width":10 }
        #########################################

        # layouts ###############################  
        # label layout
        self.label_layout = {"padx": 15, "pady": 15, "sticky":"nw"}
        # entry layout
        self.entry_layout = {"padx": 15, "pady": 15, "sticky":"ne"}
        # radio layout 
        self.radio_layout = {"padx": 10, "pady": 10, "sticky":"sw"}
        # button layout
        self.button_layout = {"padx": 10, "pady": 10, "sticky":"se"}
        #########################################

        #######################################################################

        # BACKGROUND IMAGE ####################################################
        # Carica l'immagine di sfondo
        self.bg_image = tk.PhotoImage(file="./assets/bg.png")
        bg_label = ttk.Label(self, image=self.bg_image)
        bg_label.place(x=0, y=0)
        # Posiziona l'immagine di sfondo
        self.background_label = tk.Label(self, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #######################################################################

        # GRID LAYOUT #########################################################
        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)
        #######################################################################

        # WIDGETS #############################################################
        # Input Email
        self.email = tk.StringVar()
        self.XEmail = self.Xlabel("Email",0,0)
        self.YEmail = self.Xinput(0,1,self.email)
        self.YEmail.grid(columnspan=2)
        # Input Codice Fiscale
        self.codsan = tk.StringVar()
        self.XCodSan = self.Xlabel("Codice Fiscale",0,0)
        self.XCodSan.grid_remove()
        self.YCodSan = self.Xinput(0,1, self.codsan)
        self.YCodSan.grid(columnspan=2)
        self.YCodSan.grid_remove()
        # Input Password
        self.password = tk.StringVar()
        self.XPassword = self.Xlabel("Password",1,0)
        self.YPassword = self.Xinput(1,1, self.password)
        self.YPassword.configure(show="*")
        self.YPassword.grid(columnspan=2)
        # Radio Buttons
        self.user_type = tk.StringVar()
        self.R1 = self.Xradio("Personale",self.user_type,self.toggle_fields,2,0)
        self.R2 = self.Xradio("Paziente",self.user_type,self.toggle_fields,2,1)
        # Login Button
        self.XLogin = self.Xbutton("Login",self.login_clicked,2,2)
        # Return Binding
        self.bind("<Return>", self.login_clicked)
        #######################################################################