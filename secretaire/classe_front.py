"""



create table classe(
id_class int auto_increment primary key,
nom varchar(30) unique
);

en se basant sur le code de login_front.py et ajoutant les fonctionnalités de AnneScolaire dans anne_scolaire_back.py
fait moi un interface graphique d'ajout, de modification et de suppression d'une classe
avec tkinter

"""
from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning,askyesno
from .classe_backend import Classe
from tkinter.ttk import Treeview
#from side_bar import SideBar
""" 
pour eviter l'erreur d'importation circulaire j'importe d'une autre manière

"""

from. import side_bar
import generate_key as gn
class ClasseFront:
    def __init__(self,connection):
        self.connexion=connection
    
        self.fen=Tk()
    
        self.fen.title("Classe")
        self.fen.geometry("800x600+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar.SideBar(self.fen,self.connexion)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Classe",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom=Label(self.fen,text="Nom de la classe:",font=("Times",15),fg="black",background='#51a596')
        self.label_nom.place(x=305,y=100,width=250)
        self.tex_nom=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_nom.place(x=550,y=100,width=200)
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=200,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modify)
        self.bouton_modifier.place(x=500,y=200,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=200,width=100)
        self.selected_id=IntVar()
        self.selected_nom=StringVar()
        self.E=None

        self.tree=Treeview(self.fen, columns=('Id','Designation'), show='headings')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Designation', text='Designation')
        self.tree.column('Id',width=50)
        self.tree.column('Designation',width=100)
        
        self.tree.place(x=300,y=300,height=200)
        
        self.afficher()
    def selection(self,evt):
        
        self.selected_id=self.tree.item(self.tree.selection())['values'][0]        
        self.clean_entry()
        row=self.tree.item(self.tree.selection())
        self.tex_nom.insert(0,row['values'][1])
    def clean_entry(self):
        self.tex_nom.delete(0,END)
    
    def ajouter(self):
        if self.E==None:
            self.E=Classe(self.tex_nom.get())
            id=self.E.get_last_id(self.connexion.get_curseur())
            if id[1]==True:
                f=id[0][0]
            
                if  id[0][0] ==None:
                    f=1
                else:
                    f=id[0][0]+1
            key=gn.generate_key("Cl",4,f)
            
            if self.E.save(self.connexion.get_curseur(),key):
                self.afficher()
                self.E=None
                showinfo("Succès","Ajout réussi")
            else:
                showerror("Echec","Ajout échoué")
        else:
            showwarning("Echec","Veuillez vider le formulaire")
    def modify(self):
        if self.E==None:
            self.E=Classe(self.tex_nom.get())
            if self.E.update(self.connexion.get_curseur(),self.selected_id):
                self.afficher()
                self.E=None
                showinfo("Succès","Modification réussie")
            else:
                showerror("Echec","Modification échouée")
        else:
            showwarning("Echec","Veuillez vider le formulaire")
    def supprimer(self):
        if self.E==None:
            self.E=Classe(self.tex_nom.get())
            
            if askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cette classe ?"):
                if self.E.delete(self.connexion.get_curseur()):
                    self.afficher()
                    self.E=None
                    showinfo("Succès", "Suppression réussie")
                else:
                    self.E=None
                    showerror("Echec", "Suppression échouée")
            else:
                self.E=None
                showinfo("Annulation", "Suppression annulée")
        else:
            self.E=None
            showwarning("Echec","Veuillez vider le formulaire")
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        for row in Classe("3").get_all(self.connexion.get_curseur()):
            self.tree.insert("", "end", values=row)
        self.tree.bind("<ButtonRelease-1>",self.selection)
    def get_entry(self):
        self.selected_nom.set(self.tex_nom.get())
    def fenetre(self):
        return self.fen
