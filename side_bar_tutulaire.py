"""en se basant sur side_bar.py fais moi un side_bar_tutulaire.py qui contient les boutons suivants:

    fiche de cotes
    la liste des élèves
    la liste des cours de sa classe
    les bultins 
    les statistiques de sa classe
    les palmares de sa classe"""
# Path: side_bar_tutulaire.py
# Compare this snippet from side_bar.py:
from tkinter import *

class SideBar_tutulaire:
    def __init__(self, fen,cursor=None):
        self.fen = fen
        self.curseur = cursor
        self.MenuContainer = Frame(self.fen, height=800, width=230, bg='#51a596')
        self.MenuContainer.place(x=0, y=0)
        self.titre = Label(self.MenuContainer, text="GEST IBANDA", font="Arial 15 bold", bg='#51a596', fg='white')
        self.titre.place(x=30, y=20)
        self.bouton_fiche_cotes = Button(self.MenuContainer, text='Fiche de cotes', command=self.fiche_cotes)
        self.bouton_fiche_cotes.place(x=20, y=80, width=190, height=40)
        self.bouton_liste_eleves = Button(self.MenuContainer, text='Liste des élèves', command=self.liste_eleves)
        self.bouton_liste_eleves.place(x=20, y=140, width=190, height=40)
        self.bouton_liste_cours = Button(self.MenuContainer, text='Liste des cours', command=self.liste_cours)
        self.bouton_liste_cours.place(x=20, y=200, width=190, height=40)
        self.bouton_bulletins = Button(self.MenuContainer, text='Bulletins', command=self.bulletins)
        self.bouton_bulletins.place(x=20, y=260, width=190, height=40)
        self.bouton_statistiques = Button(self.MenuContainer, text='Statistiques', command=self.statistiques)
        self.bouton_statistiques.place(x=20, y=320, width=190, height=40)
        self.bouton_palmares = Button(self.MenuContainer, text='Palmares', command=self.palmares)
        self.bouton_palmares.place(x=20, y=380, width=190, height=40)
    def place(self, x, y):
        self.MenuContainer.place(x=x, y=y)
    def fiche_cotes(self):
        print("fiche de cotes")
    def liste_eleves(self):
        print("liste des élèves")
    def liste_cours(self):
        print("liste des cours")
    def bulletins(self):
        print("bulletins")
    def statistiques(self):
        print("statistiques")
    def palmares(self):
        print("palmares")
# Compare this snippet from treeEdit.py:
