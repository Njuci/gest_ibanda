"""nous faisons une interface graphique ou serons afficher dans une treeview  les assignations des enseignants aux classes"""

from tkinter import *
from tkinter import ttk
import assigner_class_back

#from login_back import Connexion
from tkinter import ttk
import sys
import fiche_descotes
class voir_assignassignation:
    def __init__(self,indentifant) :
        self.id_user=indentifant['id_user']
        self.id_classe=0
        self.id_annee_scolaire=0
        self.fen=Tk()
        self.connexion=indentifant['connexion']
        self.fen.title("Voir Assignation des classes")
        self.fen.geometry("800x600")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Assignation des classes",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom=Label(self.fen,text="Nom",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_nom.place(x=300,y=100)
        self.buton_manager=Button(self.fen,text='Manager', background='#FF4500',font=("Times",16),fg='white',command=self.manager)
        self.buton_manager.place(x=350,y=100,width=100)
        self.tree=ttk.Treeview(self.fen,columns=('Num','Annee Scolaire','Classe','Titulaire'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('Annee Scolaire',text='Annee Scolaire')
        self.tree.heading('Classe',text='Classe')
        self.tree.heading('Titulaire',text='Titulaire')
        self.tree.column('Num',width=50)
        self.tree.column('Annee Scolaire',width=150)
        self.tree.column('Classe',width=150)
        self.tree.column('Titulaire',width=150)
        
        self.afficher()
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        assignation=assigner_class_back.Assigner_class_back("","","")
        data=assignation.get_all_c(self.connexion.get_curseur(),self.id_user)
 
        i=0
        for row in data:
            self.tree.insert('','end',iid=i,values=(i+1,row[4]+'|'+row[5],row[2]+'|'+row[3],row[0]+'|'+row[1],))
            i+=1
    
        self.tree.place(x=100,y=150)
        self.tree.bind('<ButtonRelease-1>',self.selection)
    def selection(self,event):
        item=self.tree.selection()
        
        self.id_user=self.tree.item(item,'values')[1].split('|')[0]
        #print(self.id_user)
        self.id_annee_scolaire=self.tree.item(item,'values')[2].split('|')[0]
        self.id_classe=self.tree.item(item,'values')[3].split('|')[0]
        self.id_titulaire=self.tree.item(item,'values')[3].split('|')[0]
        print(self.id_user,self.id_annee_scolaire,self.id_classe,self.id_titulaire)
    def manager(self):
        self.fen.destroy()
        identifiant={'id_user':self.id_titulaire,'id_classe':self.id_annee_scolaire,'id_annee_scolaire':self.id_user,'id_titulaire':self.id_titulaire,'connexion':self.connexion}
        fiche=fiche_descotes.fiche_descotes(identifiant)
        fiche.fenetre().mainloop()
        
    def fenetre(self):
        return self.fen 
