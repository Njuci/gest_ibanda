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
import assigner_class_front as assign
import utilisateur_front
import domaine_cours_frontemd
import cours_fronted
#import secretaire.classe_front
class Sidebar_proviseur(Frame):
    def __init__(self, fen,cursor=None):
        self.fen = fen
        self.curseur = cursor
        self.MenuContainer = Frame(self.fen, height=800, width=230, bg='#51a596')
        self.MenuContainer.place(x=0, y=0)
        self.titre = Label(self.MenuContainer, text="GEST IBANDA", font="Arial 15 bold", bg='#51a596', fg='black')
        self.titre.place(x=30, y=20)
        # bouton pour la gestion des classes
        # bouton pour la gestion des utilisateurs
        self.bouton_utilisateur = Button(self.MenuContainer, text="Utilisateurs", font="Arial 12",command=self.user)
        self.bouton_utilisateur.place(x=30, y=150 ,width=190, height=40)
        # bouton pour la gestion des matieres
        self.bouton_matiere = Button(self.MenuContainer, text="Cours", font="Arial 12",command=self.cours)
        self.bouton_matiere.place(x=30, y=200 ,width=190, height=40)
        # bouton pour la gestion des domaines de cours
        self.bouton_domaine = Button(self.MenuContainer, text="Domaines", font="Arial 12",command=self.domaine)
        self.bouton_domaine.place(x=30, y=250 ,width=190, height=40)
        # bouton pour la gestion des rapports de notes
        self.bouton_rapport = Button(self.MenuContainer, text="Rapports", font="Arial 12")
        self.bouton_rapport.place(x=30, y=300, width=190, height=40)
        # bouton pour la gestion des anne scolaire
        self.bouton_annee = Button(self.MenuContainer, text="Assigner classe", font="Arial 12",command=self.assigenr_classe)
        self.bouton_annee.place(x=30, y=350, width=190, height=40)
        # bouton pour la gestion des palmarea
        self.bouton_palmares = Button(self.MenuContainer, text="Palmares", font="Arial 12")
        self.bouton_palmares.place(x=30, y=400 ,width=190, height=40)


    def place(self, x, y):
        self.MenuContainer.place(x=x, y=y)
    def save(self):
            pass
    def domaine(self):
        self.fen.destroy()
        domain_f=domaine_cours_frontemd.Domaine_cours_front(self.curseur)
        domain_f.fenetre().mainloop()
    def user(self):
        self.fen.destroy()
        user=utilisateur_front.utilisateur_front(self.curseur)
        user.fenetre().mainloop()
    def cours(self):
        self.fen.destroy()
        cour=cours_fronted.Cours(self.curseur)
        cour.fenetre().mainloop()

    
    def assigenr_classe(self):
        self.fen.destroy()
        assign.Assigner_class_front(self.curseur)
        
# Path: side_bar.py
# Compare this snippet from side_bar_provieir.py:
# """
# en tant que proviseur, je veux avoir un side bar qui me permettra de naviguer dans l'application
# - bouton pour la Liste des classes