"""
fais moi un side bar qui correspond à SideBar dans le fichier Sider_ar.py
et qui hérite de Frame
qui a les boutons suivants:
- Accueil
- Annee scolaire
- Classe
- Eleve
et prend en compte les mesures du SideBar dans le fichier Side_bar.py """
from tkinter import *
#from classe_front import ClasseFront
#from anne_scolaire_front import anne_scolaire
#from elelve import EleveFront
""" 
pour eviter l'erreur d'importation circulaire j'importe d'une autre manière

"""
from . import classe_front
import login_front
from . import anne_scolaire_front
from . import elelve
from . import imscription_front

class SideBar:
    def __init__(self, fen,cursor=None):
        self.fen = fen
        self.curseur = cursor
        self.MenuContainer = Frame(self.fen, height=800, width=230, bg='#51a596')
        self.MenuContainer.place(x=0, y=0)
        self.titre = Label(self.MenuContainer, text="GEST IBANDA", font="Arial 15 bold", bg='#51a596', fg='white')
        self.titre.place(x=30, y=20)

        self.gest_login = Button(self.MenuContainer, text='Accueil', command=self.login)
        self.gest_login.place(x=20, y=80, width=190, height=40)

        self.gest_clsse = Button(self.MenuContainer, text='Classe', command=self.classe_scol)
        self.gest_clsse.place(x=20, y=140, width=190, height=40)

        self.gest_anne_sc = Button(self.MenuContainer, text='Anne scolaire', command=self.anne_scol)
        self.gest_anne_sc.place(x=20, y=200, width=190, height=40)

        self.gest_Clients = Button(self.MenuContainer, text='Eleve', command=self.eleve_call)
        self.gest_Clients.place(x=20, y=260, width=190, height=40)

        self.gest_Clients = Button(self.MenuContainer, text='Inscription', command=self.inscription)
        self.gest_Clients.place(x=20, y=320, width=190, height=40)
    def place(self, x, y):
        self.MenuContainer.place(x=x, y=y)
    def login(self):
         self.fen.destroy()
         login_form= login_front.Login_front()
         login_form.fenetre().mainloop()
         
    def anne_scol(self):
         self.fen.destroy()         
         anne_scola=anne_scolaire_front.anne_scolaire(self.curseur)
         anne_scola.fenetre().mainloop()

    def classe_scol(self):
         self.fen.destroy()
         class_scol=classe_front.ClasseFront(self.curseur)
         class_scol.fenetre().mainloop()
    def eleve_call(self):
         self.fen.destroy()
         ele_ve=elelve.EleveFront(self.curseur)
         ele_ve.fenetre().mainloop()
    def inscription(self):
         self.fen.destroy()
         inscription_r=imscription_front.InscriptionFront(self.curseur)
         inscription_r.fenetre().mainloop()
          
    def save(self):
            pass
    

