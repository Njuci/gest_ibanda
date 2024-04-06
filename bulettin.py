"""un combox qui contient les id_inscription des eleves inscrits dans une classe pour une annee scolaire donnee
et un tableau qui contient les cotes des eleves inscrits dans une classe pour une annee scolaire donnee
les cotes sont les cotes des eleves inscrits dans une classe pour une annee scolaire donnee et sont affiche`es dans un tableau en fonction de l'id_inscription de l'eleve
et en se basant sur les cours de la classe pour une annee scolaire donnee
sidebar tiutulaire


"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
from secretaire.eleve_back import eleve_back as Eleve
from secretaire.inscription_backend import inscription_back as Inscription
from tkinter.ttk import Treeview
from tkinter import messagebox
import side_bar_tutulaire as side_bar_tutulaire
from cours_backend import cours_back as Cours
from fiche_cote_back import Fiche_cote_back as Fiche_cote
from secretaire.anne_scolaire_back import AnneScolaire

class bulletin:
    def __init__(self,connexion):
        self.connexion=connexion
        self.fen=Tk()
        self.fen.title("Bulletins")
        self.fen.geometry("900x900+150+0")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar_tutulaire.SideBar_tutulaire(self.fen,self.connexion)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Bulletins",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_classe=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_classe.place(x=300,y=100)
        self.label_classe=Label(self.fen,text=self.connexion['id_classe'],font=("Sans Serif",19),fg='white',background='#51a596')
        self.label_classe.place(x=400,y=100)
        self.combo_classe=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.label_anne_scolaire=Label(self.fen,text="Année scolaire",font=("Sans Serif",12),fg='white',background='#51a596')
        self.combo_anne_scolaire=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.bouton_afficher=Button(self.fen,text='Afficher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.tree=ttk.Treeview(self.fen,columns=('Cours','Periode 1','Periode 2','Exanen','Senestre','Periode 3','Periode 4','Examen','Semestre','Total'),show='headings')
        
        #heding of tree
        self.tree.heading('Cours', text='Cours')
        self.tree.heading('Periode 1', text='Periode 1')
        self.tree.heading('Periode 2', text='Periode 2')
        self.tree.heading('Examen', text='Examen')
        self.tree.heading('Semestre', text='Semestre')
        self.tree.heading('Periode 3', text='Periode 3')
        self.tree.heading('Periode 4', text='Periode 4')
        self.tree.heading('Examen', text='Examen')
        self.tree.heading('Semestre', text='Semestre')
        self.tree.heading('Total', text='Total')
        #column
        self.tree.column('Cours', width=150)
        self.tree.column('Periode 1', width=70)
        self.tree.column('Periode 2', width=70)
        self.tree.column('Examen', width=70)
        self.tree.column('Semestre', width=70)
              
        self.tree.column('Periode 3', width=70)
        self.tree.column('Periode 4', width=70)
        self.tree.column('Examen', width=70)
        self.tree.column('Semestre', width=70)
        self.tree.column('Total', width=70)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        