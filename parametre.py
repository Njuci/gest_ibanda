"""ici nous allons définir les paramètres la base de données  dans le fichier parametre.cnf

Entry:
    host: localhost
    user: root
    password:
    database: gestion_ibanda
    
"""

from configparser import ConfigParser
import os

def config(filename='parametre.cnf', section='mysql'):
    # Créer un analyseur
    parser = ConfigParser()
    # Lire le fichier
    parser.read(filename)
    # Obtenir la section, par défaut mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db
def write_config(filename='parametre.cnf', section='mysql', host='localhost',  user='root', password='', database='gestion_ibanda'):
    # Créer un analyseur
    parser = ConfigParser()
    # Lire le fichier
    parser.read(filename)
    # Obtenir la section, par défaut mysql
    db = {}
    if not parser.has_section(section):
        parser.add_section(section)
    parser.set(section, 'host', host)
    parser.set(section, 'user', user)
    parser.set(section, 'password', password)
    parser.set(section, 'database', database)
    with open(filename, 'w') as configfile:
        parser.write(configfile)
    return db

def update_config(filename='parametre.cnf', section='mysql', host='localhost', user='root', password=''):
    #update the config file
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        parser.set(section, 'host', host)
        parser.set(section, 'user', user)
        parser.set(section, 'password', password)
        with open(filename, 'w') as configfile:
            parser.write(configfile)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return True
#nterface de configuration avec tkinter

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog

class Config:
    def __init__(self):
        self.fen = Tk()
        self.fen.title("Configuration")
        self.fen.geometry("500x400")
        self.fen.config(bg="white",background='#51a596')
        self.fen.resizable(False, False)
        self.config = config()
        self.host = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        self.database = StringVar()
        self.host.set("localhost")
        self.user.set("root")
        self.password.set("")
        self.database.set("gestion_ibanda")
        
   
        self.label = Label(self.fen, text="Configuration de la base de données", font="Arial 15 bold",background='#51a596')
        self.label.place(x=100, y=20)
        self.label = Label(self.fen, text="Host", font="Arial 12",background='#51a596')
        self.label.place(x=50, y=80)
        self.entry_host = Entry(self. fen, textvariable=self.host)
        self.entry_host.place(x=200, y=80)
        self.label = Label(self.fen, text="User", font="Arial 12",background='#51a596')
        self.label.place(x=50, y=120)
        self.entry_user = Entry(self.fen, textvariable=self.user)
        self.entry_user.place(x=200, y=120)
        self.label = Label(self.fen, text="Password", font="Arial 12",background='#51a596')
        self.label.place(x=50, y=160)
        self.entry_password = Entry(self.fen, textvariable=self.password)
        self.entry_password.place(x=200, y=160)
        self.label = Label(self.fen, text="Database", font="Arial 12",background='#51a596')
        self.label.place(x=50, y=200)
        self.entry_database = Entry(self.fen, textvariable=self.database)
        self.entry_database.place(x=200, y=200)
        self.bouton = Button(self.fen, text="Enregistrer", background='#FF4500',font=("Times",16),fg='white', command=self.save)
        self.bouton.place(x=200, y=240)
        
    def fenetre(self):
        return self.fen
    def save(self):
        self.host = self.entry_host.get()
        self.user = self.entry_user.get()
        self.password = self.entry_password.get()
        self.database = self.entry_database.get()
        write_config(host=self.host, user=self.user, password=self.password, database=self.database)
        messagebox.showinfo("Information", "Configuration enregistrée avec succès")
        self.fen.destroy()
def config():
    # Créer un analyseur
    parser = ConfigParser()
    #creer le fichier s'il n'existe pas et l'initialiser
    
    if not os.path.exists('parametre.cnf'):
        write_config()
    
    # Lire le fichier
    
    
    parser.read('parametre.cnf')
    # Obtenir la section, par défaut mysql
    db = {}
    if parser.has_section('mysql'):
        items = parser.items('mysql')
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format('mysql', 'parametre.cnf'))
    return db   
def main():
    try:
        config()
    except:
        Config()
if __name__ == '__main__':
    db=Config()
    db.fen.mainloop()
    
    main()