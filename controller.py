from model import Model
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login(self, email, codsan, password, user_type):
        print(email," ",codsan," ",password," ",user_type)