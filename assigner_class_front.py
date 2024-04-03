"""

cette classe nous permettra de gerer les assignations des classes aux utilisateurs
a savoir les enseignants  titulaires des classes
Interface comme celui de la classe utilisateur
avec des commentaires precis


"""
from tkinter import *
from tkinter.messagebox import showerror,showinfo
from assigner_class_back import Assigner_class_back
from user_back import User_back
from secretaire import classe_backend 
from secretaire.anne_scolaire_back import AnneScolaire
from tkinter.ttk import Treeview
from login_back import Connexion
from tkinter import ttk
import side_bar_proviseur 
class Assigner_class_front:
    def __init__(self,connexion):
        self.fen=Tk()
        self.connexion=connexion
        self.fen.title("Assigner classe")
        self.fen.geometry("800x600+150+0")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar_proviseur.Sidebar_proviseur(self.fen,self.connexion)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Assigner classe",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_tutilaire=Label(self.fen,text="Titulaire",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_tutilaire.place(x=300,y=100)
        self.combo_tutilaire=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_tutilaire.place(x=400,y=100)
        self.label_class=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_class.place(x=300,y=150)
        self.combo_class=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_class.place(x=400,y=150)
        self.label_anne_scolaire=Label(self.fen,text="Année scolaire",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_anne_scolaire.place(x=300,y=200)
        self.combo_anne_scolaire=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_anne_scolaire.place(x=400,y=200)
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=250,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=250,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=250,width=100)
        self.remplir_combo()
        self.id_tutilaire=IntVar()
        self.id_class=IntVar()
        self.id_anne_scolaire=IntVar()
        self.tree=ttk.Treeview(self.fen,columns=('Num','id_tutilaire','Nom Titulaire','id_class','id_anne_scolaire'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('id_tutilaire',text='Titulaire')
        self.tree.heading('Nom Titulaire',text='Nom Titulaire')
        self.tree.heading('id_class',text='Classe')
        self.tree.heading('id_anne_scolaire',text='Année scolaire')
        self.tree.column('Num',width=50)
        self.tree.column('id_tutilaire',width=80)
        self.tree.column('Nom Titulaire',width=100)
        self.tree.column('id_class',width=120)
        self.tree.column('id_anne_scolaire',width=150)
        self.afficher()
    def ajouter(self):
        
        assign=Assigner_class_back(self.combo_tutilaire.get().split('|')[0],self.combo_class.get().split('|')[0],self.combo_anne_scolaire.get().split('|')[0])
        if assign.save(self.connexion.get_curseur()):
            showinfo("Succès","Assignation reussie")
            self.afficher()
        else:
            showerror("Erreur","Echec de l'assignation")

    def modifier(self):
        
        assign=Assigner_class_back(self.combo_tutilaire.get().split('|')[0],self.combo_class.get().split('|')[0],self.combo_anne_scolaire.get().split('|')[0])
        if assign.update(self.connexion.get_curseur(),self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get()):
            showinfo("Succès","Modification reussie")
            self.afficher()
        else:
            showerror("Erreur","Echec de la modification")
    
    def supprimer(self):
        assign=Assigner_class_back(self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get())
        if assign.delete(self.connexion.get_curseur(),self.combo_tutilaire.get().split('|')[0],self.combo_class.get().split('|')[0],self.combo_anne_scolaire.get().split('|')[0]):
            showinfo("Succès","Suppression reussie")
            self.remplir_combo()
            self.afficher()
        else:
            showerror("Erreur","Echec de la suppression")
    def get_old_selection(self):
        self.selected=self.tree.item(self.tree.selection()[0])['values']
        self.id_tutilaire.set(self.selected[1])
        self.id_class.set(self.selected[3])
        self.id_anne_scolaire.set(self.selected[4])

    def afficher(self):
        assign=Assigner_class_back(0,0,0)
        data=assign.get_all(self.connexion.get_curseur())
        
        self.tree.delete(*self.tree.get_children())
        cpt=0

        for row in data:
            cpt+=1
            self.tree.insert('','end',values=(cpt,row[0],row[1],str(row[2])+"|"+row[3],str(row[4])+"|"+row[5]))
        self.tree.bind('<Double-Button-1>',self.get_selection)
        
        self.tree.place(x=250,y=300)
        
    def get_selection(self,event):
        self.selected=self.tree.item(self.tree.selection()[0])['values']
        #renplir les combobox avec les valeurs 
        print(self.selected)
        self.combo_tutilaire.set(str(self.selected[1])+"|"+self.selected[2])
        self.combo_class.set(self.selected[3])
        self.combo_anne_scolaire.set(self.selected[4])
        
        
    #pour remplir les combobox
    def remplir_combo(self):
        #remplir la combobox titulaire
        user=User_back("","","")
        data=user.get_all_tutilaire(self.connexion.get_curseur())
        self.combo_tutilaire['values']=[(str(row[1])+"|"+row[2]) for row in data]
        self.combo_tutilaire.bind('<<ComboboxSelected>>',self.get_id_tutilaire)
        #remplir la combobox classe
        
        classe=classe_backend.Classe("")
        data=classe.get_all(self.connexion.get_curseur())
        self.combo_class['values']=[(str(data[0])+"|"+data[1]) for data in data]
        self.combo_class.bind('<<ComboboxSelected>>',self.get_id_class)
        #remplir la combobox anne scolaire
        anne=AnneScolaire("",0)
        data=anne.get_all(self.connexion.get_curseur())
        self.combo_anne_scolaire['values']=[(str(data[0])+"|"+data[1]) for data in data]
        self.combo_anne_scolaire.bind('<<ComboboxSelected>>',self.get_id_anne_scolaire)
        #.get().split('|')[0]
    def get_id_tutilaire(self,event):
        self.id_tutilaire.set(self.combo_tutilaire.get().split('|')[0])
    def get_id_class(self,event):
        self.id_class.set(self.combo_class.get().split('|')[0])
    def get_id_anne_scolaire(self,event):
        self.id_anne_scolaire.set(self.combo_anne_scolaire.get().split('|')[0])
    def run(self):
        
        self.afficher()
    def fenetre(self):
        return self.fen
