"""nous faisons une interface graphique ou serons afficher dans une treeview  les assignations des enseignants aux classes"""

from tkinter import *
from tkinter import ttk
import assigner_class_back

from login_back import Connexion
from tkinter import ttk
import sys

class voir_assignassignation:
    def __init__(self) :
        self.id_user=0
        self.id_classe=0
        self.id_annee_scolaire=0
        self.fen=Tk()
        self.connexion=Connexion()
        self.fen.title("Voir Assignation des classes")
        self.fen.geometry("800x600")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Assignation des classes",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.buton_manager=Button(self.fen,text='Manager', background='#FF4500',font=("Times",16),fg='white',command=self.manager)
        self.buton_manager.place(x=350,y=100,width=100)
        self.tree=ttk.Treeview(self.fen,columns=('Num','Annee Scolaire','Classe','Titulaire'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('Annee Scolaire',text='Annee Scolaire')
        self.tree.heading('Classe',text='Classe')
        self.tree.heading('Titulaire',text='Titulaire')
        self.tree.column('Num',width=50)
        self.tree.column('Annee Scolaire',width=100)
        self.tree.column('Classe',width=100)
        self.tree.column('Titulaire',width=100)
        
        self.afficher()
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        assignation=assigner_class_back.Assigner_class_back("","","")
        data=assignation.get_all(self.connexion.get_curseur())
        i=0
        for row in data:
            self.tree.insert('','end',iid=i,values=(i+1,row[1],row[2],row[3]))
            i+=1
    
        self.tree.place(x=100,y=150)
        self.tree.bind('<ButtonRelease-1>',self.selection)
    def selection(self,event):
        item=self.tree.selection()
        self.id_user=self.tree.item(item,'values')[0]
        self.id_annee_scolaire=self.tree.item(item,'values')[1]
        self.id_classe=self.tree.item(item,'values')[2]
        self.id_titulaire=self.tree.item(item,'values')[3]
        
    
    def manager(self):
        self.fen.destroy()
        print(self.id_user)

