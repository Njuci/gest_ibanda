import mysql.connector 
from tkinter.messagebox import showerror,showinfo
class Connexion:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '3670njci',
            database = 'gest_ecole',
            autocommit=True
        )
        self.curseur = self.db.cursor()
    def login(self):
        try:
            if self.db.is_connected():
                 return True
        except Exception as e:
            showerror("Erreur",str(e)) 
            return False     

    def get_curseur(self):
        return self.curseur                 
    def get_connexion(self):
        return self.curseur
    def get_parametres_connexion(self):
        return self.db
    def close(self):
        self.db.close()
        self.curseur.close()