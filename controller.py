from model import *
from view import *
from utils import *

class Controller:
    log_type = "ctrl"

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login(self, email=None, codsan=None, password=None, user_type=None):
        logged=False
        if email=="admin" and password=="admin":
            logged=True
            self.paziente = Segreteria(self.view,self) # create Paziente page        
            self.view.destroy_login() # destroy login page

        if email is None:
            # try login as paziente

            data = self.model.get_data("*","paziente","codice_sanitario",codsan)
            for r in data:
                if ( r[0]==codsan and r[1]==password ) :
                    print("Logged as Paziente")
                    self.paziente = Paziente(self.view,self) # create Paziente page
                    self.view.destroy_login() # destroy login page
                    logged=True; break
                
        elif codsan is None:
            # try login as medico
            data = self.model.get_data("*","medico","email",email)
            for r in data:
                if ( r[1]==email and r[2]==password ) :
                    print("Logged as Medico")
                    self.paziente = Medico(self.view,self) # create Medico page
                    self.view.destroy_login() # destroy login page
                    logged=True; break

            # try login as infermiere
            data = self.model.get_data("*","infermiere","email",email)
            for r in data:
                if ( r[1]==email and r[2]==password ) :
                    print("Logged as Infermiere")
                    self.paziente = Infermiere(self.view,self) # create Infermiere page
                    self.view.destroy_login() # destroy login page
                    logged=True; break
            
            if not logged : Log("ctrl","@login: login fallito")
