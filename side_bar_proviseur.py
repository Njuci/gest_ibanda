"""
en tant que proviseur, je veux avoir un side bar qui me permettra de naviguer dans l'application
- bo pour la Liste des classes
- bouton pour la Liste des eleves
- bouton pour la bouton pour la Liste des utilisateurs
- bouton pour la Liste des matieres
- bouton pour la  bouton pour la Liste des notes
- bouton pour la Liste des rapports de notes
- bouton pour la  Liste des bulletins

en se basamnt sur la classe Sidebar dans le fichier side_bar.py
"""
from tkinter import Frame, Label, Button
class Sidebar_proviseur(Frame):
    def __init__(self, fen,cursor=None):
        self.fen = fen
        self.curseur = cursor
        self.MenuContainer = Frame(self.fen, height=800, width=230, bg='#51a596')
        self.MenuContainer.place(x=0, y=0)
        self.titre = Label(self.MenuContainer, text="GEST IBANDA", font="Arial 15 bold", bg='#51a596', fg='black')
        self.titre.place(x=30, y=20)
        # bouton pour la gestion des classes
        self.bouton_classe = Button(self.MenuContainer, text="Classes", font="Arial 12")
        self.bouton_classe.place(x=30, y=100,width=190,height=40)
        # bouton pour la gestion des utilisateurs
        self.bouton_utilisateur = Button(self.MenuContainer, text="Utilisateurs", font="Arial 12")
        self.bouton_utilisateur.place(x=30, y=150 ,width=190, height=40)
        # bouton pour la gestion des matieres
        self.bouton_matiere = Button(self.MenuContainer, text="Matieres", font="Arial 12")
        self.bouton_matiere.place(x=30, y=200 ,width=190, height=40)
        # bouton pour la gestion des domaines de cours
        self.bouton_domaine = Button(self.MenuContainer, text="Domaines", font="Arial 12")
        self.bouton_domaine.place(x=30, y=250 ,width=190, height=40)
        # bouton pour la gestion des rapports de notes
        self.bouton_rapport = Button(self.MenuContainer, text="Rapports", font="Arial 12")
        self.bouton_rapport.place(x=30, y=300, width=190, height=40)
        # bouton pour la gestion des anne scolaire
        self.bouton_annee = Button(self.MenuContainer, text="Annees", font="Arial 12")
        self.bouton_annee.place(x=30, y=350, width=190, height=40)
        # bouton pour la gestion des palmarea
        self.bouton_palmares = Button(self.MenuContainer, text="Palmares", font="Arial 12")
        self.bouton_palmares.place(x=30, y=400 ,width=190, height=40)


        
    def place(self, x, y):
        self.MenuContainer.place(x=x, y=y)
    def save(self):
            pass
# Path: side_bar.py
# Compare this snippet from side_bar_provieir.py:
# """
# en tant que proviseur, je veux avoir un side bar qui me permettra de naviguer dans l'application
# - bouton pour la Liste des classes