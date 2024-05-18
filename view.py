import tkinter as tk
from tkinter import ttk
from utils import *
from PIL import Image, ImageTk

class Window():
    # SET CONTROLLER ##########################################################
    def set_controller(self, controller):
        """ imposta il controller """
        self.controller = controller
    ###########################################################################

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
        btn = ttk.Button(self, text=str1, command=cmd)
        btn.grid(row=riga, column=col, **self.button_layout)
        return btn
    ###########################################################################

class View(tk.Tk, Window):
    # INIT ####################################################################
    def __init__(self):
        super().__init__()

        # SET WINDOW DEFAULT SETTINGS #########################################
        set_window_default_settings(self, "Login", 475, 200) # 475x200 Login Window
        #######################################################################
        
        # Imposta lo stile ####################################################
        self.ttkstyle = ttk.Style() # create style object
        self.ttkstyle.theme_use('clam') # set style

        # styles ################################
        # label style
        self.label_style = { "background" :"#0b6063", 
                             "foreground" :"#ffffff", 
                             "font":("Helvetica", 13), 
                             "width":15 } # label
        # entry style
        self.entry_style = { "background" :"#ffffff", 
                             "foreground" :"#000000", 
                             "font":("Helvetica", 13), 
                             "width":30 } # entry
        # radio style
        self.radio_style = { "background" :"#ffffff", 
                             "foreground" :"#000000", 
                             "font":("Helvetica", 13), 
                             "width":13 } # radio button
        # button style
        self.ttkstyle.configure("TButton", 
                                background ="#ffffff", 
                                foreground ="#000000", 
                                font=("Helvetica", 10, "bold"), 
                                width=10) # login button
        self.ttkstyle.map("TButton", background=[('active', '#0d6b6e')]) # green when mouse over
        #########################################

        # layouts ###############################  
        # label layout
        self.label_layout = {"padx": 15, "pady": 15, "sticky":"nw"} # label
        # entry layout
        self.entry_layout = {"padx": 15, "pady": 15, "sticky":"ne"} # entry
        # radio layout 
        self.radio_layout = {"padx": 10, "pady": 10, "sticky":"sw"} # usertype radio button
        # button layout
        self.button_layout = {"padx": 10, "pady": 10, "sticky":"se"} # login button
        #########################################

        #######################################################################

        # BACKGROUND IMAGE ####################################################
        # Carica l'immagine di sfondo
        self.bg_image = tk.PhotoImage(file="./assets/bg.png") # open image
        # Posiziona l'immagine di sfondo
        self.background_label = tk.Label(self, image=self.bg_image) # image label
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1) # place image label
        #######################################################################

        # GRID LAYOUT #########################################################
        self.grid_rowconfigure((0,1,2), weight=1) # all rows have same weight
        self.grid_columnconfigure((0,1,2), weight=1) # all cols have same weight 
        #######################################################################

        # WIDGETS #############################################################
        # Input Email
        self.email = tk.StringVar() # email var
        self.XEmail = self.Xlabel("Email",0,0) # email label
        self.YEmail = self.Xinput(0,1,self.email) # email entry 
        # Input Codice Fiscale
        self.codsan = tk.StringVar() # codsan var
        self.XCodSan = self.Xlabel("Codice Ficsale",0,0) # codsan label
        self.YCodSan = self.Xinput(0,1, self.codsan) # codsan entry
        # Input Password
        self.password = tk.StringVar() # password var
        self.XPassword = self.Xlabel("Password",1,0) # password label
        self.YPassword = self.Xinput(1,1, self.password) # password entry
        self.YPassword.configure(show="*") # nascondi caratteri password
        # Radio Buttons
        self.user_type = tk.StringVar() # usertype var
        self.user_type.set("Personale") # usertype default
        self.R1 = self.Xradio("Personale",self.user_type,self.toggle_fields,2,0) # personale radio button
        self.R2 = self.Xradio("Paziente",self.user_type,self.toggle_fields,2,1) # paziente radio button
        # Login Button
        self.XLogin = self.Xbutton("Login",self.authenticate,2,2) # login button
        # Return Binding
        self.bind("<Return>",self.authenticate) # call login_clicked if <RETURN> pressed
        #######################################################################

        # DEBUG : HARDCODED INPUTS ############################################
        # MEDICO
        #self.YEmail.insert(0, "giulia.verdi@example.com")
        #self.YPassword.insert(0, "password456#789")
        # INFERMIERE
        #self.YEmail.insert(0, "stefanozanolli765@gmail.com")
        #self.YPassword.insert(0, "password123#456")
        # MAIN
        #self.YEmail.insert(0, "admin")
        #self.YPassword.insert(0, "admin")
        # PAZIENTE
        self.YCodSan.insert(0, "PS123456789")
        self.YPassword.insert(0, "password#123")
        #######################################################################

        # GRID CHANGES ########################################################
        self.YEmail.grid(columnspan=2) # email entry occupa 2 colonne
        self.YCodSan.grid(columnspan=2) # codsan entry occupa 2 colonne
        self.YPassword.grid(columnspan=2) # password entry occupa 2 colonne
        self.XCodSan.grid_remove() # nascondi codsan label
        self.YCodSan.grid_remove() # nascondi codsan entry 
        #######################################################################
    ###########################################################################

    # DESTROY LOGIN ###########################################################
    def destroy_login(self):
        self.destroy()
    ###########################################################################

    # LOGIN CLICKED ###########################################################
    def authenticate(self,event=None):
        try :
            password = self.password.get()
            
            user_type = self.user_type.get()
            if user_type=="Personale":
                email = self.email.get()
                codsan = None
            elif user_type=="Paziente":
                codsan = self.codsan.get()
                email = None
            else: 
                Log("view","@authenticate: user type error")
            self.controller.login(email,codsan,password,user_type)
        except UnboundLocalError as e:
            Log("view","@authenticate: some field is empty")
            print(e)
        except Exception as e:
            print(e)
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

    # FOCUS PASSWORD ##########################################################
    def focus_password(self):
        self.YPassword.focus_set() 
    ###########################################################################

class Paziente(tk.Toplevel, Window):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller

        X=800; Y=650

        # SET WINDOW DEFAULT SETTINGS #########################################
        set_window_default_settings(self, "Paziente", X, Y) # 800x650 Paziente Window
        self.resizable(False, False)
        #######################################################################

        # Imposta lo stile ####################################################
        self.ttkstyle = ttk.Style() # create style object
        self.ttkstyle.theme_use('clam') # set style

        # styles ################################
        self.ttkstyle.configure("main.TFrame", background ="#b3ecff")
        self.ttkstyle.configure("menu.TFrame", background ="#ffffb3")
        #########################################

        # layouts ###############################
        self.Xmain_layout = { "width":X, "height":Y }
        self.Xmenu_layout = { "width":X*0.7, "height":Y*0.7 } # 70% of width and height
        #########################################

        #######################################################################
        self.Xmain = ttk.Frame(self, style="main.TFrame", **self.Xmain_layout) # Main Frame
        self.Xmain.place(relx=0.5, rely=0.5, anchor="center")

        self.Xmenu = ttk.Frame(self.Xmain, style="menu.TFrame", **self.Xmenu_layout) # Menu Frame
        self.Xmenu.place(relx=0.5, rely=0.5, anchor="center")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.XTitle = self.Xlabel("MODULO PRENOTAZIONE",0,0)



        self.mainloop()

class Medico(tk.Toplevel, Window):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller

class Infermiere(tk.Toplevel, Window):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller

class Segreteria(tk.Toplevel, Window):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller



